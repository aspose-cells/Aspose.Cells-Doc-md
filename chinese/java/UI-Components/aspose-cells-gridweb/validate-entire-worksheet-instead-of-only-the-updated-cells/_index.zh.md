---
title: 验证整个工作表而不仅仅是更新的单元格
type: docs
weight: 80
url: /zh/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **可能的使用场景**
默认情况下，GridWeb仅验证已更新的单元格，而不验证整个工作表。但是，如果您想在GridWeb将请求提交到服务器之前在客户端验证整个工作表，那么您应将acwmain.js中的needValidateall变量设置为true。
## **验证整个工作表而不仅仅是更新的单元格**
以下屏幕截图显示了acwmain.js中的needValidateall变量。请将其设置为true，现在GridWeb将验证整个工作表而不仅仅是更新的单元格。

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


