---
title: 打开文件的不同方式
type: docs
weight: 10
url: /zh/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

使用Aspose.Cells很容易打开文件，例如检索数据，或使用设计模板加快开发过程。

{{% /alert %}}

## **通过路径打开文件**

开发人员可以通过在 **Workbook** 类构造函数中指定本地计算机上文件路径来打开 Microsoft Excel 文件。只需将路径作为 *string* 传递给构造函数。Aspose.Cells 将自动检测文件格式类型。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **通过流打开文件**

也可以通过流简单地打开 Excel 文件。为此，使用接受包含文件的 *BufferStream* 对象的构造函数的重载版本。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **仅打开带有数据的文件**

要仅使用**LoadOptions**和**LoadFilter**类打开带有数据的文件，以设置这些类的相关属性和选项为需要加载的模板文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

如果尝试使用Aspose.Cells打开非本机Excel文件或其他文件格式（例如PPT/PPTX，DOC/DOCX等），将引发异常。

{{% /alert %}} {{% alert color="primary" %}}

**Workbook**的构造函数在加载大型电子表格时可能会引发*System.OutOfMemoryException*异常。该异常表明可用内存不足以完全将电子表格加载到内存中，因此必须在启用内存首选项的情况下加载电子表格。

{{% /alert %}}
