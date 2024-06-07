---
title: 添加自定义服务器端函数验证
type: docs
weight: 110
url: /zh/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb，服务器端验证
description: 本文介绍如何在GridWeb中使用服务器端验证。
---

## **可能的使用场景**
有时，您可能需要在服务器端实现数据验证。Aspose.Cells.GridWeb允许您添加自定义服务器端数据验证。您必须指定单元格范围或区域。您还可以设置用于回调的客户端验证函数与自定义服务器端验证。
## **添加自定义服务器端函数验证**
您需要设置实现**GridCustomServerValidation**接口的服务器端验证类，通过**GridValidation.ServerValidation**属性。您还需要设置客户端验证函数（应在客户端的JavaScript中编写），该函数是在回调时在客户端端验证数据时必需的。您可以通过**GridValidation.ErrorMessage**设置错误消息字符串，并通过**GridValidation.ErrorTitle**属性为您的需求设置标题。请参考一系列截图，展示了在执行下面的示例代码后在给定场景中如何工作（逐步进行）。在例子中，您不能更新B2:C3单元格中的数据。当您尝试编辑表中的这些单元格时，将提示一些错误消息，并且以前的值将被恢复。您可以打开控制台窗口（在您的浏览器中）以打印特定事件的单元格信息/详细信息。 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
