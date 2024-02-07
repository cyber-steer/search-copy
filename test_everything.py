import ctypes
from ctypes import wintypes
import os
import sys

_dll = ctypes.WinDLL("Everything-SDK/dll/Everything64.dll")

# 파일 경로 설정
file_path = os.path.join(os.getcwd(), "abc")

# 검색 설정
everything_flags = 0x00000001  # 최신 버전 상수 사용
Everything_SetSearchW = _dll.Everything_SetSearchW
# Everything_SetSearchW 함수 호출 (경로 전달, argtypes 설정)
Everything_SetSearchW.argtypes = [wintypes.LPCWSTR]
Everything_SetSearchW(file_path.encode("utf-16").encode("ascii"))

Everything_QueryW = _dll.Everything_QueryW
# Everything_QueryW 함수 호출 (옵션 전달, argtypes, restype 설정)
Everything_QueryW.argtypes = [wintypes.DWORD]
Everything_QueryW.restype = wintypes.BOOL
Everything_QueryW(everything_flags)

# 검색 결과 출력
for i in range(_dll.Everything_GetNumResults()):
    file_name = _dll.Everything_GetResultFileName(i).decode("utf-8")
    file_path = _dll.Everything_GetResultPath(i).decode("utf-8")
    print(f"{file_name} [{file_path}]")