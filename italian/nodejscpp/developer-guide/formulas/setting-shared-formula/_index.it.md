---
title: Impostare formula condivisa con Node.js tramite C++
linktitle: Impostazione Formula Condivisa
type: docs
weight: 10
url: /it/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Se vuoi aggiungere una funzione in un foglio di calcolo che esegua alcuni calcoli, questo articolo spiega come farlo usando Aspose.Cells for Node.js via C++.

{{% /alert %}}

## Impostare formula condivisa con Aspose.Cells for Node.js via C++

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

|**File di input con una colonna di dati**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Desideri aggiungere una funzione in B2 che calcolerà l'IVA per la prima riga di dati. L'IVA è del **9%**. La formula che calcola l'IVA è: **"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

Aspose.Cells consente di specificare una formula utilizzando la proprietà [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--). Ci sono due opzioni per aggiungere formule alle altre celle (B3, B4, B5, e così via) nella colonna.

Puoi ripetere ciò che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento della cella (A3*0.09, A4*0.09, A5*0.09, ecc.). Questo richiede di aggiornare i riferimenti di cella per ogni riga. Richiede anche che Aspose.Cells analizzi ogni formula singolarmente, il che può essere lento per fogli di calcolo grandi e formule complesse. Aggiunge inoltre righe di codice extra, anche se i cicli possono ridurle in parte.

Un altro approccio è utilizzare una **formula condivisa**. Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti alle celle in ogni riga in modo che l'imposta venga calcolata correttamente. Il metodo [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) è più efficiente del primo metodo.

L'esempio seguente mostra come utilizzarla.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
