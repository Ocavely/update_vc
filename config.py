# -*- coding: utf-8 -*-

# ***********************************************************************
# Modified based on the KouriChat project
# Copyright of this modification: Copyright (C) 2025, iwyxdxl
# Licensed under GNU GPL-3.0 or higher, see the LICENSE file for details.
# 
# This file is part of WeChatBot, which includes modifications to the KouriChat project.
# The original KouriChat project's copyright and license information are preserved in the LICENSE file.
# For any further details regarding the license, please refer to the LICENSE file.
# ***********************************************************************

# 用户列表(请配置要和bot说话的账号的微信昵称！)
# 例如：LISTEN_LIST = [['微信名1', '角色1'],['微信名2', '角色2']]

# DeepSeek API 配置
DEEPSEEK_API_KEY = 'apieky'
# 硅基流动API注册地址，免费15元额度 https://cloud.siliconflow.cn/
DEEPSEEK_BASE_URL = 'https://api.gptgod.online/v1'
# 硅基流动API的模型
MODEL = 'gpt-4.1-mini'
# 用户和AI对话轮数
MAX_GROUPS = 5

# 打断聊天功能
# 开启后，如果AI正在回复用户上条消息时用户发送了新消息，将打断当前回复，进行新消息的思考和回复
ENABLE_INTERRUPT_REPLY = True

# 如果要使用官方的API
# DEEPSEEK_BASE_URL = 'https://api.deepseek.com'
# 官方API的V3模型
# MODEL = 'deepseek-chat'

# 回复最大token
MAX_TOKEN = 5000
# DeepSeek温度
TEMPERATURE = 1.1

# Moonshot AI配置（用于图片和表情包识别）

MOONSHOT_API_KEY = 'apikey'
MOONSHOT_BASE_URL = 'https://api.gptgod.online/v1'
MOONSHOT_MODEL = 'gpt-4o-mini'
MOONSHOT_TEMPERATURE = 0.8
ENABLE_IMAGE_RECOGNITION = True
ENABLE_EMOJI_RECOGNITION = True

# 消息队列等待时间
QUEUE_WAITING_TIME = 5

# 表情包存放目录
EMOJI_DIR = 'emojis'
ENABLE_EMOJI_SENDING = True
EMOJI_SENDING_PROBABILITY = 20

# 自动消息配置
AUTO_MESSAGE = '请你模拟系统设置的角色，询问对方在做什么或者有没有想你或者询问为什么不理你了'
ENABLE_AUTO_MESSAGE = True
# 等待时间
MIN_COUNTDOWN_HOURS = 0.5
MAX_COUNTDOWN_HOURS = 1.0
# 消息发送时间限制
QUIET_TIME_START = '11:00'
QUIET_TIME_END = '9:00'
# 不对群聊发送自动消息
IGNORE_GROUP_CHAT_FOR_AUTO_MESSAGE = False

# 消息回复时间间隔
# 间隔时间 = 字数 * (平均时间 + 随机时间)
AVERAGE_TYPING_SPEED = 0.03
RANDOM_TYPING_SPEED_MIN = 0.01
RANDOM_TYPING_SPEED_MAX = 0.05
SEPARATE_ROW_SYMBOLS = True

# 记忆功能
# 采用综合评分公式：0.6*重要度 - 0.4*(存在时间小时数)
# 示例：
# 重要度5的旧记忆（存在12小时）得分：0.65 - 0.412 = 3 - 4.8 = -1.8
# 重要度4的新记忆（存在1小时）得分：0.64 - 0.41 = 2.4 - 0.4 = 2.0 → 保留新记忆
ENABLE_MEMORY = True
MEMORY_TEMP_DIR = 'Memory_Temp'
MAX_MESSAGE_LOG_ENTRIES = 30
MAX_MEMORY_NUMBER = 50
UPLOAD_MEMORY_TO_AI = True
# 记忆存储方式：True = 保存到单独的JSON文件，False = 保存到prompt文件中
SAVE_MEMORY_TO_SEPARATE_FILE = True
CORE_MEMORY_DIR = 'CoreMemory'

# 是否接收全部群聊消息
ACCEPT_ALL_GROUP_CHAT_MESSAGES = False
ENABLE_GROUP_AT_REPLY = True
ENABLE_GROUP_KEYWORD_REPLY = True
GROUP_KEYWORD_LIST = ['_']
GROUP_CHAT_RESPONSE_PROBABILITY = 100
GROUP_KEYWORD_REPLY_IGNORE_PROBABILITY = True

# 登录配置编辑器设置
ENABLE_LOGIN_PASSWORD = False
LOGIN_PASSWORD = '123456'
PORT = 5000

# 文字指令识别开关
# 开启后，私聊/群聊（满足触发条件）中以“/”开头的指令将被解析并执行
ENABLE_TEXT_COMMANDS = True

# 定时器/提醒设置
# 启用提醒功能
ENABLE_REMINDERS = True
# 是否允许在安静时间内发送提醒 (True/False)
# 如果设置为 False，则在安静时间内安排的提醒将被跳过。
ALLOW_REMINDERS_IN_QUIET_TIME = False
# 是否使用语音通话进行提醒
# 群聊无法使用语音通话进行提醒
USE_VOICE_CALL_FOR_REMINDERS = True

