---
title: Firmar digitalmente un proyecto de código VBA con certificado usando Node.js a través de C++
linktitle: Firmar digitalmente un proyecto de código VBA con un certificado
type: docs
weight: 110
url: /es/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aprenda cómo firmar digitalmente un proyecto de código VBA con un certificado usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Puede firmar digitalmente su proyecto de código VBA usando Aspose.Cells con su método [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Siga estos pasos para verificar si su archivo de Excel está firmado digitalmente con un certificado.

- Haga clic en **Visual Basic** desde la pestaña **Desarrollador** para abrir **Visual Basic para Aplicaciones IDE**
- Haga clic en **Herramientas** > **Firmas Digitales...** de  **Visual Basic para Aplicaciones IDE**

y mostrará el **Formulario de Firma Digital** que muestra si el documento está firmado digitalmente con un certificado o no.

{{% /alert %}} 

## **Firmar digitalmente un proyecto de código VBA con certificado en Node.js**

El siguiente código de muestra ilustra cómo hacer uso del método [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Aquí están los archivos de entrada y salida del código de muestra. Puede usar cualquier archivo de Excel y cualquier certificado para probar este código.

- [Archivo de Excel de origen](5115028.xlsm) utilizado en el código de ejemplo.
- [Archivo pfx de ejemplo](5115039.pfx) para crear la Firma Digital. Por favor, instálelo en su computadora para ejecutar este código. Su contraseña es 1234.
- [Archivo de Excel de salida](5115029.xlsm) generado por el código de ejemplo.

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
