import argparse
from blender_mcp.server import main as server_main


def main():
    """blender-mcp 包的入口函数"""
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='Blender MCP 服务端程序')

    # 添加命令行参数
    parser.add_argument('--host', type=str, default='localhost',
                        help='服务端监听地址 (默认: localhost)')
    parser.add_argument('--port', type=int, default=8080,
                        help='服务端监听端口 (默认: 8080)')


    # 解析命令行参数
    args = parser.parse_args()

    # 调用服务端主函数并传入参数
    # 假设 server_main 可以接收这些参数
    server_main()
"""

"""

if __name__ == "__main__":
    main()