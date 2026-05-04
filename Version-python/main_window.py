from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QTextEdit, QLabel, QPushButton, QComboBox, 
                             QGroupBox, QStatusBar, QApplication, QSpinBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from hex_parser import HexParser


class MainWindow(QMainWindow):
    """Byte Mark 主窗口 - 美化版"""
    
    def __init__(self):
        super().__init__()
        self.current_bytes = []  # 存储当前解析的字节
        self.init_ui()
        self.setWindowTitle("Byte Mark - 十六进制报文解析器")
        self.setGeometry(100, 100, 900, 700)
        self.apply_styles()
    
    def apply_styles(self):
        """应用QSS样式表美化界面"""
        style_sheet = """
        QMainWindow {
            background-color: #f5f5f5;
        }
        
        QWidget {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            font-size: 14px;
        }
        
        QLabel {
            color: #333333;
            font-weight: bold;
            font-size: 14px;
        }
        
        QLabel#title_label {
            font-size: 20px;
            color: #2c3e50;
            padding: 10px;
            background-color: #ecf0f1;
            border-radius: 5px;
        }
        
        QTextEdit {
            background-color: white;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            padding: 8px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 14px;
        }
        
        QTextEdit:focus {
            border: 2px solid #3498db;
        }
        
        QPushButton {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            min-width: 80px;
            font-size: 14px;
        }
        
        QPushButton:hover {
            background-color: #2980b9;
        }
        
        QPushButton:pressed {
            background-color: #21618c;
        }
        
        QComboBox {
            background-color: white;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            padding: 5px;
            min-width: 150px;
            font-size: 14px;
        }
        
        QComboBox:hover {
            border: 2px solid #3498db;
        }
        
        QGroupBox {
            font-weight: bold;
            border: 2px solid #bdc3c7;
            border-radius: 8px;
            margin-top: 10px;
            padding-top: 10px;
            background-color: #fafafa;
            font-size: 14px;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
            color: #2c3e50;
            font-size: 14px;
        }
        
        QStatusBar {
            background-color: #ecf0f1;
            color: #7f8c8d;
            font-size: 12px;
        }
        
        QSpinBox {
            background-color: white;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            padding: 5px;
            font-size: 14px;
        }
        
        QSpinBox:focus {
            border: 2px solid #3498db;
        }
        """
        self.setStyleSheet(style_sheet)
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # 标题区域
        title_label = QLabel("🔧 Byte Mark - 十六进制报文解析器")
        title_label.setObjectName("title_label")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # 输入区域
        input_group = QGroupBox("📥 输入区域")
        input_layout = QVBoxLayout(input_group)
        
        self.hex_input = QTextEdit()
        self.hex_input.setPlaceholderText("请输入十六进制数据，例如：0x1A 0x2B 0x3C 或 1A2B3C")
        self.hex_input.setMinimumHeight(120)
        input_layout.addWidget(self.hex_input)
        
        main_layout.addWidget(input_group)

        # 设置区域
        settings_group = QGroupBox("⚙️ 解析设置")
        settings_layout = QHBoxLayout(settings_group)
        
        # 索引偏移量 - 使用QSpinBox替代QTextEdit
        offset_layout = QVBoxLayout()
        offset_label = QLabel("索引偏移量：")
        self.index_offset = QSpinBox()
        self.index_offset.setRange(-10000, 10000)
        self.index_offset.setValue(0)
        self.index_offset.setMaximumHeight(30)
        offset_layout.addWidget(offset_label)
        offset_layout.addWidget(self.index_offset)
        
        # 显示格式
        format_layout = QVBoxLayout()
        format_label = QLabel("显示格式：")
        self.format_combo = QComboBox()
        self.format_combo.addItems(["十六进制(0x00)", "十进制(0)", "两者都显示(both)"])
        format_layout.addWidget(format_label)
        format_layout.addWidget(self.format_combo)
        
        settings_layout.addLayout(offset_layout)
        settings_layout.addLayout(format_layout)
        settings_layout.addStretch()
        
        main_layout.addWidget(settings_group)

        # 操作按钮
        button_layout = QHBoxLayout()
        parse_btn = QPushButton("🔍 解析报文")
        parse_btn.clicked.connect(self.parse_hex)
        parse_btn.setMinimumHeight(40)
        
        clear_btn = QPushButton("🗑️ 清空")
        clear_btn.clicked.connect(self.clear_all)
        clear_btn.setMinimumHeight(40)
        
        button_layout.addWidget(parse_btn)
        button_layout.addWidget(clear_btn)
        main_layout.addLayout(button_layout)
        
        # 输出区域
        output_group = QGroupBox("📤 解析结果")
        output_layout = QVBoxLayout(output_group)
        
        self.output_label = QLabel("💡 解析结果将显示在这里")
        self.output_label.setWordWrap(True)
        self.output_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.output_label.setMinimumHeight(100)
        output_layout.addWidget(self.output_label)
        
        main_layout.addWidget(output_group)
        
        # 状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
    
    def clear_all(self):
        """清空所有输入和输出"""
        self.hex_input.clear()
        self.index_offset.setValue(0)
        self.output_label.setText("💡 解析结果将显示在这里")
        self.current_bytes = []
        self.statusBar.showMessage("已清空")
    
    def parse_hex(self):
        hex_text = self.hex_input.toPlainText()

        if not hex_text.strip():
            self.output_label.setText("⚠️ 请输入十六进制数据")
            self.statusBar.showMessage("错误：未输入数据")
            return

        index_offset = self.index_offset.value()

        try:
            self.current_bytes = HexParser.parse_hex_bytes(hex_text)
            if self.current_bytes:
                # 根据下拉框的文本直接映射到格式类型
                format_mapping = {
                    "十六进制(0x00)": "hex",
                    "十进制(0)": "dec",
                    "两者都显示(both)": "both"
                }
                current_text = self.format_combo.currentText()
                format_type = format_mapping.get(current_text, "hex")
                
                # 对每个字节进行格式化，并添加索引
                formatted_items = []
                for index, byte in enumerate(self.current_bytes):
                    formatted_byte = HexParser.format_byte_display(byte, format_type)
                    # 使用 ljust(15) 确保每个 [索引] 值 占据相同的宽度，实现完美对齐
                    item = f"[{index + index_offset}] {formatted_byte}"
                    formatted_items.append(item)
                
                # 每10个换行
                result_lines = []
                for i in range(0, len(formatted_items), 10):
                    line_items = formatted_items[i:i+10]
                    # 使用制表符或固定空格连接，这里为了视觉整齐直接用空格连接已对齐的字符串
                    result_lines.append("    ".join(line_items))
                
                result_text = "\n".join(result_lines)
                self.output_label.setText(f"✅ 解析成功！共 {len(self.current_bytes)} 个字节：\n\n{result_text}")
                self.statusBar.showMessage(f"解析完成 - {len(self.current_bytes)} 个字节")

            else:
                self.output_label.setText("⚠️ 未检测到有效字节")
                self.statusBar.showMessage("警告：未检测到有效字节")

        except ValueError as e:
            self.output_label.setText(f"❌ 错误：{e}")
            self.statusBar.showMessage("解析错误")