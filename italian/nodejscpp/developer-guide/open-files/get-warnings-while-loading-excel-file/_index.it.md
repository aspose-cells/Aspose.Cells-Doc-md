---
title: Ottieni avvisi durante il caricamento di file Excel con Node.js tramite C++
linktitle: Ottieni Avvertimenti durante il Caricamento del File Excel
type: docs
weight: 110
url: /it/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Impara come catturare gli avvisi durante il caricamento di un file Excel usando Aspose.Cells for Node.js via C++. Gestisci efficacemente i workbook corrotti ma caricabili.
---

## **Possibili Scenari di Utilizzo**

A volte l’utente tenta di caricare un workbook che è in qualche modo corrotto ma comunque caricabile. In tali casi, Aspose.Cells visualizza avvisi durante il caricamento del workbook. È possibile catturare questi avvisi implementando l’interfaccia [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) e impostando la proprietà [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--).

## **Ottieni avvisi durante il caricamento del file Excel**

Il seguente esempio spiega come ottenere avvisi durante il caricamento di un file Excel. Il codice carica il [sample excel file](sampleDuplicateDefinedName.xlsx) che genera un avviso [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype) al caricamento. Questo avviso viene poi catturato dal metodo [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-) che stampa i messaggi di avviso sulla console. Il codice salva quindi il workbook come [file excel di output](outputDuplicateDefinedName.xlsx). Se si apre il file Excel di esempio in Microsoft Excel, verrà mostrato anche questo avviso, come mostrato nello screenshot. Si prega di consultare anche l’output della console del codice di seguito fornito per maggiori dettagli.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **Output della console**

Questo è l'output della console del codice sopra quando eseguito con il [file excel di esempio fornito](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
