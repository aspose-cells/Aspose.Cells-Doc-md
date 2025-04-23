---  
title: Aggiungi icone al foglio di lavoro con Node.js tramite C++  
linktitle: Gestione delle icone  
type: docs  
weight: 100  
url: /it/nodejs-cpp/insert-svg-to-excel/  
---  

## Aggiungi icone al foglio di lavoro in Aspose.Cells for Node.js via C++

Se hai bisogno di utilizzare [Aspose.Cells](https://products.aspose.com/cells/) per aggiungere 'icone' in un file Excel, allora questo documento può offrirti un aiuto.

L'interfaccia Excel corrispondente all'operazione di inserimento icona è la seguente:

![](1.png)

- Seleziona la posizione dell'icona da inserire nel foglio di lavoro
- Clicca sinistro su *Inserisci*->*Icone*
- Nella finestra che si apre, seleziona l'icona nel rettangolo rosso nella figura sopra
- Clic sinistro *Inserisci*, verrà inserito nel file Excel.

L'effetto è il seguente:

![](2.png)

Qui abbiamo preparato *codice di esempio* per aiutarti a inserire icone usando [Aspose.Cells](https://products.aspose.com/cells/). C'è anche un *file di esempio* necessario [sample.xlsx] e un [file di risorse] di icona [icon.zip]. Abbiamo usato l'interfaccia di Excel per inserire un'icona con lo stesso effetto di visualizzazione del [file di risorse](icon.zip) nel [file di esempio](sample.xlsx).

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Quando esegui il codice sopra nel tuo progetto, otterrai i seguenti risultati:

![](3.png)  

