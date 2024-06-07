---
title: 打开文件的不同方式
type: docs
weight: 10
url: /zh/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

使用Aspose.Cells很容易打开文件，例如检索数据，或使用设计模板加速开发过程。

{{% /alert %}}

## **通过路径打开文件**

开发人员可以通过在**Workbook**类构造函数中指定在本地计算机上的文件路径来打开Microsoft Excel文件。只需将路径作为*字符串*传递给构造函数。Aspose.Cells将自动检测文件格式类型。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **通过流打开文件**

也可以简单地使用流打开Excel文件。为此，请使用构造函数的重载版本，该版本接受包含文件的*BufferStream*对象。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **仅打开数据文件**

要仅打开带有数据的文件，请使用**LoadOptions**和**LoadFilter**类来设置相关属性和选项，以便加载要加载的模板文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

如果尝试使用Aspose.Cells打开非本机Excel文件或其他文件格式（例如PPT/PPTX、DOC/DOCX等），将会引发异常。

{{% /alert %}} {{% alert color="primary" %}}

**Workbook**构造函数可能在加载大型电子表格时抛出*System.OutOfMemoryException*。此异常表明可用内存不足以将电子表格完全加载到内存中，因此必须在启用内存首选项的情况下加载电子表格。

{{% /alert %}}
