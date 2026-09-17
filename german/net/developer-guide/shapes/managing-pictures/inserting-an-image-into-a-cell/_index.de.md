---
title: Einfügen eines Bildes in eine Zelle
linktitle: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild exakt an eine einzelne Zelle angepasst wird, entweder durch Platzieren eines schwebenden Bildes über der Zelle oder durch direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, NET-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet zwei verschiedene Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichenebene des Arbeitsblatts, die einen Zellbereich visuell überlagert, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und automatisch auf den Anzeigebereich der Zelle skaliert wird. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.

## **Einführung**
Das exakte Anpassen eines Bildes an eine einzelne Zelle ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über mehrere Zellen auszudehnen oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der besitzenden Zelle ausgerichtet bleibt.
Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:
- **Ansatz 1 — Ein schwebendes Bild über einer Zelle platzieren.** Fügen Sie ein `Picture` zum Arbeitsblatt hinzu, setzen Sie dessen `Placement` auf `MoveAndSize`, und passen Sie die Ankerzellen (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Ein Bild direkt in eine Zelle einbetten.** Weisen Sie Bild-Bytes der Eigenschaft `EmbeddedImage` der Zelle zu. Das Bild skaliert automatisch, um in den Anzeigebereich der Zelle zu passen, und wandert mit der Zelle mit.
Im weiteren Verlauf dieses Artikels werden beide Ansätze behandelt, die relevanten APIs erklärt und ihre Verwendung im Code gezeigt.

## **Ansatz 1: Ein Bild über einer Zelle platzieren**
Ein schwebendes Bild ist ein `Picture`-Objekt, das auf der Zeichenebene des Arbeitsblatts lebt. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.
Um ein schwebendes Bild genau **eine Zelle** abdecken zu lassen, müssen Sie:
1. Das Bild mit `Worksheet.Pictures.Add(int row, int column, Stream stream)` hinzufügen, was das neue Bild an die angegebene Zelle verankert.
2. Die vier Anker-Eigenschaften so setzen, dass das umschließende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. `Picture.Placement` auf `PlacementType.MoveAndSize` setzen, damit sich das Bild mit der darunter liegenden Zelle bewegt und seine Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Das Bild an einer einzelnen Zelle verankern**
Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:
- `Picture.UpperLeftRow` — der Zeilenindex der Oberkante des Bildes.
- `Picture.UpperLeftColumn` — der Spaltenindex der linken Kante des Bildes.
- `Picture.LowerRightRow` — der Zeilenindex der Unterkante des Bildes. Damit die untere Kante des Bildes am unteren Rand der Zeile `r` sitzt, setzen Sie diesen auf `r + 1`.
- `Picture.LowerRightColumn` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` sitzt, setzen Sie diesen auf `c + 1`.

{{% alert color="primary" %}}
Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle überlaufen.

### **Platzierungsverhalten steuern**
`Picture.Placement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die Größe der darunter liegenden Zeile oder Spalte ändert. Der empfohlene Wert für ein einzelnes Zellenbild ist `PlacementType.MoveAndSize`, wodurch sich das Bild zusammen mit seiner darunter liegenden Zelle bewegt und seine Größe ändert, wobei die exakte Passform erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.Worksheets[0]` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen `FileStream` mit einem `using`-Block, damit der Stream ordnungsgemäß freigegeben wird.
4. Rufen Sie `worksheet.Pictures.Add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Setzen Sie die vier Ankerkoordinaten so, dass das Bild nur Zelle C6 abdeckt: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Setzen Sie `picture.Placement = PlacementType.MoveAndSize`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spaltenbreite oder Zeilenhöhe geändert wird.
7. Optional können Sie Beispieltext in umliegende Zellen einfügen, um zu zeigen, dass nur Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Ansatz 2: Ein Bild direkt in eine Zelle einbetten**
Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `Cell.EmbeddedImage`. Das Zuweisen von Bild-Bytes zu dieser Eigenschaft bindet das Bild an die Zelle selbst, als wäre es Inline-Inhalt.

### **Wie eingebettete Bilder funktionieren**
- Das Bild wird als Teil des Zellinhalts gespeichert und nicht als Form auf der Zeichenebene.
- Das Bild skaliert automatisch, um in die gerenderten Grenzen der Zelle zu passen. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen Operationen auf Zellebene verwendet werden kann.
Dies macht `Cell.EmbeddedImage` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.Worksheets[0]` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `byte[]`-Array (zum Beispiel mit `File.ReadAllBytes`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.Cells["C6"]` oder `worksheet.Cells[5, 2]`.
5. Weisen Sie das Byte-Array der Eigenschaft `EmbeddedImage` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Ziel-Zeile und -Spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Holen Sie sich die Zielzelle C6
var cell = worksheet.Cells["C6"];
// Lesen Sie die Bilddatei in ein Byte-Array ein
byte[] imageData = File.ReadAllBytes("logo.png");
// Betten Sie das Bild direkt in die Zelle ein
cell.EmbeddedImage = imageData;
// Passen Sie optional die Zeilenhöhe und Spaltenbreite an, damit das eingebettete Bild besser sichtbar ist
worksheet.Cells.SetColumnWidth(2, 30);   // Spalte C (Index 2)
worksheet.Cells.SetRowHeight(5, 100);     // Zeile 6 (Index 5)
// Speichern Sie die resultierende Arbeitsmappe als .xlsx-Datei
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Den richtigen Ansatz wählen**
Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:
- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Kontrolle über Platzierung, Schichtung oder Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild als Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.
- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie das einfachstmögliche Einfügen eines Bildes in eine Zelle wünschen.
  - Das Bild mit der Zelle wie jeder andere Zellinhalt mitwandern soll.
  - Sie das Bild nicht als Form manipulieren müssen.
{{% /alert %}}

{{% /alert %}}

## Verwandte Artikel
- [Excel-Kamera in Aspose.Cells for .NET](/cells/de/net/excel-camera/)
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for .NET hinzufügen](/cells/de/net/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for .NET anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Seitenfeldlayout in der Pivot-Tabelle ändern](/cells/de/net/change-page-field-layout/)
- [Sparkline in Bild und HTML in Aspose.Cells for .NET konvertieren](/cells/de/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}