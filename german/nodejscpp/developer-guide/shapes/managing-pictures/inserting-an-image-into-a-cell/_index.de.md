---
title: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine Node.js-via-C++-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild genau an die Größe einer einzelnen Zelle angepasst werden kann, indem zwei verschiedene Ansätze verwendet werden, Platzieren eines schwebenden Bildes über der Zelle oder direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Node.js-via-C++-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/nodejs-cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die einen Zellbereich visuell überlagert, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und automatisch an den Anzeigebereich der Zelle skaliert wird. Wählen Sie den Ansatz, der am besten zu Ihren Layoutanforderungen passt.

{{% /alert %}}

## **Einführung**

Das genaue Anpassen eines Bildes an eine einzelne Zelle ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu spannen oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der Zelle, der es gehört, ausgerichtet bleibt.

Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:

- **Ansatz 1 — Platzieren eines schwebenden Bildes über einer Zelle.** Fügen Sie dem Arbeitsblatt ein `Picture` hinzu, setzen Sie dessen `placement` auf `MoveAndSize` und passen Sie seine Ankerzellen (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Direktes Einbetten eines Bildes in eine Zelle.** Weisen Sie der Eigenschaft `embeddedImage` der Zelle Bild-Bytes zu. Das Bild wird automatisch skaliert, um in den Anzeigebereich der Zelle zu passen, und bewegt sich mit der Zelle mit.

Der Rest dieses Artikels führt durch beide Ansätze, erklärt die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Platzieren eines Bildes über einer Zelle**

Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.

Um ein schwebendes Bild genau **eine Zelle** abdecken zu lassen, müssen Sie:

1. Fügen Sie das Bild mit `worksheet.pictures.add(row, column, stream)` hinzu, wodurch das neue Bild an die angegebene Zelle verankert wird.
2. Legen Sie die vier Anker-Eigenschaften so fest, dass das umgebende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. Setzen Sie `picture.placement` auf `PlacementType.MoveAndSize`, damit sich das Bild mit der darunterliegenden Zelle mitbewegt und in der Größe anpasst, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Verankerung des Bildes an einer einzelnen Zelle**

Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:

- `picture.upperLeftRow` — der Zeilenindex der oberen Kante des Bildes.
- `picture.upperLeftColumn` — der Spaltenindex der linken Kante des Bildes.
- `picture.lowerRightRow` — der Zeilenindex der unteren Kante des Bildes. Damit die untere Kante des Bildes am unteren Rand der Zeile `r` sitzt, setzen Sie diesen auf `r + 1`.
- `picture.lowerRightColumn` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` sitzt, setzen Sie diesen auf `c + 1`.

Um das Bild beispielsweise genau in die Zelle **C6** (Zeilenindex `5`, Spaltenindex `2`) einzupassen, setzen Sie `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6` und `lowerRightColumn = 3`.

{{% alert color="primary" %}}

Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

{{% /alert %}}

### **Steuerung des Platzierungsverhaltens**

`picture.placement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die darunterliegende Zeile oder Spalte in der Größe ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MoveAndSize`, wodurch sich das Bild zusammen mit seiner darunterliegenden Zelle bewegt und in der Größe anpasst, sodass die exakte Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie über `workbook.worksheets[0]` auf das Ziel-`Worksheet` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen Stream und stellen Sie sicher, dass der Stream nach der Verwendung ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.pictures.add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Legen Sie die vier Ankerkoordinaten so fest, dass das Bild nur Zelle C6 abdeckt: `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Setzen Sie `picture.placement = PlacementType.MoveAndSize`, damit das Bild bei Größenänderungen der Spalte oder Zeile an C6 ausgerichtet bleibt.
7. Optional können Sie Beispieltext in umliegende Zellen einfügen, um zu zeigen, dass nur Zelle C6 das Bild enthält.
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

## **Ansatz 2: Direktes Einbetten eines Bildes in eine Zelle**

Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `cell.embeddedImage`. Durch Zuweisen von Bild-Bytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Wie eingebettete Bilder funktionieren**

- Das Bild wird als Teil des Zellinhalts gespeichert, nicht als Form auf der Zeichnungsebene.
- Das Bild wird automatisch skaliert, um in die gerenderten Grenzen der Zelle zu passen. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die durch Formeln referenziert, als Teil einer Zeile sortiert oder in anderen Operationen auf Zellebene verwendet werden kann.

Dies macht `cell.embeddedImage` zur prägnantesten Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie über `workbook.worksheets[0]` auf das Ziel-`Worksheet` zu.
3. Lesen Sie die Bilddatei von der Festplatte in einen Buffer oder ein Byte-Array mit Node.js-Dateisystem-APIs (zum Beispiel `fs.readFileSync`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.cells["C6"]` oder `worksheet.cells[5, 2]`.
5. Weisen Sie das Byte-Array der Eigenschaft `embeddedImage` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Ziel-Zeile und -Spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den vollständigen Ansatz.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Holen Sie sich die Zielzelle C6
var cell = worksheet.getCells().get("C6");

// Lesen Sie die Bilddatei in ein Byte-Array ein
var imageData = fs.readFileSync("logo.png");

// Bettet das Bild direkt in die Zelle ein
cell.setEmbeddedImage(imageData);

// Optional kann die Zeilenhöhe und Spaltenbreite angepasst werden, damit das eingebettete Bild besser sichtbar ist
worksheet.getCells().setColumnWidth(2, 30);   // Spalte C (Index 2)
worksheet.getCells().setRowHeight(5, 100);     // Zeile 6 (Index 5)

// Speichern Sie die resultierende Arbeitsmappe als .xlsx-Datei
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Den richtigen Ansatz wählen**

Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:

- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Kontrolle über Platzierung, Schichtung oder Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild als Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit der Bildersammlung funktioniert.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.

- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie die einfachstmögliche Einfügung eines Bildes in eine Zelle wünschen.
  - Das Bild sich wie jeder andere Zellinhalt mit der Zelle mitbewegen soll.
  - Sie das Bild nicht als Form bearbeiten müssen.

{{% alert color="primary" %}}

Beide Ansätze können in derselben Arbeitsmappe nebeneinander bestehen. Sie können schwebende Bilder über einer Reihe von Zellen platzieren und Bilder direkt in andere Zellen einbetten, da die beiden Mechanismen unterschiedliche Speicherebenen in der Datei verwenden.

{{% /alert %}}

## **Verwandte Artikel**

- [So fügen Sie ein Bild in eine Zelle ein](/cells/de/nodejs-cpp/how-to-place-image-to-cell/)
- [Bild-Hyperlinks hinzufügen](/cells/de/nodejs-cpp/add-image-hyperlinks/)
- [Laden eines Web-Bildes von einer URL in ein Excel-Arbeitsblatt](/cells/de/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Position, Größe und Designer-Diagramm bearbeiten](/cells/de/nodejs-cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="javascript" >}}