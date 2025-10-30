---
title: Digital Signera ett VBA kodprojekt med certifikat med Node.js via C++
linktitle: Signera digitalt ett VBA kodprojekt med certifikat
type: docs
weight: 110
url: /sv/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Lär dig hur du digitalt signerar ett VBA kodprojekt med ett certifikat med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Du kan digitalt signera ditt VBA-kodprojekt med Aspose.Cells med dess [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-)-metod. Följ dessa steg för att kontrollera om din Excel-fil är digitalt signerad med ett certifikat.

- Klicka på **Visual Basic** från fliken **Utvecklare** för att öppna **Visual Basic for Applications IDE**
- Klicka på **Verktyg** > **Digitala signaturer...** av **Visual Basic for Applications IDE**

och det kommer att visa **Digital Signature Form** och visa om dokumentet är signerat digitalt med ett certifikat eller inte.

{{% /alert %}} 

## **Digital Signera ett VBA-kodprojekt med certifikat i Node.js**

Följande exempel illustrerar hur du använder [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-)-metoden. Här är in- och utdatafiler för exempelkoden. Du kan använda vilken Excel-fil som helst och vilket certifikat som helst för att testa denna kod.

- [Källa Excel-fil](5115028.xlsm) använd i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa digital signatur. Installera den på din dator för att köra denna kod. Dess lösenord är 1234.
- [Utdatat Excel-fil](5115029.xlsm) genererad av exempelkoden.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Set up paths
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const pfxPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.pfx");
const workbookPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.xlsm");

// Set Digital Signature
const password = "1234";
const comment = "Signing Digital Signature using Aspose.Cells";
const digitalSignature = new AsposeCells.DigitalSignature(fs.readFileSync(pfxPath), password, comment, new Date());

// Create workbook object from excel file
const workbook = new AsposeCells.Workbook(workbookPath);

// Sign VBA Code Project with Digital Signature
workbook.getVbaProject().sign(digitalSignature);

// Save the workbook
workbook.save(path.join(outputDir, "outputDigitallySignVbaProjectWithCertificate.xlsm"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