# 联网API配置
ENABLE_ONLINE_API = True
ONLINE_BASE_URL = 'https://api.gptgod.online/v1'
ONLINE_MODEL = 'net-gpt-4o-mini'
ONLINE_API_KEY = 'apikey'
ONLINE_API_TEMPERATURE = 0.8
ONLINE_API_MAX_TOKEN = 2000
SEARCH_DETECTION_PROMPT = '天气、最新的新闻事件使用、歌曲'
ONLINE_FIXED_PROMPT = ''

# 是否启用自动抓取消息中URL链接内容的功能
ENABLE_URL_FETCHING = True
# 网络请求超时时间 (秒)
REQUESTS_TIMEOUT = 10
# 抓取网页时使用的 User-Agent，模拟浏览器防止被屏蔽
# REQUESTS_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# REQUESTS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
REQUESTS_USER_AGENT = 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36'
# 从网页提取内容的最大字符数，防止上下文过长，影响AI处理效率和成本
MAX_WEB_CONTENT_LENGTH = 2000

# 定时重启配置
ENABLE_SCHEDULED_RESTART = True
RESTART_INTERVAL_HOURS = 2.0
RESTART_INACTIVITY_MINUTES = 15

# 图片生成配置
ENABLE_IMAGE_GENERATION = True
IMAGE_GENERATION_KEYWORD = '画/生成'
ENABLE_SELFIE_MODE = True
SELFIE_KEYWORD = '自拍/你照片/你的照片'
# AI形象描述（用于自拍时与用户消息合并生成图片）
USER_SELFIE_DESCRIPTION = ''
IMAGE_GENERATION_MODEL = 'gpt-image-2'
IMAGE_GENERATION_BASE_URL = 'https://api.gptgod.online'
IMAGE_GENERATION_API_KEY = 'apieky'
IMAGE_GENERATION_SIZE = '1024x1792'
IMAGE_GENERATION_N = 1
# 是否使用 AI 模型判断是否需要画图（开启后将不再依赖关键词匹配，改由 AI 智能判断）
USE_ASSISTANT_FOR_IMAGE_GENERATION = True
# 画图检测使用辅助模型（True）还是主模型（False）。辅助模型更快更便宜但可能自带画图工具干扰判断
IMAGE_DETECTION_USE_ASSISTANT = True

# 强制移除括号当中的内容
REMOVE_PARENTHESES = False

# 是否使用辅助模型
ENABLE_ASSISTANT_MODEL = True
ASSISTANT_BASE_URL = 'https://api.gptgod.online/v1'
ASSISTANT_MODEL = 'gpt-3.5-turbo'
ASSISTANT_API_KEY = 'apikey'
ASSISTANT_TEMPERATURE = 0.3
ASSISTANT_MAX_TOKEN = 1000
USE_ASSISTANT_FOR_MEMORY_SUMMARY = True
ENABLE_ASSISTANT_CUSTOM_PROMPT = False
ASSISTANT_CUSTOM_PROMPT = ''

# 敏感词处理配置
# 开启后遇到敏感词时自动清除Memory_Temp文件和聊天上下文
ENABLE_SENSITIVE_CONTENT_CLEARING = True

# 论坛自定义模型配置（可选）
ENABLE_FORUM_CUSTOM_MODEL = False
FORUM_BASE_URL = 'https://vg.v1api.cc/v1'
FORUM_MODEL = 'deepseek-ai/DeepSeek-V3'
FORUM_API_KEY = ''
FORUM_TEMPERATURE = 1.0
FORUM_MAX_TOKEN = 1200

# 情感优化功能配置
# 开启后，每次调用chat模型时会在系统提示词后动态插入情感优化提示词
ENABLE_EMOTION_FIX = True
EMOTION_FIX_FILE = 'emotionfix'

# GPT-SoVITS 语音合成配置
ENABLE_GPT_SOVITS_TTS = True
GPT_SOVITS_API_URL = 'http://127.0.0.1:9880/tts'
GPT_SOVITS_SET_GPT_URL = 'http://127.0.0.1:9880/set_gpt_weights'
GPT_SOVITS_SET_SOVITS_URL = 'http://127.0.0.1:9880/set_sovits_weights'
GPT_SOVITS_GPT_WEIGHTS = 'GPT_weights_v2ProPlus/Nikki-v2pp.ckpt'
GPT_SOVITS_SOVITS_WEIGHTS = 'SoVITS_weights_v2ProPlus/Nikki-v2pp.pth'
GPT_SOVITS_REF_AUDIO = 'reference_audio/730756193.wav'
GPT_SOVITS_PROMPT_TEXT = '说不定听到好听的歌，宝宝就不哭了。'
# 可调参数
GPT_SOVITS_TOP_K = 5
GPT_SOVITS_TOP_P = 1.0
GPT_SOVITS_TEMPERATURE = 1.0
GPT_SOVITS_SPEED_FACTOR = 1.0
GPT_SOVITS_REPETITION_PENALTY = 1.1
GPT_SOVITS_SAMPLE_STEPS = 32
# 语音文件存储目录
VOICE_DIR = 'voices'



# 自动补充的配置项


# 自动补充的配置项
LISTEN_LIST = [['微信名1', '角色1']]
