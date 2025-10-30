---  
title: Crear PdfBookmarkEntry para hoja de gráfico con Node.js a través de C++  
linktitle: Crear PdfBookmarkEntry para la hoja de gráficos  
type: docs  
weight: 50  
url: /es/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Aprende cómo crear PdfBookmarkEntry para hojas de gráficos usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Anteriormente, Aspose.Cells creaba [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) para una hoja normal. Pero ahora Aspose.Cells también puede crear [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) para hojas de gráficos. Como una hoja de gráfico no tiene otras celdas aparte de la celda A1, solo creará [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) para la celda A1.  

## **Crear entrada de marcador de PDF para hoja de gráfico**  

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767756.xlsx) que tiene cuatro hojas. Dos de ellas son hojas normales y las otras dos son hojas de gráficos. Crea cuatro entradas de marcadores como sigue  

- Marca de libro-I  
- Marca de libro-II-Gráfico1  
- Marca de libro-III  
- Marca de libro-IV-Gráfico2  

La siguiente captura de pantalla muestra el [PDF de salida](61767757.pdf) generado por el código de muestra como referencia.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleCreatePdfBookmarkEntryForChartSheet.xlsx");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access all four worksheets
const sheet1 = workbook.getWorksheets().get(0);
const sheet2 = workbook.getWorksheets().get(1);
const sheet3 = workbook.getWorksheets().get(2);
const sheet4 = workbook.getWorksheets().get(3);

// Create Pdf Bookmark Entry for Sheet1
const ent1 = new AsposeCells.PdfBookmarkEntry();
ent1.setDestination(sheet1.getCells().get("A1"));
ent1.setText("Bookmark-I");

// Create Pdf Bookmark Entry for Sheet2 - Chart
const ent2 = new AsposeCells.PdfBookmarkEntry();
ent2.setDestination(sheet2.getCells().get("A1"));
ent2.setText("Bookmark-II-Chart1");

// Create Pdf Bookmark Entry for Sheet3
const ent3 = new AsposeCells.PdfBookmarkEntry();
ent3.setDestination(sheet3.getCells().get("A1"));
ent3.setText("Bookmark-III");

// Create Pdf Bookmark Entry for Sheet4 - Chart
const ent4 = new AsposeCells.PdfBookmarkEntry();
ent4.setDestination(sheet4.getCells().get("A1"));
ent4.setText("Bookmark-IV-Chart2");

// Arrange all Bookmark Entries
const lst = [];
lst.push(ent2);
lst.push(ent3);
lst.push(ent4);

// Create Pdf Save Options with Bookmark Entries
const opts = new AsposeCells.PdfSaveOptions();
opts.setBookmark(ent1);

// Save the output Pdf
workbook.save("outputCreatePdfBookmarkEntryForChartSheet.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
