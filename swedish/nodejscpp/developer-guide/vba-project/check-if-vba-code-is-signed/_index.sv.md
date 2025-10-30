---
title: Kontrollera om VBA koden är signerad med Node.js via C++
linktitle: Kontrollera om VBA koden är signerad
type: docs
weight: 100
url: /sv/nodejs-cpp/check-if-vba-code-is-signed/
description: Lär dig hur man kontrollerar om VBA kodprojektet är signerat med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells låter användaren kontrollera om VBA-kodprojektet är signerat eller inte. Använd [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) -egenskapen för att kontrollera om VBA-kodprojektet är signerat eller inte.

{{% /alert %}}

Följande kod förklarar hur man kontrollerar om VBA-koden är signerad eller inte med hjälp av [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--)-egenskapen. Du kan använda vilken som helst av dina Excel-filer för att testa denna kod. För teständamål kan du använda [denna Excel-fil som används i koden](5115032.xlsm).

## **Kontrollera om VBA-koden är signerad i Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## Konsoloutput

Nedan är konsoloutputen av ovanstående kod med [exempel excelfil](5115032.xlsm) tillhandahållen via länken.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
