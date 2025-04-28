'''
#3.29 增加字体控制，修正滚动条错误
增加面部表情识别与统计

'''
'''
#3.30 增加DEEPface面部表情识别功能
#3.31 修正警告，中文显示表情
4.3 重新尝试打包
pyinstaller --name=MyApp --add-data="venv/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --hidden-import="cv2" --hidden-import="PIL" --hidden-import="ultralytics.models.yolo" C_D_FE_V_P.py
4.4 打包程序
增加视频数据记录与导出功能、输出记录文件名规则
pyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/cv2;cv2" --add-data="deepface_weights/*;deepface_weights" --hidden-import="tf_keras" --hidden-import="keras.src.backend" --hidden-import="cv2" --hidden-import="PIL" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --hidden-import="torchvision.models" --hidden-import="tensorflow.keras.layers" --clean --onefile --noconsole C_D_4_5.py
4.5视频采集窗口的颜色与透明度调节设置
footer label Row =6 
pyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/ultralytics/cfg/solutions/*.yaml;ultralytics/cfg/solutions" --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/cv2;cv2" --add-data="deepface_weights/*;deepface_weights" --hidden-import="tf_keras" --hidden-import="keras.src.backend" --hidden-import="cv2" --hidden-import="PIL" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --hidden-import="torchvision.models" --hidden-import="tensorflow.keras.layers" --clean --onefile --noconsole C_D_4_5.py
4.6 建立新的虚拟环境，然后完成打包
4.7 重新打包
pyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/cv2;cv2" --add-data="deepface_weights/*;deepface_weights" --hidden-import="tf_keras" --hidden-import="keras.src.backend" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --hidden-import="torchvision.models" --hidden-import="tensorflow.keras.layers" --clean --onefile --noconsole C_D_4_5.py
#建立当前编译器的虚拟环境，Ctrl+Shift+P 选择，实现新环境激活。python -m venv pack_env --system-site-packages
#500M的打包zhipyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="deepface_weights/*;deepface_weights" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --clean --onefile --noconsole C_D_4_5.py
3.10.7 tf_env虚拟环境
命令：pyinstaller --icon=visio45.ico  --collect-all tensorflow --collect-all keras --collect-all deepface --add-data="yolov8n.pt;." --add-data="deepface_weights/*;deepface_weights" --clean --onefile --noconsole C_D_4_5.py
4.23日 删除Keras.api确保本地运行
pyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/cv2;cv2" --add-data="deepface_weights/*;deepface_weights"  --hidden-import="deepface.basemodels" --hidden-import="deepface.modules" --hidden-import="tf_keras" --hidden-import="keras.src.backend" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --hidden-import="torchvision.models" --hidden-import="tensorflow.keras.layers" --clean --onefile --noconsole C_D_423.py
4.26  解决pyinstaller CV2打包错误
pyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --add-data="E:/2025study/2025Python/code/crowed_density/.venv/Lib/site-packages/cv2/*.*;cv2"  --collect-all cv2 --add-data="deepface_weights/*;deepface_weights"  --hidden-import="deepface.basemodels" --hidden-import="deepface.modules" --hidden-import="tf_keras" --hidden-import="keras.src.backend" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --hidden-import="torchvision.models" --hidden-import="tensorflow.keras.layers" --clean --onefile --noconsole C_D_423.py
生成了可执行的EXE，解决了CV2错误，但一点击开始检测软件就奔溃啦。
4.28 np_fix_env环境可以执行，生成requriments.txt
2.0版本用下面的打包命令发布
pyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --add-data="E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages/cv2/*.*;cv2"  --collect-all cv2 --add-data="deepface_weights/*;deepface_weights"  --hidden-import="deepface.basemodels" --hidden-import="deepface.modules" --hidden-import="tf_keras" --hidden-import="keras.src.backend" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --hidden-import="deepface.models.facial_recognition" --hidden-import="torchvision.models" --hidden-import="tensorflow.keras.layers" --paths="E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages" --clean --windowed --onefile --noconsole C_D_426.py
发布成安装包的打包命令，小的EXE文件。
pyinstaller --icon=visio45.ico --add-data="yolov8n.pt;." --add-data="E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages/ultralytics/cfg/*.yaml;ultralytics/cfg" --add-data="E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages/cv2/*.*;cv2"  --collect-all cv2 --add-data="deepface_weights/*;deepface_weights"  --hidden-import="deepface.basemodels" --hidden-import="deepface.modules" --hidden-import="tf_keras" --hidden-import="keras.src.backend" --hidden-import="ultralytics.models.yolo" --hidden-import="deepface.extendedmodels" --hidden-import="deepface.models.facial_recognition" --hidden-import="torchvision.models" --hidden-import="tensorflow.keras.layers" --paths="E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages" --clean --windowed  --noconsole C_D_426.py
'''

