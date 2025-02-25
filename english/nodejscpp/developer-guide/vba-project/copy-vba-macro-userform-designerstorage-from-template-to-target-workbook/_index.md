---  
title: Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook with Node.js via C++  
linktitle: Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook  
type: docs  
weight: 130  
url: /nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Learn how to copy a VBA project, including Designer Storage, from one Excel file to another using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**  

Aspose.Cells allows you to copy a VBA project from one Excel file into another Excel file. A VBA project consists of various types of modules i.e. Document, Procedural, Designer, etc. All modules can be copied with simple code, but for the Designer module, there is some extra data called Designer Storage that needs to be accessed or copied. The following two methods deal with Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage()**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/methods/getdesignerstorage)  
- [**VbaModuleCollection.addDesignerStorage()**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/methods/adddesignerstorage)  

## **Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook**  

Please see the following sample code. It copies the VBA project from the [template Excel file](50528345.xlsm) into an empty workbook and saves it as the [output Excel file](50528346.xlsm). If you open the VBA project inside the template Excel file, you will see a User Form as shown below. The User Form consists of Designer Storage, so it will be copied using [**VbaModuleCollection.getDesignerStorage()**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/methods/getdesignerstorage) and [**VbaModuleCollection.addDesignerStorage()**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/methods/adddesignerstorage) methods.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

The following screenshot shows the output Excel file and its contents which were copied from the template Excel file. When you click on the Button 1, it opens up the VBA User Form which itself has a command button that shows a message box on clicking.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty target workbook
const target = new AsposeCells.Workbook();

// Load the Excel file containing VBA-Macro Designer User Form
const templateFile = new AsposeCells.Workbook(path.join(sourceDir, "sampleDesignerForm.xlsm"));

// Copy all template worksheets to target workbook
templateFile.getWorksheets().forEach(ws => {
    if (ws.getType() === AsposeCells.SheetType.Worksheet) {
        const s = target.getWorksheets().add(ws.getName());
        s.copy(ws);

        // Put message in cell A2 of the target worksheet
        s.getCells().get("A2").putValue("VBA Macro and User Form copied from template to target.");
    }
});

// Copy the VBA-Macro Designer UserForm from Template to Target 
templateFile.getVbaProject().getModules().forEach(vbaItem => {
    if (vbaItem.getName() === "ThisWorkbook") {
        // Copy ThisWorkbook module code
        target.getVbaProject().getModules().get("ThisWorkbook").setCodes(vbaItem.getCodes());
    } else {
        console.log(vbaItem.getName());

        let vbaMod = 0;
        const sheet = target.getWorksheets().getSheetByCodeName(vbaItem.getName());
        if (sheet == null) {
            vbaMod = target.getVbaProject().getModules().add(vbaItem.getType(), vbaItem.getName());
        } else {
            vbaMod = target.getVbaProject().getModules().add(sheet);
        }

        target.getVbaProject().getModules().get(vbaMod).setCodes(vbaItem.getCodes());

        if (vbaItem.getType() === AsposeCells.VbaModuleType.Designer) {
            // Get the data of the user form i.e. designer storage
            const designerStorage = templateFile.getVbaProject().getModules().getDesignerStorage(vbaItem.getName());

            // Add the designer storage to target Vba Project
            target.getVbaProject().getModules().addDesignerStorage(vbaItem.getName(), designerStorage);
        }
    }
});

// Save the target workbook
target.save(path.join(outputDir, "outputDesignerForm.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  
  