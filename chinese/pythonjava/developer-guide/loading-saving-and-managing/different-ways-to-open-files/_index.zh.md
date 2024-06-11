---
title: 打开文件的不同方式
type: docs
weight: 10
url: /zh/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

使用Aspose.Cells很容易打开文件，例如检索数据，或使用设计模板加快开发过程。

{{% /alert %}}

## **通过路径打开文件**

开发人员可以通过在**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**类构造函数中将文件路径指定为*string*来在本地计算机上打开Microsoft Excel文件。只需在构造函数中传递路径。Aspose.Cells将自动检测文件格式类型。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **通过流打开文件**

也可以通过流简单地打开 Excel 文件。为此，使用接受包含文件的 *BufferStream* 对象的构造函数的重载版本。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **仅打开带有数据的文件**

要仅打开包含数据的文件，请使用**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)**和**[LoadFilter](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)**类来设置加载的模板文件的相关属性和类的选项。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

如果尝试使用Aspose.Cells打开非本机Excel文件或其他文件格式（例如PPT/PPTX，DOC/DOCX等），将引发异常。

{{% /alert %}} {{% alert color="primary" %}}

在加载大型电子表格时，**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**构造函数可能会引发*System.OutOfMemoryException*。此异常表明可用内存不足以完全将电子表格加载到内存中，因此必须在启用内存首选项的情况下加载电子表格。

{{% /alert %}}