# from pathlib import Pathvisio
from deepface.models.facial_recognition import VGGFace
from deepface import DeepFace 
#from deepface.basemodels import VGGFace
from tensorflow import keras
import time
import csv  # 在文件开头添加csv导入
from pathlib import Path
import sys
import os
import tkinter as tk
from deepface import DeepFace
from ultralytics import YOLO
import torch
import tensorflow as tf
import torchvision
from tkinter import ttk, StringVar, messagebox
import cv2
import numpy as np
from PIL import ImageGrab, Image
import threading
sys.path.append("path/to/ultralytics")
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # 禁用GPU
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"     # 禁用TensorFlow日志
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"     # 禁用TensorFlow日志
os.environ["TF_USE_LEGACY_KERAS"] = "1"
os.environ["KERAS_BACKEND"] = "tensorflow"
# 必须放在其他cv2导入之前
os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"
os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # 解决lib冲突
os.environ["CUDA_MODULE_LOADING"] = "LAZY"   # 延迟加载CUDA模块
def get_config_path():
    """动态获取 ultralytics/cfg 目录路径（兼容打包和开发环境）"""
    if getattr(sys, 'frozen', False):
        # 打包后路径：_MEIPASS/ultralytics/cfg
        cfg_path = Path(sys._MEIPASS) / 'ultralytics/cfg'
    else:
        # 开发环境路径：site-packages/ultralytics/cfg
        from ultralytics import __file__ as ultralytics_init_path
        cfg_path = Path(ultralytics_init_path).parent / 'cfg'

    return str(cfg_path)


# 设置环境变量，强制指定 YOLO 配置文件路径
os.environ['ULTRALYTICS_CFG'] = get_config_path()
# 强制加载 TensorFlow 内部 API

# 在代码开头添加以下代码
tf.compat.v1.logging.set_verbosity(
    tf.compat.v1.logging.ERROR)  # 禁用TensorFlow日志
# ---------- 新增兼容性代码 ----------


# 禁用TorchVision的扩展功能
torchvision.disable_beta_transforms_warning()  # 正确方法

# 在文件开头添加以下兼容性代码
# 检查版本兼容性

assert torch.__version__ >= "2.0.1", f"Detected PyTorch {torch.__version__}, required >=2.0.1"
assert torchvision.__version__ >= "0.15.2", f"Detected TorchVision {torchvision.__version__}, required >=0.15.2"


class EnhancedVideoPersonDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("AI赋能教学督导--洛阳理工学院")

        # 初始化字体样式
        self.style = ttk.Style()
        self.default_font = ('Microsoft YaHei', 12)
        self.style.configure('.', font=self.default_font)

        # 模型参数默认值
        self.conf_threshold = 0.5
        self.iou_threshold = 0.45
        # 创建透明覆盖窗口
        self.overlay = tk.Toplevel(root)
        self.overlay.attributes("-alpha", 0.3)
        self.overlay.attributes("-topmost", True)
        self.overlay.config(bg="blue")
        # 在初始化部分修改颜色属性
        self.overlay_color = "#0000FF"  # 使用十六进制颜色值
        self.alpha_value = 0.3
        # 创建自定义按钮样式
        self.style.configure('Color.TButton', background=self.overlay_color)

        # 初始化窗口参数
        self.x, self.y = 420, 100
        self.width, self.height = 800, 600
        self.overlay.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        # 表情统计相关
        self.emotion_counts = {
            '生气': 0,
            '厌恶': 0,
            '恐惧': 0,
            '开心': 0,
            '悲伤': 0,
            '惊讶': 0,
            '中性': 0
        }

        # 创建增强控制面板
        self.create_enhanced_control_panel()
        # 初始化YOLOv8模型
        self.model = YOLO('yolov8n.pt')  # 需提前下载模型
        self.detecting = False
        self.last_time = 0
        self.fps = 5

        # 绑定窗口事件
        self.overlay.bind("<B1-Motion>", self.resize_overlay)
        self.overlay.bind("<Button-1>", self.start_move)
        # 在初始化部分新增以下属性
        self.recording = False
        self.last_log_time = 0
        self.log_interval_seconds = 60
        self.current_person_count = 0
        self.video_filename = "未命名视频"
        # 新增文件名相关属性
        self.current_filename = ""
        self.start_time = None

    def create_enhanced_control_panel(self):
        """创建增强版控制面板"""
        self.control_frame = ttk.LabelFrame(self.root, text="高级控制")
        self.control_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        # 视频区域参数设置
        area_frame = ttk.LabelFrame(self.control_frame, text="检测区域设置")
        area_frame.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        ttk.Label(area_frame, text="宽度:").grid(row=0, column=0)
        self.width_entry = ttk.Entry(area_frame, width=8)
        self.width_entry.insert(0, "800")
        self.width_entry.grid(row=0, column=1)

        ttk.Label(area_frame, text="高度:").grid(row=0, column=2)
        self.height_entry = ttk.Entry(area_frame, width=8)
        self.height_entry.insert(0, "600")
        self.height_entry.grid(row=0, column=3)

        ttk.Label(area_frame, text="X坐标:").grid(row=1, column=0)
        self.x_entry = ttk.Entry(area_frame, width=8)
        self.x_entry.insert(0, "100")
        self.x_entry.grid(row=1, column=1)

        ttk.Label(area_frame, text="Y坐标:").grid(row=1, column=2)
        self.y_entry = ttk.Entry(area_frame, width=8)
        self.y_entry.insert(0, "100")
        self.y_entry.grid(row=1, column=3)

        ttk.Button(area_frame, text="应用参数",
                   command=self.apply_parameters).grid(row=2, columnspan=4, pady=5)

        # 模型参数设置
        param_frame = ttk.LabelFrame(self.control_frame, text="模型参数调整")
        param_frame.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

        # --------- 置信度组件 ---------
        conf_row = ttk.Frame(param_frame)
        conf_row.grid(row=0, column=0, sticky='ew', pady=2)

        ttk.Label(conf_row, text="置信度:").pack(side=tk.LEFT, padx=5)
        self.conf_entry = ttk.Entry(conf_row, width=6)
        self.conf_entry.insert(0, "0.50")
        self.conf_entry.pack(side=tk.LEFT)
        self.conf_value = ttk.Label(conf_row, text="0.50")
        self.conf_value.pack(side=tk.LEFT, padx=5)
        self.conf_entry.bind("<Return>", self.update_from_entry)

        # IOU组件
        iou_row = ttk.Frame(param_frame)
        iou_row.grid(row=1, column=0, sticky='ew', pady=2)

        ttk.Label(iou_row, text="IOU阈值:").pack(side=tk.LEFT, padx=5)
        self.iou_entry = ttk.Entry(iou_row, width=6)
        self.iou_entry.insert(0, "0.45")
        self.iou_entry.pack(side=tk.LEFT)
        self.iou_value = ttk.Label(iou_row, text="0.45")
        self.iou_value.pack(side=tk.LEFT, padx=5)
        self.iou_entry.bind("<Return>", self.update_from_entry)

        # 滑动条设置
        self.conf_slider = ttk.Scale(param_frame, from_=0.1, to=1.0)
        self.conf_slider.set(0.5)
        self.conf_slider.grid(row=0, column=1, sticky='ew')

        self.iou_slider = ttk.Scale(param_frame, from_=0.1, to=0.9)
        self.iou_slider.set(0.45)
        self.iou_slider.grid(row=1, column=1)

        # 绑定滑动条事件（在所有组件初始化后）
        self.conf_slider.configure(
            command=lambda v: self.update_from_slider('conf'))
        self.iou_slider.configure(
            command=lambda v: self.update_from_slider('iou'))
        # 字体设置组件
        font_frame = ttk.LabelFrame(self.control_frame, text="字体设置")
        font_frame.grid(row=3, column=0, padx=5, pady=5, sticky='ew')

        ttk.Label(font_frame, text="字体大小:").pack(side=tk.LEFT, padx=5)
        self.font_size = ttk.Combobox(
            font_frame, values=["10", "12", "14", "16", "18"], width=5)
        self.font_size.set("12")
        self.font_size.pack(side=tk.LEFT)
        ttk.Button(font_frame, text="应用字体", command=self.apply_font).pack(
            side=tk.LEFT, padx=10)

        # 表情统计组件
        emotion_frame = ttk.LabelFrame(self.control_frame, text="表情统计")
        emotion_frame.grid(row=4, column=0, padx=5, pady=5, sticky='ew')

        self.emotion_labels = {}
        emotions = ['开心', '中性', '悲伤', '惊讶', '生气', '恐惧', '厌恶']
        for i, emotion in enumerate(emotions):
            ttk.Label(emotion_frame, text=f"{emotion.capitalize()}:").grid(
                row=i//2, column=(i % 2)*2, padx=5, sticky='e')
            self.emotion_labels[emotion] = ttk.Label(emotion_frame, text="0")
            self.emotion_labels[emotion].grid(
                row=i//2, column=(i % 2)*2+1, padx=5, sticky='w')

        # 检测控制
        ctrl_frame = ttk.Frame(self.control_frame)
        ctrl_frame.grid(row=2, column=0, pady=10)
        self.start_btn = ttk.Button(
            ctrl_frame, text="开始检测", command=self.toggle_detection)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        self.status_label = ttk.Label(ctrl_frame, text="状态: 等待开始")
        self.status_label.pack(side=tk.LEFT)
        self.count_label = ttk.Label(ctrl_frame, text="检测人数: 0")
        self.count_label.pack(side=tk.LEFT, padx=10)
        # 新增底部提示信息
        footer_label = ttk.Label(
            self.control_frame,
            text="改进建议: limeng@lit.edu.cn",
            foreground="#666666",
            font=('Microsoft YaHei', 9)
        )
        footer_label.grid(row=6, column=0, padx=10, pady=(15, 3), sticky='ew')
        # 在原有控件后新增数据记录组件
        log_frame = ttk.LabelFrame(self.control_frame, text="数据记录")
        log_frame.grid(row=5, column=0, padx=5, pady=5, sticky='ew')

        ttk.Label(log_frame, text="视频名称:").grid(row=0, column=0, padx=5)
        self.video_name_entry = ttk.Entry(log_frame, width=20)
        self.video_name_entry.grid(row=0, column=1, padx=5)

        ttk.Label(log_frame, text="记录间隔(分钟):").grid(row=0, column=2, padx=5)
        self.interval_entry = ttk.Entry(log_frame, width=6)
        self.interval_entry.insert(0, "1")
        self.interval_entry.grid(row=0, column=3, padx=5)

        self.log_btn = ttk.Button(
            log_frame, text="开始记录", command=self.toggle_logging)
        self.log_btn.grid(row=0, column=4, padx=5)

        self.log_status = ttk.Label(
            log_frame, text="记录状态: 未启动", foreground="gray")
        self.log_status.grid(row=1, column=0, columnspan=5, pady=3)
        # 修改显示设置部分的控件
        display_frame = ttk.LabelFrame(self.control_frame, text="视频采集窗口颜色设置")
        display_frame.grid(row=3, column=0, padx=5, pady=5, sticky='ew')

        # 颜色选择组件
        color_row = ttk.Frame(display_frame)
        color_row.pack(pady=3, fill=tk.X)

        ttk.Label(color_row, text="窗口颜色:").pack(side=tk.LEFT, padx=5)
        self.color_btn = ttk.Button(
            color_row,
            text="■",
            width=3,
            command=self.choose_color,
            style='Color.TButton'
        )
        self.color_btn.pack(side=tk.LEFT)
        # 透明度组件
        alpha_row = ttk.Frame(display_frame)
        alpha_row.pack(pady=3, fill=tk.X)
        ttk.Label(alpha_row, text="透明度:").pack(side=tk.LEFT, padx=5)
        self.alpha_slider = ttk.Scale(
            alpha_row,
            from_=0.1,
            to=1.0,
            value=self.alpha_value,
            command=lambda v: self.update_display_settings()
        )
        self.alpha_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.alpha_value_label = ttk.Label(
            alpha_row, text=f"{self.alpha_value:.1f}")
        self.alpha_value_label.pack(side=tk.LEFT, padx=5)

    def choose_color(self):
        """打开颜色选择对话框"""
        from tkinter import colorchooser
        color_code = colorchooser.askcolor(
            title="选择窗口颜色",
            initialcolor=self.overlay_color
        )
        if color_code[1]:  # 用户选择了颜色
            self.overlay_color = color_code[1]
            # 通过样式系统更新按钮颜色
            self.style.configure(
                'Color.TButton', background=self.overlay_color)
            self.update_display_settings()

    def update_display_settings(self, event=None):
        """更新显示设置"""
        try:
            # 获取最新透明度值
            new_alpha = round(self.alpha_slider.get(), 1)
            self.alpha_value_label.config(text=f"{new_alpha:.1f}")

            # 应用新设置
            self.overlay.config(bg=self.overlay_color)
            self.overlay.attributes("-alpha", new_alpha)

            # 保存当前设置
            self.alpha_value = new_alpha

        except Exception as e:
            print(f"显示设置更新失败: {str(e)}")

    def toggle_logging(self):
        if self.recording:
            self.recording = False
            self.log_btn.config(text="开始记录")
            self.log_status.config(text="记录状态: 已停止", foreground="black")
        else:
            try:
                # 获取记录参数时锁定文件名
                self.video_filename = self.video_name_entry.get() or "未命名视频"
                # 生成合法文件名
                self.start_time = time.strftime("%Y-%m-%d_%H-%M-%S")
                safe_video_name = "".join(
                    [c if c.isalnum() else "_" for c in self.video_filename])
                self.current_filename = f"{safe_video_name}_{self.start_time}.csv"
                interval = float(self.interval_entry.get())
                if interval <= 0:
                    raise ValueError("间隔必须大于0")
                self.log_interval_seconds = interval * 60
                self.video_filename = self.video_name_entry.get() or "未命名视频"
                self.recording = True
                self.last_log_time = time.time()
                self.log_btn.config(text="停止记录")
                self.log_status.config(
                    text=f"记录中: 每{interval}分钟一次", foreground="green")
            except ValueError as e:
                messagebox.showerror("输入错误", f"无效的时间间隔: {str(e)}")

    def log_data(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "视频名称": self.video_filename,
            "记录时间": timestamp,
            "总人数": self.current_person_count,
            **self.emotion_counts
        }

        # 使用新文件名和正确编码
        file_exists = os.path.exists(self.current_filename)
        with open(self.current_filename, "a", newline="", encoding="utf-8-sig") as f:  # 修改编码
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()  # 自动写入带BOM的头部
            writer.writerow(data)

    def analyze_emotion(self, face_img):
        """使用DEEPface分析面部表情"""
        try:
            # 转换图像格式并调整大小
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            face_img = cv2.resize(face_img, (48, 48))
            analysis = DeepFace.analyze(
                face_img, actions=['emotion'], enforce_detection=False)
            english_emotion = analysis[0]['dominant_emotion']
            # 英文到中文的映射
            emotion_map = {
                'angry': '生气',
                'disgust': '厌恶',
                'fear': '恐惧',
                'happy': '开心',
                'sad': '悲伤',
                'surprise': '惊讶',
                'neutral': '中性'
            }
            return emotion_map.get(english_emotion, '未知')
        except Exception as e:
            print(f"表情分析失败: {str(e)}")
            return None

    def apply_font(self):
        """应用字体设置"""
        try:
            new_size = int(self.font_size.get())
            self.style.configure('.', font=('Microsoft YaHei', new_size))
            # 更新特殊控件
            self.style.configure('TCombobox', font=(
                'Microsoft YaHei', new_size))
            self.style.configure('TButton', font=(
                'Microsoft YaHei', new_size-1))
        except ValueError:
            messagebox.showerror("错误", "请输入有效的字体大小")

    def update_from_slider(self, param_type):
        """滑动条触发更新"""
        if param_type == 'conf':
            value = round(self.conf_slider.get(), 2)
            self.conf_threshold = value
            self.conf_entry.delete(0, tk.END)
            self.conf_entry.insert(0, f"{value:.2f}")
            self.conf_value.config(text=f"{value:.2f}")
        else:
            value = round(self.iou_slider.get(), 2)
            self.iou_threshold = value
            self.iou_entry.delete(0, tk.END)
            self.iou_entry.insert(0, f"{value:.2f}")
            self.iou_value.config(text=f"{value:.2f}")

    def update_from_entry(self, event):
        """输入框触发更新"""
        widget = event.widget
        try:
            value = float(widget.get())
            if widget == self.conf_entry:
                value = max(0.1, min(1.0, value))
                self.conf_slider.set(value)
                self.conf_threshold = round(value, 2)
                self.conf_value.config(text=f"{value:.2f}")
            else:
                value = max(0.1, min(0.9, value))
                self.iou_slider.set(value)
                self.iou_threshold = round(value, 2)
                self.iou_value.config(text=f"{value:.2f}")
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数值")

    def apply_parameters(self):
        """应用视频区域参数（增强校验）"""
        try:
            new_width = int(self.width_entry.get())
            new_height = int(self.height_entry.get())
            new_x = int(self.x_entry.get())
            new_y = int(self.y_entry.get())

            # 获取屏幕尺寸
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # 参数校验
            if new_width <= 0 or new_height <= 0:
                raise ValueError("窗口尺寸必须为正值")

            # 自动修正坐标溢出
            new_x = max(0, min(new_x, screen_width - 10))  # 保留10px余量
            new_y = max(0, min(new_y, screen_height - 10))

            # 动态调整尺寸防止溢出
            self.width = min(new_width, screen_width - new_x)
            self.height = min(new_height, screen_height - new_y)

            # 设置最小尺寸
            self.width = max(self.width, 100)
            self.height = max(self.height, 100)

            # 更新窗口
            self.x = new_x
            self.y = new_y
            self.overlay.geometry(
                f"{self.width}x{self.height}+{self.x}+{self.y}")

        except ValueError as e:
            tk.messagebox.showerror("参数错误", f"无效的输入参数：{str(e)}")

    def toggle_detection(self):
        self.detecting = not self.detecting
        if self.detecting:
            self.start_btn.config(text="停止检测")
            self.status_label.config(text="状态: 检测中...", foreground="green")
            threading.Thread(target=self.detect_persons, daemon=True).start()
        else:
            self.start_btn.config(text="开始检测")
            self.status_label.config(text="状态: 已停止", foreground="red")
            # 重置统计
            for emotion in self.emotion_counts:
                self.emotion_counts[emotion] = 0
                self.emotion_labels[emotion].config(text="0")

    def detect_persons(self):
        while self.detecting:
            current_time = time.time()
            if current_time - self.last_time > 1/self.fps:
                try:
                    screenshot = ImageGrab.grab(bbox=self.get_screen_area())
                    frame = cv2.cvtColor(
                        np.array(screenshot), cv2.COLOR_RGB2BGR)

                    # 使用调整后的参数进行检测
                    results = self.model.predict(
                        frame,
                        conf=self.conf_threshold,
                        iou=self.iou_threshold,
                        verbose=False
                    )

                    person_count = 0
                    # 重置表情计数
                    for emotion in self.emotion_counts:
                        self.emotion_counts[emotion] = 0

                    for result in results:
                        boxes = result.boxes
                        for box in boxes:
                            if box.cls == 0:  # 0对应person类
                                person_count += 1
                                # 提取人脸区域
                                x1, y1, x2, y2 = map(int, box.xyxy[0])
                                face_roi = frame[y1:y2, x1:x2]
                                if face_roi.size != 0:
                                    emotion = self.analyze_emotion(face_roi)
                                    if emotion and emotion in self.emotion_counts:
                                        self.emotion_counts[emotion] += 1

                    # 更新界面显示
                    self.count_label.config(text=f"检测人数: {person_count}")
                    for emotion, label in self.emotion_labels.items():
                        label.config(text=str(self.emotion_counts[emotion]))

                    self.last_time = current_time
                    # 在检测结果更新后添加
                    self.current_person_count = person_count

                    # 记录数据逻辑
                    if self.recording and (current_time - self.last_log_time >= self.log_interval_seconds):
                        self.log_data()
                        self.last_log_time = current_time
                except Exception as e:
                    print(f"检测错误: {str(e)}")
                    # 增加硬件加速禁用选项
                    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
                    self.toggle_detection()
                    

    def get_screen_area(self):
        try:
            x = max(self.overlay.winfo_x(), 0)
            y = max(self.overlay.winfo_y(), 0)

            # 获取实际渲染尺寸（避免使用存储的width/height）
            rendered_width = self.overlay.winfo_width()
            rendered_height = self.overlay.winfo_height()

            # 计算右边界和底边界并校验
            right = x + max(rendered_width, 100)  # 最小宽度100
            bottom = y + max(rendered_height, 100)  # 最小高度100

            # 限制不超过屏幕边界
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            right = min(right, screen_width)
            bottom = min(bottom, screen_height)

            return (x, y, right, bottom)
        except Exception as e:
            print(f"坐标计算错误: {str(e)}")
            # 返回安全区域（屏幕左上角100x100）
            return (0, 0, 100, 100)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def resize_overlay(self, event):
        dx = event.x - self.x
        dy = event.y - self.y

        # 计算新尺寸并限制最小值为100x100
        new_width = max(self.width + dx, 100)
        new_height = max(self.height + dy, 100)

        # 获取屏幕尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 动态限制最大尺寸（防止窗口溢出屏幕）
        max_width = screen_width - self.overlay.winfo_x()
        max_height = screen_height - self.overlay.winfo_y()
        new_width = min(new_width, max_width)
        new_height = min(new_height, max_height)

        # 更新尺寸
        self.width = new_width
        self.height = new_height

        # 应用新尺寸
        if self.width > 0 and self.height > 0:
            self.overlay.geometry(
                f"{self.width}x{self.height}+{self.overlay.winfo_x()}+{self.overlay.winfo_y()}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedVideoPersonDetector(root)
    root.mainloop()
