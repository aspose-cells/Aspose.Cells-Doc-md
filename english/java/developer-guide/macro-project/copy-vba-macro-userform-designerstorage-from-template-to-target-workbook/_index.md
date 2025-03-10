---
title: Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook
type: docs
weight: 60
url: /java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to copy the VBA project from one Excel file into another Excel file. VBA project consists of various types of modules i.e. Document, Procedural, Designer etc. All modules can be copied with simple code but for Designer module, there is some extra data called Designer Storage that needs to be accessed or copied. The following two methods deal with Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook**

Please see the following sample code. It copies the VBA project from the [template Excel file](50528367.xlsm) into an empty workbook and saves it as the [output Excel file](50528366.xlsm). If you open the VBA project inside the template Excel file, you will see a User Form as shown below. The User Form consists of Designer Storage, so it will be copied using [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) and [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-) methods.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

The following screenshot shows the output Excel file and its contents which were copied from the template Excel file. When you click on the Button 1, it opens up the VBA User Form which itself has a command button that shows a message box on clicking.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}