---
title: Einfügen eines Bildes in eine Zelle
linktitle: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine Java-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie Sie ein Bild exakt an eine einzelne Zelle anpassen, indem Sie entweder ein schwebendes Bild über der Zelle platzieren oder das Bild direkt in die Zelle einbetten.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet zwei verschiedene Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichenebene des Arbeitsblatts, die einen Zellbereich visuell überlagert, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.

## **Einführung**
Ein Bild exakt an eine einzelne Zelle anzupassen ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu strecken oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der zugehörigen Zelle ausgerichtet bleibt.
Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:
- **Ansatz 1 — Platzieren Sie ein schwebendes Bild über einer Zelle.** Fügen Sie dem Arbeitsblatt ein `Picture` hinzu, setzen Sie dessen `Placement` auf `MOVE_AND_SIZE` und passen Sie die Ankerzellen (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Betten Sie ein Bild direkt in eine Zelle ein.** Weisen Sie Bildbytes dem Setter `getEmbeddedImage()` der Zelle zu. Das Bild wird automatisch skaliert, um in den Anzeigebereich der Zelle zu passen, und bewegt sich mit der Zelle mit.
Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Bild über einer Zelle platzieren**
Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichenebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.
Um ein schwebendes Bild genau **eine Zelle** abdecken zu lassen, müssen Sie:
1. Fügen Sie das Bild mit `Worksheet.getPictures().add(int row, int column, InputStream stream)` hinzu, wodurch das neue Bild an die angegebene Zelle verankert wird.
2. Setzen Sie die vier Anker-Eigenschaften so, dass das Begrenzungsrechteck des Bildes mit der Zielzelle übereinstimmt.
3. Setzen Sie `Picture.setPlacement()` auf `PlacementType.MOVE_AND_SIZE`, damit sich das Bild mit der zugrunde liegenden Zelle bewegt und in der Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Bild an einer einzelnen Zelle verankern**
Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:
- `Picture.getUpperLeftRow()` — der Zeilenindex der Oberkante des Bildes.
- `Picture.getUpperLeftColumn()` — der Spaltenindex der linken Kante des Bildes.
- `Picture.getLowerRightRow()` — der Zeilenindex der Unterkante des Bildes. Damit die Unterkante des Bildes am unteren Rand der Zeile `r` sitzt, setzen Sie diesen auf `r + 1`.
- `Picture.getLowerRightColumn()` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` sitzt, setzen Sie diesen auf `c + 1`.

{{% alert color="primary" %}}
Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Die Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

### **Platzierungsverhalten steuern**
`Picture.getPlacement()` gibt eine Enumeration vom Typ `PlacementType` zurück, die steuert, wie sich das Bild verhält, wenn der Benutzer die darunterliegende Zeile oder Spalte in der Größe ändert. Der empfohlene Wert für ein Einzelzellenbild ist `PlacementType.MOVE_AND_SIZE`, wodurch sich das Bild zusammen mit der zugrunde liegenden Zelle bewegt und in der Größe ändert, wodurch die exakte Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine bestehende).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einem `InputStream` (z. B. einem `FileInputStream`) unter Verwendung eines try-with-resources-Blocks, damit der Stream ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.getPictures().add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Setzen Sie die vier Ankerkoordinaten so, dass das Bild nur die Zelle C6 abdeckt: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Setzen Sie `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`, damit das Bild bei Größenänderungen der Spalte oder Zeile mit C6 ausgerichtet bleibt.
7. Optional können Sie Beispieltext in umliegende Zellen einfügen, um zu zeigen, dass nur die Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Ansatz 2: Bild direkt in einer Zelle einbetten**
Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Methode `Cell.setEmbeddedImage(byte[])`. Durch Zuweisen von Bildbytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Wie eingebettete Bilder funktionieren**
- Das Bild wird als Teil des Zellinhalts gespeichert und nicht als Form auf der Zeichenebene.
- Das Bild wird automatisch skaliert, um in die dargestellten Grenzen der Zelle zu passen. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen Zelloperationen verwendet werden kann.
Dies macht `setEmbeddedImage()` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine bestehende).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `byte[]`-Array (z. B. durch Lesen der Datei über `Files.readAllBytes()` aus `java.nio.file`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.getCells().get("C6")` oder `worksheet.getCells().get(5, 2)`.
5. Weisen Sie das Byte-Array mit `cell.setEmbeddedImage(bytes)` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Die Zielzelle C6 abrufen
Cell cell = worksheet.getCells().get("C6");
// Die Bilddatei in ein Byte-Array einlesen
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));
// Das Bild direkt in die Zelle einbetten
cell.setEmbeddedImage(imageData);
// Optional die Zeilenhöhe und Spaltenbreite anpassen, damit das eingebettete Bild besser sichtbar ist
worksheet.getCells().setColumnWidth(2, 30);   // Spalte C (Index 2)
worksheet.getCells().setRowHeight(5, 100);     // Zeile 6 (Index 5)
// Die resultierende Arbeitsmappe als .xlsx-Datei speichern
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Den richtigen Ansatz wählen**
Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, aber sie unterscheiden sich darin, wie das Bild gespeichert wird und wie es sich verhält:
- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Steuerung der Platzierung, Schichtung oder Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild wie eine Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.
- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie die einfachstmögliche Einfügung eines Bildes in eine Zelle wünschen.
  - Das Bild soll sich wie jeder andere Zellinhalt mit der Zelle bewegen.
  - Sie das Bild nicht als Form bearbeiten müssen.
{{% /alert %}}

{{% /alert %}}

## Verwandte Artikel
- [Excel-Kamera in Aspose.Cells for Java](/cells/de/java/excel-camera/)
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for Java hinzufügen](/cells/de/java/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for Java anwenden](/cells/de/java/apply-style-to-pivot-table/)
- [Seitenfeldlayout in einer Pivot-Tabelle ändern](/cells/de/java/change-page-field-layout/)
- [Sparkline in Bild und HTML in Aspose.Cells for Java konvertieren](/cells/de/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}