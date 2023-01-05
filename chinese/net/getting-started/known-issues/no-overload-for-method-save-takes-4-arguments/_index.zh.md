---
title: 方法 Save 没有重载需要 4 个参数
type: docs
weight: 70
url: /zh/net/no-overload-for-method-save-takes-4-arguments/
---
## **症状**

“使用 Aspose.Cells 版本，当我尝试将工作簿保存到 Response 对象时使用 Save 方法时出现此错误。我在联机文档中找到了此代码片段。”

### **错误截图**

![待办事项：图片_替代_文本](no-overload-for-method-save-takes-4-arguments_1.png)

### **解决方案**

请用**.NET 2.0**产品的编译版本，因为它在 VS.NET 2008/2010 上运行良好。实际上我们为不同的环境、项目类型和系统等提供了单独的dll。供参考，请查看：<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

 Aspose.Cells for .NET 兼容所有 .NET 框架版本，即 2.x、3.x、4.x 等，适用于任何类型的项目，例如 Asp.NET/Winforms、Web 项目、Windows/Web 服务、控制台应用程序或其他项目等我们为不同的.NET框架版本提供不同的dll。有关详细信息，请阅读**自述文件.txt**安装目录下的“\Bin”文件夹中。但是这个**自述文件.txt**文件存在。

当您在 Web 应用程序中使用我们的产品时，请使用 Aspose.Cells.dll 来自**NET 2.0**“/bin”目录中的文件夹。供您参考，dll 在**.NET 3.5 客户资料**directory 仅用于以 Net frame client profile 作为 VS.NET 目标框架的控制台应用程序。请检查您的项目，您的项目可能正在引用此 dll。

### **参考**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
