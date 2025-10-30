---
title: Firmare digitalmente un progetto di codice VBA con certificato usando Node.js tramite C++
linktitle: Firma digitalmente un progetto di codice VBA con certificato
type: docs
weight: 110
url: /it/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Impara come firmare digitalmente un progetto di codice VBA con un certificato usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Puoi firmare digitalmente il progetto di codice VBA usando Aspose.Cells con il suo metodo [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Segui questi passaggi per verificare se il file Excel è firmato digitalmente con un certificato.

- Fare clic su **Visual Basic** dalla scheda **Sviluppo** per aprire l'**IDE di Visual Basic for Applications**
- Fare clic su **Strumenti** > **Firme digitali...** dell' **IDE di Visual Basic for Applications**

e verrà mostrato il **Modulo di firma digitale** che indica se il documento è firmato digitalmente con un certificato o meno.

{{% /alert %}} 

## **Firmare digitalmente un progetto di codice VBA con certificato in Node.js**

Il seguente esempio di codice illustra come utilizzare il metodo [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Ecco i file di input e output del codice di esempio. Puoi usare qualsiasi file Excel e qualsiasi certificato per testare questo codice.

- [File Excel di origine](5115028.xlsm) utilizzato nel codice di esempio.
- [File pfx di esempio](5115039.pfx) per creare una firma digitale. Si prega di installarlo sul computer per eseguire questo codice. La password è 1234.
- [File Excel di output](5115029.xlsm) generato dal codice di esempio.

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
