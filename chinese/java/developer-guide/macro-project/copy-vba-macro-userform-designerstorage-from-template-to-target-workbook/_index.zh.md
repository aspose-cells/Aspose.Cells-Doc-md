---
title: 将 VBA 宏 UserForm DesignerStorage 从模板复制到目标工作簿
type: docs
weight: 60
url: /zh/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **可能的使用场景**

Aspose.Cells 允许您将 VBA 项目从一个 Excel 文件复制到另一个 Excel 文件。 VBA 项目由各种类型的模块组成，即文档、过程、设计器等。所有模块都可以用简单的代码复制，但对于设计器模块，有一些额外的数据需要访问或复制，称为设计器存储。以下两种方法处理 Designer Storage。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **将 VBA 宏 UserForm DesignerStorage 从模板复制到目标工作簿**

请参阅以下示例代码。它将 VBA 项目从[模板 Excel 文件](50528367.xlsm)到一个空的工作簿中并将其另存为[输出Excel文件](50528366.xlsm).如果您打开模板 Excel 文件中的 VBA 项目，您将看到如下所示的用户窗体。用户表单由 Designer Storage 组成，因此将使用[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)） 和[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])） 方法。

![待办事项：图像_替代_文本](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

以下屏幕截图显示了输出 Excel 文件及其从模板 Excel 文件复制的内容。当您单击按钮 1 时，它会打开 VBA 用户窗体，它本身有一个命令按钮，单击时会显示一个消息框。

![待办事项：图像_替代_文本](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
