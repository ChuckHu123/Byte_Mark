from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QTextEdit, QLabel, QPushButton, QComboBox)
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

        central_widget = QWidget()           # 1. 创建中央部件
        self.setCentralWidget(central_widget) # 2. 设置为窗口中央部件
        layout = QVBoxLayout(central_widget)  # 3. 创建布局并绑定到部件

        title_label = QLabel("Byte Mark ξ( ✿＞◡❛)!")
        layout.addWidget(title_label)

        self.hex_input = QTextEdit()
        layout.addWidget(self.hex_input)

        self.index_offset = QTextEdit()
        layout.addWidget(QLabel("索引偏移量："))
        layout.addWidget(self.index_offset)
        
        layout.addWidget(QLabel("显示格式："))

        self.format_combo = QComboBox()
        self.format_combo.addItems(["十六进制(0x00)", "十进制(0)", "两者都显示(both)"])
        layout.addWidget(self.format_combo)

        parse_btn = QPushButton("解析")
        parse_btn.clicked.connect(self.parse_hex)
        layout.addWidget(parse_btn)
        
        self.output_label = QLabel("结果将显示在这里")
        layout.addWidget(self.output_label)
    
    def parse_hex(self):

        hex_text = self.hex_input.toPlainText()

        index_offset = 0
        if self.index_offset.toPlainText():
            if self.index_offset.toPlainText().isdigit():
                index_offset = int(self.index_offset.toPlainText())
            else:
                self.output_label.setText("❌ 索引偏移量必须是数字")
                return

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
                formatted_bytes = []
                for index, byte in enumerate(self.current_bytes):
                    formatted_byte = HexParser.format_byte_display(byte, format_type)
                    formatted_bytes.append(f"[{index + index_offset}] {formatted_byte}")
                
                result_text = ", ".join(formatted_bytes)
                self.output_label.setText(f"✅ 解析成功！共 {len(self.current_bytes)} 个字节：\n{result_text}")

            else:
                self.output_label.setText("⚠️ 未检测到有效字节")

        except ValueError as e:
            self.output_label.setText(f"❌ 错误：{e}")