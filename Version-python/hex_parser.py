class HexParser:
    """十六进制报文解析器"""

    @staticmethod
    def parse_hex_bytes(input_text):
        """
        解析十六进制字符串为字节列表
        
        任务：
        1. 接收一个字符串（如 "00 01 ff 19 23" 或 "00,01,ff" 或 "0001ff"）
        2. 清理输入（去除空格、逗号等）
        3. 验证每个字节是否有效（0-9, A-F）
        4. 返回字节列表，如 ['00', '01', 'FF', '19', '23']
        
        提示：
        - 先用 replace() 处理逗号和换行
        - 用 split() 分割字符串
        - 用 upper() 转大写
        - 用 zfill(2) 补齐两位
        
        Args:
            input_text: 用户输入的十六进制字符串
            
        Returns:
            list: 解析后的字节列表
            
        Raises:
            ValueError: 如果输入格式不正确
        """
        # TODO: 在这里实现你的解析逻辑
        input_text = input_text.replace(" ", "").replace(",", "") # 去除空格和逗号
        input_text = input_text.upper() # 把所有小写字母转换为大写字母
        
        for byte in input_text.split():
            if len(byte) != 2 or not all(c in '0123456789ABCDEF' for c in byte):
                raise ValueError("输入包含无效字节: " + byte)

        pass
    
    @staticmethod
    def format_byte_display(byte_hex, format_type='hex'):
        """
        格式化字节显示
        
        任务：
        1. 根据 format_type 返回不同格式
           - 'hex': 返回 "0xFF"
           - 'dec': 返回 "255"
           - 'both': 返回 "0xFF (255)"
        
        提示：
        - 用 int(byte_hex, 16) 将十六进制转为十进制
        
        Args:
            byte_hex: 十六进制字节，如 'FF'
            format_type: 显示格式 ('hex', 'dec', 'both')
            
        Returns:
            str: 格式化后的文本
        """
        # TODO: 在这里实现格式化逻辑
        pass