---
title: 从模板复制VBA宏用户窗体设计存储到目标工作簿
type: docs
weight: 60
url: /zh/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能的使用场景**

Aspose.Cells允许您从一个Excel文件复制VBA项目到另一个Excel文件。VBA项目包括各种类型的模块，如文档、过程、设计师等。所有模块都可以通过简单的代码复制，但对于设计师模块，需要访问或复制名为“设计师存储”的一些额外数据。以下两种方法处理“设计师存储”。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **将VBA宏用户窗体设计器存储从模板复制到目标工作簿**

请参考以下示例代码。它从[模板Excel文件](50528367.xlsm)中复制VBA项目到一个空工作簿，并将其另存为[输出Excel文件](50528366.xlsm)。如果您在模板Excel文件中查看VBA项目，您将看到一个用户窗体，如下所示。用户窗体包括设计师存储，因此它将使用[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))和[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))方法进行复制。

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

以下截图显示了从模板Excel文件复制的输出Excel文件及其内容。当您单击按钮1时，它会打开VBA用户窗体，该用户窗体本身具有一个在单击时显示消息框的命令按钮。

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
