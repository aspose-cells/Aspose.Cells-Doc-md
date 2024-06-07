---
title: 管理文档属性
type: docs
weight: 30
url: /zh/cpp/managing-document-properties/
---

## **可能的使用场景**
Aspose.Cells允许您处理内置和自定义文档属性。这是用于打开这些*文档属性*的Microsoft Excel界面。只需单击*高级属性*，如此处所示的示例截图，并查看它们。

![todo:image_alt_text](managing-document-properties_1.png)
## **管理文档属性**
以下示例代码加载[sample excel file](23166989.xlsx)并读取内置文档属性，例如*Title, Subject*，然后更改它们。然后它还读取自定义文档属性，即*MyCustom1*，然后添加一个新的自定义文档属性，即*MyCustom5*，并写入[output excel file](23166986.xlsx)。以下屏幕截图显示了示例代码对样本excel文件的影响。

![todo:image_alt_text](managing-document-properties_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **控制台输出**
这是以上示例代码执行时提供的[样本excel文件](23166989.xlsx)的控制台输出。

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
