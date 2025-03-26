import matplotlib.pyplot as plt
import numpy as np

def create_educational_games_core_elements_chart():
    """创建教育游戏核心要素图表"""
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    
    # 要素和描述
    elements = [
        '教育目标',
        '游戏化体验',
        '渐进式难度',
        '即时反馈',
        '情境化内容',
        '多样化路径',
        '社交互动',
        '评估机制'
    ]
    
    # 创建柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 绘制柱状图
    y_pos = np.arange(len(elements))
    values = np.ones(len(elements)) * 100  # 所有要素同等重要
    
    bars = ax.barh(y_pos, values, align='center', color='#3498db', alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(elements, fontsize=12)
    ax.invert_yaxis()  # 从上到下显示标签
    ax.set_xlabel('重要性', fontsize=12)
    ax.set_xlim(0, 120)  # 为了留出空间显示标签
    
    # 在柱状图上添加标签
    for i, bar in enumerate(bars):
        ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                '核心要素', va='center', fontsize=10)
    
    # 设置标题
    plt.title('教育游戏的核心要素', size=20, fontweight='bold')
    
    # 添加描述文本
    plt.figtext(0.5, 0.01, '教育游戏核心要素图表 © 教育游戏社团', ha='center', fontsize=12)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/educational_games_core_elements.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 创建带有描述的图表
    descriptions = [
        '明确的教育目标和预期学习成果',
        '提供真正的游戏体验，激发内在动机',
        '从简单到复杂的难度设计',
        '提供及时、有意义的反馈',
        '将学习内容置于有意义的情境中',
        '适应不同学习风格和能力的学习路径',
        '促进学习者之间的互动和协作',
        '帮助了解学习进展和成效'
    ]
    
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.axis('off')
    
    # 添加标题
    ax.text(0.5, 0.95, '教育游戏的核心要素及描述', ha='center', va='top', fontsize=20, fontweight='bold')
    
    # 添加要素和描述
    for i, (element, desc) in enumerate(zip(elements, descriptions)):
        y_pos = 0.85 - i * 0.1
        ax.text(0.1, y_pos, f"{i+1}. {element}:", fontsize=14, fontweight='bold')
        ax.text(0.3, y_pos, desc, fontsize=12)
    
    # 添加注释
    ax.text(0.5, 0.05, '教育游戏核心要素详细说明 © 教育游戏社团', ha='center', fontsize=10)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/educational_games_core_elements_description.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_educational_games_research_framework():
    """创建教育游戏研究框架图"""
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    
    # 创建图表
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    # 定义框架层级
    layers = [
        '理论基础层',
        '设计要素层',
        '实施过程层',
        '评估反馈层',
        '影响因素层'
    ]
    
    descriptions = [
        '学习理论、游戏设计理论、学科领域理论',
        '教育目标、内容结构、游戏机制、交互方式、反馈系统、评估方法',
        '游戏环境搭建、学习者引导和支持、教师角色和干预、技术支持',
        '学习成效评估、游戏体验评价、实施过程监测和改进',
        '学习者因素、环境因素、游戏特性因素'
    ]
    
    # 绘制框架层级
    box_height = 0.15
    box_spacing = 0.05
    box_width = 0.8
    
    for i, (layer, desc) in enumerate(zip(layers, descriptions)):
        y_pos = 0.8 - i * (box_height + box_spacing)
        
        # 绘制框
        rect = plt.Rectangle((0.1, y_pos), box_width, box_height, 
                            facecolor='#3498db', alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        
        # 添加层级名称
        ax.text(0.5, y_pos + box_height/2, layer, ha='center', va='center', 
                fontsize=14, fontweight='bold', color='white')
        
        # 添加描述
        ax.text(0.5, y_pos - 0.02, desc, ha='center', va='top', 
                fontsize=10, style='italic')
    
    # 添加标题
    ax.text(0.5, 0.95, '教育游戏研究框架', ha='center', va='top', 
            fontsize=20, fontweight='bold')
    
    # 添加箭头表示层级之间的关系
    arrow_x = 0.05
    for i in range(len(layers)-1):
        y_start = 0.8 - i * (box_height + box_spacing)
        y_end = y_start - (box_height + box_spacing)
        ax.arrow(arrow_x, y_start, 0, y_end - y_start + box_height, 
                head_width=0.02, head_length=0.02, fc='black', ec='black')
    
    # 添加注释
    ax.text(0.5, 0.05, '教育游戏研究框架图 © 教育游戏社团', ha='center', fontsize=10)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/educational_games_research_framework.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_educational_games_types_comparison():
    """创建不同类型教育游戏对比图"""
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    
    # 定义游戏类型和评估维度
    game_types = ['Unity 3D游戏', 'Unity 2D游戏', 'HTML5/Web游戏', '移动端游戏', 'VR/AR游戏']
    dimensions = ['开发复杂度', '沉浸感', '可访问性', '跨平台性', '硬件要求']
    
    # 评分数据 (1-5分)
    scores = np.array([
        [5, 5, 2, 3, 4],  # Unity 3D
        [3, 3, 3, 4, 2],  # Unity 2D
        [2, 2, 5, 5, 1],  # HTML5/Web
        [3, 2, 4, 3, 2],  # 移动端
        [5, 5, 1, 2, 5]   # VR/AR
    ])
    
    # 创建热力图
    fig, ax = plt.subplots(figsize=(12, 8))
    im = ax.imshow(scores, cmap='YlGnBu')
    
    # 添加标签
    ax.set_xticks(np.arange(len(dimensions)))
    ax.set_yticks(np.arange(len(game_types)))
    ax.set_xticklabels(dimensions, fontsize=12)
    ax.set_yticklabels(game_types, fontsize=12)
    
    # 旋转x轴标签
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # 添加数值标签
    for i in range(len(game_types)):
        for j in range(len(dimensions)):
            text = ax.text(j, i, scores[i, j], ha="center", va="center", color="black", fontsize=12)
    
    # 添加标题
    ax.set_title("不同类型教育游戏对比 (1-5分评估)", fontsize=16, fontweight='bold')
    
    # 添加颜色条
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("评分 (1=低, 5=高)", rotation=-90, va="bottom", fontsize=12)
    
    # 添加注释
    plt.figtext(0.5, 0.01, '教育游戏类型对比图 © 教育游戏社团', ha='center', fontsize=10)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/educational_games_types_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 创建优缺点表格
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.axis('off')
    
    # 添加标题
    ax.text(0.5, 0.95, '不同类型教育游戏的优缺点', ha='center', va='top', fontsize=20, fontweight='bold')
    
    # 定义表格内容
    types = game_types
    advantages = [
        '强大的可视化能力，高度沉浸感，支持复杂交互',
        '开发周期短，成本较低，适合初学者学习游戏开发',
        '无需下载安装，跨平台兼容，易于分享和传播',
        '便携性强，随时随地可访问，可利用移动设备特殊功能',
        '提供最沉浸式的学习体验，支持直观的交互方式'
    ]
    
    disadvantages = [
        '学习曲线陡峭，开发成本高，需要专业团队',
        '图形和物理效果不如3D游戏，表现力有限',
        '性能受限于浏览器和网络条件，复杂功能实现困难',
        '受设备性能和屏幕尺寸限制，需要应用商店审核',
        '硬件要求高，开发成本高，用户基础相对较小'
    ]
    
    suitable_scenarios = [
        '科学实验模拟，历史场景重现，复杂系统可视化教学',
        '基础编程教学，逻辑思维训练，简单科学概念演示',
        '教育机构在线学习平台，编程教学，快速原型设计',
        '碎片化学习，儿童早期教育，语言学习',
        '医学教育，工程培训，历史文化遗产虚拟参观'
    ]
    
    # 绘制表格
    row_height = 0.15
    col_widths = [0.2, 0.25, 0.25, 0.3]
    headers = ['游戏类型', '优势', '劣势', '适用场景']
    
    # 绘制表头
    for i, header in enumerate(headers):
        x_pos = sum(col_widths[:i]) + col_widths[i]/2
        ax.text(x_pos, 0.9, header, ha='center', va='center', fontsize=14, fontweight='bold')
    
    # 绘制分隔线
    ax.axhline(y=0.88, xmin=0, xmax=1, color='black', linewidth=1)
    
    # 绘制表格内容
    for i, (type_name, adv, disadv, scenario) in enumerate(zip(types, advantages, disadvantages, suitable_scenarios)):
        y_pos = 0.85 - i * row_height
        
        # 游戏类型
        ax.text(col_widths[0]/2, y_pos, type_name, ha='center', va='center', fontsize=12, fontweight='bold')
        
        # 优势
        ax.text(col_widths[0] + col_widths[1]/2, y_pos, adv, ha='center', va='center', fontsize=10, wrap=True)
        
        # 劣势
        ax.text(col_widths[0] + col_widths[1] + col_widths[2]/2, y_pos, disadv, ha='center', va='center', fontsize=10, wrap=True)
        
        # 适用场景
        ax.text(col_widths[0] + col_widths[1] + col_widths[2] + col_widths[3]/2, y_pos, scenario, ha='center', va='center', fontsize=10, wrap=True)
        
        # 绘制行分隔线
        if i < len(types) - 1:
            ax.axhline(y=y_pos - row_height/2, xmin=0, xmax=1, color='black', linewidth=0.5, alpha=0.3)
    
    # 绘制列分隔线
    for i in range(1, len(col_widths)):
        x_pos = sum(col_widths[:i])
        ax.axvline(x=x_pos, ymin=0.1, ymax=0.88, color='black', linewidth=0.5, alpha=0.3)
    
    # 添加注释
    ax.text(0.5, 0.05, '教育游戏类型优缺点对比表 © 教育游戏社团', ha='center', fontsize=10)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/educational_games_types_advantages_disadvantages.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_ai_educational_games_cases():
    """创建大模型+教育游戏案例展示图"""
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    
    # 创建图表
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.axis('off')
    
    # 添加标题
    ax.text(0.5, 0.95, '大模型+教育游戏优秀案例', ha='center', va='top', fontsize=20, fontweight='bold')
    
    # 定义案例内容
    cases = [
        '学学孙膑 (清华大学深圳)',
        '学学孔子 (清华大学深圳)',
        'AgentMarket (清华大学深圳)',
        'Khanmigo (可汗学院)',
        '以正教育大模型',
        'Cogniti化学教育Agent'
    ]
    
    types = [
        '养成类AI教育游戏',
        '角色扮演与古代文化学习',
        'AI社交游戏',
        'AI教育助手',
        '教育大模型系统',
        '学科专用AI教育助手'
    ]
    
    features = [
        '角色扮演、AI互动、教育目标、进化能力',
        '文化浸润、情境学习、智能对话、知识检验',
        'AI捏人、多角色互动、社交环境、动态剧情',
        '个性化指导、教师助手、写作教练、问题解决',
        '多Agent协作、自主交互、个性化教学、全面覆盖',
        '学科专精、教育公平、理解检测、知识评估'
    ]
    
    values = [
        '探索教师与学生互动模式，体验教育过程中的挑战和成就感',
        '传承和弘扬中国传统文化，以生动互动方式学习儒家经典',
        '探索AI社交互动可能性，体验不同性格和背景的AI角色',
        '提供即时个性化学习支持，培养独立思考和问题解决能力',
        '提高教学效率和质量，实现教育资源的智能化整合与个性化推送',
        '促进教育公平，缩小学生之间的知识差距，提供专业学科支持'
    ]
    
    # 绘制案例卡片
    card_height = 0.13
    card_spacing = 0.03
    card_width = 0.9
    
    for i, (case, type_name, feature, value) in enumerate(zip(cases, types, features, values)):
        y_pos = 0.85 - i * (card_height + card_spacing)
        
        # 绘制卡片背景
        rect = plt.Rectangle((0.05, y_pos), card_width, card_height, 
                            facecolor='#f0f0f0', alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        
        # 添加案例名称
        ax.text(0.1, y_pos + card_height - 0.02, case, ha='left', va='top', 
                fontsize=14, fontweight='bold', color='#3498db')
        
        # 添加类型
        ax.text(0.1, y_pos + card_height - 0.05, f"类型: {type_name}", ha='left', va='top', 
                fontsize=12, color='#333333')
        
        # 添加特点
        ax.text(0.1, y_pos + card_height/2 - 0.02, f"特点: {feature}", ha='left', va='center', 
                fontsize=10, color='#333333')
        
        # 添加教育价值
        ax.text(0.1, y_pos + 0.02, f"教育价值: {value}", ha='left', va='bottom', 
                fontsize=10, color='#333333', style='italic')
    
    # 添加注释
    ax.text(0.5, 0.05, '大模型+教育游戏案例展示 © 教育游戏社团', ha='center', fontsize=10)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/ai_educational_games_cases.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 创建发展趋势图
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    # 添加标题
    ax.text(0.5, 0.95, '大模型+教育游戏的发展趋势与前景', ha='center', va='top', fontsize=20, fontweight='bold')
    
    # 定义趋势和前景
    trends = [
        '个性化学习的深化',
        '多模态交互的普及',
        '情感计算的融入',
        '协作学习的增强',
        '跨学科整合的加强'
    ]
    
    trend_descs = [
        '大模型将能够更精准识别学习者特点，提供高度个性化的学习内容和路径',
        '结合语音、图像、视频等多种模态，创造更丰富、更沉浸的学习体验',
        '识别和响应学习者的情绪状态，调整教学策略，建立更自然的师生关系',
        '支持多人协作学习环境，促进互动和知识共享，培养团队合作能力',
        '打破学科界限，实现知识的综合应用，培养跨学科思维和创新能力'
    ]
    
    prospects = [
        '教育资源的普及与公平',
        '终身学习的支持',
        '教育评估的革新',
        '教育生态的重构',
        '技术与人文的融合'
    ]
    
    prospect_descs = [
        '优质教育资源的广泛分享，缩小不同地区、群体间的教育差距',
        '为各年龄段、各职业背景的学习者提供支持，适应快速变化的知识需求',
        '从结果评估转向过程评估，关注全面发展，提供及时有效的反馈',
        '教师角色转变，学校功能拓展，教育理念更新，从标准化到个性化',
        '技术赋能下的人文关怀，价值观和伦理意识培养，人机协作新模式'
    ]
    
    # 绘制趋势部分
    ax.text(0.25, 0.85, '发展趋势', ha='center', va='center', fontsize=16, fontweight='bold')
    
    for i, (trend, desc) in enumerate(zip(trends, trend_descs)):
        y_pos = 0.75 - i * 0.1
        ax.text(0.1, y_pos, f"{i+1}. {trend}", ha='left', va='center', fontsize=12, fontweight='bold')
        ax.text(0.1, y_pos - 0.03, desc, ha='left', va='top', fontsize=10, wrap=True)
    
    # 绘制前景部分
    ax.text(0.75, 0.85, '未来前景', ha='center', va='center', fontsize=16, fontweight='bold')
    
    for i, (prospect, desc) in enumerate(zip(prospects, prospect_descs)):
        y_pos = 0.75 - i * 0.1
        ax.text(0.6, y_pos, f"{i+1}. {prospect}", ha='left', va='center', fontsize=12, fontweight='bold')
        ax.text(0.6, y_pos - 0.03, desc, ha='left', va='top', fontsize=10, wrap=True)
    
    # 添加分隔线
    ax.axvline(x=0.5, ymin=0.1, ymax=0.9, color='black', linewidth=0.5, alpha=0.3)
    
    # 添加注释
    ax.text(0.5, 0.05, '大模型+教育游戏发展趋势与前景 © 教育游戏社团', ha='center', fontsize=10)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/ai_educational_games_trends_prospects.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_educational_games_core_elements_chart()
    create_educational_games_research_framework()
    create_educational_games_types_comparison()
    create_ai_educational_games_cases()
