class HexParser:
    """十六进制报文解析器"""

    @staticmethod
    def parse_hex_bytes(input_text):
        if not input_text or not input_text.strip():
            return []

        result = []
        input_text = input_text.replace("\n", " ").replace(",", " ") # 去除换行符和逗号
        input_text = input_text.upper() # 把所有小写字母转换为大写字母
        input_text = input_text.replace("0x", "").replace("0X", "")  # 移除 0x 前缀

        for byte in input_text.split():
            if not byte:
                continue
                
            if not all(c in '0123456789ABCDEF' for c in byte):
                raise ValueError("输入包含无效字节: " + byte)

            if len(byte) == 1:
                byte = byte.zfill(2)
                result.append(byte)
            elif len(byte) == 2:
                result.append(byte)
            else:
                if len(byte) % 2 == 0:
                    for i in range(0, len(byte), 2):
                        result.append(byte[i:i+2])
                else:
                    raise ValueError("字符串长度为奇数无法正确解析: " + byte)

        return result
    
    @staticmethod
    def format_byte_display(byte_hex, format_type='hex'):
        if format_type == 'hex':
            return "0x" + byte_hex
        elif format_type == 'dec':
            return str(int(byte_hex, 16))
        elif format_type == 'both':
            return "0x" + byte_hex + " (" + str(int(byte_hex, 16)) + ")"