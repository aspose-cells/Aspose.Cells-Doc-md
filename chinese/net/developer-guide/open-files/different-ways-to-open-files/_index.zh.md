---
title: 打开文件的不同方式
type: docs
weight: 10
url: /zh/net/different-ways-to-open-files/
description: 本文介绍如何使用 Aspose.Cells for .NET API 打开 Excel 文件。
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

使用 Aspose.Cells 可以轻松打开文件，例如检索数据或使用设计器模板来加快开发过程。

{{% /alert %}}

##  **如何通过路径打开 Excel 文件**

开发者可以通过在本地计算机上指定Microsoft Excel文件的文件路径来打开该文件。**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**类构造函数。只需将构造函数中的路径作为 *string* 传递即可。 Aspose.Cells会自动检测文件格式类型。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **如何通过流打开 Excel 文件**

将 Excel 文件作为流打开也很简单。为此，请使用构造函数的重载版本，该构造函数采用*溪流*包含该文件的对象。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **如何打开仅包含数据的文件**

要打开仅包含数据的文件，请使用**[加载选项](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**和**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**classes 设置要加载的模板文件的类的相关属性和选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **如何仅加载可见图纸**

加载时**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**有时您可能只需要工作簿中可见工作表中的数据。 Aspose.Cells 允许您在加载工作簿时跳过不可见工作表中的数据。为此，请创建一个继承的自定义函数**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**类并将其实例传递给**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

这是该方法的实现*定制加载*上面代码片段中引用的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

如果您尝试通过 Aspose.Cells 打开非本机 Excel 文件或其他文件格式（例如 PPT/PPTX、DOC/DOCX 等），则会抛出异常。

{{% /alert %}} {{% alert color="primary" %}}

很有可能**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**构造函数可能会抛出*System.OutOfMemoryException*加载大型电子表格时。此异常表明可用内存不足以将电子表格完全加载到内存中，因此必须在启用内存首选项时加载电子表格。

{{% /alert %}}
