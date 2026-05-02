# -*- coding: utf-8 -*-

import os
import re
import emoji
import time
import requests
from datetime import datetime
from typing import Optional
from config import *


class GPTSovitsTTS:
    def __init__(self):
        self.voice_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), VOICE_DIR)
        os.makedirs(self.voice_dir, exist_ok=True)

        self.tts_api_url = GPT_SOVITS_API_URL
        self.set_gpt_url = GPT_SOVITS_SET_GPT_URL
        self.set_sovits_url = GPT_SOVITS_SET_SOVITS_URL

        self.gpt_weights_path = GPT_SOVITS_GPT_WEIGHTS
        self.sovits_weights_path = GPT_SOVITS_SOVITS_WEIGHTS

        self.ref_audio_path = GPT_SOVITS_REF_AUDIO
        self.prompt_text = GPT_SOVITS_PROMPT_TEXT

        self.top_k = GPT_SOVITS_TOP_K
        self.top_p = GPT_SOVITS_TOP_P
        self.temperature = GPT_SOVITS_TEMPERATURE
        self.speed_factor = GPT_SOVITS_SPEED_FACTOR
        self.repetition_penalty = GPT_SOVITS_REPETITION_PENALTY
        self.sample_steps = GPT_SOVITS_SAMPLE_STEPS

        self._initialized = False

    def _init_weights(self):
        if self._initialized:
            return True

        try:
            if self.set_gpt_url:
                resp = requests.get(self.set_gpt_url, params={"weights_path": self.gpt_weights_path}, timeout=10)
                if resp.status_code == 200:
                    print(f"GPT模型权重已设置: {self.gpt_weights_path}")
                else:
                    print(f"设置GPT权重失败: {resp.text}")

            if self.set_sovits_url:
                resp = requests.get(self.set_sovits_url, params={"weights_path": self.sovits_weights_path}, timeout=10)
                if resp.status_code == 200:
                    print(f"SoVITS模型权重已设置: {self.sovits_weights_path}")
                else:
                    print(f"设置SoVITS权重失败: {resp.text}")

            self._initialized = True
            return True
        except Exception as e:
            print(f"GPT-SoVITS权重初始化失败: {e}")
            return False

    def check_api_available(self):
        try:
            resp = requests.get(f"{self.tts_api_url.replace('/tts', '/control')}?command=status", timeout=5)
            return True
        except:
            return False

    def _clear_tts_text(self, text: str) -> str:
        try:
            text = emoji.replace_emoji(text, replace='')
        except Exception:
            pass

        text = text.replace('$', ',').replace('\r\n', '\n').replace('\r', '\n').replace('\n', ',')
        text = re.sub(r'\[.*?\]', '', text)
        return text.strip()

    def generate_audio(self, text: str) -> Optional[str]:
        if not text or not text.strip():
            return None

        if not ENABLE_GPT_SOVITS_TTS:
            print("GPT-SoVITS TTS功能已禁用")
            return None

        if not os.path.exists(self.ref_audio_path):
            print(f"参考音频文件不存在: {self.ref_audio_path}")
            return None

        if not self._init_weights():
            print("GPT-SoVITS权重初始化失败，无法生成语音")
            return None

        try:
            if not os.path.exists(self.voice_dir):
                os.makedirs(self.voice_dir)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            voice_path = os.path.join(self.voice_dir, f"voice_{timestamp}.wav")

            payload = {
                "text": text,
                "text_lang": "zh",
                "prompt_lang": "zh",
                "text_split_method": "cut5",
                "ref_audio_path": self.ref_audio_path,
                "prompt_text": self.prompt_text,
                "no_prompt": False,
                "aux_ref_audio_paths": [],
                "top_k": self.top_k,
                "top_p": self.top_p,
                "temperature": self.temperature,
                "speed_factor": self.speed_factor,
                "repetition_penalty": self.repetition_penalty,
                "seed": -1,
                "parallel_infer": True,
                "split_bucket": False,
                "super_sampling": False,
                "sample_steps": self.sample_steps,
                "batch_size": 2,
                "batch_threshold": 0.75,
                "media_type": "wav",
                "streaming_mode": False,
            }

            print(f"TTS请求: API={self.tts_api_url}, 参考音频={self.ref_audio_path}")
            print(f"请求参数: text={text[:20]}..., ref_audio={self.ref_audio_path}, prompt={self.prompt_text[:20]}...")
            response = requests.post(self.tts_api_url, json=payload, timeout=60)
            
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', '')
                print(f"TTS响应: status={response.status_code}, content_type={content_type}, size={len(response.content)}")
                
                if 'application/json' in content_type:
                    print(f"TTS返回JSON错误: {response.json()}")
                    return None
                    
                if len(response.content) < 1000:
                    print(f"TTS返回内容过小: {len(response.content)} 字节，可能是错误响应")
                    return None
                with open(voice_path, "wb") as f:
                    f.write(response.content)
                print(f"语音生成成功: {voice_path}")
                return voice_path
            else:
                error_msg = response.json().get("message", "未知错误") if response.content else f"HTTP {response.status_code}"
                print(f"TTS API返回错误: {error_msg}")
                return None

        except requests.exceptions.Timeout:
            print("TTS API请求超时")
            return None
        except requests.exceptions.ConnectionError:
            print(f"TTS API连接失败: {self.tts_api_url}")
            return None
        except Exception as e:
            print(f"语音生成失败: {str(e)}")
            return None

    def del_audio_file(self, audio_file_path: str):
        try:
            if os.path.isfile(audio_file_path):
                os.remove(audio_file_path)
                print(f"清理语音文件: {audio_file_path}")
        except Exception as e:
            print(f"清理语音文件失败 {audio_file_path}: {str(e)}")


tts_service = GPTSovitsTTS()