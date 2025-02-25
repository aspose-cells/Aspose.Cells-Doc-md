---  
title: Check Password to modify using Aspose.Cells for Node.js via C++  
linktitle: Check Password to modify  
type: docs  
weight: 2400  
url: /nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Learn how to check if a password to modify matches using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Sometimes, you need to check if the given password matches with the **Password to modify** programmatically. Aspose.Cells provides the `WorkbookSettings.writeProtection.validatePassword()` method which you can use to check if the given Password to modify is correct or not.  
{{% /alert %}}  

## **Check Password to modify in Microsoft Excel**  

You can assign **Password to open** and **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot which shows the interface Microsoft Excel provides to specify these passwords.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Check Password to modify using Aspose.Cells for Node.js via C++**  

The following sample codes load the [source Excel](5112232.xlsx) file. It has a Password to open as 1234 and Password to modify as 5678. The code first checks if 567 is the correct Password to modify and it returns false, and then it checks if 5678 is the Password to modify and it returns true.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **Console Output**  

Here is the Console Output of the above sample code after loading the [source Excel](5112232.xlsx) file.  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
