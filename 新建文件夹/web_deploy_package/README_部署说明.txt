网页部署包说明

文件说明
1. app.py               主程序
2. requirements.txt     依赖文件
3. README_部署说明.txt  部署说明

最简单部署方式：Streamlit Community Cloud

步骤：
1）注册 / 登录 Streamlit Community Cloud
2）连接 GitHub
3）新建一个 GitHub 仓库
4）把 app.py 和 requirements.txt 上传到仓库根目录
5）在 Streamlit Community Cloud 中点击 Create app
6）选择该 GitHub 仓库
7）Branch 选择 main
8）Main file path 填 app.py
9）点击 Deploy

部署成功后，会得到一个公开网址，可直接在 Mac、iPad、iPhone 浏览器打开。

补充：
- 这个项目当前只依赖 streamlit 和 Python 标准库
- 如果后续你再加入 pandas、matplotlib、openpyxl 等，需要同步写进 requirements.txt
