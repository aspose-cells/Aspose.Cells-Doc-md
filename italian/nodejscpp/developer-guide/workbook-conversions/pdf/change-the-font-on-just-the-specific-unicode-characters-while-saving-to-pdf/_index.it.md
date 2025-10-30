---
title: Cambia il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF con Node.js tramite C++
linktitle: Cambia il Font solo per i caratteri Unicode specifici durante il salvataggio in PDF
type: docs
weight: 260
url: /it/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Scopri come cambiare il font di caratteri Unicode specifici durante il salvataggio in PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Alcuni caratteri Unicode non possono essere visualizzati dal font specificato dall'utente. Uno di questi caratteri Unicode è **Trattino Non-Rotoso** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con **Times New Roman**, ma può essere visualizzato con altri font come **Arial Unicode MS**.

Quando si verifica un carattere del genere all'interno di una parola o frase in un font specifico come Times New Roman, Aspose.Cells cambia il font dell'intera parola o frase in un font che può mostrare questo carattere, come Arial Unicode o MS.

Tuttavia, questo comportamento non è desiderabile per alcuni utenti e vogliono modificare solo il font di quel carattere specifico invece di cambiare il font di tutta la parola o frase.

Per risolvere questo problema, Aspose.Cells fornisce la proprietà `PdfSaveOptions.isFontSubstitutionCharGranularity` che deve essere impostata su true in modo che il font di caratteri non visualizzabili venga modificato solo se necessario, mentre il resto della parola o frase rimarrà nel font originale.

{{% /alert %}} 

## **Esempio**
Lo screenshot seguente confronta i due file PDF generati dal codice di esempio qui sotto.

Uno viene generato senza impostare la proprietà `PdfSaveOptions.isFontSubstitutionCharGranularity` e l'altro dopo aver impostato la proprietà su true.

Come si può vedere nel primo PDF, il font dell'intera frase è cambiato da Times New Roman a Arial Unicode MS a causa dell'en dash non break. Nel secondo PDF, solo il font dell'en dash non break è cambiato.

|**Primo file Pdf**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Secondo file Pdf**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Codice di Esempio**


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
