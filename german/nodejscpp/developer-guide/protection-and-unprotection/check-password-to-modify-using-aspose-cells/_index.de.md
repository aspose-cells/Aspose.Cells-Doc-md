---  
title: Passwort zum Ändern mit Aspose.Cells for Node.js via C++ überprüfen  
linktitle: Passwort zum Ändern prüfen  
type: docs  
weight: 2400  
url: /de/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Erfahren Sie, wie Sie prüfen, ob das Änderungs Passwort mit Aspose.Cells for Node.js via C++ übereinstimmt.  
---  

{{% alert color="primary" %}}  
Manchmal müssen Sie programmgesteuert prüfen, ob das angegebene Passwort mit dem **Passwort zum Ändern** übereinstimmt. Aspose.Cells bietet die Methode `WorkbookSettings.writeProtection.validatePassword()`, die Sie verwenden können, um zu überprüfen, ob das angegebene Passwort korrekt ist.  
{{% /alert %}}  

## **Passwort zum Ändern in Microsoft Excel überprüfen**  

Sie können beim Erstellen Ihrer Arbeitsbücher in Microsoft Excel **Passwort zum Öffnen** und **Passwort zum Ändern** zuweisen. Bitte sehen Sie sich diesen Screenshot an, der die Benutzeroberfläche zeigt, die Microsoft Excel zum Angeben dieser Passwörter bereitstellt.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Passwort zum Ändern mit Aspose.Cells for Node.js via C++ überprüfen**  

Die folgenden Beispielcodes laden die [Quelldatei Excel](5112232.xlsx). Sie hat ein Passwort zum Öffnen als 1234 und zum Ändern als 5678. Der Code überprüft zuerst, ob 567 das richtige Passwort zum Ändern ist, und gibt false zurück, und überprüft anschließend, ob 5678 das Passwort zum Ändern ist, wobei true zurückgegeben wird.  

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

### **Konsolenausgabe**  

Hier ist die Konsolenausgabe des obigen Beispielscodes nach dem Laden der [Quell-Excel](5112232.xlsx)-Datei.  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
