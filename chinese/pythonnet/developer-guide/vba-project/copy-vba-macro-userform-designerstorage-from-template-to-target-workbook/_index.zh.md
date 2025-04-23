---
title: 将VBA宏用户表单DesignerStorage从模板复制到目标工作簿
type: docs
weight: 130
url: /zh/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能的使用场景**

Aspose.Cells for Python via .NET允许您将VBA项目从一个Excel文件复制到另一个Excel文件。VBA项目由各种模块类型组成，例如文档、过程、设计师模块等。所有模块都可以通过简单代码复制，但对于设计师模块，还需要访问或复制一些额外数据，称为设计师存储。以下两个方法涉及设计师存储。

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **将VBA宏用户表单DesignerStorage从模板复制到目标工作簿**

请参见以下示例代码。它将从[模板Excel文件](50528345.xlsm)中复制VBA项目到一个空工作簿，并将其保存为[输出Excel文件](50528346.xlsm)。如果您打开模板Excel文件中的VBA项目，您将看到如下所示的用户表单。用户表单包含设计师存储，因此将使用[**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)和[**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage)方法进行复制。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

以下截图显示了复制自模板Excel文件的输出Excel文件及其内容。当您点击按钮1时，它会打开VBA用户表单，该用户表单本身有一个在单击时显示消息框的命令按钮。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

