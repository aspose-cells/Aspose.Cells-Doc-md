---
title: Verificar si el código VBA está firmado con Node.js vía C++
linktitle: Verifique si el Código VBA está firmado
type: docs
weight: 100
url: /es/nodejs-cpp/check-if-vba-code-is-signed/
description: Aprende cómo verificar si el proyecto de código VBA está firmado usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells permite al usuario verificar si el proyecto de código VBA está firmado o no. Por favor utiliza la propiedad [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) para verificar si el proyecto de código VBA está firmado o no.

{{% /alert %}}

El siguiente código explica cómo verificar si el código VBA está firmado o no usando la propiedad [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--). Puedes usar cualquiera de tus archivos de Excel para probar este código. Para fines de prueba, puedes usar [este archivo de Excel usado en el código](5115032.xlsm).

## **Verificar si el código VBA está firmado en Node.js**

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

## Salida de la consola

A continuación se muestra la salida de consola del código anterior utilizando el [archivo excel de muestra](5115032.xlsm) proporcionado por el enlace.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
