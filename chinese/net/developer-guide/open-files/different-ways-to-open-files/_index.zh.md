---
title: 打开文件的不同方式
type: docs
weight: 10
url: /zh/net/different-ways-to-open-files/
description: 本文解释了如何使用Aspose.Cells for .NET API打开Excel文件。
keywords: C#无需Excel打开Excel文件，如何打开Excel文件。
---

{{% alert color="primary" %}}

使用Aspose.Cells很容易打开文件，例如检索数据，或使用设计模板加速开发过程。

{{% /alert %}}

## **通过路径打开Excel文件**

开发人员可以通过本地计算机上的文件路径打开Microsoft Excel文件，将其指定在**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**类构造函数中。只需将路径作为*字符串*传递到构造函数中。Aspose.Cells会自动检测文件格式类型。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **通过流打开Excel文件**

也可以将Excel文件作为流打开。要这样做，使用重载版本的构造函数，该构造函数接受包含该文件的*Stream*对象。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **仅带有数据的文件如何打开**

要打开仅带有数据的文件，请使用**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**和**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**类设置相关属性和选项，以加载要加载的模板文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **仅加载可见工作表**

在加载**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**时，有时您可能只需获取工作簿中可见工作表的数据。Aspose.Cells允许您在加载工作簿时跳过不可见工作表中的数据。为此，请创建一个继承**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**类的自定义函数，并将其实例传递给**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

以下是上述代码片段中引用的*CustomnLoad*类的实现。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

如果尝试使用Aspose.Cells打开非本机Excel文件或其他文件格式（例如PPT/PPTX、DOC/DOCX等），将会引发异常。

{{% /alert %}} {{% alert color="primary" %}}

当加载大型电子表格时，**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**构造函数可能会引发*System.OutOfMemoryException*。此异常表明可用内存不足以完全将电子表格加载到内存中，因此必须在启用内存优先级的情况下加载电子表格。

{{% /alert %}}
