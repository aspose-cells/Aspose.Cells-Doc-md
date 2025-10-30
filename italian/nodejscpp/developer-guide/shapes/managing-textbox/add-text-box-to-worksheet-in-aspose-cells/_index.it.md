---
title: Come aggiungere/inserire una TextBox nel Foglio di lavoro con Node.js tramite C++
linktitle: Aggiungi una casella di testo al foglio di lavoro
type: docs
weight: 10
url: /it/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Come aggiungere/inserire una TextBox nel Foglio di lavoro in Aspose.Cells for Node.js via C++.
keywords: Aggiungi/inserisci testo alla Text Box nel Foglio di lavoro Excel Aspose Node.js tramite C++
---

## Aggiungere casella di testo al foglio di lavoro in Excel

Nel programma Excel (versione 07 e successive), ci sono due punti in cui puoi inserire caselle di testo. Uno in "inserisci-shapes", l'altro sulla destra del menu superiore dell'opzione "Inserisci".

### metodo uno:

![1](1.png)

### metodo due:

![2](2.png)

## Come creare

Puoi creare caselle di testo con testo orizzontale o verticale.

- Seleziona l'opzione corrispondente (orizzontale o verticale)
- Fai clic sinistro sulla pagina
- Tieni premuto il pulsante sinistro e trascina una distanza sulla pagina
- Rilascia il pulsante sinistro

Ora hai una casella di testo.

## Aggiungi casella di testo al foglio di lavoro in Aspose.Cells for Node.js via C++

Quando è necessario inserire automaticamente molte caselle di testo nel foglio di lavoro, il metodo di inserimento manuale è chiaramente un disastro. Se questo ti disturba, penso che questo documento ti sarà di aiuto. [Aspose.Cells](https://products.aspose.com/cells/) ti fornisce un'API per effettuare facilmente inserimenti di massa nel tuo codice.

Il seguente codice di esempio crea una casella di testo.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Otterrai un file simile a [file risultato](result.xlsx). Nel file, vedrai quanto segue:

![](52449.png)

{{< app/cells/assistant language="nodejs-cpp" >}}
