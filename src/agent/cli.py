import argparse



def main():
    parser = argparse.ArgumentParser(description='AI Agent 命令行工具')
    args = parser.parse_args()
    print(hello())


if __name__ == '__main__':
    main()