---
title: 添加自定义服务器端函数验证
type: docs
weight: 110
url: /zh/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb，服务器端验证
description: 本文介绍了如何在GridWeb中使用服务器端验证。
---

## **可能的使用场景**
有时候，您可能需要在服务器端实现数据验证。Aspose.Cells.GridWeb允许您添加自定义服务器端数据验证。您必须指定单元格范围或区域。您还可以为回调设置客户端验证函数与自定义服务器端验证。
## **添加自定义服务器端函数验证**
您需要通过GridValidation.ServerValidation属性设置实现了GridCustomServerValidation接口的服务器验证类。您还需要设置客户端验证函数（应该在客户端以JavaScript编写），这个函数是必须的，用于在回调时在客户端端验证数据。您可以通过GridValidation.ErrorMessage和GridValidation.ErrorTitle属性设置错误消息字符串和标题以满足您的需求。请查看一系列屏幕截图，展示了在执行下面的示例代码后（逐步）在给定场景中的工作方式。在示例中，您无法更新B2:C3单元格中的数据。当您尝试编辑工作表中的这些单元格时，将会提示一些错误消息，并且之前的值将被恢复。您可以打开控制台窗口（在您的浏览器中）来打印特定事件的单元格信息/细节。 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
