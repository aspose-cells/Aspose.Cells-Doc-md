---
title: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild mithilfe zweier verschiedener Ansätze exakt an die Größe einer einzelnen Zelle angepasst werden kann: Platzieren eines schwebenden Bildes über der Zelle oder direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, NET-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die einen Zellbereich visuell überlagert, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layoutanforderungen passt.

{{% /alert %}}

## **Einführung**

Das exakte Anpassen eines Bildes an eine einzelne Zelle ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Bestandslisten dienen. Anstatt ein Bild über viele Zellen zu strecken oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der ihm gehörenden Zelle ausgerichtet bleibt.

Aspose.Cells unterstützt dieses Szenario auf zwei sich ergänzende Arten:

- **Ansatz 1 — Platzieren eines schwebenden Bildes über einer Zelle.** Fügen Sie ein `Picture` zum Arbeitsblatt hinzu, setzen Sie dessen `Placement` auf `MoveAndSize` und passen Sie die Ankerzellen (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Direktes Einbetten eines Bildes in eine Zelle.** Weisen Sie Bild-Bytes der Eigenschaft `EmbeddedImage` der Zelle zu. Das Bild skaliert automatisch, um in den Anzeigebereich der Zelle zu passen, und wandert mit der Zelle mit.

Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Platzieren eines Bildes über einer Zelle**

Ein schwebendes Bild ist ein `Picture`-Objekt, das auf der Zeichnungsebene des Arbeitsblatts lebt. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.

Um ein schwebendes Bild genau **eine Zelle** abdecken zu lassen, müssen Sie:

1. Das Bild mit `Worksheet.Pictures.Add(int row, int column, Stream stream)` hinzufügen, wodurch das neue Bild an die angegebene Zelle verankert wird.
2. Die vier Ankereigenschaften so setzen, dass das Begrenzungsrechteck des Bildes mit der Zielzelle übereinstimmt.
3. `Picture.Placement` auf `PlacementType.MoveAndSize` setzen, damit das Bild zusammen mit der darunterliegenden Zelle verschoben und in der Größe verändert wird, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Verankern des Bildes an einer einzelnen Zelle**

Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:

- `Picture.UpperLeftRow` — der Zeilenindex der oberen Kante des Bildes.
- `Picture.UpperLeftColumn` — der Spaltenindex der linken Kante des Bildes.
- `Picture.LowerRightRow` — der Zeilenindex der unteren Kante des Bildes. Damit die untere Kante des Bildes am unteren Rand der Zeile `r` sitzt, setzen Sie diesen auf `r + 1`.
- `Picture.LowerRightColumn` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` sitzt, setzen Sie diesen auf `c + 1`.

Um beispielsweise das Bild genau in die Zelle **C6** (Zeilenindex `5`, Spaltenindex `2`) einzupassen, setzen Sie `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` und `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache dafür, dass Bilder in eine benachbarte Zelle hinein überzulappen scheinen.

{{% /alert %}}

### **Steuern des Platzierungsverhaltens**

`Picture.Placement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die darunterliegende Zeile oder Spalte in der Größe ändert. Der empfohlene Wert für ein einzelnes Zellbild ist `PlacementType.MoveAndSize`, wodurch das Bild zusammen mit seiner darunterliegenden Zelle verschoben und in der Größe verändert wird, wobei die exakte Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.Worksheets[0]` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen `FileStream` mithilfe eines `using`-Blocks, sodass der Stream ordnungsgemäß freigegeben wird.
4. Rufen Sie `worksheet.Pictures.Add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Speichern Sie die zurückgegebene `Picture`-Referenz.
5. Setzen Sie die vier Ankerkoordinaten so, dass das Bild nur die Zelle C6 abdeckt: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Setzen Sie `picture.Placement = PlacementType.MoveAndSize`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe verändert wird.
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

## **Ansatz 2: Direktes Einbetten eines Bildes in eine Zelle**

Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `Cell.EmbeddedImage`. Durch Zuweisen von Bild-Bytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Wie eingebettete Bilder funktionieren**

- Das Bild wird als Teil des Zellinhalts gespeichert, nicht als Form auf der Zeichnungsebene.
- Das Bild skaliert automatisch, um in die gerenderten Grenzen der Zelle zu passen. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen zellbezogenen Operationen verwendet werden kann.

Dies macht `Cell.EmbeddedImage` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.Worksheets[0]` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `byte[]`-Array (zum Beispiel mit `File.ReadAllBytes`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.Cells["C6"]` oder `worksheet.Cells[5, 2]`.
5. Weisen Sie das Byte-Array der Eigenschaft `EmbeddedImage` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielreihe und -spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den vollständigen Ansatz.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Zielzelle C6 abrufen
var cell = worksheet.Cells["C6"];

// Bilddatei in ein Byte-Array einlesen
byte[] imageData = File.ReadAllBytes("logo.png");

// Bild direkt in die Zelle einbetten
cell.EmbeddedImage = imageData;

// Optional Zeilenhöhe und Spaltenbreite anpassen, damit das eingebettete Bild besser sichtbar ist
worksheet.Cells.SetColumnWidth(2, 30);   // Spalte C (Index 2)
worksheet.Cells.SetRowHeight(5, 100);     // Zeile 6 (Index 5)

// Die resultierende Arbeitsmappe als .xlsx-Datei speichern
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Den richtigen Ansatz wählen**

Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:

- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Steuerung der Platzierung, der Schichtung oder der Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild als Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.

- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie das einfachstmögliche Einfügen eines Bildes in eine Zelle wünschen.
  - Das Bild mit der Zelle wie jeder andere Zelleninhalt mitwandern soll.
  - Sie das Bild nicht als Form manipulieren müssen.

{{% alert color="primary" %}}

Beide Ansätze können in derselben Arbeitsmappe koexistieren. Sie können schwebende Bilder über einer Reihe von Zellen platzieren und Bilder direkt in andere Zellen einbetten, da die beiden Mechanismen unterschiedliche Speicherebenen in der Datei verwenden.

{{% /alert %}}

## **Verwandte Artikel**

- [How to Insert Picture in Cell](/cells/de/net/how-to-place-image-to-cell/)
- [How to Fit Image to Cell Width and Height](/cells/de/net/how-to-fit-image-to-cell-width-height/)
- [Add Image Hyperlinks](/cells/de/net/add-image-hyperlinks/)
- [Load a Web Image from a URL into an Excel Worksheet](/cells/de/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipulate Position Size and Designer Chart](/cells/de/net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="csharp" >}}