import streamlit as st
from dataclasses import dataclass
from typing import Dict, List

st.set_page_config(
    page_title="Python 24-Week Learning System",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Links ----------
CS50P_PLL_URL = "https://pll.harvard.edu/course/cs50s-introduction-programming-python"
CS50P_OCW_URL = "https://cs50.harvard.edu/python/2022/"
ML_AI_URL = "https://pll.harvard.edu/course/machine-learning-and-ai-python"

CS50_WEEK_LINKS = {
    1: "https://cs50.harvard.edu/python/2022/weeks/0/",
    2: "https://cs50.harvard.edu/python/2022/weeks/0/",
    3: "https://cs50.harvard.edu/python/2022/weeks/1/",
    4: "https://cs50.harvard.edu/python/2022/weeks/2/",
    5: "https://cs50.harvard.edu/python/2022/weeks/0/",
    6: "https://cs50.harvard.edu/python/2022/weeks/3/",
    7: "https://cs50.harvard.edu/python/2022/weeks/5/",
    8: "https://cs50.harvard.edu/python/2022/",
    9: "https://cs50.harvard.edu/python/2022/weeks/6/",
    10: "https://cs50.harvard.edu/python/2022/weeks/3/",
    11: "https://cs50.harvard.edu/python/2022/weeks/6/",
    12: "https://cs50.harvard.edu/python/2022/weeks/6/",
    13: "https://cs50.harvard.edu/python/2022/weeks/6/",
    14: "https://cs50.harvard.edu/python/2022/weeks/3/",
    15: "https://cs50.harvard.edu/python/2022/weeks/4/",
    16: "https://cs50.harvard.edu/python/2022/",
    17: ML_AI_URL,
    18: ML_AI_URL,
    19: ML_AI_URL,
    20: ML_AI_URL,
    21: "https://cs50.harvard.edu/python/2022/weeks/2/",
    22: "https://cs50.harvard.edu/python/2022/weeks/4/",
    23: ML_AI_URL,
    24: CS50P_OCW_URL,
}

# ---------- Models ----------
@dataclass
class WeekData:
    week: int
    stage: str
    title: str
    theme: str
    harvard_short_title: str
    harvard_goal: str
    core_question: str
    life_analogy: List[str]
    thinking_steps: List[str]
    exam_mapping: List[str]
    textbook_focus: List[str]
    exam_goals: List[str]
    code_lab_title: str
    code_lab_story: str
    follow_code: str
    modify_task: str
    modify_hint: str
    challenge_task: str
    challenge_hint: str
    write_code_prompt: str
    write_code_levels: Dict[str, str]


FOUNDATION_WEEKS = [
    WeekData(
        1, "Phase 1｜Foundation", "Python是什么 + 输入输出 + 变量", "让电脑听懂我说话",
        "CS50P Shorts First：Functions / Variables", "先抓住 print、input、变量三件事，不要求完整看长 Lecture。",
        "电脑完全不会脑补，那程序员怎么把意思说清楚？",
        ["print 像让电脑开口说话。", "input 像让电脑先听你说一句。", "变量像贴了名字的盒子。"],
        ["程序是一行一行的步骤。", "电脑只会执行明确写出的内容。", "变量让信息可以反复使用。"],
        ["选择题会考输入输出函数。", "填空题会考变量赋值。", "编程题会考自我介绍程序。"],
        ["print()", "input()", "变量赋值", "字符串基础", "程序格式"],
        ["会写输入输出", "会创建变量", "会读最简单程序"],
        "Code Lab 1｜迎新机器人", "训练一个迎新机器人：它先认识新同学，再说欢迎语。",
        """name = input('What is your name? ')
age = input('How old are you? ')
print('Hello,', name)
print('You are', age, 'years old!')""",
        "新增一个 favorite_color 变量，让机器人再多问一句最喜欢的颜色。",
        "复制一行 input 的结构即可。",
        "输出一句完整句子，例如：Lucy is 18 years old and loves blue.",
        "把多个变量放到同一行 print 里。",
        "输入学生名字和专业，输出一句欢迎语。",
        {"基础": "至少使用 2 个 input 和 1 个 print。", "进阶": "欢迎语里同时出现名字和专业。", "挑战": "再加一个兴趣爱好。"},
    ),
    WeekData(
        2, "Phase 1｜Foundation", "数据类型 + 运算 + 类型转换", "数字和文字，电脑怎么分得清",
        "CS50P Shorts First：Values / Types / Expressions", "重点理解 18 和 '18' 的区别，先会 int()、float()。",
        "人眼觉得差不多的数据，为什么电脑要分得这么严格？",
        ["18 是真正的数字卡片。", "'18' 更像写着 18 的便签纸。", "bool 像开灯和关灯。"],
        ["数据类型决定‘这个值能做什么’。", "input() 默认读入的是字符串。", "类型转换是在告诉电脑换一种理解方式。"],
        ["选择题会考 int / float / str / bool 区分。", "填空题会考 input() 默认类型。", "编程题会考 BMI、平均分。"],
        ["int", "float", "str", "bool", "算术运算", "类型转换"],
        ["分清常见数据类型", "会做基础计算", "会把输入转成数字"],
        "Code Lab 2｜太空补给站", "你在太空补给站当管理员，要算宇航员 BMI 和零食总价。",
        """weight = float(input('Weight (kg): '))
height = float(input('Height (m): '))
bmi = weight / (height ** 2)
print('BMI =', round(bmi, 2))""",
        "把 BMI 程序改成总价计算器：输入单价和数量，输出总价。",
        "总价 = 单价 * 数量。",
        "如果总价超过 50，输出 Too expensive，否则输出 Budget OK。",
        "先把 total 算出来，再判断。",
        "输入两门课程成绩，输出总分和平均分。",
        {"基础": "使用 float 或 int 完成输入与计算。", "进阶": "平均分保留两位小数。", "挑战": "再输出一句判断：平均分是否及格。"},
    ),
    WeekData(
        3, "Phase 1｜Foundation", "条件判断 if / elif / else", "让电脑学会做选择",
        "CS50P Shorts First：Conditionals", "本周优先看 Conditionals 的短内容与讲义，把 if / elif / else 写顺。",
        "现实世界充满‘如果……那么……’，电脑到底靠什么做选择？",
        ["红灯停、绿灯行，就是 if / else。", "90 分以上 A、80–89 B，是 elif 场景。", "密码是否正确、是否成年都属于条件判断。"],
        ["电脑只看条件是真是假。", "if 先判断第一层。", "elif 用于多层选择。", "else 负责兜底。"],
        ["选择题会考 = 和 == 区别。", "填空题会考比较运算符。", "编程题会考成绩等级、奇偶判断。"],
        ["if", "elif", "else", "比较运算符", "逻辑运算符"],
        ["会写单分支、双分支、多分支", "会做判断类编程题", "会看懂条件结构"],
        "Code Lab 3｜魔法学院分班器", "你要给新生自动分班：不同分数进入不同学院。",
        """score = int(input('Score: '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('C')""",
        "把成绩评级改成‘是否成年’判断。",
        "把变量名 score 改成 age，再改判断条件和输出内容。",
        "输入一个数字，判断它是正数、负数还是 0。",
        "需要 if / elif / else 三层结构。",
        "输入成绩，输出 A / B / C / D 等级。",
        {"基础": "至少有 if 和 else。", "进阶": "补上 elif。", "挑战": "把 60 以下输出为 D。"},
    ),
    WeekData(
        4, "Phase 1｜Foundation", "循环 for / while", "让电脑重复工作",
        "CS50P Shorts First：Loops", "先把 for / while 的基本感觉建立起来，不追求一次全懂。",
        "为什么程序员不会写 100 次 print，而是会让电脑自己重复？",
        ["每天打卡、每天练琴，都是现实中的循环。", "for 像‘做 10 次’。", "while 像‘只要还没成功就继续做’。"],
        ["循环的价值是把重复步骤自动化。", "for 常搭配 range()。", "while 常用于‘满足条件就继续’。", "写循环前先想停止条件。"],
        ["选择题会考 range(5) 生成什么。", "填空题会考 break 的作用。", "编程题会考 1~100、累加求和、猜数字。"],
        ["for", "while", "range()", "break", "累加变量"],
        ["会写 for 和 while", "会做累加和计数", "会理解循环停止条件"],
        "Code Lab 4｜宝箱雨游戏", "天空会掉下很多宝箱，你要用循环统计总金币。",
        """total = 0
for i in range(1, 6):
    total += 10
    print('Box', i, 'opened!')
print('Total gold =', total)""",
        "把每个宝箱金币从 10 改成 20，再把宝箱数量从 5 改成 8。",
        "改 range 的结束值和 total += 后面的数字。",
        "用 while 写一个‘猜数字直到猜中才停止’的小程序。",
        "需要 while True，再配合 if 和 break。",
        "输出 1 到 100，并计算 1 到 100 的总和。",
        {"基础": "至少写出 for 循环输出。", "进阶": "再增加一个 total 变量。", "挑战": "尝试写 while 版本。"},
    ),
    WeekData(
        5, "Phase 1｜Foundation", "函数 def / return", "把重复工作装进工具箱",
        "CS50P Shorts First：Functions Revisit", "函数这部分理解透了，代码会清爽很多。",
        "当一段动作会反复出现时，为什么程序员不喜欢复制粘贴？",
        ["榨汁机像函数：放水果进去，得到果汁。", "奶茶机像函数：你给参数，它给你结果。", "函数的意义在于可重复使用。"],
        ["函数先定义，再调用。", "参数像交给机器的原料。", "return 像机器最后给你的成品。"],
        ["选择题会考 def 和 return 的作用。", "填空题会考参数位置。", "编程题会考 add、max、grade 这类基础函数。"],
        ["def", "参数", "return", "函数调用"],
        ["会定义函数", "会调用函数", "会写简单 return"],
        "Code Lab 5｜魔法饮料机", "你要写一个魔法饮料机函数，只要输入两个数字，它就能调出一杯能量饮料。",
        """def add(a, b):
    return a + b

result = add(3, 5)
print(result)""",
        "把 add 改成 multiply，让饮料机返回两个数字相乘的结果。",
        "改函数名和 return 里的运算符。",
        "写一个 grade(score) 函数，返回 A、B 或 C。",
        "函数里面照样可以写 if / elif / else。",
        "写一个函数，输入半径，返回圆的面积。",
        {"基础": "先写出 def 和 return。", "进阶": "函数带一个参数。", "挑战": "函数里面再加判断。"},
    ),
    WeekData(
        6, "Phase 1｜Foundation", "综合拼装", "真正开始像程序员一样拼积木",
        "CS50P Shorts First：Exceptions / Libraries（轻触）", "哈佛内容只做轻量接触，主任务仍然是综合基础题。",
        "为什么真正的程序不是单个知识点，而是把输入、判断、循环和函数拼成完整流程？",
        ["像搭乐高，难的是组合。", "像做一道菜，洗菜、切菜、下锅都要连起来。", "综合题不是新语法，而是旧知识的组合。"],
        ["先拆步骤，再决定每一步用什么知识。", "输入负责拿到信息。", "判断负责做选择。", "循环负责重复。", "函数负责封装。"],
        ["编程题会考登录验证、菜单系统。", "改错题会考条件位置、缩进、类型转换遗漏。", "综合题关键是先读懂题再拆步骤。"],
        ["综合程序设计", "输入+判断", "判断+循环", "函数+判断"],
        ["能完成短综合题", "知道先拆步骤", "开始形成题感"],
        "Code Lab 6｜迷你冒险菜单", "你要给一款文字冒险游戏写一个开始菜单，玩家输入 1 或 2 进入不同分支。",
        """print('1. Say Hello')
print('2. Check even or odd')
choice = input('Choose: ')

if choice == '1':
    print('Hello, traveler!')
elif choice == '2':
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        print('Even')
    else:
        print('Odd')
else:
    print('Invalid choice')""",
        "增加一个选项 3：输入名字后打印欢迎语。",
        "先多打印一行菜单，再加一个 elif choice == '3'。",
        "把奇偶判断写成函数，再在菜单里调用它。",
        "先写 def check_even(n): ...，再在菜单里使用。",
        "写一个菜单系统：1 查询奇偶，2 查询成绩等级，3 退出。",
        {"基础": "完成两个菜单选项。", "进阶": "加入类型转换。", "挑战": "把一个功能封装成函数。"},
    ),
    WeekData(
        7, "Phase 1｜Foundation", "考试题型专项", "从会做，到会考",
        "CS50P Shorts First：检查代码的思路", "这一周哈佛只轻触‘程序员会检查代码’这个想法，主线是题型训练。",
        "为什么有的人会写题却考不出来？因为‘会做’和‘会考’之间还差一层题型识别。",
        ["考试像跑步比赛，会跑不等于一定发挥稳。", "模板题像常见球路，认出来反应更快。", "改错题最能暴露低级错误。"],
        ["先判断题型。", "再匹配模板。", "最后检查缩进、括号、引号、= 和 ==。"],
        ["选择题会考语法辨析。", "改错题会考 = / ==、缩进、冒号。", "编程题会考奇偶数、成绩分级、循环。"],
        ["选择题", "填空题", "改错题", "短编程题"],
        ["形成题型识别能力", "减少低级错误", "稳定基础分"],
        "Code Lab 7｜Bug Hunter 抓虫游戏", "你是代码侦探，要抓出程序里的 Bug。",
        """age = int(input('Age: '))
if age == 18:
    print('ok')
else:
    print('not 18')""",
        "把错误版本 if age = 18: 修好。",
        "比较要用 ==，不是 =。",
        "自己设计一个会出错的小程序，再试着给它改正。",
        "最容易制造的错误有：缩进不对、漏冒号、比较符号写错。",
        "写一个包含 3 个常见错误的小程序，并把它改正。",
        {"基础": "先改 1 个错误。", "进阶": "再解释为什么错。", "挑战": "自己设计 Bug 再修。"},
    ),
    WeekData(
        8, "Phase 1｜Foundation", "模拟考试 + 查漏补缺", "最后一周只做拿分动作",
        "Harvard Hub：考后继续学入口", "最后一周不再追哈佛课程进度，现在最重要的是做卷、复盘、稳住基础分。",
        "冲刺阶段最有效的动作是什么？不是学新难点，而是把已经会的东西稳定写出来。",
        ["考试前像比赛前热身，重点是稳定。", "基础题拿稳，比临时追难题更划算。", "错题复盘像赛前看录像。"],
        ["先做卷，别先看答案。", "把错题分成：粗心错、没理解、模板不熟。", "只回补最影响分数的地方。"],
        ["模拟卷要覆盖输入输出、类型、if、循环、函数。", "查漏重点是奇偶、成绩分级、1~100、return。"],
        ["模拟卷", "错题复盘", "模板回顾", "考前冲刺"],
        ["能完成完整基础卷", "知道自己的薄弱点", "带着稳定感上考场"],
        "Code Lab 8｜终极通关战", "你要通过终极试炼：输入分数，输出等级；输入数字，判断奇偶；最后再写一个小函数。",
        """score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('C')""",
        "把这段程序改成会员等级版本，例如 Gold / Silver / Bronze。",
        "结构不变，只改变量名和输出内容。",
        "把等级判断写成函数 grade(score)，然后调用它。",
        "把 if 结构搬进 def grade(score): 里面，再 return 等级。",
        "做一套 mini 模拟卷：奇偶、分级、循环、函数各一题。",
        {"基础": "至少完成 2 题。", "进阶": "改正所有错题。", "挑战": "自己总结 5 条考前模板。"},
    ),
]

APPLICATION_WEEKS = [
    WeekData(9, "Phase 2｜Application", "字符串 Strings", "让电脑处理文字", "CS50P Shorts First：Text / File Thinking", "本周重点不是死记 API，而是感受‘文字也是可操作的数据’。", "为什么电脑不仅能算数，还能处理名字、句子和文本？", ["字符串像一串有顺序的字母珠子。", "切片像从一串珠子里截出一段。", "replace 像给句子换词。"], ["字符串也是数据。", "很多文本题本质是‘取一部分、改一部分、查一部分’。", "split 能把一句话拆成多个小块。"], ["考试会考字符串大小写、切片、替换。", "输出题常让你判断处理后的文本。"], ["索引", "切片", "upper/lower", "replace", "split"], ["会做基本字符串处理", "会看懂文本操作题"], "Code Lab 9｜名字美化器", "你要把一串普通名字变成更正式、更整齐的展示文本。", """name = input('Name: ')
print(name.upper())
print(name.lower())
print(name.title())""", "在程序中再加一行：输出名字的前 3 个字符。", "切片写法像 name[:3]。", "输入一句英文，用 replace 把其中一个单词替换掉。", "先观察原句，再决定替换哪个词。", "输入一句英文，输出全大写版本、单词个数、替换后的版本。", {"基础": "完成 upper() 或 lower()。", "进阶": "用 split() 统计单词数。", "挑战": "再做一次 replace()。"}),
    WeekData(10, "Phase 2｜Application", "列表 List", "让电脑一次记住很多东西", "CS50P Shorts First：Loops + Collections", "本周抓住一个感觉：列表就像一排收纳盒。", "为什么程序不能只靠一个变量，而要学会一次存很多值？", ["列表像一排有编号的抽屉。", "append 像往抽屉尾巴再塞一个东西。", "remove 像把其中一件东西拿出来。"], ["列表适合保存一组同类数据。", "索引能定位某个元素。", "for 常和列表一起用。"], ["考试会考列表创建、索引、遍历。", "编程题常见购物清单、成绩列表。"], ["list", "append", "remove", "索引", "遍历列表"], ["会建立和修改列表", "会遍历列表输出内容"], "Code Lab 10｜校园购物清单", "你要帮宿舍准备采购清单。", """items = ['milk', 'bread', 'apple']
items.append('juice')
for item in items:
    print(item)""", "把清单里多加两个物品，再删除一个。", "append 和 remove 分别负责增加与删除。", "输入 3 个成绩放进列表，再输出最高分。", "先把成绩存起来，再尝试用 max()。", "做一个待办清单程序：显示列表、追加任务、删除任务。", {"基础": "会 append。", "进阶": "会 remove。", "挑战": "配合 for 输出全部元素。"}),
    WeekData(11, "Phase 2｜Application", "字典 Dictionary", "让电脑按名字找信息", "CS50P Shorts First：Mapping Ideas", "本周先抓住 key / value 的感觉，不追求复杂嵌套。", "如果想让电脑按‘名字’找到‘内容’，为什么列表不够用？", ["字典像通讯录：名字对应电话号码。", "key 像标签，value 像标签后面的内容。", "用 key 查 value 很像查字典。"], ["字典最适合‘名称→信息’的结构。", "它不像列表那样靠位置。", "改一个值时只需要找到 key。"], ["考试会考 key / value 基础用法。", "编程题常见学生成绩字典、词汇查询器。"], ["dict", "key/value", "查找", "增删改"], ["会创建字典", "会按 key 查值", "会更新信息"], "Code Lab 11｜迷你通讯录", "你要给朋友们建一个简单通讯录。", """phone_book = {'Amy': '123', 'Ben': '456'}
print(phone_book['Amy'])
phone_book['Cindy'] = '789'
print(phone_book)""", "往通讯录里再加一个新同学。", "用新名字作为 key，新号码作为 value。", "做一个英文单词查询器：输入单词，输出中文意思。", "先写一个小字典，再根据输入去查询。", "做一个学生成绩表：姓名对应成绩，并能更新其中一个学生的分数。", {"基础": "会新增 key。", "进阶": "会查找某个 key。", "挑战": "会修改已有值。"}),
    WeekData(12, "Phase 2｜Application", "元组 Tuple + 集合 Set", "哪些数据不能改？哪些数据不能重复？", "CS50P Shorts First：Data Structure Contrast", "本周不是背定义，而是理解‘稳定数据’和‘去重数据’。", "为什么有的数据适合锁死不改，有的数据适合自动去重？", ["tuple 像封好的档案袋，不随便改。", "set 像‘不允许重复’的名单箱。", "去重像自动把重复报名的人合并。"], ["tuple 适合不想改动的数据。", "set 适合做去重和成员判断。", "这一周重点是感受用途差异。"], ["考试常考 tuple 和 list、set 和 list 的区别。", "编程题会用到去重场景。"], ["tuple", "set", "去重", "成员判断"], ["知道 tuple / set 用途", "会做简单去重题"], "Code Lab 12｜兴趣标签去重器", "你要整理一堆重复的兴趣标签。", """tags = ['music', 'dance', 'music', 'reading']
unique_tags = set(tags)
print(unique_tags)""", "在原列表中再加入两个重复标签，观察结果。", "集合会自动去重。", "把一个元组打印出来，并尝试解释为什么它不适合频繁修改。", "先定义一个 tuple，例如 ('red', 'blue', 'green')。", "做一个报名名单去重器：输入一些名字，输出不重复名单。", {"基础": "会用 set 去重。", "进阶": "知道 tuple 不能随便改。", "挑战": "结合循环输出去重后的结果。"}),
    WeekData(13, "Phase 2｜Application", "文件基础 File I/O", "让程序记住东西", "CS50P Shorts First：Files", "本周重点是感受：程序不只会算，还能把结果保存下来。", "为什么程序结束后，数据还想留下来？", ["文件像一个能长期保存内容的记事本。", "write 像往本子上写字。", "read 像把本子内容再读出来。"], ["with open 可以更安全地操作文件。", "写文件让程序有‘记忆感’。", "很多真实程序都要保存结果。"], ["考试会考 read / write 基础。", "编程题常见日记保存器、成绩保存器。"], ["open", "read", "write", "with open"], ["会读写基础文件", "知道 with open 的用法"], "Code Lab 13｜数字日记本", "你要写一个能把一句话保存进文本文件的小程序。", """with open('note.txt', 'w', encoding='utf-8') as f:
    f.write('Today I learned Python!')
print('Saved!')""", "把保存内容改成用户输入的一句话。", "先 input，再把结果写进去。", "再写一段读取文件内容并打印的代码。", "需要使用模式 'r'。", "做一个学习记录器：输入今天学了什么，保存到文件，再读出来显示。", {"基础": "完成 write。", "进阶": "再完成 read。", "挑战": "让保存内容来自 input。"}),
    WeekData(14, "Phase 2｜Application", "异常处理 try / except", "程序出错了怎么办", "CS50P Shorts First：Exceptions", "重点不是把异常学深，而是知道如何避免程序一报错就崩掉。", "程序遇到错误时，是不是只能直接崩掉？", ["try 像先大胆尝试。", "except 像提前准备一个备用方案。", "异常处理像给程序装安全气囊。"], ["有些输入一定会出错。", "try / except 能让程序更稳。", "真正的程序需要考虑用户乱输入。"], ["考试会考 try / except 基础结构。", "编程题常见安全计算器。"], ["try", "except", "ValueError", "输入容错"], ["会写最基础异常处理", "知道为什么要防止崩溃"], "Code Lab 14｜安全计算器", "你要做一个不会轻易崩掉的加法器。", """try:
    a = int(input('A: '))
    b = int(input('B: '))
    print(a + b)
except ValueError:
    print('Please enter numbers only.')""", "把提示文字改成更友好的版本。", "except 里可以自由写提示语。", "做一个安全年龄输入器：如果用户输入不是数字，就提醒重来。", "先把 int(input()) 放进 try 里。", "做一个能处理输入错误的平均分计算器。", {"基础": "写出 try / except。", "进阶": "识别 ValueError。", "挑战": "在 except 中给出清晰提示。"}),
    WeekData(15, "Phase 2｜Application", "模块与库 import", "站在别人肩膀上写代码", "CS50P Shorts First：Libraries", "这周重点是感受 import 的力量，而不是背大量库。", "为什么程序员不是什么都自己发明，而常常直接调用现成工具？", ["库像工具箱。", "random 像随机抽签机。", "math 像数学工具盒。"], ["import 的意义是借用已有能力。", "学会几个常用库就够建立感觉。", "越往后越会发现工具箱的重要。"], ["考试会考 import 基本写法。", "编程题常见 random、math。"], ["import", "random", "math", "datetime"], ["会导入基础库", "会调用简单函数"], "Code Lab 15｜幸运转盘", "你要做一个随机抽签器，决定今天谁先上台。", """import random
names = ['Amy', 'Ben', 'Cindy']
print(random.choice(names))""", "把名单改成 5 个人。", "多加几个名字，观察结果变化。", "再做一个随机掷骰子程序，输出 1 到 6。", "可以使用 random.randint(1, 6)。", "做一个随机抽签 + 随机分组小工具。", {"基础": "完成 import random。", "进阶": "会使用 choice 或 randint。", "挑战": "把随机功能放进函数里。"}),
    WeekData(16, "Phase 2｜Application", "应用期综合项目", "第一次做像样的小程序", "Harvard Guidance：项目式学习入口", "本周不是学新语法，而是把 9–15 周内容真正串起来。", "怎样把多个看似分散的知识点，拼成一个完整小程序？", ["项目像搭一栋小房子，不是单块积木。", "先想功能，再想每部分需要什么语法。", "小项目的价值在于串联。"], ["先写最小可用版本。", "再一点一点加功能。", "不要一开始就追求完美。"], ["考试中综合题和真实项目思路很像。", "先拆步骤再写代码会明显更稳。"], ["综合项目", "输入/输出", "列表/字典", "函数", "文件"], ["能完成一个小项目", "开始形成产品意识"], "Code Lab 16｜学习计划管理器", "你要做一个简单学习计划器：输入任务，保存任务，显示任务。", """tasks = []
for i in range(3):
    task = input('Task: ')
    tasks.append(task)
print(tasks)""", "让程序在输出任务时给每个任务编号。", "可以用 for i in range(len(tasks))。", "让程序把任务保存到文件里。", "把 write 和循环结合起来。", "完成一个小项目：待办清单、成绩分析器或单词小工具三选一。", {"基础": "完成最小版本。", "进阶": "增加一个新功能。", "挑战": "增加保存到文件。"}),
]

PROJECT_WEEKS = [
    WeekData(17, "Phase 3｜Project & AI", "数据分析入门", "让 Python 像 Excel 一样帮我工作", "Harvard AI Course：先看概念，不碰重数学", "本周重点是表格思维：一行一列、记录和字段。", "为什么很多现实问题最后都会变成‘数据表’？", ["一张成绩表就像很多条记录排在一起。", "每一列像一个字段。", "数据分析先是整理，再是统计。"], ["表格思维是数据分析的起点。", "可以先用列表和字典模拟表格。", "真实世界的数据很多都能抽成记录。"], ["这一周更偏能力拓展。", "考试如果遇到综合题，也能从‘记录’角度理解。"], ["记录", "字段", "表格思维", "简单统计"], ["知道什么叫记录与字段", "会做简单统计"], "Code Lab 17｜成绩分析台", "你要统计一个小班级的成绩数据。", """scores = [88, 92, 76, 95, 84]
print('Count =', len(scores))
print('Max =', max(scores))
print('Min =', min(scores))
print('Average =', sum(scores) / len(scores))""", "再添加 3 个分数，重新观察平均分变化。", "把列表中的数字改掉就可以。", "做一个消费记录分析器：统计总花费和最大花费。", "和成绩分析思路完全类似。", "输入 5 个成绩，输出最高分、最低分、平均分，并给出一句总结。", {"基础": "会统计 max/min。", "进阶": "会算平均分。", "挑战": "换成另一组数据。"}),
    WeekData(18, "Phase 3｜Project & AI", "可视化入门", "让数据会说话", "Harvard AI Course：理解图表如何帮助观察规律", "这一周重点是让孩子感受到‘图表比一堆数字更直观’。", "为什么一堆数字放在图里，看起来会更清楚？", ["柱状图像把数字竖起来给你看。", "折线图像看趋势。", "可视化是在帮大脑省力。"], ["图表是数据表达，不是炫技。", "先学会选择最简单的图。", "很多分析从图开始更容易讲清楚。"], ["这周主要是素养提升。", "也能反过来帮助读题和总结。"], ["柱状图", "折线图", "趋势", "比较"], ["知道常见图表用途", "能把数据结果转成更直观表达"], "Code Lab 18｜学习时长看板", "你要展示一周 7 天的学习时长。", """days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hours = [1, 2, 1.5, 2, 1, 3, 2]
for d, h in zip(days, hours):
    print(d, ':' , '*' * int(h))""", "把每天的时长换成自己的真实数据。", "星号图先帮助建立‘可视化感觉’。", "做一个成绩条形展示：分数越高，星号越长。", "仍然可以先用文本星号模拟。", "完成一个‘文本版可视化’程序：展示任意一组数据的长度对比。", {"基础": "会输出文本图。", "进阶": "换成自己的数据。", "挑战": "比较两组数据。"}),
    WeekData(19, "Phase 3｜Project & AI", "AI 思维入门", "什么叫机器学习，Python为什么和AI有关", "Harvard AI Course：概念优先", "本周重点是理解 AI / ML 的概念，不碰难数学。", "为什么大家总说 Python 和 AI 关系很近？", ["AI 像让机器学会做判断。", "机器学习像从很多例子里总结规则。", "Python 像一套很适合实验和搭模型的工具。"], ["AI 不等于魔法。", "机器学习本质是在数据中找规律。", "先理解概念，再谈算法。"], ["这周主要用于建立方向感。", "不作为当前应试主线。"], ["AI", "机器学习", "数据", "规则"], ["能说清 AI 和 Python 的关系", "对后续课程不陌生"], "Code Lab 19｜最简单推荐器", "你要做一个最简单的‘推荐系统’：根据年龄推荐内容。", """age = int(input('Age: '))
if age < 18:
    print('Recommend: animation')
else:
    print('Recommend: movie')""", "把推荐逻辑改成‘根据学习时长给建议’。", "变量和输出内容都可以自由换。", "再做一个‘根据天气推荐穿搭’的小程序。", "本质仍然是规则判断。", "写一个规则型建议器：输入两个条件，给出一个推荐结果。", {"基础": "完成一个 if 推荐器。", "进阶": "增加 elif。", "挑战": "同时参考两个条件。"}),
    WeekData(20, "Phase 3｜Project & AI", "规则型小AI项目", "先做假的AI，再理解真的AI", "Harvard AI Course：概念 + 规则模拟", "重点不是追求真 AI，而是先体验‘智能感’从何而来。", "为什么一个看起来很聪明的程序，很多时候先是‘规则写得好’？", ["规则型 AI 像一套精心设计的客服流程。", "很多智能感，先来自条件判断组合。", "会写规则，才更容易理解模型。"], ["先做假 AI，再理解真 AI。", "复杂系统常由简单规则叠起来。", "if / elif 本身就能做很多‘像 AI’的事。"], ["适合作为兴趣拔高。", "也能反向巩固判断结构。"], ["规则系统", "多条件判断", "简单推荐器"], ["能写规则型智能程序", "理解智能感的来源"], "Code Lab 20｜学习建议机器人", "你要做一个会给学习建议的机器人。", """hours = float(input('Study hours today: '))
score = int(input('Last quiz score: '))
if hours < 1 and score < 70:
    print('Need more practice')
elif hours >= 1 and score >= 70:
    print('Keep going')
else:
    print('Review the basics')""", "把判断条件再丰富一点，比如增加‘是否按时完成作业’。", "多一个输入，多一层逻辑。", "写一个电影推荐机器人：根据年龄、心情、类型偏好推荐。", "先列规则，再写代码。", "设计一个你自己的‘智能建议器’，至少根据两个输入给结果。", {"基础": "完成双条件判断。", "进阶": "增加一个新输入。", "挑战": "自己定义规则并解释。"}),
    WeekData(21, "Phase 3｜Project & AI", "小游戏项目周", "让编程变得好玩", "Harvard Guidance：游戏是练逻辑和反馈的好方式", "这周重点是通过小游戏提升手感与成就感。", "为什么小游戏特别适合练编程？", ["游戏有即时反馈。", "规则清楚、目标明确，特别适合练逻辑。", "小游戏是项目的缩小版。"], ["小游戏能综合输入、判断、循环。", "先有趣，后深入。", "手感往往在游戏练习里长得很快。"], ["考试虽然不考游戏，但游戏能显著提升写代码流畅度。"], ["输入", "判断", "循环", "随机"], ["提升代码手感", "更愿意主动练习"], "Code Lab 21｜石头剪刀布", "你要做一个石头剪刀布小游戏。", """import random
choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = input('Your choice: ')
print('Computer:', computer)
print('Player:', player)""", "补上胜负判断逻辑。", "先只处理一种玩家获胜情况，再慢慢补齐。", "给游戏加上‘再玩一轮’的循环。", "可以用 while 和再次输入。", "完成一个小游戏：猜数字、石头剪刀布、问答闯关三选一。", {"基础": "完成最小游戏流程。", "进阶": "补上胜负判断。", "挑战": "加入循环和计分。"}),
    WeekData(22, "Phase 3｜Project & AI", "实用工具项目周", "让 Python 真的帮生活做事", "Harvard Guidance：做实用工具比空看更能建立成就感", "本周把编程拉回现实生活，做一个真能用的小工具。", "什么样的程序最容易让人觉得‘学这个真有用’？", ["实用工具像生活中的小助手。", "看得见结果，就更容易坚持。", "很多真正的软件，一开始都只是小工具。"], ["项目不需要大，但要解决一个真实小问题。", "工具型项目特别适合建立价值感。"], ["也能帮助孩子形成‘编程服务现实’的感觉。"], ["项目规划", "输入输出", "保存结果", "函数"], ["能做一个可用小工具", "体验项目落地感"], "Code Lab 22｜小型记账器", "你要做一个简单记账器：输入花费项目和金额，计算总支出。", """records = []
for i in range(3):
    name = input('Item: ')
    money = float(input('Money: '))
    records.append((name, money))
print(records)""", "把总支出算出来。", "遍历 records，把金额累加。", "把记账结果保存到文件。", "可以用 with open 写出每一项。", "完成一个实用工具：计划器、单词复习器、记账器、成绩计算器四选一。", {"基础": "完成数据输入。", "进阶": "完成统计结果。", "挑战": "加入保存功能。"}),
    WeekData(23, "Phase 3｜Project & AI", "期末综合项目周", "做一个真正属于自己的小作品", "Harvard AI Course：项目展示思维", "本周重点是自主感：选题、改文案、解释逻辑。", "什么时候一个程序才算‘自己的作品’？", ["自己决定题目时，程序会更有归属感。", "项目不一定大，但要有自己的选择。", "能讲清楚逻辑，比代码长更重要。"], ["选题先从自己真的想用开始。", "先做最小版本，再慢慢加。", "最终要能解释自己的设计。"], ["这周更像作品训练，不是单纯刷题。"], ["项目选题", "功能设计", "逻辑解释", "展示"], ["完成一个个人作品", "会解释自己的代码"], "Code Lab 23｜我的作品草稿台", "你先写一个最小版本，再逐步添加功能。", """project_name = input('Project name: ')
print('My project is', project_name)
print('Version 1: basic output done!')""", "给项目加一个真正的输入和真正的输出。", "先别贪大，先保证最小版本能跑。", "给项目增加一个第二功能，例如保存、判断、统计、随机。", "在最小版本上加一个功能最稳。", "独立完成一个你自己的小项目，并能用 3 句话解释它。", {"基础": "完成最小版本。", "进阶": "增加一个功能。", "挑战": "把作品讲清楚。"}),
    WeekData(24, "Phase 3｜Project & AI", "毕业周 / 展示周 / 回顾周", "我已经不是零基础了", "Harvard Hub：下一阶段学习入口", "最后一周不追新内容，重点是回顾成长、展示作品和规划下一步。", "怎样判断自己已经不再是零基础？", ["能看懂基础代码。", "能独立写出小程序。", "能讲清楚自己做过什么。"], ["回顾能让成长变具体。", "作品展示能增强成就感。", "下一步路线会比继续乱学更重要。"], ["毕业周也可以回看考试和项目中最有价值的部分。"], ["成长回顾", "作品展示", "下一步路线"], ["看见自己的成长", "知道下一阶段怎么学"], "Code Lab 24｜毕业展示板", "把过去 24 周做过的内容，挑 1–2 个代表作品展示出来。", """print('I can use Python now!')
print('Project 1: ...')
print('Project 2: ...')""", "把展示内容改成你自己的真实项目。", "项目名、功能、收获都可以写进去。", "给自己的未来写一个 4 周继续学习计划。", "从‘还想学什么’倒推计划。", "做一个毕业总结：我学会了什么、最喜欢什么、下一步想做什么。", {"基础": "列出 3 项已学会内容。", "进阶": "展示 1 个作品。", "挑战": "写出未来 4 周计划。"}),
]

ALL_WEEKS = FOUNDATION_WEEKS + APPLICATION_WEEKS + PROJECT_WEEKS
WEEKS: Dict[int, WeekData] = {w.week: w for w in ALL_WEEKS}

PARENT_TIPS = {
    1: "陪她说出 print / input / 变量分别像什么，不要上来就考定义。",
    2: "重点盯 input() 默认是字符串，以及 int()/float() 为什么要用。",
    3: "多让她口头解释‘为什么这里用 if，而不是直接 print’。",
    4: "循环最容易乱，让她先讲清‘什么时候停’。",
    5: "函数这周别追求多，先稳住 def、参数、return。",
    6: "综合题先拆步骤，再写代码，家长不要催她一步到位。",
    7: "这一周更像考试训练，帮助她识别题型比讲新内容更重要。",
    8: "少学新内容，多看错题和模板，让状态稳下来。",
    9: "字符串周别只背函数名，让她用真实句子练切片和替换。",
    10: "列表周重点是‘一次装很多东西’，可以用购物清单举例。",
    11: "字典周多用通讯录或成绩表类比，孩子会更快懂 key/value。",
    12: "tuple / set 不用讲太深，抓住‘不改’和‘去重’两个关键词。",
    13: "文件周很容易让孩子有成就感，可以鼓励她保存自己的学习记录。",
    14: "异常处理周告诉她：报错不是失败，是程序在提醒你保护自己。",
    15: "import 周重在兴趣激发，让她感受‘原来能直接调用工具’。",
    16: "项目周别急着追美观，先让最小版本能运行。",
    17: "数据分析周可以用真实成绩或学习时长数据，效果最好。",
    18: "可视化周目标是把数字变直观，不必一开始就追图表库。",
    19: "AI 概念周不要讲得太玄，抓住‘数据+规则/模型’就够。",
    20: "规则型小AI本质还是 if/elif，别被‘AI’两个字吓到。",
    21: "小游戏周要鼓励她多试错，玩出来的手感很重要。",
    22: "实用工具周建议做她自己会用的东西，价值感会更强。",
    23: "综合项目周重点是自主感，哪怕作品小，也要让她自己做主。",
    24: "毕业周多夸她已经不是零基础了，再一起规划下一步。",
}

EXAM_BANK = [
    {"type": "选择题", "question": "Python 中字符串类型是？", "answer": "str", "hint": "带引号的文本一般是字符串。"},
    {"type": "填空题", "question": "定义函数用的关键字是 ______。", "answer": "def", "hint": "函数定义从这个三字母关键字开始。"},
    {"type": "改错题", "question": "把 if age = 18: 改正确。", "answer": "if age == 18:", "hint": "比较要用双等号。"},
    {"type": "编程题", "question": "输入一个整数，判断奇偶。", "answer": "用 n % 2 == 0 判断。", "hint": "余数为 0 就是偶数。"},
    {"type": "选择题", "question": "range(5) 通常生成哪些数字？", "answer": "0,1,2,3,4", "hint": "从 0 开始，不含 5。"},
    {"type": "填空题", "question": "把输入内容转成整数的写法是 ______。", "answer": "int(input())", "hint": "先 input，再用 int 包起来。"},
    {"type": "概念题", "question": "字典最适合存什么？", "answer": "键值对应关系", "hint": "例如姓名对应成绩。"},
    {"type": "项目题", "question": "请设计一个你自己的小工具项目。", "answer": "任意合理工具都可以，如记账器、计划器。", "hint": "先做最小版本。"},
]

# ---------- Session State ----------
if "completed_weeks" not in st.session_state:
    st.session_state.completed_weeks = set()
if "notes" not in st.session_state:
    st.session_state.notes = {i: "" for i in range(1, 25)}
if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {}

# ---------- Helpers ----------
def progress_percent() -> int:
    return int(len(st.session_state.completed_weeks) / 24 * 100)


def mark_week_complete(week: int):
    st.session_state.completed_weeks.add(week)


def link_button(label: str, url: str):
    st.markdown(f"[**{label}**]({url})")


def week_link(week: int) -> str:
    return CS50_WEEK_LINKS.get(week, CS50P_OCW_URL)



def make_quiz(week: int) -> List[Dict]:
    data = WEEKS[week]
    topic = data.textbook_focus[0]
    quiz = [
        {
            "part": "Part A｜概念理解",
            "prompt": f"Week {week} 的核心主题更接近哪一项？",
            "options": [data.theme, "只背语法定义", "只看视频不动手", "只做难题"],
            "answer": 0,
            "difficulty": "基础",
            "explanation": "每周主题先抓理解方向。",
            "skill": "概念理解",
        },
        {
            "part": "Part A｜概念理解",
            "prompt": f"本周最重要的知识焦点之一是？",
            "options": [topic, "Photoshop", "3D 建模", "网页设计"],
            "answer": 0,
            "difficulty": "基础",
            "explanation": f"本周教材焦点之一就是 {topic}。",
            "skill": "概念理解",
        },
        {
            "part": "Part A｜概念理解",
            "prompt": "学习 Python 时，最稳的路径更接近哪一项？",
            "options": ["先理解，再跟敲，再微改，再做题", "只背答案", "只看视频", "只做难题"],
            "answer": 0,
            "difficulty": "基础",
            "explanation": "真正能学会的路径是理解 + 动手 + 输出。",
            "skill": "概念理解",
        },
        {
            "part": "Part A｜概念理解",
            "prompt": "本周如果只做一件最重要的事，应该更偏向哪一项？",
            "options": [data.exam_goals[0], "跳过基础直接学AI", "只追求写很长代码", "只记英文单词"],
            "answer": 0,
            "difficulty": "进阶",
            "explanation": "每周先稳住本周最核心能力。",
            "skill": "概念理解",
        },
        {
            "part": "Part B｜读代码",
            "prompt": "读代码时，最先应该关注什么？",
            "options": ["变量和输入输出在做什么", "背景颜色", "字体大小", "窗口位置"],
            "answer": 0,
            "difficulty": "基础",
            "explanation": "先看输入、变量、判断、循环在做什么。",
            "skill": "读代码",
        },
        {
            "part": "Part B｜读代码",
            "prompt": "如果一段代码用了 if / for / def，正确做法更接近？",
            "options": ["先分清每一部分在解决什么问题", "直接背下来", "只记住行数", "只看最后一行"],
            "answer": 0,
            "difficulty": "进阶",
            "explanation": "读代码的核心是看结构和作用。",
            "skill": "读代码",
        },
        {
            "part": "Part B｜读代码",
            "prompt": "看到一段稍长代码时，最稳的阅读顺序通常是？",
            "options": ["先看输入，再看处理中间逻辑，最后看输出", "先看注释长度", "先数一共有几行", "先改变量名"],
            "answer": 0,
            "difficulty": "进阶",
            "explanation": "程序通常遵循输入 → 处理 → 输出的基本流。",
            "skill": "读代码",
        },
        {
            "part": "Part B｜读代码",
            "prompt": "如果代码里出现循环，最值得先确认的是？",
            "options": ["它什么时候停止", "它有几种颜色", "它是不是英文", "它是不是超过10行"],
            "answer": 0,
            "difficulty": "挑战",
            "explanation": "循环题最关键的是停止条件。",
            "skill": "读代码",
        },
        {
            "part": "Part C｜改错/补全",
            "prompt": "改错题最先要检查什么？",
            "options": ["缩进、冒号、括号、= 和 ==", "颜色", "标题", "注释长度"],
            "answer": 0,
            "difficulty": "基础",
            "explanation": "这些是最常见低级错误。",
            "skill": "改错补全",
        },
        {
            "part": "Part C｜改错/补全",
            "prompt": "如果程序需要用户输入数字，常见关键动作是什么？",
            "options": ["必要时做类型转换", "删除变量", "一定要加图片", "加更多空行"],
            "answer": 0,
            "difficulty": "基础",
            "explanation": "输入经常需要 int() 或 float()。",
            "skill": "改错补全",
        },
        {
            "part": "Part C｜改错/补全",
            "prompt": "综合题更稳的起手式是？",
            "options": ["先拆步骤再写代码", "直接一口气写完", "先随便写几行", "先复制网上答案"],
            "answer": 0,
            "difficulty": "进阶",
            "explanation": "先拆步骤会明显更稳。",
            "skill": "改错补全",
        },
        {
            "part": "Part C｜改错/补全",
            "prompt": "如果 if 语句报错，最常见的原因之一是？",
            "options": ["漏了冒号或缩进不对", "电脑太旧", "屏幕太亮", "网络太慢"],
            "answer": 0,
            "difficulty": "进阶",
            "explanation": "if / for / def 这类结构最常见错误就是冒号和缩进。",
            "skill": "改错补全",
        },
        {
            "part": "Part C｜改错/补全",
            "prompt": "补全代码题时，最重要的是先看什么？",
            "options": ["上下文在想完成什么功能", "空格数量", "代码颜色", "页面布局"],
            "answer": 0,
            "difficulty": "挑战",
            "explanation": "补全不是猜单词，而是看功能逻辑。",
            "skill": "改错补全",
        },
        {
            "part": "Part D｜写代码思维",
            "prompt": "真正开始写代码前，最稳的一步通常是？",
            "options": ["先写出思路或步骤", "先写最后一行", "先改主题颜色", "先复制整段答案"],
            "answer": 0,
            "difficulty": "基础",
            "explanation": "先写思路能明显降低卡壳概率。",
            "skill": "写代码思维",
        },
        {
            "part": "Part D｜写代码思维",
            "prompt": "如果一道写代码题卡住了，最好的处理方式更接近？",
            "options": ["先做最小版本，再慢慢补功能", "直接放弃", "一直盯着题目不动", "换成别的语言"],
            "answer": 0,
            "difficulty": "挑战",
            "explanation": "先做最小可运行版本，是最稳的编程策略。",
            "skill": "写代码思维",
        },
    ]
    return quiz



def stage_summary(stage: str) -> str:
    if "Foundation" in stage:
        return "目标：打基础 + 应试，建立‘不怕 Python’的感觉。"
    if "Application" in stage:
        return "目标：从‘会写一点’升级到‘会用 Python 做事’。"
    return "目标：做项目、接触数据与 AI 方向，建立更长线的学习路线。"


# ---------- Render Blocks ----------
def render_harvard_links(week: int):
    data = WEEKS[week]
    st.subheader("🎓 Harvard Video Guidance｜Shorts / 讲义优先")
    a, b = st.columns([1.4, 1])
    with a:
        st.markdown(f"**本周哈佛导航：{data.harvard_short_title}**")
        st.write(data.harvard_goal)
        st.write("- 默认顺序：先看 Shorts / 讲义，再做本周系统内容。")
        st.write("- Full Lecture 是可选项，不是本周必须。")
        link_button("Open Harvard Week / Course Page", week_link(week))
    with b:
        st.info(stage_summary(data.stage))
        if week >= 17:
            link_button("Open Harvard ML & AI Course", ML_AI_URL)
        else:
            link_button("Open CS50P Official Page", CS50P_PLL_URL)
            link_button("Open CS50P OpenCourseWare", CS50P_OCW_URL)


def render_understanding_block(data: WeekData):
    st.subheader("🧠 哈佛理解课｜加厚版")
    st.markdown(f"**核心问题：** {data.core_question}")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**生活类比**")
        for x in data.life_analogy:
            st.write(f"- {x}")
    with c2:
        st.markdown("**思维拆解**")
        for x in data.thinking_steps:
            st.write(f"- {x}")

    st.markdown("**考试映射**")
    for x in data.exam_mapping:
        st.write(f"- {x}")


def render_codelab(data: WeekData):
    st.subheader("🎮 趣味游戏 Code Lab")
    st.markdown(f"**{data.code_lab_title}**")
    st.write(data.code_lab_story)
    tab1, tab2, tab3 = st.tabs(["跟敲", "微改", "小挑战"])
    with tab1:
        st.markdown("**先跟着敲一遍，先有手感。**")
        st.code(data.follow_code, language="python")
        st.caption("目标：能把代码独立敲进编辑器并顺利运行。")
    with tab2:
        st.markdown("**第二步不是抄完就结束，而是改一小点。**")
        st.write(data.modify_task)
        st.info(f"提示：{data.modify_hint}")
    with tab3:
        st.markdown("**第三步用一个小挑战，把‘看懂’变成‘会写一点’。**")
        st.write(data.challenge_task)
        st.info(f"提示：{data.challenge_hint}")


def render_write_prompt(data: WeekData):
    st.subheader("💻 写代码题")
    st.write(data.write_code_prompt)
    c1, c2, c3 = st.columns(3)
    c1.info(f"基础：{data.write_code_levels['基础']}")
    c2.info(f"进阶：{data.write_code_levels['进阶']}")
    c3.info(f"挑战：{data.write_code_levels['挑战']}")
    st.text_area("在这里先写思路，再去本地编辑器实现", key=f"write_plan_{data.week}", height=120)


def render_quiz(week: int):
    quiz = make_quiz(week)
    st.subheader("📝 周测系统｜4层结构")
    st.caption("Part A 概念理解｜Part B 读代码｜Part C 改错/补全｜Part D 写代码题")

    answers = []
    for idx, q in enumerate(quiz, start=1):
        st.markdown(f"**Q{idx}. [{q['part']}] {q['prompt']}**")
        choice = st.radio(
            f"week{week}_q{idx}",
            q["options"],
            key=f"week{week}_q{idx}",
            label_visibility="collapsed",
        )
        answers.append(choice)
        st.caption(f"难度：{q['difficulty']}")

    if st.button(f"提交 Week {week} 周测", key=f"submit_week_{week}"):
        score = 0
        skills = {"概念理解": [0, 0], "读代码": [0, 0], "改错补全": [0, 0], "写代码思维": [0, 0]}
        for choice, q in zip(answers, quiz):
            skill = q["skill"]
            skills[skill][1] += 1
            if q["options"].index(choice) == q["answer"]:
                score += 1
                skills[skill][0] += 1
        st.session_state.quiz_scores[week] = score
        st.success(f"本次得分：{score} / {len(quiz)}")
        st.markdown("### 📊 能力分析")
        for skill, (correct, total) in skills.items():
            pct = int(correct / total * 100) if total else 0
            st.write(f"- {skill}: {correct}/{total}（{pct}%）")
        for idx, q in enumerate(quiz, start=1):
            st.info(f"Q{idx} 正确答案：{q['options'][q['answer']]}｜解析：{q['explanation']}")


def render_week(week: int):
    data = WEEKS[week]
    col1, col2 = st.columns([2.2, 1])
    with col1:
        st.markdown(f"## Week {data.week}｜{data.title}")
        st.markdown(f"### 🎯 本周主题：{data.theme}")
        st.caption(data.stage)
    with col2:
        done = week in st.session_state.completed_weeks
        st.metric("完成状态", "已完成" if done else "进行中")
        if st.button("✅ 标记本周完成", key=f"done_{week}"):
            mark_week_complete(week)
            st.success("已记录完成。")

    render_harvard_links(week)
    st.divider()

    left, right = st.columns([1.45, 1])
    with left:
        render_understanding_block(data)
        st.markdown("### 📘 教材 / 课程焦点")
        for item in data.textbook_focus:
            st.write(f"- {item}")
        st.markdown("### 🎯 本周目标")
        for item in data.exam_goals:
            st.write(f"- {item}")
    with right:
        render_codelab(data)
        st.markdown("### 🗒️ 本周学习笔记")
        st.session_state.notes[week] = st.text_area(
            "写下本周最重要的 3 句话",
            value=st.session_state.notes[week],
            key=f"note_{week}",
            height=160,
        )

    st.divider()
    st.markdown("### ⏰ 建议学习分配（每周3小时）")
    st.write("- 周六 1小时：Harvard Shorts / 讲义 + 哈佛理解课")
    st.write("- 周日 1小时：Code Lab 跟敲 / 微改 + 教材映射")
    st.write("- 周一 1小时：小挑战 + 写代码题 + 周测系统")

    render_write_prompt(data)
    st.divider()
    render_quiz(week)


def render_home():
    st.markdown(
        """
        <div style="padding:1rem 1.2rem;border-radius:18px;background:linear-gradient(135deg,#edf5ff,#f7fbff);border:1px solid #d7e7ff;">
            <h2 style="margin-bottom:0.25rem;">🐍 Python 24-Week Learning System</h2>
            <div>Harvard CS50 逻辑 + 教材考试落地 + 项目拔高 + 家长陪学视角</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("总进度", f"{progress_percent()}%")
    c2.metric("已完成周数", f"{len(st.session_state.completed_weeks)} / 24")
    avg = round(sum(st.session_state.quiz_scores.values()) / max(len(st.session_state.quiz_scores), 1), 2) if st.session_state.quiz_scores else 0
    c3.metric("平均周测得分", avg)
    c4.metric("课程阶段", "24周完整版")
    st.progress(progress_percent() / 100)

    left, right = st.columns([1.5, 1])
    with left:
        st.markdown("### 🚀 系统目标")
        st.write("- 前 8 周：打基础 + 应试，建立‘不怕 Python’的感觉")
        st.write("- 中 8 周：从‘会写一点’升级到‘会用 Python 做事’")
        st.write("- 后 8 周：做项目、接触数据和 AI 方向，建立长线能力")

        st.markdown("### 🗺️ 24周学习路线")
        for phase_name, start, end in [("Phase 1｜Foundation", 1, 8), ("Phase 2｜Application", 9, 16), ("Phase 3｜Project & AI", 17, 24)]:
            st.markdown(f"**{phase_name}**")
            for i in range(start, end + 1):
                status = "✅" if i in st.session_state.completed_weeks else "⬜"
                st.write(f"{status} Week {i}: {WEEKS[i].title}")
    with right:
        next_week = next((i for i in range(1, 25) if i not in st.session_state.completed_weeks), 24)
        d = WEEKS[next_week]
        st.markdown("### 💡 当前推荐")
        st.write(f"**建议先学：Week {next_week}**")
        st.write(d.title)
        st.write(f"主题：{d.theme}")
        st.caption(d.stage)
        st.markdown("### 👨‍👩‍👧 家长提醒")
        st.info(PARENT_TIPS[next_week])

    st.divider()
    st.markdown("### 🎓 Harvard Learning Path")
    hc1, hc2, hc3 = st.columns(3)
    with hc1:
        st.markdown("#### CS50P 主课程")
        st.write("作为 Python 主线基础课，建议 Shorts / 讲义优先。")
        link_button("Open CS50P Official Page", CS50P_PLL_URL)
    with hc2:
        st.markdown("#### CS50P OpenCourseWare")
        st.write("课程周次、讲义和材料都在这里。")
        link_button("Open CS50P OpenCourseWare", CS50P_OCW_URL)
    with hc3:
        st.markdown("#### ML & AI with Python")
        st.write("更适合作为第 17 周以后概念拓展与兴趣延伸。")
        link_button("Open ML & AI Course", ML_AI_URL)

    st.divider()
    st.markdown("### 📌 使用说明")
    st.write("1. 每周先打开 Harvard 对应页面，但默认只看 Shorts / 讲义核心。")
    st.write("2. 再学哈佛理解课，抓核心问题、生活类比、思维拆解和考试映射。")
    st.write("3. Code Lab 一定按‘跟敲 → 微改 → 小挑战’走。")
    st.write("4. 周测系统用于检查概念理解、读代码、改错补全和写代码思路。")


def render_harvard_course_hub():
    st.markdown("## 🎓 Harvard Course Hub｜哈佛课程中心")
    st.write("系统默认策略：**Shorts / 讲义优先，Lecture 选看**。24周课程分三个阶段接入 Harvard 资源。")

    a, b = st.columns(2)
    with a:
        st.markdown("### 主线课程：CS50's Introduction to Programming with Python")
        st.write("适合作为 Python 主线基础课。前 1–16 周主要参考这里的逻辑与讲义。")
        link_button("CS50P Official Course Page", CS50P_PLL_URL)
        link_button("CS50P OpenCourseWare", CS50P_OCW_URL)
    with b:
        st.markdown("### 进阶课程：Machine Learning and AI with Python")
        st.write("更适合作为 17–24 周的兴趣拓展入口。")
        link_button("Open ML & AI with Python", ML_AI_URL)

    st.divider()
    st.markdown("### 三阶段如何使用 Harvard 资源")
    st.write("- Phase 1（1–8周）：CS50P 为主，重点是基础逻辑与考试映射。")
    st.write("- Phase 2（9–16周）：继续借 Harvard 的问题拆解方式，但更强调应用。")
    st.write("- Phase 3（17–24周）：把 Harvard AI 课程作为概念与方向感入口。")


def render_exam_center():
    st.markdown("## 🧾 Exam Center｜考试中心")
    st.write("这里用于刷基础题、看提示、背模板，也适合阶段性复盘。")

    mode = st.selectbox("选择练习模式", ["随机练习", "只看答案提示"])
    for idx, item in enumerate(EXAM_BANK, start=1):
        with st.expander(f"{idx}. [{item['type']}] {item['question'].splitlines()[0]}"):
            st.write(item["question"])
            if mode == "随机练习":
                st.text_input(f"你的答案 #{idx}", key=f"exam_{idx}")
                if st.button(f"查看参考答案 #{idx}", key=f"show_exam_{idx}"):
                    st.success(f"参考答案：{item['answer']}")
                    st.info(f"提示：{item['hint']}")
            else:
                st.info(f"提示：{item['hint']}")
                st.success(f"参考答案：{item['answer']}")

    st.divider()
    st.markdown("### 🎯 高频模板")
    tab1, tab2, tab3, tab4 = st.tabs(["奇偶判断", "成绩分级", "1-100循环", "基础函数"])
    with tab1:
        st.code("""n = int(input())
if n % 2 == 0:
    print('偶数')
else:
    print('奇数')""", language="python")
    with tab2:
        st.code("""score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('C')""", language="python")
    with tab3:
        st.code("""for i in range(1, 101):
    print(i)""", language="python")
    with tab4:
        st.code("""def add(a, b):
    return a + b""", language="python")


def render_parent_panel():
    st.markdown("## 👨‍👩‍👧 Parent Panel｜家长面板")
    st.write("这个页面帮助家长快速看进度、看薄弱点、看陪学建议。")

    c1, c2, c3 = st.columns(3)
    c1.metric("完成周数", len(st.session_state.completed_weeks))
    c2.metric("总进度", f"{progress_percent()}%")
    weak = "基础阶段优先稳住输入 / 判断 / 循环" if len(st.session_state.quiz_scores) < 6 else "根据最近周测继续观察薄弱项"
    c3.metric("当前关注点", weak)

    st.markdown("### 📈 周测记录")
    if st.session_state.quiz_scores:
        for week in range(1, 25):
            if week in st.session_state.quiz_scores:
                total = len(make_quiz(week))
                st.write(f"- Week {week}: {st.session_state.quiz_scores[week]} / {total}")
            else:
                st.write(f"- Week {week}: 尚未提交")
    else:
        st.info("还没有周测记录。")

    selected_week = st.selectbox("选择周数", list(range(1, 25)), format_func=lambda x: f"Week {x}")
    st.markdown("### 🪄 每周陪学建议")
    st.info(PARENT_TIPS[selected_week])

    st.markdown("### 🗒️ 学生笔记总览")
    for week in range(1, 25):
        with st.expander(f"Week {week} 学习笔记"):
            note = st.session_state.notes.get(week, "")
            st.write(note if note.strip() else "暂无笔记")


def render_about():
    st.markdown("## ℹ️ 系统说明")
    st.write("这是一个面向零基础、学习时间有限、又希望从考试走向能力的 Python 24 周学习系统。")
    st.write("设计逻辑：Harvard Shorts First → 哈佛理解课 → Code Lab → 教材/课程映射 → 写代码题 → 周测系统。")
    st.write("当前版本为 Streamlit 可运行版，适合先测试内容结构与交互流程。")


# ---------- Sidebar ----------
st.sidebar.title("📚 Navigation")
page_options = ["Home", "Harvard Course Hub"] + [f"Week {i}" for i in range(1, 25)] + ["Exam Center", "Parent Panel", "About"]
page = st.sidebar.radio("选择页面", page_options)

st.sidebar.markdown("---")
st.sidebar.write(f"**进度：{progress_percent()}%**")
st.sidebar.progress(progress_percent() / 100)
st.sidebar.markdown("### 🧭 Three Phases")
st.sidebar.write("- Phase 1：Week 1–8")
st.sidebar.write("- Phase 2：Week 9–16")
st.sidebar.write("- Phase 3：Week 17–24")
st.sidebar.markdown("### 🎓 Quick Links")
st.sidebar.markdown(f"- [CS50P Official]({CS50P_PLL_URL})")
st.sidebar.markdown(f"- [CS50P OCW]({CS50P_OCW_URL})")
st.sidebar.markdown(f"- [ML & AI with Python]({ML_AI_URL})")

if page == "Home":
    render_home()
elif page == "Harvard Course Hub":
    render_harvard_course_hub()
elif page.startswith("Week"):
    render_week(int(page.split()[1]))
elif page == "Exam Center":
    render_exam_center()
elif page == "Parent Panel":
    render_parent_panel()
else:
    render_about()
