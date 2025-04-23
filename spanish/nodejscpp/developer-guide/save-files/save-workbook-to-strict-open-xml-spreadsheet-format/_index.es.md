---  
title: Guardar Libro de trabajo en Formato de Hoja de Cálculo XML Abierto Estricto con Node.js a través de C++  
linktitle: Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto  
type: docs  
weight: 150  
url: /es/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Aprende cómo guardar un libro de trabajo en formato de Hoja de Cálculo XML Abierto Estricto usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells for Node.js via C++ te permite guardar el libro de trabajo en formato *Strict Open XML Spreadsheet*. Para ello, proporciona la propiedad [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--). Si estableces su valor como [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), entonces el archivo Excel de salida se guardará en formato de Hoja de Cálculo XML Abierto Estricto.  

## **Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto**  

El siguiente código de ejemplo crea un libro de trabajo y establece el valor de la propiedad [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) como [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) y lo guarda como [archivo Excel de salida](67338272.xlsx). Si abres el archivo Excel en Microsoft Excel y abres el cuadro de diálogo Guardar como..., verás su formato como *Strict Open XML Spreadsheet* como se muestra en esta captura de pantalla.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Specify - Strict Open XML Spreadsheet - Format.
wb.getSettings().setCompliance(AsposeCells.OoxmlCompliance.Iso29500_2008_Strict);

// Add message in cell B4 of first worksheet.
const b4 = wb.getWorksheets().get(0).getCells().get("B4");
b4.putValue("This Excel file has Strict Open XML Spreadsheet format.");

// Save to output Excel file.
wb.save("outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

