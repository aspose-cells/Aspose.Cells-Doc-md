---
title: 将VBA宏用户表单DesignerStorage从模板复制到目标工作簿
type: docs
weight: 60
url: /zh/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能的使用场景**

Aspose.Cells 允许您将一个Excel文件中的VBA项目复制到另一个Excel文件中。 VBA 项目由各种类型的模块组成，例如 文档、程序、设计师等。所有模块都可以通过简单的代码进行复制，但对于设计师模块，需要访问或复制一些额外的称为设计存储的数据。以下两种方法处理设计存储。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **将VBA宏用户表单DesignerStorage从模板复制到目标工作簿**

请参阅以下示例代码。它将VBA项目从 [模板Excel文件](50528367.xlsm) 复制到一个空工作簿，并将其保存为 [输出Excel文件](50528366.xlsm)。如果您在模板Excel文件中打开VBA项目，您会看到如下所示的用户窗体。用户窗体包含设计器存储，因此将使用 [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) 和 [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-) 方法进行复制。

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

以下截图显示了从模板Excel文件复制的输出Excel文件及其内容。当您单击“按钮1”时，它将打开VBA用户表单，该表单本身具有一个命令按钮，点击会显示一个消息框。

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
