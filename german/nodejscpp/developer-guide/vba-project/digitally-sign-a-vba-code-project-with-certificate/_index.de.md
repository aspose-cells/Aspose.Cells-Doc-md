---
title: Digitale Signatur eines VBA Code Projekts mit Zertifikat mit Node.js via C++
linktitle: Digitale Signatur eines VBA Codeprojekts mit Zertifikat
type: docs
weight: 110
url: /de/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Erfahren Sie, wie Sie ein VBA Codeprojekt mit einem Zertifikat mithilfe von Aspose.Cells for Node.js via C++ digital signieren.
---

{{% alert color="primary" %}}

Sie können Ihr VBA-Codeprojekt mit Aspose.Cells und seiner [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-) Methode digital signieren. Bitte folgen Sie diesen Schritten, um zu prüfen, ob Ihre Excel-Datei mit einem Zertifikat digital signiert ist.

- Klicken Sie auf **Visual Basic** im **Entwicklertools**-Tab, um die **Visual Basic for Applications-IDE** zu öffnen
- Klicken Sie auf **Extras** > **Digitale Signaturen...** des **Visual Basic for Applications IDE**

und es wird das **Digitale Signaturformular** anzeigen, das anzeigt, ob das Dokument digital mit einem Zertifikat signiert ist oder nicht.

{{% /alert %}} 

## **Digitales Signieren eines VBA-Codeprojekts mit Zertifikat in Node.js**

Der folgende Beispielcode zeigt, wie man die [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-)-Methode nutzt. Hier sind die Eingabe- und Ausgabedateien des Beispielcodes. Sie können jede Excel-Datei und jedes Zertifikat zum Testen dieses Codes verwenden.

- [Quell-Excel-Datei](5115028.xlsm), die im Beispielcode verwendet wird.
- [Beispiel-PFX-Datei](5115039.pfx) zur Erstellung einer digitalen Signatur. Bitte installieren Sie diese auf Ihrem Computer, um diesen Code auszuführen. Das Kennwort lautet 1234.
- [Ausgabe-Excel-Datei](5115029.xlsm), die vom Beispielcode generiert wurde.

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
