---
title: 打开文件的不同方式
type: docs
weight: 10
url: /zh/net/different-ways-to-open-files/
description: 本文章解释了如何使用Aspose.Cells for .NET API 打开 Excel 文件。
keywords: C#打开Excel文件而不使用Excel，我该如何打开Excel文件。
---

{{% alert color="primary" %}}

使用Aspose.Cells很容易打开文件，例如检索数据，或使用设计模板加快开发过程。

{{% /alert %}}

## **如何通过路径打开Excel文件**

开发人员可以通过在构造函数中指定本地计算机上的文件路径来打开Microsoft Excel文件。只需将路径作为*string*传递给构造函数。Aspose.Cells将自动检测文件格式类型。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **如何通过流打开Excel文件**

通过流打开Excel文件也很简单。为此，请使用接收包含文件的*流*对象的构造函数的重载版本。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **如何只打开具有数据的文件**

要仅打开具有数据的文件，使用[**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)和[**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)类设置文件模板的相关属性和选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **如何仅加载可见工作表**

在加载 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 时，有时您可能只需要工作簿中可见工作表中的数据。Aspose.Cells允许您在加载工作簿时跳过不可见工作表中的数据。要做到这一点，请创建一个继承 [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) 类的自定义函数，并将其实例传递给 [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) 属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

以下是上述片段中引用的*CustomnLoad*类的实现。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

如果尝试使用Aspose.Cells打开非本机Excel文件或其他文件格式（例如PPT/PPTX，DOC/DOCX等），将引发异常。

{{% /alert %}} {{% alert color="primary" %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)构造函数在加载大型电子表格时可能会引发*System.OutOfMemoryException*。此异常表明可用内存不足以完全将电子表格加载到内存中，因此必须在启用内存偏好的情况下加载电子表格。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
