---
title: Save方法没有4个参数的重载
type: docs
weight: 70
url: /zh/net/no-overload-for-method-save-takes-4-arguments/
---

## **症状**

"使用Aspose.Cells版本，当我使用Save方法尝试将工作簿保存到响应对象时，我会遇到这个错误。我在网上文档中找到了这段代码片段。"

### **错误截图**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **解决方案**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NET与所有的.NET框架版本都兼容且运行良好，例如2.x、3.x、4.x等，适用于各种项目类型，如Asp.NET/Winforms、Web项目、Windows/Web服务、控制台应用程序或其他项目等。我们为不同的.NET框架版本提供不同的dll。有关更多信息，请阅读安装目录下"\Bin"文件夹中的**readme.txt**。但是，这个**readme.txt**文件是存在的。

当您在web应用程序中使用我们的产品时，请从"/bin"目录中的**NET 2.0**文件夹中使用Aspose.Cells.dll。您应该注意，**.NET 3.5客户端配置**目录中的dll仅用于VS.NET的目标框架为客户端配置的控制台应用程序。请检查您的项目，可能您的项目正在引用这个dll。

### **参考**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
