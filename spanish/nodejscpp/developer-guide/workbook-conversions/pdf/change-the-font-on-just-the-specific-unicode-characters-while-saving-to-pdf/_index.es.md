---
title: Cambiar la fuente solo en caracteres Unicode específicos al guardar en PDF con Node.js a través de C++
linktitle: Cambiar la fuente solo de los caracteres Unicode específicos al guardar en PDF
type: docs
weight: 260
url: /es/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aprende cómo cambiar la fuente de caracteres Unicode específicos al guardar en PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Algunos caracteres Unicode no se pueden mostrar con la fuente especificada por el usuario. Uno de estos caracteres Unicode es **Guión no separable** (U+2011) y su número Unicode es 8209. Este carácter no se puede mostrar con **Times New Roman**, pero se puede mostrar con otras fuentes como **Arial Unicode MS**.

Cuando aparece un carácter así dentro de alguna palabra o frase en una fuente específica como Times New Roman, Aspose.Cells cambia toda la fuente de la palabra o frase a una que pueda mostrar ese carácter, como Arial Unicode o MS.

Sin embargo, este comportamiento no es deseado para algunos usuarios y solo quieren que la fuente de ese carácter específico cambie en lugar de toda la palabra o frase.

Para solucionar este problema, Aspose.Cells ofrece la propiedad `PdfSaveOptions.isFontSubstitutionCharGranularity` que debe establecerse en true para que solo la fuente de los caracteres no visibles sea cambiada a una fuente visible, mientras que el resto de la palabra o frase permanecen en la fuente original.

{{% /alert %}} 

## **Ejemplo**
La siguiente captura de pantalla compara los dos PDF generados por el código de muestra a continuación.

Una se genera sin configurar la propiedad `PdfSaveOptions.isFontSubstitutionCharGranularity` y la otra después de establecerla en true.

Como se puede ver en el primer PDF, la fuente de toda la frase cambió de Times New Roman a Arial Unicode MS debido al guion no separable. Mientras que en el segundo PDF, solo cambió la fuente del guion no separable.

|**Primer archivo PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Segundo archivo PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Código de muestra**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



{{< app/cells/assistant language="nodejs-cpp" >}}
