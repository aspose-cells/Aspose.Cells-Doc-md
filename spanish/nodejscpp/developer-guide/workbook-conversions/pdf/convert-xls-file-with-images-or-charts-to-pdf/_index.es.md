---
title: Convertir archivo XLS con imágenes o gráficos a PDF con Node.js a través de C++
linktitle: Convertir archivo XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells soporta convertir archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for Node.js via C++ puede trabajar de manera independiente para convertir una hoja de cálculo a PDF: no se requiere Aspose.PDF para Node.js a través de C++ para la conversión. El proceso puede hacerse en memoria ya que no depende de archivos XML temporales o intermedios. Esto significa que archivos de Excel grandes, por ejemplo, que contienen imágenes, gráficos y otros objetos de dibujo, pueden convertirse rápida y eficientemente.

{{% /alert %}} 
## **Código de muestra**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

Si la hoja de cálculo contiene fórmulas, es recomendable llamar al método [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizar a PDF. Esto asegura que los valores dependientes de fórmulas se recalculen y que los valores correctos se rendericen en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
