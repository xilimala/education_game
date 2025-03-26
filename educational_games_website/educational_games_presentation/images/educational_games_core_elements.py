import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    """创建雷达图"""
    # 计算角度
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarAxes(PolarAxes):
        name = 'radar'
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """重写fill方法以便于绘制雷达图"""
            return super().fill(*(np.deg2rad(np.rad2deg(args[0]) + 90), *args[1:]),
                                closed=closed, **kwargs)

        def plot(self, *args, **kwargs):
            """重写plot方法以便于绘制雷达图"""
            return super().plot(*(np.deg2rad(np.rad2deg(args[0]) + 90), *args[1:]),
                                **kwargs)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta) + 90, labels)

        def _gen_axes_patch(self):
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                spine_dict = {}
                for i in range(num_vars):
                    spine = Spine(axes=self,
                                  spine_type='line',
                                  path=Path([(0.5, 0.5),
                                            (0.5 + 0.5 * np.cos(theta[i] + np.pi / 2),
                                             0.5 + 0.5 * np.sin(theta[i] + np.pi / 2))]))
                    spine.set_transform(Affine2D().scale(1.0, 1.0) +
                                        self.transAxes)
                    spine_dict[f'spine{i}'] = spine
                return spine_dict
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


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
    
    # 创建雷达图
    theta = radar_factory(len(elements), frame='polygon')
    
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='radar'))
    
    # 绘制雷达图
    values = np.ones(len(elements))
    ax.plot(theta, values, 'o-', linewidth=2, color='#3498db')
    ax.fill(theta, values, alpha=0.25, color='#3498db')
    
    # 设置标签
    ax.set_varlabels(elements)
    
    # 设置标题
    plt.title('教育游戏的核心要素', size=20, y=1.1, fontweight='bold')
    
    # 添加描述文本
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
    
    # 在图表下方添加描述
    plt.figtext(0.5, 0.01, '教育游戏核心要素图表 © 教育游戏社团', ha='center', fontsize=12)
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('/home/ubuntu/educational_games_presentation/images/educational_games_core_elements.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 创建带有描述的图表
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

if __name__ == "__main__":
    create_educational_games_core_elements_chart()
