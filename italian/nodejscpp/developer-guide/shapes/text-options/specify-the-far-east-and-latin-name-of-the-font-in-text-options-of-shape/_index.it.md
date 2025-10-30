---  
title: Specifica il nome del carattere Far East e Latin nelle Opzioni di Testo di una forma con Node.js via C++  
linktitle: Specificare il Nome Estremo Orientale e Latino del Carattere nelle Opzioni di Testo della Forma  
type: docs  
weight: 1600  
url: /it/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Impara come specificare i nomi dei caratteri Far East e Latin nelle opzioni di testo delle forme usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

A volte vuoi mostrare del testo in un carattere di lingua Far East, ad esempio Giapponese, Cinese, Tailandese, ecc. Aspose.Cells for Node.js via C++ fornisce la proprietà [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--) che può essere usata per specificare il nome del carattere per la lingua Far East. Inoltre, puoi anche specificare il nome del carattere Latin usando la proprietà [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--).  

## **Specificare il Nome Estremo Orientale e Latino del Carattere nelle Opzioni di Testo della Forma**  

Il seguente esempio di codice crea una casella di testo e vi aggiunge del testo giapponese. Poi specifica i nomi dei caratteri Latin e Far East del testo e salva il libro di lavoro come [file Excel di output](67338274.xlsx). La schermata seguente mostra i nomi dei caratteri Latin e Far East della casella di testo di output in Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
