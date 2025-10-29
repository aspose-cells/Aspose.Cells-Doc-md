---
title: 管理文档属性
type: docs
weight: 30
url: /zh/cpp/managing-document-properties/
---

## **可能的使用场景**
Aspose.Cells 允许您使用内置和自定义文档属性。 这是打开这些 *文档属性* 的 Microsoft Excel 界面。 只需单击 *高级属性*，如此屏幕截图中所示，并查看它们。

![todo:image_alt_text](managing-document-properties_1.png)
## **管理文档属性**
以下示例代码加载 [示例 Excel 文件](23166989.xlsx) 并读取内置文档属性，例如 *标题、主题*，然后更改它们。 然后它还读取自定义文档属性，即 *自定义1*，然后添加新的自定义文档属性，即 *自定义5*，并写入 [输出 Excel 文件](23166986.xlsx)。 以下屏幕截图显示了示例代码对示例 Excel 文件的影响。

![todo:image_alt_text](managing-document-properties_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **控制台输出**
这是上述示例代码在使用提供的 [示例 Excel 文件](23166989.xlsx) 时执行的控制台输出。

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
