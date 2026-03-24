import subprocess

#   'rm -rf /home/wensyu/DetectorFreeSfM/SfM_dataset/example_dataset/example_scene/* && '#删除之前的结果

def main():
    # 程序的主要逻辑
    print("Hello, world!")
    # 你可以在这里添加更多的代码来实现功能
    #subprocess.run(
    #["wsl", "-d", "Ubuntu-22.04","conda activate detectorfreesfm"], capture_output=True, text=True)
    cmd = (
            'source /root/anaconda3/etc/profile.d/conda.sh && '
            'conda activate detectorfreesfm && '
            'cd /home/wensyu/DetectorFreeSfM && '
            'python eval_dataset.py +demo=dfsfm.yaml'
        #'python eval_dataset.py'
    )

    result=subprocess.run(
        ["wsl", "-d", "Ubuntu-22.04", "bash", "-c", cmd],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    # 打印执行结果
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

# 这个判断是为了确保当文件被直接执行时才运行 main() 函数
if __name__ == "__main__":
    main()


    #eval_dataset.py +demo=dfsfm.yaml
    '''    result = subprocess.run(
        ["wsl", "-d", "Ubuntu-22.04", "python3", "/home/wensyu/DetectorFreeSfM/eval_dataset.py","+demo=dfsfm.yaml"],
        capture_output=True,
        text=True
    )'''