---
title: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine Node.js-via-Java-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild mithilfe zweier verschiedener Ansätze genau an die Größe einer einzelnen Zelle angepasst wird, durch Platzieren eines schwebenden Bildes über der Zelle oder durch direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Node.js-via-Java-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/nodejs-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die einen Zellenbereich visuell überlagert, während ein eingebettetes Bild innerhalb der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der Ihren Layout-Anforderungen am besten entspricht.

{{% /alert %}}

## **Einführung**

Das genaue Anpassen eines Bildes an eine einzelne Zelle ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu spannen oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der ihm zugeordneten Zelle ausgerichtet bleibt.

Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:

- **Ansatz 1 — Platzieren Sie ein schwebendes Bild über einer Zelle.** Fügen Sie dem Arbeitsblatt eine `Picture` hinzu, setzen Sie deren `Placement` auf `MoveAndSize`, und passen Sie die Ankerzellen (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Betten Sie ein Bild direkt in eine Zelle ein.** Weisen Sie Bild-Bytes der Eigenschaft `EmbeddedImage` der Zelle zu. Das Bild wird automatisch skaliert, um in den Anzeigebereich der Zelle zu passen, und wandert mit der Zelle mit.

Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Platzieren eines Bildes über einer Zelle**

Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellenbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.

Um ein schwebendes Bild so zu platzieren, dass es **genau eine Zelle** abdeckt, müssen Sie:

1. Fügen Sie das Bild mit `worksheet.getPictures().add(int row, int column, InputStream stream)` hinzu, wodurch das neue Bild an der angegebenen Zelle verankert wird.
2. Legen Sie die vier Anker-Eigenschaften so fest, dass das umschließende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. Setzen Sie `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`, damit sich das Bild mit der darunter liegenden Zelle mitbewegt und seine Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Verankerung des Bildes an einer einzelnen Zelle**

Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:

- `picture.setUpperLeftRow(int)` — der Zeilenindex der Oberkante des Bildes.
- `picture.setUpperLeftColumn(int)` — der Spaltenindex der linken Kante des Bildes.
- `picture.setLowerRightRow(int)` — der Zeilenindex der Unterkante des Bildes. Damit die Unterkante des Bildes am unteren Rand der Zeile `r` sitzt, setzen Sie diesen auf `r + 1`.
- `picture.setLowerRightColumn(int)` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` sitzt, setzen Sie diesen auf `c + 1`.

Um das Bild beispielsweise genau in Zelle **C6** (Zeilenindex `5`, Spaltenindex `2`) einzupassen, setzen Sie `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` und `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

{{% /alert %}}

### **Steuerung des Platzierungsverhaltens**

`Picture.Placement` ist eine Enumeration vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die Zeile oder Spalte darunter in der Größe ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MoveAndSize`, wodurch sich das Bild gemeinsam mit der darunter liegenden Zelle bewegt und seine Größe ändert, sodass die genaue Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen `InputStream` (beispielsweise unter Verwendung von `FileInputStream`), damit der Stream ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.getPictures().add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Legen Sie die vier Anker-Koordinaten so fest, dass das Bild nur Zelle C6 abdeckt: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Setzen Sie `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe geändert wird.
7. Optional können Sie Beispieltext in umliegende Zellen einfügen, um zu zeigen, dass nur Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den vollständigen Ansatz.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Ansatz 2: Direktes Einbetten eines Bildes in eine Zelle**

Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `Cell.EmbeddedImage`. Durch Zuweisen von Bild-Bytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Funktionsweise eingebetteter Bilder**

- Das Bild wird als Teil des Zellinhalts und nicht als Form auf der Zeichnungsebene gespeichert.
- Das Bild wird automatisch skaliert, um in die gerenderten Grenzen der Zelle zu passen. Es sind keine Anker-Koordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die durch Formeln referenziert, als Teil einer Zeile sortiert oder in anderen zellenbezogenen Operationen verwendet werden kann.

Dies macht `Cell.EmbeddedImage` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein Byte-Array ein (beispielsweise unter Verwendung von `Files.readAllBytes` aus `java.nio.file.Files`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.getCells().get("C6")` oder `worksheet.getCells().get(5, 2)`.
5. Weisen Sie das Byte-Array der Eigenschaft `EmbeddedImage` der Zelle über `cell.setEmbeddedImage(bytes)` zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den vollständigen Ansatz.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Die Zielzelle C6 abrufen
var cell = worksheet.getCells().get("C6");

// Die Bilddatei in ein Byte-Array einlesen
var imageData = fs.readFileSync("logo.png");

// Das Bild direkt in die Zelle einbetten
cell.setEmbeddedImage(imageData);

// Optional die Zeilenhöhe und Spaltenbreite anpassen, damit das eingebettete Bild besser sichtbar ist
worksheet.getCells().setColumnWidth(2, 30);   // Spalte C (Index 2)
worksheet.getCells().setRowHeight(5, 100);     // Zeile 6 (Index 5)

// Die resultierende Arbeitsmappe als .xlsx-Datei speichern
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Den richtigen Ansatz wählen**

Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:

- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Steuerung der Platzierung, der Schichtung oder der Ausrichtung an anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild als Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Anker-Koordinaten dynamisch basierend auf dem Arbeitsblatt-Layout berechnen müssen.

- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie das einfachstmögliche Einfügen eines Bildes in eine Zelle wünschen.
  - Das Bild wie jeder andere Zellinhalt mit der Zelle mitwandern soll.
  - Sie das Bild nicht als Form manipulieren müssen.

{{% alert color="primary" %}}

Beide Ansätze können in derselben Arbeitsmappe koexistieren. Sie können schwebende Bilder über einem Satz von Zellen platzieren und Bilder direkt in andere Zellen einbetten, da die beiden Mechanismen unterschiedliche Speicherebenen in der Datei verwenden.

{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}