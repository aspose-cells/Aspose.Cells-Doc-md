---  
title: Kontrollera lösenord för att ändra med Aspose.Cells for Node.js via C++  
linktitle: Kontrollera lösenord för att ändra  
type: docs  
weight: 2400  
url: /sv/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Lär dig hur man kontrollerar om ett lösenord för att ändra matchar med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Ibland behöver du kontrollera om det givna lösenordet matchar med **Lösenord för att ändra** programatiskt. Aspose.Cells erbjuder metoden `WorkbookSettings.writeProtection.validatePassword()` som du kan använda för att kontrollera om det givna Lösenord för att ändra är korrekt eller inte.  
{{% /alert %}}  

## **Kontrollera lösenord för modifiering i Microsoft Excel**  

Du kan tilldela **Lösenord för att öppna** och **Lösenord för att modifiera** när du skapar dina arbetsböcker i Microsoft Excel. Se denna skärmbild som visar gränssnittet som Microsoft Excel tillhandahåller för att ange dessa lösenord.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Kontrollera lösenord för att ändra med Aspose.Cells for Node.js via C++**  

Följande exempel laddar [källexemplet](5112232.xlsx). Filen har ett Lösenord för öppning 1234 och ett Lösenord för att ändra 5678. Koden kontrollerar först om 567 är det korrekta lösenordet för att ändra och ger `false`, och sedan kontrollerar den om 5678 är rätt lösenord för att ändra och ger `true`.  

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

### **Konsoloutput**  

Här är konsolens utmatning av ovanstående kod efter att ha laddat den [käll-Excel-filen](5112232.xlsx).  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
