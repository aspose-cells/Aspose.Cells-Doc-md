---
title: 将VBA宏用户表单DesignerStorage从模板复制到目标工作簿
type: docs
weight: 130
url: /zh/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能的使用场景**

Aspose.Cells允许您将一个Excel文件中的VBA项目复制到另一个Excel文件中。VBA项目包括各种类型的模块，即文档、过程、设计师等。所有模块可以使用简单的代码复制，但对于设计师模块，需要访问或复制一些额外的数据称为设计师存储。以下两种方法处理设计师存储。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **将VBA宏用户表单DesignerStorage从模板复制到目标工作簿**

请参见以下示例代码。它将从[模板Excel文件](50528345.xlsm)中复制VBA项目到一个空工作簿，并将其保存为[输出Excel文件](50528346.xlsm)。如果您打开模板Excel文件中的VBA项目，您将看到如下所示的用户表单。用户表单包含设计师存储，因此将使用[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)和[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)方法进行复制。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

以下截图显示了复制自模板Excel文件的输出Excel文件及其内容。当您点击按钮1时，它会打开VBA用户表单，该用户表单本身有一个在单击时显示消息框的命令按钮。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
