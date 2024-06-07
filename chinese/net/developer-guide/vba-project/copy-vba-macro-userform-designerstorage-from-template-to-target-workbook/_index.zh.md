---
title: 从模板复制VBA宏用户窗体设计存储到目标工作簿
type: docs
weight: 130
url: /zh/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能的使用场景**

Aspose.Cells允许您将一个Excel文件中的VBA项目复制到另一个Excel文件中。 VBA项目包括各种类型的模块，例如文档、过程、设计师等。可以使用简单的代码复制所有模块，但是对于设计师模块，有一些额外的名为设计师存储的数据需要访问或复制。以下两种方法处理设计师存储。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **将VBA宏用户窗体设计器存储从模板复制到目标工作簿**

请参阅以下示例代码。 它将VBA项目从[模板Excel文件](50528345.xlsm)复制到一个空工作簿中，并将其另存为[输出Excel文件](50528346.xlsm)。 如果您在模板Excel文件中打开VBA项目，您将看到如下所示的用户窗体。 用户窗体包含设计者存储，因此将使用[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)和[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)方法进行复制。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

以下截图显示了从模板Excel文件中复制的输出Excel文件及其内容。 当您单击按钮1时，它将打开VBA用户窗体，该窗体本身有一个命令按钮，单击后将显示消息框。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
