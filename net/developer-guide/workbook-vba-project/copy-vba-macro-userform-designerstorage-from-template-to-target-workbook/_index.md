---
title: Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook
type: docs
weight: 130
url: /net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to copy a VBA project from one Excel file into another Excel file. VBA project consists of various types of modules i.e. Document, Procedural, Designer, etc. All modules can be copied with simple code but for the Designer module, there is some extra data called Designer Storage that needs to be accessed or copied. The following two methods deal with Designer Storage.

- [VbaModuleCollection.GetDesignerStorage()](https://apireference.aspose.com/net/cells/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [VbaModuleCollection.AddDesignerStorage()](https://apireference.aspose.com/net/cells/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)
## **Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook**
Please see the following sample code. It copies the VBA project from the [template Excel file](attachments/50270298/50528345.xlsm) into an empty workbook and saves it as the [output Excel file](attachments/50270298/50528346.xlsm). If you open the VBA project inside the template Excel file, you will see a User Form as shown below. The User Form consists of Designer Storage, so it will be copied using [VbaModuleCollection.GetDesignerStorage()](https://apireference.aspose.com/net/cells/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) and [VbaModuleCollection.AddDesignerStorage()](https://apireference.aspose.com/net/cells/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage) methods.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

The following screenshot shows the output Excel file and its contents which were copied from the template Excel file. When you click on the Button 1, it opens up the VBA User Form which itself has a command button that shows a message box on clicking.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}