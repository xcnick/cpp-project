Cpp-Project Template
===
Cpp工程模板
## 预安装
* Clang/Gcc：编译器
*	CMake：Makefile生成工具

## 编译
* 系统：
  支持Linux/Mac系统
* 编译命令：
  ```bash
  ./build.py
  ```
* 生成目录：
  - 可执行文件路径 `./build/Cpp-Project/release/bin/`
  - 库路径 `./build/Cpp-Project/release/lib/`

* 编译&打包：
  ```bash
  ./build.py --package
  ```
  打包路径：`./build/Cpp-Project/package/`

## 开发
* 修改`build.py`和`CMakeLists.txt`中的项目名称
* 根据不同的代码功能创建代码文件夹
* 根据实际代码修改CMakeLists.txt文件