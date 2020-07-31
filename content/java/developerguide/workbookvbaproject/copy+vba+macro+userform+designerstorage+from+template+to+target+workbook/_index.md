---
title : "Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook" 
description : "" 
weight : 12273 
toc : false
type: docs
url: /java/developerguide/workbookvbaproject/copy+vba+macro+userform+designerstorage+from+template+to+target+workbook/
---

# Aspose.Cells for Java : Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook](#copy-vba-macro-userform-designerstorage-from-template-to-target-workbook)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
## Possible Usage Scenarios

Aspose.Cells allows you to copy the VBA project from one Excel file into another Excel file. VBA project consists of various types of modules i.e. Document, Procedural, Designer etc. All modules can be copied with simple code but for Designer module, there is some extra data called Designer Storage that needs to be accessed or copied. The following two methods deal with Designer Storage.

*   [VbaModuleCollection.GetDesignerStorage()](https://apireference.aspose.com/java/cells/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
*   VbaModuleCollection.AddDesignerStorage()

## Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook

Please see the following sample code. It copies the VBA project from the [template Excel file](https://docs2.aspose.com/cells/java/attachments/50270505/50528367.xlsm) into an empty workbook and saves it as the [output Excel file](https://docs2.aspose.com/cells/java/attachments/50270505/50528366.xlsm). If you open the VBA project inside the template Excel file, you will see a User Form as shown below. The User Form consists of Designer Storage, so it will be copied using [VbaModuleCollection.GetDesignerStorage()](https://apireference.aspose.com/java/cells/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) and VbaModuleCollection.AddDesignerStorage() methods.

![](https://docs2.aspose.com/cells/java/attachments/50270505/50528365.png)

The following screenshot shows the output Excel file and its contents which were copied from the template Excel file. When you click on the `Button 1`, it opens up the `VBA User Form` which itself has a command button that shows a message box on clicking.

![](https://docs2.aspose.com/cells/java/attachments/50270505/50528364.png)

## Sample Code

