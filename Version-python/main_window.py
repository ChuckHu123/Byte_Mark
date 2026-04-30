from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QTextEdit, QLabel, QPushButton)
from hex_parser import HexParser


class MainWindow(QMainWindow):
    """Byte Mark 主窗口"""
    
    def __init__(self):
        super().__init__()
        self.current_bytes = []  # 存储当前解析的字节
        self.init_ui()
        self.setWindowTitle("Byte Mark")
        self.setGeometry(100, 100, 800, 600)
    
    def init_ui(self):
        """
        初始化用户界面
        
        任务：
        1. 创建一个中央部件（QWidget）
        2. 创建垂直布局（QVBoxLayout）
        3. 添加以下组件：
           - 标题标签（QLabel）
           - 输入框（QTextEdit）
           - 解析按钮（QPushButton）
           - 输出标签（QLabel，用于显示结果）
        4. 连接信号和槽（按钮点击事件）
        
        提示：
        - 用 setLayout() 设置布局
        - 用 connect() 连接信号
        """
        # TODO: 在这里创建你的界面

        central_widget = QWidget()           # 1. 创建中央部件
        self.setCentralWidget(central_widget) # 2. 设置为窗口中央部件
        layout = QVBoxLayout(central_widget)  # 3. 创建布局并绑定到部件

        title_label = QLabel("Byte Mark ξ( ✿＞◡❛)!")
        layout.addWidget(title_label)

        self.hex_input = QTextEdit()
        layout.addWidget(self.hex_input)
        
        parse_btn = QPushButton("解析")
        parse_btn.clicked.connect(self.parse_hex)
        layout.addWidget(parse_btn)
        
        self.output_label = QLabel("结果将显示在这里")
        layout.addWidget(self.output_label)

        pass
    
    def parse_hex(self):
        """
        解析按钮点击时的处理函数
        
        任务：
        1. 从输入框获取文本
        2. 调用 HexParser.parse_hex_bytes() 解析
        3. 将结果显示在输出标签上
        4. 如果有错误，显示错误信息
        
        提示：
        - 用 self.hex_input.toPlainText() 获取输入
        - 用 try-except 捕获异常
        - 用 self.output_label.setText() 显示结果
        """
        # TODO: 在这里实现解析逻辑
        pass