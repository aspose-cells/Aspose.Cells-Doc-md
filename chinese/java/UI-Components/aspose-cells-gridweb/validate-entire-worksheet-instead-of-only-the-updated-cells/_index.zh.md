---
title: 验证整个工作表而不是仅验证更新的单元格
type: docs
weight: 80
url: /zh/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
##  **可能的使用场景**
默认情况下，GridWeb 仅验证更新的单元格，而不验证整个工作表。但是，如果您想在 GridWeb 将请求发送到服务器之前在客户端验证整个工作表，那么您应该将 acwmain.js 中的 needValidateall 变量设置为 true。
##  **验证整个工作表而不是仅验证更新的单元格**
以下屏幕截图显示了 acwmain.js 中的 needValidateall 变量。请将其设置为 true，现在 GridWeb 将验证您的整个工作表，而不仅仅是更新的单元格。

![待办事项：图像_替代_文本](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


