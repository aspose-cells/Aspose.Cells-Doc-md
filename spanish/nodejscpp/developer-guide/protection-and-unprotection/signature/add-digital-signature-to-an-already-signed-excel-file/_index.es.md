---
title: Agregar firma digital a un archivo de Excel ya firmado con Node.js mediante C++
linktitle: Agregar Firma Digital a un archivo de Excel que ya está firmado
type: docs
weight: 20
url: /es/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Este artículo describe cómo agregar una firma digital a un archivo de Excel ya firmado usando Node.js con Aspose.Cells for Node.js via C++.
keywords: Agregar firma digital a un archivo de Excel ya firmado, cómo agregar una firma digital a un documento de Excel ya firmado usando Node.js a través de C++.
---

## **Escenarios de uso posibles**

Aspose.Cells for Node.js via C++ proporciona el método [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) que puede usar para agregar una firma digital a un archivo de Excel ya firmado.

{{% alert color="primary" %}}

Tenga en cuenta que al agregar una firma digital a un documento de Excel ya firmado, si el documento original es un documento generado por Aspose.Cells, funciona bien. Pero si el documento original es generado por otros motores (por ejemplo, Microsoft Excel, etc.), Aspose.Cells no puede mantener el archivo igual después de cargarlo y volver a guardarlo, lo que invalidará la firma original.

{{% /alert %}}

## **Cómo agregar una firma digital a un archivo de Excel ya firmado**

El código de ejemplo siguiente demuestra cómo usar el método [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) para agregar una firma digital a un archivo de Excel ya firmado. Por favor, revise el [archivo de Excel de ejemplo](50528280.xlsx) utilizado en este código. Este archivo ya está firmado digitalmente. Por favor, revise el [archivo de Excel de salida](50528281.xlsx) generado por el código. Hemos utilizado el certificado de demostración llamado [AsposeDemo.pfx](50528279.pfx), que tiene una contraseña **aspose**. La captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo después de la ejecución.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Código de muestra**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
