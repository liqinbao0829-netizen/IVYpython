import streamlit as st
from dataclasses import dataclass
from typing import List, Dict

st.set_page_config(page_title="Python 24-Week Learning System", page_icon="🐍", layout="wide", initial_sidebar_state="expanded")

CS50P_OCW_URL = "https://cs50.harvard.edu/python/2022/"
CS50P_PLL_URL = "https://pll.harvard.edu/course/cs50s-introduction-programming-python"
ML_AI_URL = "https://pll.harvard.edu/course/machine-learning-and-ai-python"


@dataclass
class QuizQuestion:
    qtype: str
    prompt: str
    options: List[str]
    answer: str
    explanation: str
    reference: str


@dataclass
class WeekData:
    week: int
    unit: str
    title: str
    theme: str
    harvard_link: str
    harvard_understanding: List[str]
    vivid_notes: List[str]
    lab_title: str
    follow_code: str
    follow_answer: str
    modify_task: str
    modify_answer: str
    challenge_task: str
    challenge_answer: str
    exam_focus: List[str]
    write_code_prompt: str
    write_code_answer: str
    parent_tip: str
    quiz: List[QuizQuestion]


def progress_percent() -> int:
    return int(len(st.session_state.completed_weeks) / 24 * 100)


def mark_week_complete(week: int):
    st.session_state.completed_weeks.add(week)


def link_button(label: str, url: str):
    st.markdown(f"[**{label}**]({url})")


