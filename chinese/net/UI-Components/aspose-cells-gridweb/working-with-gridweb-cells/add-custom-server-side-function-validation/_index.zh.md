---
title: 添加自定义服务器端功能验证
type: docs
weight: 110
url: /zh/net/add-custom-server-side-function-validation/
---
## **可能的使用场景**
有时，您可能需要在服务器端实施数据验证。 Aspose.Cells.GridWeb 允许您添加自定义服务器端数据验证。您必须指定单元格范围或区域。您还可以使用自定义服务器端验证为回调设置客户端验证函数。
## **添加自定义服务器端功能验证**
您需要设置实现的服务器验证类**网格自定义服务器验证**接口通过**网格验证.服务器验证**属性。您还需要设置客户端验证功能（它应该在客户端用JavaScript编写），该功能是回调时在客户端验证数据所必需的。您可以通过以下方式设置错误消息字符串**网格验证.ErrorMessage**和标题通过**GridValidation.ErrorTitle**满足您需求的属性。在执行下面的示例代码后，请查看一系列屏幕截图，这些屏幕截图显示了它在给定场景中的工作方式（逐步）。在示例中，您无法更新 B2:C3 单元格中的数据。当您尝试编辑工作表中的这些单元格时，系统会提示您一些错误消息，并且将恢复以前的值。您可以打开控制台窗口（在您的浏览器中）以打印某些事件的单元格信息/详细信息。

![待办事项：图片_替代_文本](add-custom-server-side-function-validation_1.png)

![待办事项：图片_替代_文本](add-custom-server-side-function-validation_2.png)

![待办事项：图片_替代_文本](add-custom-server-side-function-validation_3.png)

![待办事项：图片_替代_文本](add-custom-server-side-function-validation_4.png)

![待办事项：图片_替代_文本](add-custom-server-side-function-validation_5.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
