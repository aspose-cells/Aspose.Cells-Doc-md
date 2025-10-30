---  
title: Renderizzare il riempimento a gradiente per WordArt durante la conversione di fogli di calcolo in HTML con Node.js tramite C++  
linktitle: Rendere il riempimento a gradienti per il WordArt durante la conversione dei fogli di calcolo in HTML  
type: docs  
weight: 90  
url: /it/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Scopri come rendere il riempimento a gradiente per WordArt durante la conversione di fogli di calcolo in HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  
Prima di Aspose.Cells 17.1, Aspose.Cells non rendeva il riempimento a gradiente di WordArt quando il file Excel veniva convertito in formato HTML. Dalla versione 17.1 di Aspose.Cells, il riempimento a gradiente di WordArt è supportato. La schermata seguente confronta l'effetto sul riempimento a gradiente convertendo il file Excel con Aspose.Cells 17.1 e le versioni precedenti.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Rendi il riempimento a sfumatura per l'WordArt durante la conversione dei fogli di calcolo in HTML**  
Il seguente esempio di codice converte il [file excel di origine](22774111.xlsx) in [formato HTML di output](22774109.zip). Il file excel di origine contiene un oggetto WordArt con riempimento a gradiente come mostrato nella schermata sopra.  

## **Codice di Esempio**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
