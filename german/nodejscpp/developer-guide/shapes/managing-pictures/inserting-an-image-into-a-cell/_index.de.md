---
title: Einfügen eines Bildes in eine Zelle
linktitle: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine Node.js via C++ Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild genau an eine einzelne Zelle angepasst werden kann, entweder durch Platzieren eines schwebenden Bildes über der Zelle oder durch direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Node.js via C++ Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/nodejs-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild einer einzelnen Zelle zuzuordnen. Ein schwebendes Bild ist eine Form auf der Zeichenebene des Arbeitsblatts, die einen Zellbereich visuell überlagert, während ein eingebettetes Bild innerhalb der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.
{{% /alert %}}

## **Introduction**
Das genaue Anpassen eines Bildes an eine einzelne Zelle ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu strecken oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der Zelle, der es gehört, ausgerichtet bleibt.
Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:
- **Ansatz 1 — Platzieren eines schwebenden Bildes über einer Zelle.** Fügen Sie dem Arbeitsblatt eine `Picture` hinzu, setzen Sie deren `placement` auf `MoveAndSize`, und passen Sie die Ankerzellen (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Direktes Einbetten eines Bildes in eine Zelle.** Weisen Sie Bild-Bytes der Eigenschaft `embeddedImage` der Zelle zu. Das Bild wird automatisch skaliert, um in den Anzeigebereich der Zelle zu passen, und wandert mit der Zelle mit.
Der Rest dieses Artikels führt durch beide Ansätze, erklärt die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Approach 1: Place a Picture Over a Cell**
Ein schwebendes Bild ist ein `Picture`-Objekt, das auf der Zeichenebene des Arbeitsblatts lebt. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen dessen visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.
Um ein schwebendes Bild genau **eine Zelle** abdecken zu lassen, müssen Sie:
1. Das Bild mit `worksheet.pictures.add(row, column, stream)` hinzufügen, was das neue Bild an die angegebene Zelle verankert.
2. Die vier Anker-Eigenschaften so setzen, dass das umschließende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. `picture.placement` auf `PlacementType.MoveAndSize` setzen, damit sich das Bild mit der darunter liegenden Zelle bewegt und seine Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Anchoring the Picture to a Single Cell**
Der Anker des Bildes wird durch vier nullbasierte Index-Eigenschaften definiert:
- `picture.upperLeftRow` — der Zeilenindex der Oberkante des Bildes.
- `picture.upperLeftColumn` — der Spaltenindex der linken Kante des Bildes.
- `picture.lowerRightRow` — der Zeilenindex der Unterkante des Bildes. Damit die Unterkante des Bildes am unteren Rand der Zeile `r` sitzt, setzen Sie dies auf `r + 1`.
- `picture.lowerRightColumn` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` sitzt, setzen Sie dies auf `c + 1`.

{{% alert color="primary" %}}
Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

### **Controlling Placement Behavior**
`picture.placement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die Zeile oder Spalte darunter in der Größe ändert. Der empfohlene Wert für ein Einzelzellbild ist `PlacementType.MoveAndSize`, was bewirkt, dass sich das Bild gemeinsam mit seiner darunter liegenden Zelle bewegt und seine Größe ändert und so die genaue Anpassung beibehält.

### **Step-by-Step Instructions**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.worksheets[0]` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen Stream und stellen Sie sicher, dass der Stream nach der Verwendung ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.pictures.add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Setzen Sie die vier Anker-Koordinaten so, dass das Bild nur die Zelle C6 abdeckt: `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Setzen Sie `picture.placement = PlacementType.MoveAndSize`, um das Bild an C6 ausgerichtet zu halten, wenn die Spalte oder Zeile in der Größe geändert wird.
7. Optional können Sie Beispieltext zu umgebenden Zellen hinzufügen, um zu zeigen, dass nur Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `cell.embeddedImage`. Durch das Zuweisen von Bild-Bytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **How Embedded Images Work**
- Das Bild wird als Teil des Zellinhalts gespeichert, nicht als Form auf der Zeichenebene.
- Das Bild wird automatisch skaliert, um in die gerenderten Grenzen der Zelle zu passen. Es sind keine Anker-Koordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen Zelloperationen verwendet werden kann.
Dies macht `cell.embeddedImage` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das innerhalb dieser Zelle lebt" ist.

### **Step-by-Step Instructions**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.worksheets[0]` zu.
3. Lesen Sie die Bilddatei mit Node.js-Dateisystem-APIs (zum Beispiel `fs.readFileSync`) von der Festplatte in einen Buffer oder ein Byte-Array.
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.cells["C6"]` oder `worksheet.cells[5, 2]`.
5. Weisen Sie das Byte-Array der Eigenschaft `embeddedImage` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und Zielspalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Get the target cell C6
var cell = worksheet.getCells().get("C6");
// Read the image file into a byte array
var imageData = fs.readFileSync("logo.png");
// Embed the image directly into the cell
cell.setEmbeddedImage(imageData);
// Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30);   // Column C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Row 6 (index 5)
// Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Choosing the Right Approach**
Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, aber sie unterscheiden sich darin, wie das Bild gespeichert wird und wie es sich verhält:
- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Kontrolle über Platzierung, Schichtung oder Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild als Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit der Bildersammlung arbeitet.
  - Sie Anker-Koordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.
- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie das einfachstmögliche Einfügen eines Bildes in eine Zelle wünschen.
  - Das Bild wie jeder andere Zellinhalt mit der Zelle mitwandern soll.
{{% /alert %}}

## Related Articles
- [Excel-Kamera in Aspose.Cells for Node.js via C++](/cells/de/nodejs-cpp/excel-camera/)
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for Node.js via C++ hinzufügen](/cells/de/nodejs-cpp/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for Node.js via C++ anwenden](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)
- [Seitenfeld-Layout in der Pivot-Tabelle ändern](/cells/de/nodejs-cpp/change-page-field-layout/)
- [Sparkline in Bild und HTML in Aspose.Cells for Node.js via C++ konvertieren](/cells/de/nodejs-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript" >}}