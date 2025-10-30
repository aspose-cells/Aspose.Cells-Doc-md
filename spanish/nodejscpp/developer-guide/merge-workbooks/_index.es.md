---
title: Combina múltiples libros de trabajo en un solo libro usando Node.js a través de C++
linktitle: Combinar libros de trabajo
type: docs
weight: 66
url: /es/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aprende cómo combinar múltiples libros de trabajo en un solo libro usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A veces, necesitas combinar libros de trabajo con contenido variado como imágenes, gráficos y datos en un solo libro. Aspose.Cells for Node.js via C++ soporta esta función. Este artículo muestra cómo crear una aplicación de consola y combinar libros de trabajo con unas pocas líneas de código usando Aspose.Cells.

{{% /alert %}}

## **Combinar libros de trabajo con imágenes y gráficos**

El código de ejemplo combina dos libros de trabajo en un solo libro usando Aspose.Cells for Node.js via C++. El código carga los libros de origen, usa el método [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) para combinarlos, y guarda el libro de salida.

### **Libros de trabajo de origen**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Libros de trabajo de salida**

- [combined.xlsx](5473095.xlsx)

### **Capturas de pantalla**

A continuación se muestran capturas de pantalla de los libros de trabajo de origen y de salida.

{{% alert color="primary" %}}

Puede utilizar cualquier libro de trabajo de origen. Estas imágenes son solo con fines ilustrativos.

{{% /alert %}}

**La primera hoja de cálculo del libro de trabajo de gráficos: apilada** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Segunda hoja de cálculo del libro de trabajo de gráficos: línea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primera hoja de cálculo del libro de trabajo de imagen: imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Las tres hojas de cálculo en el libro de trabajo combinado: apilada, línea, imagen** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **Temas avanzados**
- [Combinar múltiples hojas de cálculo en una sola hoja de cálculo](/cells/es/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionar archivos](/cells/es/nodejs-cpp/merge-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
