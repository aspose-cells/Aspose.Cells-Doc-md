---
title: Combina più cartelle di lavoro in un unica cartella di lavoro con Node.js tramite C++
linktitle: Unione Cartelle di Lavoro
type: docs
weight: 66
url: /it/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Impara come combinare più cartelle di lavoro in un unica cartella di lavoro usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A volte, è necessario combinare le cartelle di lavoro con contenuti vari come immagini, grafici e dati in un'unica cartella di lavoro. Aspose.Cells for Node.js via C++ supporta questa funzionalità. Questo articolo mostra come creare un'applicazione console e combinare le cartelle di lavoro con poche semplici righe di codice usando Aspose.Cells.

{{% /alert %}}

## **Unione Cartelle di Lavoro con Immagini e Grafici**

Il codice di esempio combina due cartelle di lavoro in un'unica cartella di lavoro usando Aspose.Cells for Node.js via C++. Il codice carica le cartelle di lavoro di origine, utilizza il metodo [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) per combinarle, e salva la cartella di lavoro risultante.

### **Cartelle di Lavoro di Origine**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Cartelle di Lavoro di Output**

- [combined.xlsx](5473095.xlsx)

### **Screenshot**

Di seguito sono riportati gli screenshot delle cartelle di lavoro di origine e di output.

{{% alert color="primary" %}}

Puoi utilizzare qualsiasi cartella di lavoro di origine. Queste immagini sono solo a scopo illustrativo.

{{% /alert %}}

**Il primo foglio di lavoro della cartella di lavoro dei grafici - sovrapposto** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Secondo foglio di lavoro della cartella di lavoro dei grafici - linea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primo foglio di lavoro della cartella di immagini - immagine** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Tutti e tre i fogli di lavoro nel libro combinato - sovrapposti, linea, immagine** 

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

## **Argomenti avanzati**
- [Unisci più fogli di lavoro in un'unica scheda](/cells/it/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Unire file](/cells/it/nodejs-cpp/merge-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
