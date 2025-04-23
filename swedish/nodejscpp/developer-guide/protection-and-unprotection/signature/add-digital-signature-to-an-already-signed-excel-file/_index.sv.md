---
title: Lägg till digital signatur i en redan signerad Excel fil med Node.js via C++
linktitle: Lägg till digital signatur i en redan signerad Excelfil
type: docs
weight: 20
url: /sv/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Denna artikel beskriver hur man kan lägga till en digital signatur i en redan signerad Excel fil med Node.js och Aspose.Cells for Node.js via C++.
keywords: Lägg till digital signatur i en redan signerad Excel fil, hur man lägger till en digital signatur i ett redan signerad Excel dokument med Node.js via C++.
---

## **Möjliga användningsscenario**

Aspose.Cells for Node.js via C++ tillhandahåller [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)-metoden som kan användas för att lägga till en digital signatur i en redan signerad Excel-fil.

{{% alert color="primary" %}}

Vänligen observera att när du lägger till en digital signatur i ett redan signerad Excel-dokument, fungerar det bäst om den ursprungliga filen är genererad av Aspose.Cells. Men om den ursprungliga filen är genererad av andra motorer (t.ex. Microsoft Excel) kan Aspose.Cells inte behålla filen oförändrad efter att den laddats och sparats om, vilket gör den ursprungliga signaturen ogiltig.

{{% /alert %}}

## **Hur man lägger till en digital signatur till en redan signerad Excel-fil**

 Följande exempel visar hur man använder [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)-metoden för att lägga till en digital signatur i en redan signerad Excel-fil. Kontrollera [exempel-Excel-filen](50528280.xlsx) som används i denna kod. Denna fil är redan digitalt signerad. Kontrollera [utdata Excel-filen](50528281.xlsx) som genereras av koden. Vi har använt demosertifikatet [AsposeDemo.pfx](50528279.pfx) i denna kod, som har ett lösenord **aspose**. Skärmbilden visar effekten av kodexemplet på exemplexcel-filen efter körning.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
