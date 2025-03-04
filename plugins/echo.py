from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

weather = on_command("1", aliases={"天气", "天气预报"}, priority=5)
@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值

count = 0
debug_count = 0
@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    from nonebot.log import logger
    global debug_count
    debug_count += 1
    logger.error(debug_count)
    if city_name not in ["北京", "上海"]:  # 如果参数不符合要求，则提示用户重新输入
        global count
        count += 1
        await weather.reject_arg('city', str(count))

# 在这里编写获取天气信息的函数
async def get_weather(city: str) -> str:
    return f"{city}的天气是..."