---  
title: Symbole mit Node.js via C++ zum Arbeitsblatt hinzufügen  
linktitle: Symbole verwalten  
type: docs  
weight: 100  
url: /de/nodejs-cpp/insert-svg-to-excel/  
---  

## Symbole in Arbeitsblatt hinzufügen in Aspose.Cells for Node.js via C++

Wenn Sie [Aspose.Cells](https://products.aspose.com/cells/) verwenden müssen, um 'Symbole' in eine Excel-Datei hinzuzufügen, kann Ihnen dieses Dokument einige Hilfe bieten.

Die Excel-Benutzeroberfläche für die Einfüge-Symbol-Operation sieht wie folgt aus:

![](1.png)

- Wählen Sie die Position des Symbols, das in das Arbeitsblatt eingefügt werden soll
- Klicken Sie links auf *Einfügen*->*Symbole*
- In dem sich öffnenden Fenster wählen Sie das Symbol im roten Rechteck in der obigen Abbildung aus
- Linksklick *Einfügen*, es wird in die Excel-Datei eingefügt.

Der Effekt ist wie folgt:

![](2.png)

Hier haben wir *Beispiellcode* vorbereitet, um Ihnen beim Einfügen von Symbolen mit [Aspose.Cells](https://products.aspose.com/cells/) zu helfen. Es gibt auch eine notwendige [Beispiel-Datei](sample.xlsx) und eine Symbol [Ressourcendatei](icon.zip). Wir haben die Excel-Oberfläche benutzt, um ein Symbol mit dem gleichen Anzeigeeffekt wie die [Ressourcendatei](icon.zip) in der [Beispiel-Datei](sample.xlsx) einzufügen.

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

Wenn Sie den obigen Code in Ihrem Projekt ausführen, erhalten Sie die folgenden Ergebnisse:

![](3.png)  

