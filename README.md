# 网站自动签到

这个项目通过GitHub Actions实现每日自动签到功能。

## 使用方法

1. Fork 这个仓库到你的GitHub账号

2. 在你的仓库中设置以下Secrets:
   - COOKIE: 你的网站cookie（必需）
   - FORMHASH: 你的formhash值（必需）
   - WEBSITE: 网站域名（必需）

   设置路径: 仓库 -> Settings -> Secrets and variables -> Actions -> New repository secret

3. GitHub Actions会根据设定的时间（默认每天北京时间2:10）自动运行签到脚本

4. 你也可以手动触发工作流:
   - 进入Actions标签
   - 选择"网站自动签到"工作流
   - 点击"Run workflow"按钮

## 本地测试

如果你想在本地测试这个脚本：

1. 克隆仓库:
   ```
   git clone [仓库URL]
   cd [仓库名]
   ```

2. 安装依赖:
   ```
   pip install -r requirements.txt
   ```

3. 设置环境变量:
   ```
   # Linux/Mac
   export COOKIE="你的cookie"
   export FORMHASH="你的formhash"
   export WEBSITE="网站域名"
   
   # Windows (CMD)
   set COOKIE=你的cookie
   set FORMHASH=你的formhash
   set WEBSITE=网站域名
   ```

4. 运行脚本:
   ```
   python checkin.py
   ```

## 注意事项

- cookie包含敏感信息，请不要直接在代码中硬编码或分享
- 定期检查签到是否正常运行
- 如果网站更新了验证机制，可能需要更新脚本 
