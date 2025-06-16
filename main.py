import os
import subprocess
import sys

def main():
    student_id = input("학번을 입력하세요: ").strip()
    filename = f"{student_id}.py"

    if not os.path.isfile(filename):
        print(f"오류: {filename} 파일이 존재하지 않습니다.")
        return

    print(f"{filename} 파일을 실행합니다...\n")

    # 현재 파이썬으로 실행
    subprocess.run([sys.executable, filename])

if __name__ == "__main__":
    main()