def card_title(icon: str, text: str):
    st.markdown(
        f"""
        <div style="padding:10px 14px;border-radius:16px;background:#f5f8ff;border:1px solid #d7e3ff;
        margin-top:8px;margin-bottom:10px;font-weight:700;font-size:24px;">
            {icon} {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def make_quiz(title: str, keyword: str, symbol: str, use: str, common_bug: str, sample: str) -> List[QuizQuestion]:
    return [
        QuizQuestion("single", f"【单选1】关于“{title}”的说法，最准确的是哪一项？",
                     [f"{title}主要用于{use}", f"{title}主要用于删除文件", f"{title}主要用于关闭浏览器", f"{title}主要用于安装系统"],
                     f"{title}主要用于{use}",
                     f"{title}在本周的核心用途就是：{use}。", "考点：概念理解"),
        QuizQuestion("single", f"【单选2】本周“{title}”的高频关键词或符号是哪一个？",
                     [symbol, "shutdown()", "close()", "reset()"],
                     symbol,
                     f"本周最应先记住的标志性关键词或符号是 {symbol}。", "考点：基础语法"),
        QuizQuestion("single", f"【单选3】学习“{title}”时，最稳的解题起手动作是什么？",
                     ["先想输入、处理、输出", "先抄答案", "先猜结果", "先跳过"],
                     "先想输入、处理、输出",
                     "中国国内大学机考题里，能先拆输入、处理、输出，正确率会明显更高。", "考点：解题步骤"),
        QuizQuestion("single", f"【单选4】下列哪一项最可能是“{title}”相关题目的常见错误？",
                     [common_bug, "屏幕太亮", "字体太小", "电脑太慢"],
                     common_bug,
                     f"{title}相关题最容易出的问题之一就是：{common_bug}。", "考点：常见错误"),
        QuizQuestion("single", f"【单选5】关于“{title}”的复习顺序，哪一种更符合考试准备？",
                     ["讲义→例题→改错→编程", "只背定义", "只做选择题", "只看视频"],
                     "讲义→例题→改错→编程",
                     "国内大学计算机基础考试常见的有效复习顺序是：先懂概念，再做例题，再练改错和编程。", "考点：复习路径"),
        QuizQuestion("single", f"【单选6】“{title}”真正学会的标志更接近哪一项？",
                     [f"能独立完成一个和“{sample}”相关的小程序", "会复制答案", "记住一条定义", "看过一段视频"],
                     f"能独立完成一个和“{sample}”相关的小程序",
                     "会独立写出来，才是真正学会。", "考点：能力目标"),
        QuizQuestion("judge", f"【判断7】“{title}”只会出现在选择题，不会出现在改错题和编程题中。",
                     ["正确", "错误"], "错误",
                     f"{title}既可能出现在选择题，也可能出现在改错题、程序阅读题和编程题中。", "考点：题型分布"),
        QuizQuestion("judge", f"【判断8】学习“{title}”时，只背概念定义，不动手写代码，也能稳定拿高分。",
                     ["正确", "错误"], "错误",
                     "国内大学机考和期末卷都很看重动手能力，只背定义不够。", "考点：学习方法"),
        QuizQuestion("judge", f"【判断9】调试“{title}”相关程序时，逐行检查逻辑和语法，比一次性大改更稳。",
                     ["正确", "错误"], "正确",
                     "逐行检查是最稳的调试方式。", "考点：调试思路"),
        QuizQuestion("blank", f"【填空10】本周“{title}”的代表性关键词 / 符号是：____。",
                     [], symbol,
                     f"本周代表性关键词或符号是 {symbol}。", "考点：关键词记忆"),
        QuizQuestion("blank", f"【填空11】“{title}”最常见的一类程序错误是：____。",
                     [], common_bug,
                     f"常见错误就是：{common_bug}。", "考点：易错点"),
        QuizQuestion("blank", f"【填空12】遇到“{title}”题目时，推荐先拆成“输入—处理—____”三步。",
                     [], "输出",
                     "程序题最稳的基本框架是：输入—处理—输出。", "考点：程序结构"),
        QuizQuestion("short", f"【程序阅读13】请用自己的话说明：为什么“{title}”会成为本周核心知识点？",
                     [], "参考答案：因为它直接决定程序如何完成本周这一类任务，是后续改错题和编程题的基础。",
                     "这一题对应国内大学计算机考试中的“简答/程序理解”风格。", "考点：知识理解"),
        QuizQuestion("fix", f"【改错14】请写出一种“{title}”相关的常见错误，并给出正确改法。",
                     [], f"参考答案示例：{common_bug}；改法应围绕 {symbol} 或 {keyword} 的正确写法展开。",
                     "这一题对应国内大学计算机基础中的改错题。", "考点：改错"),
        QuizQuestion("code", f"【编程15】请设计一个和“{sample}”相关的小程序，并说明它的输入、处理、输出。",
                     [], f"参考答案方向：围绕“{sample}”写一个最小可运行程序，先明确输入，再写处理逻辑，最后输出结果。",
                     "这一题对应国内大学课程期末卷或机考里的基础编程题。", "考点：程序设计"),
    ]


def week_dict(
    week: int,
    unit: str,
    title: str,
    theme: str,
    harvard_link: str,
    harvard_understanding: List[str],
    vivid_notes: List[str],
    lab_title: str,
    follow_code: str,
    modify_task: str,
    modify_answer: str,
    challenge_task: str,
    challenge_answer: str,
    exam_focus: List[str],
    write_code_prompt: str,
    write_code_answer: str,
    parent_tip: str,
    quiz_meta: Dict[str, str],
) -> WeekData:
    return WeekData(
        week=week,
        unit=unit,
        title=title,
        theme=theme,
        harvard_link=harvard_link,
        harvard_understanding=harvard_understanding,
        vivid_notes=vivid_notes,
        lab_title=lab_title,
        follow_code=follow_code,
        follow_answer=follow_code,
        modify_task=modify_task,
        modify_answer=modify_answer,
        challenge_task=challenge_task,
        challenge_answer=challenge_answer,
        exam_focus=exam_focus,
        write_code_prompt=write_code_prompt,
        write_code_answer=write_code_answer,
        parent_tip=parent_tip,
        quiz=make_quiz(
            title=title,
            keyword=quiz_meta["keyword"],
            symbol=quiz_meta["symbol"],
            use=quiz_meta["use"],
            common_bug=quiz_meta["bug"],
            sample=quiz_meta["sample"],
        ),
    )


WEEKS: Dict[int, WeekData] = {}

WEEKS[1] = week_dict(
    1, "Unit 1 基础表达", "变量 Variable", "给数据贴标签，让电脑记住信息",
    "https://cs50.harvard.edu/python/2022/weeks/0/",
    ["哈佛这里会先让学生理解：程序是在操作信息。", "变量像带标签的盒子，可以把 name、age、score 这类信息装进去。", "变量不是死概念，而是后面一切输入、计算、判断的基础。", "这一周真正的目标是：会给数据起有意义的名字。"],
    ["把变量想成便利贴，标签清楚，程序就不容易迷路。", "现实中说“这是小明的成绩”，代码里就是 score = 95。", "变量名像路标，变量值像房子里的内容。", "所以这周不是背术语，而是练‘给数据命名’。"],
    "自我介绍机器人",
    """name = input("What is your name? ")
age = input("How old are you? ")
print("Hello,", name)
print("You are", age, "years old.")""",
    "新增一个 school 变量，让机器人多输出一句学校信息。",
    """name = input("What is your name? ")
age = input("How old are you? ")
school = input("What school are you in? ")
print("Hello,", name)
print("You are", age, "years old.")
print("You study at", school)""",
    "输入姓名、年龄、城市，输出一句完整自我介绍。",
    """name = input("Name: ")
age = input("Age: ")
city = input("City: ")
print(name, "is", age, "years old and lives in", city + ".")""",
    ["会区分变量名和变量值。", "会写最简单的赋值语句。", "能读懂 name = 'Tom' 这类代码。", "变量命名尽量见名知意。"],
    "写一个程序：输入姓名和班级，输出欢迎语。",
    """name = input("请输入姓名：")
class_name = input("请输入班级：")
print("欢迎你，", name)
print("你来自", class_name)""",
    "这一周最适合让孩子用自己的生活信息来写变量，这样记得更牢。",
    {"keyword": "变量", "symbol": "=", "use": "保存信息", "bug": "把变量名和值混淆", "sample": "变量赋值"}
)

WEEKS[2] = week_dict(
    2, "Unit 1 基础表达", "数据类型 Data Types", "分清数字、文字和真假",
    "https://cs50.harvard.edu/python/2022/weeks/0/",
    ["哈佛会反复强调：18 和 '18' 看起来一样，但程序理解方式完全不同。", "数字可以计算，字符串更像带引号的文字。", "input() 默认拿到的是字符串，所以很多初学者输入了数字却算不出来。", "这一周真正要理解的是：数据类型决定这个值能做什么。"],
    ["数字像积木，可以直接拼起来做运算；字符串像便利签，上面有字，但不一定能算。", "如果把 '18' 当成数字去加 1，程序会紧张。", "这一周像在学翻译规则：电脑怎么理解你给它的内容。", "会区分 int、float、str，后面几乎所有题都会轻松很多。"],
    "BMI 计算器",
    """weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / (height ** 2)
print("BMI =", round(bmi, 2))""",
    "把 BMI 程序改成总价计算器。",
    """price = float(input("Price: "))
count = int(input("Count: "))
total = price * count
print("Total =", total)""",
    "输入两门成绩，输出总分和平均分。",
    """a = float(input("Score 1: "))
b = float(input("Score 2: "))
total = a + b
avg = total / 2
print("Total =", total)
print("Average =", round(avg, 2))""",
    ["会区分 int、float、str。", "知道 input() 默认得到字符串。", "会用 int() / float() 做类型转换。", "会做简单四则运算。"],
    "写一个程序：输入长和宽，输出长方形面积。",
    """length = float(input("请输入长："))
width = float(input("请输入宽："))
area = length * width
print("面积是：", area)""",
    "这一周要盯住一个核心坑：input() 默认是字符串。",
    {"keyword": "数据类型", "symbol": "int() / float() / str()", "use": "区分数字和文字", "bug": "忘记类型转换", "sample": "输入数字求和"}
)

WEEKS[3] = week_dict(
    3, "Unit 1 基础表达", "顺序结构 Sequence", "程序是一行一行按顺序执行的",
    "https://cs50.harvard.edu/python/2022/weeks/0/",
    ["哈佛在最开始讲程序时，重点就是 execution order，也就是执行顺序。", "程序不会猜你的意思，它只会从上到下，一步一步执行。", "顺序结构看起来简单，但所有复杂程序都建立在先做什么、后做什么上。", "这一周要真正理解：代码顺序错了，结果就会错。"],
    ["顺序结构像做菜：先洗菜，再切菜，再下锅。", "程序也是一样，先 input，再计算，再 print。", "很多初学者不是不会写，而是顺序排错了。", "所以这一周反而是基础中的基础。"],
    "早餐下单程序",
    """food = input("What food do you want? ")
price = float(input("What is the price? "))
count = int(input("How many? "))
total = price * count
print("You ordered", food)
print("Total =", total)""",
    "在输出总价前，增加一句“正在计算……”。",
    """food = input("What food do you want? ")
price = float(input("What is the price? "))
count = int(input("How many? "))
print("Calculating...")
total = price * count
print("You ordered", food)
print("Total =", total)""",
    "输入姓名、语文、数学，按顺序输出姓名、总分、平均分。",
    """name = input("Name: ")
chinese = float(input("Chinese: "))
math = float(input("Math: "))
total = chinese + math
avg = total / 2
print("Name:", name)
print("Total:", total)
print("Average:", avg)""",
    ["知道程序默认从上到下执行。", "能判断一段代码执行的先后顺序。", "知道计算前必须先有数据。", "会分析顺序错误导致的结果错误。"],
    "写一个程序：输入名字和零花钱，输出一句完整描述。",
    """name = input("请输入名字：")
money = float(input("请输入零花钱："))
print(name, "has", money, "yuan.")""",
    "这一周可多让孩子口头描述‘代码先做什么，再做什么’。",
    {"keyword": "顺序结构", "symbol": "从上到下", "use": "安排程序步骤", "bug": "执行顺序写反", "sample": "先输入后计算"}
)

# Generate weeks 4-24 in a stable way
topics = {
    4: ("Unit 2 选择结构", "if 基础判断", "让程序学会做选择", "https://cs50.harvard.edu/python/2022/weeks/1/", "if 条件:", "条件成立才执行", "忘写冒号", "年龄判断"),
    5: ("Unit 2 选择结构", "if / else / elif", "让程序做完整分支选择", "https://cs50.harvard.edu/python/2022/weeks/1/", "elif / else", "根据不同条件输出不同结果", "分支顺序错误", "成绩评级"),
    6: ("Unit 3 循环结构", "for 循环", "让程序按次数重复做事", "https://cs50.harvard.edu/python/2022/weeks/2/", "for / range()", "重复固定次数", "range 范围理解错", "打印1到10"),
    7: ("Unit 3 循环结构", "while 循环", "只要条件成立，就继续循环", "https://cs50.harvard.edu/python/2022/weeks/2/", "while 条件:", "条件成立就继续", "忘记更新变量导致死循环", "密码验证"),
    8: ("Unit 3 循环结构", "循环综合", "累加、计数、综合循环", "https://cs50.harvard.edu/python/2022/weeks/2/", "count / total / +=", "统计和累加", "忘记初始化 total", "1到100求和"),
    9: ("Unit 4 函数", "函数基础 def", "把重复工作装进工具箱", "https://cs50.harvard.edu/python/2022/weeks/3/", "def", "封装重复代码", "定义了函数却没调用", "say_hello"),
    10: ("Unit 4 函数", "参数与返回值", "让函数真正变得有用", "https://cs50.harvard.edu/python/2022/weeks/3/", "return", "让函数接收数据并返回结果", "把 return 写成 print", "add(a, b)"),
    11: ("Unit 5 字符串", "字符串基础", "让程序处理文字", "https://cs50.harvard.edu/python/2022/weeks/0/", "upper() / lower() / len()", "处理文字信息", "忘记字符串要加引号", "名字拼接"),
    12: ("Unit 6 列表", "列表基础", "一次装下很多数据", "https://cs50.harvard.edu/python/2022/weeks/4/", "[] / append()", "保存一组数据", "索引从 1 开始想错", "foods[0]"),
    13: ("Unit 6 列表", "列表遍历", "批量处理一组数据", "https://cs50.harvard.edu/python/2022/weeks/4/", "for x in list", "逐个处理一组数据", "不会把列表和循环连起来", "遍历 fruits"),
    14: ("Unit 7 字典", "字典 Dictionary", "按名字找信息", "https://cs50.harvard.edu/python/2022/weeks/5/", "{key: value}", "按名字找信息", "把列表索引和字典 key 混淆", "student['name']"),
    15: ("Unit 8 文件与异常", "文件读写", "让程序把信息保存下来", "https://cs50.harvard.edu/python/2022/weeks/6/", "open() / read() / write()", "保存和读取数据", "读写模式写错", "note.txt"),
    16: ("Unit 8 文件与异常", "异常处理", "程序出错也不要崩掉", "https://cs50.harvard.edu/python/2022/weeks/7/", "try / except", "防止程序崩掉", "没有预判输入错误", "安全输入"),
    17: ("Unit 9 综合应用", "综合项目 1：菜单系统", "把前面的基础拼起来", "https://cs50.harvard.edu/python/2022/weeks/3/", "输入 + 判断 + 循环", "整合多个知识点", "程序结构混乱", "菜单系统"),
    18: ("Unit 9 综合应用", "综合项目 2：数据统计", "用代码处理一组数字", "https://cs50.harvard.edu/python/2022/weeks/4/", "total / count / avg", "处理一组数字", "平均值公式写错", "求平均分"),
    19: ("Unit 10 常用结构补充", "元组与集合", "哪些数据不改，哪些数据不重复", "https://cs50.harvard.edu/python/2022/weeks/4/", "() / {}", "区分不可改和去重", "把 tuple 和 list 混淆", "set 去重"),
    20: ("Unit 10 常用结构补充", "模块与库 import", "借用别人写好的工具", "https://cs50.harvard.edu/python/2022/weeks/7/", "import", "调用现成工具", "导入后不会调用函数", "random.choice"),
    21: ("Unit 11 项目周", "小游戏项目", "让编程变得更好玩", ML_AI_URL, "规则逻辑", "做交互小游戏", "规则判断写不全", "猜数字"),
    22: ("Unit 11 项目周", "实用工具项目", "让 Python 真正帮生活做事", ML_AI_URL, "菜单 + 功能", "解决生活小任务", "功能切换逻辑写乱", "多功能计算器"),
    23: ("Unit 12 展示周", "项目整理与表达", "会写，也要会讲", ML_AI_URL, "输入-处理-输出", "讲清代码思路", "会写但不会说", "程序说明"),
    24: ("Unit 12 展示周", "毕业回顾与总复习", "把 24 周知识真正串起来", ML_AI_URL, "整合", "串联全部知识", "知识点割裂", "复习菜单"),
}

for w, meta in topics.items():
    if w in WEEKS:
        continue
    unit, title, theme, harvard_link, symbol, use, bug, sample = meta
    WEEKS[w] = week_dict(
        w, unit, title, theme, harvard_link,
        [f"哈佛理解课对应主题：{title}。", f"这一周最重要的是理解：{theme}。", f"这一章的核心关键词是 {symbol}。", "不是死背语法，而是把它放进真实任务里。"],
        [f"这周像在学习：{title}。", "要把知识点放进现实情境里理解。", "会做一个小任务，比背定义更重要。", "所以这一周重点是有趣讲义 + 动手体验。"],
        f"{title} 小实验",
        f'print("Week {w}: {title}")',
        f"围绕 {title} 做一个小修改。",
        f'print("Modified week {w}: {title}")',
        f"围绕 {title} 写一个小挑战程序。",
        f'print("Challenge week {w}: {title}")',
        [f"会理解这一章的核心：{theme}。", f"会做和 {title} 对应的基础题。", f"知道 {title} 最容易错在哪里。", "会把知识点连到考试题上。"],
        f"写一个和 {title} 相关的小程序。",
        f'print("This is my {title} program.")',
        "这周更重要的是让孩子说出‘这一章到底在解决什么问题’。",
        {"keyword": title, "symbol": symbol, "use": use, "bug": bug, "sample": sample}
    )




# Weeks 11-24 expanded content
WEEKS[11] = week_dict(
    11, 'Unit 5 字符串', '字符串基础', '让程序处理文字，而不只是处理数字',
    'https://cs50.harvard.edu/python/2022/weeks/0/',
    ['哈佛在最早的输入输出里其实就已经埋下了字符串的概念，因为用户输入的大部分内容本来就是文字。', '这一周真正要理解的是：字符串不是‘带引号的句子’这么简单，它是程序处理语言、名字、标题、密码的基础容器。', 'CS50 风格会很强调字符串方法的实用性，比如大小写转换、长度判断、拼接显示，因为这些都直接出现在真实程序里。', '这周的主线不是死记方法名，而是理解：文字也能像数据一样被程序操作。'],
    ['把字符串想成一串带顺序的字母珠子，你不光能看它，还能拼它、改它、统计它。', '如果数字像积木，字符串就像一排字母卡片，每张卡片都有位置。', '现实里名字、城市、邮箱、课程标题，本质上都是字符串。', '所以这一周是在学：怎么让程序‘看懂文字’。'],
    '用户名格式化器',
    'name = input("Enter your name: ")\nprint(name.upper())\nprint(name.lower())\nprint(len(name))',
    '把程序改成同时输出 title() 格式，并显示欢迎语。',
    'name = input("Enter your name: ")\nprint(name.upper())\nprint(name.lower())\nprint(name.title())\nprint("Welcome,", name.title())',
    '输入 first_name 和 last_name，拼接成完整姓名并输出长度。',
    'first_name = input("First name: ")\nlast_name = input("Last name: ")\nfull_name = first_name + " " + last_name\nprint(full_name)\nprint(len(full_name))',
    ['知道字符串要用引号表示。', '会做字符串拼接。', '会用 upper() / lower() / title() / len()。', '会处理基础字符串输出题。'],
    '写一个程序：输入英文名和城市名，输出一句完整介绍，并把名字转成首字母大写。',
    'name = input("请输入英文名：")\ncity = input("请输入城市：")\nprint(name.title(), "comes from", city.title())',
    '这周很适合用孩子自己的英文名、学校名、城市名来做练习，代入感会更强。',
    {'keyword': '字符串', 'symbol': 'upper() / lower() / len()', 'use': '处理文字信息', 'bug': '忘记字符串要加引号', 'sample': '名字拼接'}
)

WEEKS[12] = week_dict(
    12, 'Unit 5 字符串', '字符串进阶：切片与查找', '学会从文字里取出一部分信息',
    'https://cs50.harvard.edu/python/2022/weeks/0/',
    ['哈佛式学习会很强调：真正理解字符串，必须理解它是按位置排列的。', '切片和索引的意义，在于你可以从一整段文字里精准拿到其中一部分。', '这一周不只是学语法，而是在学‘如何从信息里抽取信息’。', '邮箱前缀、姓名首字母、隐藏手机号，这些现实任务都能用切片解决。'],
    ['字符串切片像拿剪刀剪彩带：从第几位开始，剪到第几位结束。', '索引像座位号，程序靠位置去找字符。', '你不是只能整句打印，还能只拿前 3 个字母、后 4 个数字。', '这一周很像在学‘文字版手术刀’。'],
    '邮箱前缀提取器',
    'email = input("Email: ")\nprint(email[0])\nprint(email[:5])',
    '再输出邮箱最后 3 个字符。',
    'email = input("Email: ")\nprint(email[0])\nprint(email[:5])\nprint(email[-3:])',
    '输入一个单词，输出它的首字母、末字母和中间部分。',
    'word = input("Word: ")\nprint(word[0])\nprint(word[-1])\nprint(word[1:-1])',
    ['知道索引从 0 开始。', '会写 s[0]、s[-1]、s[:3] 这类表达式。', '会做基础切片题。', '会分析字符串查找和截取的输出结果。'],
    '写一个程序：输入手机号字符串，输出前3位和后4位。',
    'phone = input("请输入手机号：")\nprint("前3位：", phone[:3])\nprint("后4位：", phone[-4:])',
    '这周最容易错的是索引起点和切片边界，别急着求快。',
    {'keyword': '字符串切片', 'symbol': 's[a:b]', 'use': '从文字中截取部分信息', 'bug': '索引和边界写错', 'sample': '手机号截取'}
)

WEEKS[13] = week_dict(
    13, 'Unit 6 列表', '列表基础', '一次保存很多数据，而不是只保存一个值',
    'https://cs50.harvard.edu/python/2022/weeks/4/',
    ['哈佛会让学生从‘单个变量’走到‘一组数据’，这是编程能力的重要升级。', '列表的价值不只是会写中括号，而是让程序能处理一批信息。', '当你有多门成绩、多个商品、多个名字时，列表会比一个个变量自然得多。', '这一周重点是：理解列表是有顺序、可修改的一组数据。'],
    ['列表像收纳盒，不是只放一个苹果，而是能放一篮苹果。', '每个元素都有位置，程序通过位置去拿。', '如果变量像一个小抽屉，列表就像一整排抽屉。', '这周不是背 append，而是建立‘一组数据’这个思维。'],
    '购物篮清单',
    'foods = ["apple", "milk", "bread"]\nprint(foods[0])\nprint(len(foods))',
    '往列表里再加入 banana，并输出整个列表。',
    'foods = ["apple", "milk", "bread"]\nfoods.append("banana")\nprint(foods)\nprint(len(foods))',
    '建立一个三门学科列表，并输出最后一个元素。',
    'subjects = ["Math", "English", "Physics"]\nprint(subjects[-1])',
    ['知道列表用 [] 表示。', '知道索引从 0 开始。', '会读取和修改列表元素。', '会用 append() 添加元素。'],
    '写一个列表保存 4 个电影名，并输出第 2 个和最后 1 个。',
    'movies = ["Dune", "Frozen", "Avatar", "Coco"]\nprint(movies[1])\nprint(movies[-1])',
    '这周可重点盯住：列表是一组数据，索引从 0 开始。',
    {'keyword': '列表', 'symbol': '[] / append()', 'use': '保存一组数据', 'bug': '索引从 1 开始想错', 'sample': 'foods[0]'}
)

WEEKS[14] = week_dict(
    14, 'Unit 6 列表', '列表进阶：遍历与统计', '批量处理一组数据',
    'https://cs50.harvard.edu/python/2022/weeks/4/',
    ['哈佛会把列表和 for 循环自然连起来，因为它们是最常见的搭配。', '真正会列表的人，不是只会建列表，而是会遍历、统计、筛选。', '这一周会把列表、循环、判断三样东西串在一起。', '重点不是某一个方法，而是学会批量处理一组数据。'],
    ['列表像一排学生，for 循环像老师点名，一个个叫过去。', '以前你要手动看每个元素，现在程序可以自动巡一遍。', '这周会第一次很明显感受到‘程序帮我批量做事’。', '会做这一周，很多国内考试里的列表题就不慌了。'],
    '成绩筛选器',
    'scores = [70, 82, 95, 60, 88]\nfor s in scores:\n    print(s)',
    '只输出大于 80 的成绩。',
    'scores = [70, 82, 95, 60, 88]\nfor s in scores:\n    if s > 80:\n        print(s)',
    '统计列表中及格成绩（>=60）的个数。',
    'scores = [70, 82, 95, 60, 88]\ncount = 0\nfor s in scores:\n    if s >= 60:\n        count += 1\nprint(count)',
    ['会 for x in list。', '会做列表遍历题。', '会把列表和判断结合起来。', '会做基础统计题。'],
    '写一个程序：遍历列表 [12, 35, 67, 20, 89]，输出其中的偶数。',
    'nums = [12, 35, 67, 20, 89]\nfor n in nums:\n    if n % 2 == 0:\n        print(n)',
    '这周重点不是新概念多，而是把旧概念连起来。',
    {'keyword': '列表遍历', 'symbol': 'for x in list', 'use': '逐个处理一组数据', 'bug': '不会把列表和循环连起来', 'sample': '遍历 fruits'}
)

WEEKS[15] = week_dict(
    15, 'Unit 7 字典', '字典 Dictionary', '按名字找信息，而不是按位置找信息',
    'https://cs50.harvard.edu/python/2022/weeks/5/',
    ['哈佛会通过字典让学生理解：并不是所有数据都适合按位置存。', '列表适合按顺序找，字典适合按名字、标签、键去找。', '学生信息、商品信息、配置参数，这些都很适合字典。', '这一周重点是：什么时候该用字典，而不是硬套列表。'],
    ['字典像通讯录，你不是按第 3 行找电话，而是按姓名找电话。', 'key 像标签，value 像标签后面的内容。', '如果信息本来带名字，字典会比列表顺手很多。', '这周是在学‘按标签取值’。'],
    '学生信息卡',
    'student = {"name": "Tom", "score": 95}\nprint(student["name"])\nprint(student["score"])',
    '再增加一个 city 字段，并输出它。',
    'student = {"name": "Tom", "score": 95, "city": "Boston"}\nprint(student["city"])',
    '写一个字典保存一本书的 title 和 price，并输出 price。',
    'book = {"title": "Python", "price": 88}\nprint(book["price"])',
    ['知道字典用 {}。', '知道 key:value 结构。', '会通过 key 取值。', '会做基础字典题。'],
    '写一个字典保存姓名、年龄、城市，并输出城市和年龄。',
    'info = {"name": "Ivy", "age": 18, "city": "Seattle"}\nprint(info["city"])\nprint(info["age"])',
    '这周很适合让孩子比较：列表按位置取，字典按键取。',
    {'keyword': '字典', 'symbol': '{key: value}', 'use': '按名字找信息', 'bug': '把列表索引和字典 key 混淆', 'sample': "student['name']"}
)

WEEKS[16] = week_dict(
    16, 'Unit 8 文件与异常', '文件读写 File I/O', '让程序把结果保存下来，而不是一关就消失',
    'https://cs50.harvard.edu/python/2022/weeks/6/',
    ['哈佛会把程序从‘只在当下运行’推进到‘能把结果留下来’。', '文件读写的意义是：程序结束了，信息还在。', '这一步很关键，因为它让程序开始真正和外部世界交互。', '这一周重点是：理解为什么程序需要记忆。'],
    ['如果变量像短期记忆，文件就像长期档案柜。', '文件像笔记本，程序可以往里写字，也可以翻出来再看。', '一旦学会文件，程序就不只是算一下，而是能留下记录。', '这周会让程序更像工具，不像一次性计算器。'],
    '学习日志记录器',
    'with open("note.txt", "w", encoding="utf-8") as f:\n    f.write("I am learning Python.")',
    '让用户输入今天主题，再写入 note.txt。',
    'topic = input("Today\'s topic: ")\nwith open("note.txt", "w", encoding="utf-8") as f:\n    f.write(topic)',
    '先写入 diary.txt，再把内容读取出来。',
    'with open("diary.txt", "w", encoding="utf-8") as f:\n    f.write("Today is a good day.")\n\nwith open("diary.txt", "r", encoding="utf-8") as f:\n    print(f.read())',
    ['知道 open 的基本格式。', '会区分 r 和 w。', '会做最简单文件读写。', "知道 encoding='utf-8' 的作用。"],
    '写一个程序：把输入的姓名写入 user.txt，然后再读出来。',
    'name = input("请输入姓名：")\nwith open("user.txt", "w", encoding="utf-8") as f:\n    f.write(name)\n\nwith open("user.txt", "r", encoding="utf-8") as f:\n    print(f.read())',
    '这周要帮助孩子理解：程序为什么需要把东西存进文件。',
    {'keyword': '文件读写', 'symbol': 'open() / read() / write()', 'use': '保存和读取数据', 'bug': '读写模式写错', 'sample': 'note.txt'}
)

WEEKS[17] = week_dict(
    17, 'Unit 8 文件与异常', '异常处理 try / except', '程序出错了，也不要一下子崩掉',
    'https://cs50.harvard.edu/python/2022/weeks/7/',
    ['哈佛会强调：优秀程序不是永远不出错，而是出错时仍然可控。', 'try / except 的意义，就是提前为可能的错误准备处理方案。', '用户输错、类型不对、除数为 0，这些都不是例外，而是常见场景。', '这一周重点是：让程序更稳，而不是更花。'],
    ['异常处理像下雨时带伞：不是希望出事，而是提前准备。', '如果程序一出错就崩掉，体验会很差；try/except 就是在救场。', '这不是高级玩法，而是很实用的‘防翻车’能力。', '这周会让代码从脆弱变得更成熟。'],
    '安全除法器',
    'try:\n    a = int(input("a: "))\n    b = int(input("b: "))\n    print(a / b)\nexcept:\n    print("Input error")',
    '把报错提示改得更具体一些。',
    'try:\n    a = int(input("a: "))\n    b = int(input("b: "))\n    print(a / b)\nexcept:\n    print("请输入正确的整数，并避免除数导致程序失败。")',
    '捕获输入不是整数时的异常，并提示用户重新理解输入要求。',
    'try:\n    n = int(input("Enter an integer: "))\n    print(n)\nexcept:\n    print("That is not an integer.")',
    ['会写 try / except。', '知道异常处理的作用。', '会处理输入错误。', '知道程序不应轻易崩掉。'],
    '写一个程序：输入两个整数，输出商；如果输入错误，提示“输入无效”。',
    'try:\n    a = int(input("请输入第一个整数："))\n    b = int(input("请输入第二个整数："))\n    print(a / b)\nexcept:\n    print("输入无效")',
    '这周要让孩子理解：异常处理不是多余，而是程序成熟的表现。',
    {'keyword': '异常处理', 'symbol': 'try / except', 'use': '防止程序崩掉', 'bug': '没有预判输入错误', 'sample': '安全输入'}
)

WEEKS[18] = week_dict(
    18, 'Unit 9 综合应用', '综合项目 1：菜单系统', '把前面的变量、判断、循环拼起来',
    'https://cs50.harvard.edu/python/2022/weeks/3/',
    ['哈佛风格特别重视把零散知识连成完整任务。', '菜单系统是很好的综合训练，因为它会同时用到输入、判断、循环、函数。', '这一周不是学新符号，而是学如何搭一个程序骨架。', '重点不是界面花哨，而是结构清楚。'],
    ['菜单系统像商场导览牌：你先选，再进对应模块。', '综合题会拉开差距，不是因为新知识难，而是因为旧知识要一起工作。', '很多人单点会、综合不会，本质上是不会搭框架。', '这一周要学的是：先搭骨架，再填内容。'],
    '菜单型小工具',
    'print("1. Add")\nprint("2. Exit")\nchoice = input("Choose: ")\nif choice == "1":\n    print("You chose Add")\nelse:\n    print("Bye")',
    '增加一个选项 3，输出 Help。',
    'print("1. Add")\nprint("2. Exit")\nprint("3. Help")\nchoice = input("Choose: ")\nif choice == "1":\n    print("You chose Add")\nelif choice == "3":\n    print("Help")\nelse:\n    print("Bye")',
    '做一个简易成绩菜单：输入成绩，输出等级；输入 0 退出。',
    'while True:\n    score = int(input("Enter score (0 to exit): "))\n    if score == 0:\n        break\n    if score >= 90:\n        print("A")\n    elif score >= 80:\n        print("B")\n    else:\n        print("C")',
    ['会把输入、判断、循环组合。', '会写菜单型程序。', '会分析综合题结构。', '知道先搭框架，再填细节。'],
    '写一个二选一菜单：1 输出 Hello；2 输出 Bye。',
    'print("1. Hello")\nprint("2. Bye")\nchoice = input("Choose: ")\nif choice == "1":\n    print("Hello")\nelse:\n    print("Bye")',
    '这一周不要追求复杂，先让孩子把框架搭出来。',
    {'keyword': '综合项目', 'symbol': '输入 + 判断 + 循环', 'use': '整合多个知识点', 'bug': '程序结构混乱', 'sample': '菜单系统'}
)

WEEKS[19] = week_dict(
    19, 'Unit 9 综合应用', '综合项目 2：数据统计', '用程序像小型 Excel 一样处理数据',
    'https://cs50.harvard.edu/python/2022/weeks/4/',
    ['哈佛会很重视让程序处理数据，而不只是做一步任务。', '平均值、最大值、最小值、计数，都是统计类题目的核心动作。', '这一周会把列表、循环、条件真正放进一类有用的题型中。', '重点是让孩子感受到：程序可以替人做重复的数据处理。'],
    ['这一周像把 Python 变成迷你 Excel。', '数字列表就像一串成绩，程序帮你自动算平均、找最高。', '会做数据统计，说明你已经不是只会写句子，而是在处理信息。', '这周很适合建立‘程序为我算’的成就感。'],
    '平均分计算器',
    'scores = [80, 90, 75, 95]\ntotal = 0\nfor s in scores:\n    total += s\navg = total / len(scores)\nprint(avg)',
    '再输出最高分和最低分。',
    'scores = [80, 90, 75, 95]\ntotal = 0\nfor s in scores:\n    total += s\navg = total / len(scores)\nprint(avg)\nprint(max(scores))\nprint(min(scores))',
    '统计列表中大于 80 的成绩有几个。',
    'scores = [80, 90, 75, 95, 81]\ncount = 0\nfor s in scores:\n    if s > 80:\n        count += 1\nprint(count)',
    ['会求平均值。', '会统计符合条件的个数。', '会处理简单列表数据题。', '会把循环和判断结合起来做统计。'],
    '写一个程序：对列表 [56, 72, 88, 91, 64] 统计及格人数和平均分。',
    'scores = [56, 72, 88, 91, 64]\ncount = 0\ntotal = 0\nfor s in scores:\n    total += s\n    if s >= 60:\n        count += 1\nprint("及格人数：", count)\nprint("平均分：", total / len(scores))',
    '这周很适合讲清楚 total、count、avg 三个角色。',
    {'keyword': '数据统计', 'symbol': 'total / count / avg', 'use': '处理一组数字', 'bug': '平均值公式写错', 'sample': '求平均分'}
)

WEEKS[20] = week_dict(
    20, 'Unit 10 常用结构补充', '元组、集合与模块', '认识更多数据容器和现成工具',
    'https://cs50.harvard.edu/python/2022/weeks/7/',
    ['这一周不只是补概念，而是帮助孩子建立‘不同问题要用不同工具’的意识。', 'tuple 更像不可改的列表，set 更像自动去重的集合，module 则像借来的工具箱。', '真正成熟的程序员思维，不是所有题都只会 list 和 if。', '这一周的重点是：知道什么时候换工具。'],
    ['tuple 像封好的快递箱，装好后不轻易改。', 'set 像不允许重名的名单，重复内容会被自动合并。', 'module 像工具间，你不用自己打铁做扳手，可以先去借。', '这一周是把工具箱再扩充一层。'],
    '不重复名单 + 随机点名',
    'import random\nnames = {"Tom", "Tom", "Amy", "Bob"}\nprint(names)\nprint(random.choice(["Tom", "Amy", "Bob"]))',
    '再加入一个 Lily，并打印集合长度。',
    'import random\nnames = {"Tom", "Tom", "Amy", "Bob"}\nnames.add("Lily")\nprint(names)\nprint(len(names))\nprint(random.choice(["Tom", "Amy", "Bob", "Lily"]))',
    '创建一个 tuple 保存三个月份，并输出第一个；再用 set 对城市列表去重。',
    'months = ("Jan", "Feb", "Mar")\nprint(months[0])\n\ncities = ["Beijing", "Shanghai", "Beijing", "Shenzhen"]\nprint(set(cities))',
    ['知道 tuple 不可改。', '知道 set 自动去重。', '会区分 list / tuple / set。', '知道 import 可以借用现成模块。'],
    '导入 random，随机输出 1 到 6 之间的一个整数，并演示 set 去重。',
    'import random\nprint(random.randint(1, 6))\n\nnums = [1, 2, 2, 3, 3, 4]\nprint(set(nums))',
    '这周不要追求全会，重点是让孩子知道：不同容器和模块各有用处。',
    {'keyword': '元组集合模块', 'symbol': '() / {} / import', 'use': '区分容器并借用工具', 'bug': '把 tuple 和 list 混淆', 'sample': 'set 去重'}
)

WEEKS[21] = week_dict(
    21, 'Unit 11 项目周', '小游戏项目', '让编程变得更好玩，也更有拥有感',
    'https://pll.harvard.edu/course/machine-learning-and-ai-python',
    ['很多哈佛课程都很重视项目驱动，因为兴趣会显著提高学习持续性。', '小游戏项目特别适合训练规则逻辑、输入输出和循环控制。', '这一周的重点不是做大游戏，而是把规则写清楚、让程序跑起来。', '会做小游戏，孩子会第一次强烈感到：这是我做出来的东西。'],
    ['小游戏像小型程序宇宙：有规则、有输入、有反馈。', '哪怕只是猜数字，只要规则跑通，成就感就会很强。', '这一周会把 if、while、变量真正用起来。', '这类项目特别适合建立长期兴趣。'],
    '猜数字小游戏',
    'secret = 5\nguess = int(input("Guess: "))\nif guess == secret:\n    print("Correct!")\nelse:\n    print("Wrong!")',
    '如果猜错，提示 Too high 或 Too low。',
    'secret = 5\nguess = int(input("Guess: "))\nif guess == secret:\n    print("Correct!")\nelif guess > secret:\n    print("Too high")\nelse:\n    print("Too low")',
    '让用户可以连续猜，直到猜对为止。',
    'secret = 5\nwhile True:\n    guess = int(input("Guess: "))\n    if guess == secret:\n        print("Correct!")\n        break\n    elif guess > secret:\n        print("Too high")\n    else:\n        print("Too low")',
    ['会写简单规则游戏。', '会把 while 和 if 组合。', '会让程序持续运行直到成功。', '会分析小游戏逻辑。'],
    '写一个简化版石头剪刀布：输入 rock 或 paper，输出对应提示。',
    'choice = input("rock or paper: ")\nif choice == "rock":\n    print("You chose rock.")\nelse:\n    print("You chose paper.")',
    '这周不要只看对错，更要看孩子是否对‘自己做出东西’有兴趣。',
    {'keyword': '小游戏项目', 'symbol': '规则逻辑', 'use': '做交互小游戏', 'bug': '规则判断写不全', 'sample': '猜数字'}
)

WEEKS[22] = week_dict(
    22, 'Unit 11 项目周', '实用工具项目', '让 Python 真的帮生活做事',
    'https://pll.harvard.edu/course/machine-learning-and-ai-python',
    ['项目驱动学习里，工具项目特别有价值，因为它最容易和真实生活连接。', '当孩子发现程序真的能替自己做事，学习动机会明显增强。', '工具类项目通常不需要复杂界面，但逻辑一定要清楚。', '这一周的重点是：做一个有功能闭环的小工具。'],
    ['工具项目像一个数字小帮手，帮你算、帮你记、帮你判断。', '程序一旦能解决生活小问题，就不只是课程作业，而是有用了。', '这周重点不是花哨，而是‘好用’。', '这类项目特别适合培养‘代码是工具’的意识。'],
    '三合一计算工具',
    'print("1. BMI")\nprint("2. Price")\nchoice = input("Choose: ")\nif choice == "1":\n    weight = float(input("Weight: "))\n    height = float(input("Height: "))\n    print(weight / (height ** 2))\nelse:\n    price = float(input("Price: "))\n    count = int(input("Count: "))\n    print(price * count)',
    '再增加一个 3. Score Average 功能。',
    'print("1. BMI")\nprint("2. Price")\nprint("3. Score Average")\nchoice = input("Choose: ")\nif choice == "1":\n    weight = float(input("Weight: "))\n    height = float(input("Height: "))\n    print(weight / (height ** 2))\nelif choice == "3":\n    a = float(input("Score 1: "))\n    b = float(input("Score 2: "))\n    print((a + b) / 2)\nelse:\n    price = float(input("Price: "))\n    count = int(input("Count: "))\n    print(price * count)',
    '做一个简易学习时间统计器，输入 3 天学习时长，输出总时长。',
    'total = 0\nfor i in range(3):\n    h = float(input("Hours: "))\n    total += h\nprint("Total hours:", total)',
    ['会做小工具型程序。', '会组合多个小功能。', '会根据需求选择合适结构。', '知道工具项目重在可用。'],
    '写一个程序：输入商品单价和数量，输出总价，并判断是否超过 100。',
    'price = float(input("单价："))\ncount = int(input("数量："))\ntotal = price * count\nprint("总价：", total)\nif total > 100:\n    print("超过100")\nelse:\n    print("不超过100")',
    '这周很适合让孩子自己提一个小需求，再把它做成程序。',
    {'keyword': '实用工具', 'symbol': '菜单 + 功能', 'use': '解决生活小任务', 'bug': '功能切换逻辑写乱', 'sample': '多功能计算器'}
)

WEEKS[23] = week_dict(
    23, 'Unit 12 展示周', '项目整理与表达', '不只是会写，还要会讲清楚',
    'https://pll.harvard.edu/course/machine-learning-and-ai-python',
    ['很多项目式课程都会要求学生解释自己的代码，而不只是把代码跑出来。', '真正学会一个程序，不只是能敲出来，还要能说清楚它做什么、怎么做、为什么这样做。', '这一周没有很多新语法，但对考试答题和项目展示都很重要。', '重点是：把代码讲成自然语言。'],
    ['项目表达像给别人导览你的房子：门在哪、客厅在哪、为什么这么设计。', '能讲清楚，说明脑子里的结构已经清楚了。', '很多学生代码会写一点，但说不清思路，这会影响考试和项目表现。', '这周是在从‘会做’走向‘会表达’。'],
    '讲解自己的程序',
    'def add(a, b):\n    return a + b\n\nprint(add(2, 3))',
    '试着用 3 句话解释这段程序在做什么。',
    '1. 先定义一个 add 函数。\n2. 这个函数接收两个参数 a 和 b。\n3. 它返回两个数的和，然后被 print 输出。',
    '把你喜欢的一段程序，写出‘输入、处理、输出’三步说明。',
    '输入：用户输入数字。\n处理：程序判断奇偶。\n输出：显示“偶数”或“奇数”。',
    ['会讲清程序做什么。', '会拆输入、处理、输出。', '会做项目说明。', '会用自然语言复盘代码。'],
    '写一个小程序，并在注释里说明它做什么。',
    '# 这个程序输入两个数，输出它们的和\na = float(input("请输入第一个数："))\nb = float(input("请输入第二个数："))\nprint(a + b)',
    '这周可多让孩子口述思路，而不是只看运行结果。',
    {'keyword': '项目表达', 'symbol': '输入-处理-输出', 'use': '讲清代码思路', 'bug': '会写但不会说', 'sample': '程序说明'}
)

WEEKS[24] = week_dict(
    24, 'Unit 12 展示周', '毕业回顾与总复习', '把前面学过的知识真正串起来',
    'https://pll.harvard.edu/course/machine-learning-and-ai-python',
    ['最后一周不再追求新知识，而是把旧知识串成体系。', '真正有效的复习，不是把知识重新堆一遍，而是整理成结构化地图。', '如果孩子能说出变量、判断、循环、函数、数据结构之间的关系，说明已经真正入门。', '这一周的重点是整合、查漏和建立信心。'],
    ['24 周像走完一条山路，现在要在山顶回头看整张地图。', '变量、判断、循环、函数，不再是零散点，而是一整套工具链。', '总复习不是‘更累’，而是‘更清楚’。', '这周最重要的是把知识点讲顺、练顺、考顺。'],
    '总复习清单程序',
    'topics = ["variable", "if", "loop", "function"]\nfor t in topics:\n    print("Review:", t)',
    '把 topics 扩展为 6 个知识点，并输出需要重点复习的 3 个。',
    'topics = ["variable", "type", "if", "loop", "function", "list"]\nfor t in topics:\n    print("Review:", t)\n\nfor t in topics[:3]:\n    print("Key review:", t)',
    '做一个小复习菜单，选择 1 输出变量，2 输出循环，3 输出函数。',
    'print("1. variable")\nprint("2. loop")\nprint("3. function")\nchoice = input("Choose: ")\nif choice == "1":\n    print("Review variable")\nelif choice == "2":\n    print("Review loop")\nelse:\n    print("Review function")',
    ['会串联前面 24 周内容。', '知道每类题该用什么工具。', '会回顾高频错题。', '会以考试视角做总复盘。'],
    '写一个程序：输出你最需要复习的 3 个 Python 主题。',
    'topics = ["if", "while", "function"]\nfor t in topics:\n    print("Need review:", t)',
    '最后一周最重要的不是再加新东西，而是把旧东西讲顺、练顺、考顺。',
    {'keyword': '总复习', 'symbol': '整合', 'use': '串联全部知识', 'bug': '知识点割裂', 'sample': '复习菜单'}
)


# ---- Customized overrides for weeks 2-24 based on the requested teaching logic ----
CUSTOM_OVERRIDES = {
    2: dict(
        harvard_understanding=[
            "哈佛这里会先让学生看到：同样看起来像‘18’的内容，电脑会区分它到底是数字 18，还是文字 '18'。",
            "老师会通过 input() 的例子讲：用户输入进来的内容，程序默认先按字符串理解，所以很多计算题第一步不是算，而是先判断类型。",
            "哈佛的讲法不是先背 int、float、str 定义，而是先让学生感受到：数据类型不同，程序能做的事情就不同。",
            "这一周真正的目标是：会判断一个值是什么类型，知道什么时候要做类型转换。",
        ],
        vivid_notes=[
            "把数据类型想成收纳盒：数字盒里装的是能计算的内容，文字盒里装的是能显示和拼接的内容。",
            "18 像一个人名牌上的数字照片，'18' 像写在纸上的两个字符，看着像，身份却不同。",
            "这一周像在教孩子给数据办身份证：你得先知道它是谁，才能决定怎么用。",
            "所以这周不是死背术语，而是练‘看懂这个值到底是什么’。",
        ],
        lab_title="成绩求和小实验",
        follow_code='''a = int(input("请输入第一个分数："))
b = int(input("请输入第二个分数："))
print("总分：", a + b)''',
        modify_task="把程序改成：再输入第三个分数，并输出平均分。",
        modify_answer='''a = int(input("请输入第一个分数："))
b = int(input("请输入第二个分数："))
c = int(input("请输入第三个分数："))
total = a + b + c
print("总分：", total)
print("平均分：", total / 3)''',
        challenge_task="输入商品单价和数量，输出总价，要求单价用 float，数量用 int。",
        challenge_answer='''price = float(input("请输入单价："))
count = int(input("请输入数量："))
total = price * count
print("总价：", total)''',
    ),
    3: dict(
        harvard_understanding=[
            "哈佛这里会先让学生观察：程序不会猜你的想法，它只会严格按照代码从上到下执行。",
            "老师通常会用一小段输入、计算、输出的代码演示：哪一行先写，哪一步就先发生。",
            "哈佛的重点不是把‘顺序结构’当名词记住，而是让学生真正理解：程序结果对不对，常常取决于步骤顺序对不对。",
            "这一周真正的目标是：会按‘输入→处理→输出’去安排代码顺序。",
        ],
        vivid_notes=[
            "把顺序结构想成做早餐：先拿面包、再加热、再装盘，步骤乱了，结果就乱。",
            "程序像一位特别听话的助手，你让它先做什么，它就先做什么，不会替你补脑。",
            "很多孩子不是不会写代码，而是像先端盘子再炒菜，顺序排反了。",
            "所以这周不是学新招式，而是练‘把步骤排正确’。",
        ],
        lab_title="三步购物小实验",
        follow_code='''name = input("商品名：")
price = float(input("单价："))
count = int(input("数量："))
total = price * count
print(name)
print("总价：", total)''',
        modify_task="在计算 total 前增加一句“正在计算……”，体会代码按顺序执行。",
        modify_answer='''name = input("商品名：")
price = float(input("单价："))
count = int(input("数量："))
print("正在计算……")
total = price * count
print(name)
print("总价：", total)''',
        challenge_task="输入姓名、语文、数学，按顺序输出姓名、总分、平均分。",
        challenge_answer='''name = input("姓名：")
chinese = float(input("语文："))
math = float(input("数学："))
total = chinese + math
avg = total / 2
print("姓名：", name)
print("总分：", total)
print("平均分：", avg)''',
    ),
    4: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：if 的本质，不是背格式，而是让程序学会在条件成立时才行动。",
            "老师会把条件判断讲成一个‘门卫逻辑’：条件满足，门打开；条件不满足，程序就不进去。",
            "哈佛的讲法通常会用布尔结果带学生看清楚：条件判断其实是在问程序一句‘是真的吗？’。",
            "这一周真正的目标是：会写最基础的 if 判断，让程序根据条件做反应。",
        ],
        vivid_notes=[
            "把 if 想成门禁卡：刷卡通过，门开；条件不满足，门不开。",
            "程序第一次像有了‘会不会做这件事’的判断力。",
            "生活里‘如果下雨就带伞’，代码里就是 if 条件成立就执行。",
            "所以这周不是背 if，而是学会‘先判断，再动作’。",
        ],
        lab_title="年龄判断小实验",
        follow_code='''age = int(input("请输入年龄："))
if age >= 18:
    print("你已经成年")''',
        modify_task="把程序改成：如果分数大于等于 60，就输出“及格”。",
        modify_answer='''score = int(input("请输入分数："))
if score >= 60:
    print("及格")''',
        challenge_task="输入一个数字，如果它是偶数，就输出“这是偶数”。",
        challenge_answer='''num = int(input("请输入一个数字："))
if num % 2 == 0:
    print("这是偶数")''',
    ),
    5: dict(
        harvard_understanding=[
            "哈佛这里会先让学生看到：现实问题往往不是‘做或不做’两种情况，而是有多种可能结果。",
            "老师会把 if / elif / else 讲成一条分流路线：先判断第一种，再判断第二种，最后处理剩下的情况。",
            "哈佛强调分支顺序很重要，因为程序只会按你写下来的先后去检查条件。",
            "这一周真正的目标是：会写完整分支，让程序在不同情况下给出不同结果。",
        ],
        vivid_notes=[
            "把多分支想成岔路口：走左边、走右边、还是走默认那条路。",
            "成绩评级就是典型多分支：90 分以上一个结果，80 分以上又是另一个结果。",
            "程序不会自己挑最合适的路，它只会按你设计的分支顺序走。",
            "所以这周是在练‘把不同情况分清楚’。",
        ],
        lab_title="成绩等级小实验",
        follow_code='''score = int(input("请输入分数："))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")''',
        modify_task="把程序改成四档：A、B、C、D。",
        modify_answer='''score = int(input("请输入分数："))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")''',
        challenge_task="输入天气：sunny / rainy / snowy，输出不同提示。",
        challenge_answer='''weather = input("请输入天气：")
if weather == "sunny":
    print("适合出门")
elif weather == "rainy":
    print("记得带伞")
else:
    print("注意保暖")''',
    ),
    6: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：for 循环适合处理‘重复固定次数’的问题。",
            "老师会通过 range() 带学生看到：程序并不是神奇地重复，而是按设定好的次数一轮一轮执行。",
            "哈佛的重点不是先记语法，而是让学生知道：当你已经清楚要重复多少次时，for 循环最合适。",
            "这一周真正的目标是：会用 for + range() 让程序重复执行固定次数。",
        ],
        vivid_notes=[
            "把 for 想成老师点名：点 5 次，就叫 5 个人。",
            "如果你已经知道要做 10 次，for 就像提前排好队的重复按钮。",
            "它不像 while 那样看条件一直转，而是按次数有节奏地走。",
            "所以这周不是练花样，而是练‘确定次数的重复’。",
        ],
        lab_title="打印数字小实验",
        follow_code='''for i in range(1, 6):
    print(i)''',
        modify_task="把程序改成打印 1 到 10。",
        modify_answer='''for i in range(1, 11):
    print(i)''',
        challenge_task="用 for 循环输出 5 句“我在学 Python”。",
        challenge_answer='''for i in range(5):
    print("我在学 Python")''',
    ),
    7: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：while 循环适合‘条件满足就继续’这一类问题。",
            "老师会强调 while 不是按次数重复，而是看条件是否还成立，所以变量更新非常关键。",
            "哈佛常会用输入验证这类场景解释：当答案没对，就继续问；答案对了，才停下来。",
            "这一周真正的目标是：会写 while 条件循环，并知道如何让它停下来。",
        ],
        vivid_notes=[
            "把 while 想成‘只要没到站，就继续走’。",
            "它像一个看条件的保安，不是看次数，而是看门口条件还成不成立。",
            "如果忘了更新变量，程序就会像原地转圈，形成死循环。",
            "所以这周不是只会写 while，而是会让 while 合理开始、合理结束。",
        ],
        lab_title="密码验证小实验",
        follow_code='''password = "1234"
user_input = input("请输入密码：")
while user_input != password:
    user_input = input("密码错误，请重新输入：")
print("登录成功")''',
        modify_task="把正确密码改成 8888，并修改提示语。",
        modify_answer='''password = "8888"
user_input = input("请输入密码：")
while user_input != password:
    user_input = input("不对，再输一次：")
print("登录成功")''',
        challenge_task="输入一个数字，只要它小于 10，就持续让用户重新输入。",
        challenge_answer='''num = int(input("请输入一个数字："))
while num < 10:
    num = int(input("太小了，请重新输入："))
print("输入结束")''',
    ),
    8: dict(
        harvard_understanding=[
            "哈佛这里会先让学生看到：循环不只是重复打印，它还能在重复过程中累计结果。",
            "老师会用 total、count 这样的变量解释：每一轮循环都可以顺手更新统计信息。",
            "哈佛的重点是让学生理解‘循环 + 变量更新’如何一起工作，这才是综合循环的价值。",
            "这一周真正的目标是：会在循环里做累加、计数和简单统计。",
        ],
        vivid_notes=[
            "把循环综合想成记账：每来一笔，就把总数更新一下。",
            "循环像一圈一圈跑步，total 像边跑边记下已经跑了多少米。",
            "count 负责数次数，total 负责加结果，它们像两个小助手。",
            "所以这周是在练‘重复做事时顺手把结果记下来’。",
        ],
        lab_title="1到100求和小实验",
        follow_code='''total = 0
for i in range(1, 101):
    total += i
print(total)''',
        modify_task="把程序改成求 1 到 50 的和。",
        modify_answer='''total = 0
for i in range(1, 51):
    total += i
print(total)''',
        challenge_task="统计 1 到 20 中有多少个偶数。",
        challenge_answer='''count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1
print(count)''',
    ),
    9: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：函数的意义不是为了变复杂，而是为了把重复工作装进一个可以反复调用的工具。",
            "老师会先写出重复代码，再引出 def，让学生感受到函数是在帮程序‘收纳动作’。",
            "哈佛讲函数时很强调命名，因为函数名应该直接表达‘这个工具是干什么的’。",
            "这一周真正的目标是：会定义函数，也会调用函数。",
        ],
        vivid_notes=[
            "把函数想成家里的小家电：按下同一个按钮，它就完成固定工作。",
            "你不需要每次都重新搭过程，函数就是把步骤打包好。",
            "如果一段代码会反复出现，就像每天都要烧水，这时候就该有个‘工具’。",
            "所以这周是在练‘把重复劳动收进工具箱’。",
        ],
        lab_title="问候函数小实验",
        follow_code='''def say_hello():
    print("Hello")

say_hello()''',
        modify_task="把函数改成 say_hi()，输出 Hi。",
        modify_answer='''def say_hi():
    print("Hi")

say_hi()''',
        challenge_task="写一个函数 print_line()，调用后输出 10 个 *。",
        challenge_answer='''def print_line():
    print("*" * 10)

print_line()''',
    ),
    10: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：没有参数和返回值的函数只是第一步，真正有用的函数要能接收信息，也能把结果交回来。",
            "老师会把参数讲成‘送进工具箱的材料’，把返回值讲成‘工具做完后交出的成品’。",
            "哈佛强调 return，因为它代表函数真正算出了结果，而不是只在屏幕上说一句话。",
            "这一周真正的目标是：会写带参数的函数，并会用 return 返回结果。",
        ],
        vivid_notes=[
            "把参数想成做蛋糕时放进去的鸡蛋和面粉，把返回值想成最后拿出来的蛋糕。",
            "函数不是只会表演，它还要能接活、出结果。",
            "print 像当众把话说出来，return 像把结果递回给程序继续使用。",
            "所以这周是在练‘函数真正开始有用了’。",
        ],
        lab_title="加法函数小实验",
        follow_code='''def add(a, b):
    return a + b

result = add(3, 5)
print(result)''',
        modify_task="把程序改成乘法函数 multiply(a, b)。",
        modify_answer='''def multiply(a, b):
    return a * b

result = multiply(3, 5)
print(result)''',
        challenge_task="写一个函数 bigger(a, b)，返回较大的那个数。",
        challenge_answer='''def bigger(a, b):
    if a > b:
        return a
    return b

print(bigger(8, 5))''',
    ),
    11: dict(
        harvard_understanding=[
            "哈佛这里会先让学生看到：程序处理的很多都不是数字，而是名字、句子、标题这类文字信息。",
            "老师会通过大小写转换、长度判断、拼接显示这些具体动作，让学生理解字符串也能被程序加工。",
            "哈佛的讲法不是把字符串当成死定义，而是让学生看见：文字也有规则，也能被操作。",
            "这一周真正的目标是：会做基础字符串处理，比如拼接、改大小写、求长度。",
        ],
        vivid_notes=[
            "把字符串想成一串排好队的字母珠子，你可以数它、拼它、改它。",
            "数字像砖块，字符串像写着字的卡片，虽然不能乱算，但可以整理和展示。",
            "名字、城市、课程名，这些在程序里本质上都是字符串。",
            "所以这周是在练‘让程序会处理文字’。",
        ],
        lab_title="名字格式化小实验",
        follow_code='''name = input("请输入名字：")
print(name.upper())
print(name.lower())
print(len(name))''',
        modify_task="再输出 title() 格式，并显示欢迎语。",
        modify_answer='''name = input("请输入名字：")
print(name.upper())
print(name.lower())
print(name.title())
print("欢迎你，", name.title())''',
        challenge_task="输入 first_name 和 last_name，拼接成完整姓名并输出长度。",
        challenge_answer='''first_name = input("First name: ")
last_name = input("Last name: ")
full_name = first_name + " " + last_name
print(full_name)
print(len(full_name))''',
    ),
    12: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：当程序需要处理一串文字时，字符串其实是按位置排好的字符序列。",
            "老师会通过索引和切片让学生看到：程序不仅能看整段文字，还能精准取出其中一部分。",
            "哈佛的重点不是背 s[a:b] 这种写法，而是理解：位置决定你能从字符串里拿到什么。",
            "这一周真正的目标是：会用索引和切片从字符串里提取信息。",
        ],
        vivid_notes=[
            "把字符串切片想成剪彩带：从哪开始剪，到哪结束，拿到的就是中间那一段。",
            "每个字符都像排队站位，索引就是它们的座位号。",
            "你不一定要整句都拿，可以只取前 3 位、后 4 位、中间一段。",
            "所以这周是在练‘从文字里精准取信息’。",
        ],
        lab_title="手机号切片小实验",
        follow_code='''phone = input("请输入手机号：")
print(phone[:3])
print(phone[-4:])''',
        modify_task="再输出手机号的第 1 位字符和最后 1 位字符。",
        modify_answer='''phone = input("请输入手机号：")
print(phone[:3])
print(phone[-4:])
print(phone[0])
print(phone[-1])''',
        challenge_task="输入一个英文单词，输出首字母、末字母和中间部分。",
        challenge_answer='''word = input("请输入一个单词：")
print(word[0])
print(word[-1])
print(word[1:-1])''',
    ),
    13: dict(
        harvard_understanding=[
            "哈佛这里会先让学生从‘一个变量装一个值’走到‘一个列表装一组值’。",
            "老师会强调列表的价值不在中括号本身，而在于程序终于能一次管理很多数据。",
            "哈佛常会通过名字清单、成绩清单这类例子，让学生理解列表是有顺序、可修改的一组数据。",
            "这一周真正的目标是：会创建列表、读取元素、添加元素。",
        ],
        vivid_notes=[
            "把列表想成一整排抽屉，不再只有一个小盒子。",
            "以前变量一次只装一个苹果，列表现在可以装一篮苹果。",
            "每个元素都有位置，程序可以按位置拿东西。",
            "所以这周是在练‘一次管理一组数据’。",
        ],
        lab_title="水果清单小实验",
        follow_code='''fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(len(fruits))''',
        modify_task="往列表里再加入 grape，并输出整个列表。",
        modify_answer='''fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)
print(len(fruits))''',
        challenge_task="建立一个三门学科列表，并输出最后一个元素。",
        challenge_answer='''subjects = ["Math", "English", "Physics"]
print(subjects[-1])''',
    ),
    14: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：列表有了一组数据后，下一步就要学会把这一组数据逐个处理。",
            "老师会把 for 和 list 连起来讲，因为遍历列表是最自然、最常用的批量处理方式。",
            "哈佛的重点不是只是输出每个元素，而是让学生看到：遍历后还能判断、筛选、统计。",
            "这一周真正的目标是：会用 for 循环遍历列表，并做简单批量处理。",
        ],
        vivid_notes=[
            "把列表遍历想成老师点名：名单在手里，一个一个叫过去。",
            "程序不需要你手动盯每个元素，它可以自己巡一遍。",
            "一旦会遍历，程序就像有了批处理能力。",
            "所以这周是在练‘一组数据一个个过一遍’。",
        ],
        lab_title="成绩遍历小实验",
        follow_code='''scores = [70, 82, 95, 60, 88]
for s in scores:
    print(s)''',
        modify_task="只输出大于 80 的成绩。",
        modify_answer='''scores = [70, 82, 95, 60, 88]
for s in scores:
    if s > 80:
        print(s)''',
        challenge_task="统计列表中及格成绩（>=60）的个数。",
        challenge_answer='''scores = [70, 82, 95, 60, 88]
count = 0
for s in scores:
    if s >= 60:
        count += 1
print(count)''',
    ),
    15: dict(
        harvard_understanding=[
            "哈佛这里会先让学生看到：并不是所有数据都适合按位置找，有些信息更适合按名字去找。",
            "老师会把字典讲成 key 和 value 的配对关系，让学生理解‘标签→内容’这一层结构。",
            "哈佛讲字典时，常用学生信息、商品信息这类现实例子，让学生看到它和列表的不同。",
            "这一周真正的目标是：会创建字典，并通过 key 读取对应的值。",
        ],
        vivid_notes=[
            "把字典想成通讯录：你找的是姓名，不是第几行。",
            "key 像抽屉外的标签，value 像抽屉里的东西。",
            "如果信息本来就带名字，字典比列表更顺手。",
            "所以这周是在练‘按标签找信息’。",
        ],
        lab_title="学生信息卡小实验",
        follow_code='''student = {"name": "Tom", "score": 95}
print(student["name"])
print(student["score"])''',
        modify_task="再增加一个 city 字段，并输出它。",
        modify_answer='''student = {"name": "Tom", "score": 95, "city": "Boston"}
print(student["city"])''',
        challenge_task="写一个字典保存一本书的 title 和 price，并输出 price。",
        challenge_answer='''book = {"title": "Python", "price": 88}
print(book["price"])''',
    ),
    16: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：程序不应该只会当场运行，还应该学会把结果保存下来。",
            "老师会通过 open()、write()、read() 让学生看到：程序可以和外部文件发生联系。",
            "哈佛讲文件时，很重视 r 和 w 模式的区别，因为这决定程序是在读旧内容，还是写新内容。",
            "这一周真正的目标是：会做最基本的文件写入和读取。",
        ],
        vivid_notes=[
            "把文件想成笔记本，程序现在不只是会想，还会记。",
            "变量像短时记忆，文件像长期档案柜。",
            "程序一关，变量会消失；写进文件，内容就留下来了。",
            "所以这周是在练‘让程序把信息存住’。",
        ],
        lab_title="学习日志小实验",
        follow_code='''with open("note.txt", "w", encoding="utf-8") as f:
    f.write("I am learning Python.")''',
        modify_task="让用户输入今天主题，再写入 note.txt。",
        modify_answer='''topic = input("Today's topic: ")
with open("note.txt", "w", encoding="utf-8") as f:
    f.write(topic)''',
        challenge_task="先写入 diary.txt，再把内容读取出来。",
        challenge_answer='''with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("Today is a good day.")

with open("diary.txt", "r", encoding="utf-8") as f:
    print(f.read())''',
    ),
    17: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：好程序不是永远不出错，而是出错时也能有处理方案。",
            "老师会把 try / except 讲成给程序提前准备‘应急预案’，尤其是面对用户输入时。",
            "哈佛会用整数输入、除法错误这类最常见场景，让学生知道异常并不罕见。",
            "这一周真正的目标是：会写 try / except，让程序在出错时不直接崩掉。",
        ],
        vivid_notes=[
            "把异常处理想成下雨带伞，不是盼着出事，而是提前准备。",
            "用户输错内容，就像路上突然有坑，程序得学会绕过去。",
            "没有异常处理的程序很脆弱，一碰就翻车。",
            "所以这周是在练‘让程序更稳’。",
        ],
        lab_title="安全除法小实验",
        follow_code='''try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except:
    print("Input error")''',
        modify_task="把报错提示改得更具体一些。",
        modify_answer='''try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except:
    print("请输入正确的整数，并避免除数导致程序失败。")''',
        challenge_task="捕获输入不是整数时的异常，并提示用户重新理解输入要求。",
        challenge_answer='''try:
    n = int(input("Enter an integer: "))
    print(n)
except:
    print("That is not an integer.")''',
    ),
    18: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：综合题的关键不是新知识，而是把已经学过的变量、判断、循环组合起来。",
            "老师会通过菜单系统这种小项目，让学生看到程序骨架应该先搭起来，再往里填功能。",
            "哈佛强调结构感，因为很多孩子单点会写，但一到综合题就乱。",
            "这一周真正的目标是：会搭一个简单菜单系统，把前面知识真正连起来。",
        ],
        vivid_notes=[
            "把菜单系统想成商场导览牌：先选编号，再去对应功能。",
            "综合项目不是更难的新知识，而是让旧知识一起上班。",
            "程序骨架像房子的框架，先立起来，房间再慢慢填。",
            "所以这周是在练‘把零件拼成完整东西’。",
        ],
        lab_title="菜单系统小实验",
        follow_code='''print("1. Add")
print("2. Exit")
choice = input("Choose: ")
if choice == "1":
    print("You chose Add")
else:
    print("Bye")''',
        modify_task="增加一个选项 3，输出 Help。",
        modify_answer='''print("1. Add")
print("2. Exit")
print("3. Help")
choice = input("Choose: ")
if choice == "1":
    print("You chose Add")
elif choice == "3":
    print("Help")
else:
    print("Bye")''',
        challenge_task="做一个简易成绩菜单：输入成绩，输出等级；输入 0 退出。",
        challenge_answer='''while True:
    score = int(input("Enter score (0 to exit): "))
    if score == 0:
        break
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")''',
    ),
    19: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：数据统计不是靠一眼看出来，而是靠程序一轮一轮把结果累出来。",
            "老师会通过 total、count、avg 这些变量，让学生看到统计题的骨架其实很清楚。",
            "哈佛讲这类内容时，会反复强调‘先遍历，再更新结果’，而不是直接猜答案。",
            "这一周真正的目标是：会对一组数据做总和、平均值、计数等基础统计。",
        ],
        vivid_notes=[
            "把数据统计想成迷你 Excel：数字进来，程序帮你自动汇总。",
            "total 像总账本，count 像计数器，avg 像最后算出的平均结果。",
            "这时候程序开始真正替人做重复的数据工作。",
            "所以这周是在练‘让程序帮我算一组数据’。",
        ],
        lab_title="平均分统计小实验",
        follow_code='''scores = [80, 90, 75, 95]
total = 0
for s in scores:
    total += s
avg = total / len(scores)
print(avg)''',
        modify_task="再输出最高分和最低分。",
        modify_answer='''scores = [80, 90, 75, 95]
total = 0
for s in scores:
    total += s
avg = total / len(scores)
print(avg)
print(max(scores))
print(min(scores))''',
        challenge_task="统计列表中大于 80 的成绩有几个。",
        challenge_answer='''scores = [80, 90, 75, 95, 81]
count = 0
for s in scores:
    if s > 80:
        count += 1
print(count)''',
    ),
    20: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：不同问题适合不同工具，不是所有数据都只用一种结构。",
            "老师会把 tuple、set、module 分开讲清楚：哪些适合不改，哪些适合去重，哪些是现成可借的工具。",
            "哈佛强调对比学习，因为只有比较过 list、tuple、set，孩子才知道什么时候该换工具。",
            "这一周真正的目标是：认识元组、集合、模块，并知道它们各自的基本用途。",
        ],
        vivid_notes=[
            "tuple 像封好的礼盒，装好后不轻易改。",
            "set 像不允许重复名字的名单，重复内容会自动合并。",
            "module 像学校工具室，你不用自己造锤子，可以先借现成工具。",
            "所以这周是在练‘遇到不同问题，换合适工具’。",
        ],
        lab_title="集合去重与模块小实验",
        follow_code='''import random
names = {"Tom", "Tom", "Amy", "Bob"}
print(names)
print(random.choice(["Tom", "Amy", "Bob"]))''',
        modify_task="再加入一个 Lily，并打印集合长度。",
        modify_answer='''import random
names = {"Tom", "Tom", "Amy", "Bob"}
names.add("Lily")
print(names)
print(len(names))
print(random.choice(["Tom", "Amy", "Bob", "Lily"]))''',
        challenge_task="创建一个 tuple 保存三个月份，并输出第一个；再用 set 对城市列表去重。",
        challenge_answer='''months = ("Jan", "Feb", "Mar")
print(months[0])

cities = ["Beijing", "Shanghai", "Beijing", "Shenzhen"]
print(set(cities))''',
    ),
    21: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：项目不是为了好看，而是为了把前面学过的规则逻辑真正跑起来。",
            "老师做小游戏时，通常会把重点放在规则设计、输入反馈和循环控制，而不是复杂画面。",
            "哈佛式项目学习很强调‘从一个最小可运行版本开始’，先让游戏能玩，再慢慢加规则。",
            "这一周真正的目标是：用已学知识做一个能互动的小游戏。",
        ],
        vivid_notes=[
            "小游戏像一个小小程序世界：有规则、有判断、有结果。",
            "哪怕只是猜数字，只要能玩起来，孩子就会很有拥有感。",
            "这周不是追求大制作，而是体验‘我写的程序真的能玩’。",
            "所以这周是在练‘把代码变成可互动的小作品’。",
        ],
        lab_title="猜数字小游戏",
        follow_code='''secret = 5
guess = int(input("Guess: "))
if guess == secret:
    print("Correct!")
else:
    print("Wrong!")''',
        modify_task="如果猜错，提示 Too high 或 Too low。",
        modify_answer='''secret = 5
guess = int(input("Guess: "))
if guess == secret:
    print("Correct!")
elif guess > secret:
    print("Too high")
else:
    print("Too low")''',
        challenge_task="让用户可以连续猜，直到猜对为止。",
        challenge_answer='''secret = 5
while True:
    guess = int(input("Guess: "))
    if guess == secret:
        print("Correct!")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")''',
    ),
    22: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：一个实用工具项目，不一定复杂，但一定要能真正解决一个小问题。",
            "老师做工具项目时，通常会先明确功能，再决定用菜单、判断、循环还是函数去实现。",
            "哈佛强调工具意识，因为程序真正有生命力，往往来自它是否能帮人完成任务。",
            "这一周真正的目标是：做一个简单但完整的小工具。",
        ],
        vivid_notes=[
            "实用工具像数字小助手，帮你计算、统计、判断。",
            "当程序开始替生活做事，孩子会第一次明显感到‘代码有用’。",
            "这周不是比花哨，而是比有没有真正解决问题。",
            "所以这周是在练‘把需求做成工具’。",
        ],
        lab_title="多功能计算器小实验",
        follow_code='''print("1. BMI")
print("2. Price")
choice = input("Choose: ")
if choice == "1":
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    print(weight / (height ** 2))
else:
    price = float(input("Price: "))
    count = int(input("Count: "))
    print(price * count)''',
        modify_task="再增加一个 3. Score Average 功能。",
        modify_answer='''print("1. BMI")
print("2. Price")
print("3. Score Average")
choice = input("Choose: ")
if choice == "1":
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    print(weight / (height ** 2))
elif choice == "3":
    a = float(input("Score 1: "))
    b = float(input("Score 2: "))
    print((a + b) / 2)
else:
    price = float(input("Price: "))
    count = int(input("Count: "))
    print(price * count)''',
        challenge_task="做一个简易学习时间统计器，输入 3 天学习时长，输出总时长。",
        challenge_answer='''total = 0
for i in range(3):
    h = float(input("Hours: "))
    total += h
print("Total hours:", total)''',
    ),
    23: dict(
        harvard_understanding=[
            "哈佛这里会先让学生理解：项目完成不等于学习结束，真正会了的人还能把自己的代码讲清楚。",
            "老师会把程序表达拆成‘输入、处理、输出’三部分，帮助学生形成清晰的讲解结构。",
            "哈佛强调解释能力，因为能说清楚，就说明脑子里的逻辑已经真正理顺了。",
            "这一周真正的目标是：会用自然语言讲清楚程序在做什么、怎么做。",
        ],
        vivid_notes=[
            "项目表达像带别人参观你的房子：门在哪里、客厅在哪里、为什么这样设计。",
            "很多人能写一点代码，但说不清思路，这说明结构还没真正成型。",
            "会表达，程序才不只是‘跑出来了’，而是‘真的懂了’。",
            "所以这周是在练‘把代码翻译成人话’。",
        ],
        lab_title="程序讲解小实验",
        follow_code='''def add(a, b):
    return a + b

print(add(2, 3))''',
        modify_task="试着用 3 句话解释这段程序在做什么。",
        modify_answer='''1. 先定义一个 add 函数。
2. 这个函数接收两个参数 a 和 b。
3. 它返回两个数的和，然后被 print 输出。''',
        challenge_task="把你喜欢的一段程序，写出‘输入、处理、输出’三步说明。",
        challenge_answer='''输入：用户输入数字。
处理：程序判断奇偶。
输出：显示“偶数”或“奇数”。''',
    ),
    24: dict(
        harvard_understanding=[
            "哈佛这里会先让学生回头梳理：变量、判断、循环、函数、数据结构之间到底是怎么连接的。",
            "老师做总复习时，不会只把知识点重新念一遍，而是会帮助学生把零散内容串成一张结构地图。",
            "哈佛强调复盘能力，因为真正入门不是每章都见过，而是能在脑子里形成整体框架。",
            "这一周真正的目标是：把 24 周知识讲顺、连顺、用顺。",
        ],
        vivid_notes=[
            "总复习像爬到山顶后回头看整条路，前面每一个弯现在都能串起来。",
            "变量像起点，判断和循环像路上的动作，函数和数据结构像装备工具。",
            "复习不是把东西再堆一遍，而是让脑子里的地图更清楚。",
            "所以这周是在练‘把零散知识连成一整套工具链’。",
        ],
        lab_title="复习菜单小实验",
        follow_code='''topics = ["variable", "if", "loop", "function"]
for t in topics:
    print("Review:", t)''',
        modify_task="把 topics 扩展为 6 个知识点，并输出需要重点复习的 3 个。",
        modify_answer='''topics = ["variable", "type", "if", "loop", "function", "list"]
for t in topics:
    print("Review:", t)

for t in topics[:3]:
    print("Key review:", t)''',
        challenge_task="做一个小复习菜单，选择 1 输出变量，2 输出循环，3 输出函数。",
        challenge_answer='''print("1. variable")
print("2. loop")
print("3. function")
choice = input("Choose: ")
if choice == "1":
    print("Review variable")
elif choice == "2":
    print("Review loop")
else:
    print("Review function")''',
    ),
}

for _week, _cfg in CUSTOM_OVERRIDES.items():
    WEEKS[_week].harvard_understanding = _cfg["harvard_understanding"]
    WEEKS[_week].vivid_notes = _cfg["vivid_notes"]
    WEEKS[_week].lab_title = _cfg["lab_title"]
    WEEKS[_week].follow_code = _cfg["follow_code"]
    WEEKS[_week].follow_answer = _cfg["follow_code"]
    WEEKS[_week].modify_task = _cfg["modify_task"]
    WEEKS[_week].modify_answer = _cfg["modify_answer"]
    WEEKS[_week].challenge_task = _cfg["challenge_task"]
    WEEKS[_week].challenge_answer = _cfg["challenge_answer"]

if "completed_weeks" not in st.session_state:
    st.session_state.completed_weeks = set()
if "notes" not in st.session_state:
    st.session_state.notes = {i: "" for i in range(1, 25)}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = {}


def render_week(week_num: int):
    week = WEEKS[week_num]

    top_left, top_right = st.columns([3, 1])
    with top_left:
        st.markdown(f"# Week {week.week} | {week.title}")
        st.markdown(f"### {week.unit}")
        st.markdown(f"## 🎯 本周主题：{week.theme}")
        link_button("Open Harvard Course Link", week.harvard_link)
    with top_right:
        st.markdown("### 完成状态")
        st.markdown("## 进行中" if week.week not in st.session_state.completed_weeks else "## 已完成")
        if st.button("✅ 标记本周完成", key=f"done_{week.week}"):
            mark_week_complete(week.week)
            st.success("已记录完成")

    st.markdown("---")
    left, right = st.columns(2)

    with left:
        card_title("🧠", "哈佛理解课")
        for item in week.harvard_understanding:
            st.write(f"- {item}")

        card_title("🌟", "生动讲解课")
        for item in week.vivid_notes:
            st.write(f"- {item}")

    with right:
        card_title("🧪", "动手实验室（趣味游戏）")
        st.markdown(f"**实验主题：{week.lab_title}**")
        st.code(week.follow_code, language="python")
        with st.expander("查看跟敲参考答案"):
            st.code(week.follow_answer, language="python")

        st.markdown(f"**微改任务：** {week.modify_task}")
        with st.expander("查看微改参考答案"):
            st.code(week.modify_answer, language="python")

        st.markdown(f"**小挑战：** {week.challenge_task}")
        with st.expander("查看小挑战参考答案"):
            st.code(week.challenge_answer, language="python")

        card_title("🎯", "考试重点")
        for item in week.exam_focus:
            st.write(f"- {item}")

        card_title("💻", "写代码题")
        st.write(week.write_code_prompt)
        with st.expander("查看写代码题参考答案"):
            st.code(week.write_code_answer, language="python")

        card_title("✍️", "本周学习笔记")
        st.session_state.notes[week.week] = st.text_area(
            "写下本周最重要的 3 句话",
            value=st.session_state.notes[week.week],
            key=f"note_{week.week}",
            height=120
        )

    st.markdown("---")
    card_title("📝", "周测系统（15题｜中国国内大学计算机考试风格）")
    answers = {}
    objective_total = 0
    objective_score = 0

    for idx, q in enumerate(week.quiz, start=1):
        st.markdown(f"**第{idx}题：{q.prompt}**")
        st.caption(q.reference)

        if q.qtype in ["single", "judge"]:
            selected = st.radio(
                f"week_{week.week}_q_{idx}",
                q.options,
                key=f"week_{week.week}_q_{idx}",
                label_visibility="collapsed"
            )
            answers[idx] = selected
        elif q.qtype == "blank":
            answers[idx] = st.text_input(
                f"week_{week.week}_q_{idx}",
                key=f"week_{week.week}_q_{idx}",
                placeholder="请填写答案"
            )
        else:
            answers[idx] = st.text_area(
                f"week_{week.week}_q_{idx}",
                key=f"week_{week.week}_q_{idx}",
                height=100,
                placeholder="请先自己作答，再提交查看参考答案"
            )

    if st.button(f"提交 Week {week.week} 周测", key=f"submit_{week.week}"):
        for idx, q in enumerate(week.quiz, start=1):
            if q.qtype in ["single", "judge", "blank"]:
                objective_total += 1
                user_answer = str(answers[idx]).strip()
                if user_answer == q.answer:
                    objective_score += 1

        st.success(f"客观题得分：{objective_score} / {objective_total}")
        st.info("说明：单选 / 判断 / 填空自动评分；程序阅读 / 改错 / 编程题提供参考答案。")

        for idx, q in enumerate(week.quiz, start=1):
            st.markdown(f"**第{idx}题答案**")
            if q.qtype in ["single", "judge", "blank"]:
                st.write(f"**正确答案：** {q.answer}")
            else:
                st.write(q.answer)
            st.write(f"**解析：** {q.explanation}")
            st.markdown("---")


def render_home():
    st.title("🐍 Python 24-Week Learning System")
    st.metric("总进度", f"{progress_percent()}%")
    st.progress(progress_percent() / 100)
    st.info("这是稳定主文件：24 周课程可运行，已去掉教材考试区，并按每周主题区分哈佛理解课、生动讲解课、考试重点和周测。")
    st.write("课程主线：变量 → 数据类型 → 顺序结构 → if → 多分支 → for → while → 循环综合 → 函数 → 参数返回值 → 字符串 → 列表 → 列表遍历 → 字典 → 文件 → 异常 → 项目整合 → 数据统计 → 元组集合 → 模块 → 小游戏 → 工具项目 → 项目表达 → 总复习")


def render_harvard_hub():
    st.title("🎓 Harvard Course Hub")
    link_button("CS50P Official", CS50P_PLL_URL)
    link_button("CS50P OpenCourseWare", CS50P_OCW_URL)
    link_button("Machine Learning & AI with Python", ML_AI_URL)


def render_parent_panel():
    st.title("👨‍👩‍👧 Parent Panel")
    st.write(f"已完成周数：{len(st.session_state.completed_weeks)}")
    selected_week = st.selectbox("选择周数", list(range(1, 25)), format_func=lambda x: f"Week {x}")
    st.info(WEEKS[selected_week].parent_tip)


def render_about():
    st.title("ℹ️ About")
    st.write("这是稳定主文件版。")
    st.write("已去掉教材考试区，保留：哈佛理解课 / 生动讲解课 / 动手实验室 / 考试重点 / 写代码题 / 学习笔记 / 周测系统。")


st.sidebar.title("📚 Navigation")
page_options = ["Home", "Harvard Course Hub"] + [f"Week {i}" for i in range(1, 25)] + ["Parent Panel", "About"]
page = st.sidebar.radio("选择页面", page_options)
st.sidebar.write(f"**进度：{progress_percent()}%**")
st.sidebar.progress(progress_percent() / 100)

if page == "Home":
    render_home()
elif page == "Harvard Course Hub":
    render_harvard_hub()
elif page.startswith("Week"):
    render_week(int(page.split()[1]))
elif page == "Parent Panel":
    render_parent_panel()
else:
    render_about()
