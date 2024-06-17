---
title: Save 方法没有接受 4 个参数的重载
type: docs
weight: 70
url: /zh/net/no-overload-for-method-save-takes-4-arguments/
---

## **症状**

"使用 Aspose.Cells 版本，当我尝试将工作簿保存到 Response 对象时，使用 Save 方法时会出现此错误。我在在线文档中找到了此代码片段的记录。

### **错误的屏幕截图**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **解决方案**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NET与所有.NET框架版本（如2.x、3.x、4.x等）兼容并可以很好地运行，适用于任何类型的项目，如Asp.NET/Winforms、Web项目、Windows/Web服务、控制台应用程序或其他项目等。我们为不同的.NET框架版本提供不同的dll。有关更多信息，请阅读安装目录中“\Bin”文件夹中的**readme.txt**文件。但是，这个**readme.txt**文件是存在的。

当你在 web 应用程序中使用我们的产品时，请从 "/bin" 目录下的 **NET 2.0** 文件夹中使用 Aspose.Cells.dll。据我们了解，**.NET 3.5 Client Profile** 目录中的 dll 仅适用于以 VS.NET 的客户端配置为目标框架的控制台应用程序。请检查你的项目，很有可能你的项目正在引用这个 dll。

### **参考资料**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
