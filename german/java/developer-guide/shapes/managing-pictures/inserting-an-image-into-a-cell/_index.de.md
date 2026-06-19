---
title: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine Java-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild mithilfe zweier verschiedener Ansätze genau an die Größe einer einzelnen Zelle angepasst werden kann: Platzieren eines schwebenden Bildes über der Zelle oder direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die visuell über einem Zellbereich liegt, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.

{{% /alert %}}

## **Einführung**

Ein Bild genau an eine einzelne Zelle anzupassen, ist eine häufige Anforderung beim Erstellen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu strecken oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der ihm zugeordneten Zelle ausgerichtet bleibt.

Aspose.Cells unterstützt dieses Szenario auf zwei sich ergänzende Weisen:

- **Ansatz 1 — Platzieren eines schwebenden Bildes über einer Zelle.** Fügen Sie dem Arbeitsblatt ein `Picture` hinzu, setzen Sie dessen `Placement` auf `MOVE_AND_SIZE`, und passen Sie dessen Ankerzellen (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Direktes Einbetten eines Bildes in eine Zelle.** Weisen Sie Bildbytes dem `getEmbeddedImage()`-Setter der Zelle zu. Das Bild wird automatisch skaliert, um in den Anzeigebereich der Zelle zu passen, und bewegt sich mit der Zelle mit.

Im weiteren Verlauf dieses Artikels werden beide Ansätze erläutert, die relevanten APIs erklärt und deren Verwendung im Code gezeigt.

## **Ansatz 1: Platzieren eines Bildes über einer Zelle**

Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen dessen visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.

Um ein schwebendes Bild so zu platzieren, dass es **genau eine Zelle** abdeckt, müssen Sie:

1. Das Bild mit `Worksheet.getPictures().add(int row, int column, InputStream stream)` hinzufügen, wodurch das neue Bild an der angegebenen Zelle verankert wird.
2. Die vier Anker-Eigenschaften so setzen, dass das umschließende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. `Picture.setPlacement()` auf `PlacementType.MOVE_AND_SIZE` setzen, sodass das Bild sich mit der darunter liegenden Zelle mitbewegt und in der Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Verankerung des Bildes an einer einzelnen Zelle**

Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:

- `Picture.getUpperLeftRow()` — der Zeilenindex der oberen Kante des Bildes.
- `Picture.getUpperLeftColumn()` — der Spaltenindex der linken Kante des Bildes.
- `Picture.getLowerRightRow()` — der Zeilenindex der unteren Kante des Bildes. Damit die untere Kante des Bildes am unteren Rand der Zeile `r` liegt, setzen Sie diesen Wert auf `r + 1`.
- `Picture.getLowerRightColumn()` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` liegt, setzen Sie diesen Wert auf `c + 1`.

Um das Bild beispielsweise genau in die Zelle **C6** (Zeilenindex `5`, Spaltenindex `2`) einzupassen, setzen Sie `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` und `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Die Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

{{% /alert %}}

### **Steuerung des Platzierungsverhaltens**

`Picture.getPlacement()` gibt eine Enumeration vom Typ `PlacementType` zurück, die steuert, wie sich das Bild verhält, wenn der Benutzer die darunter liegende Zeile oder Spalte in der Größe ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MOVE_AND_SIZE`, wodurch das Bild gemeinsam mit seiner darunter liegenden Zelle verschoben und in der Größe geändert wird, sodass die genaue Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen `InputStream` (z. B. einen `FileInputStream`) mithilfe eines try-with-resources-Blocks, damit der Stream ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.getPictures().add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Speichern Sie die zurückgegebene `Picture`-Referenz.
5. Setzen Sie die vier Anker-Koordinaten so, dass das Bild nur die Zelle C6 abdeckt: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Setzen Sie `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe geändert wird.
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

## **Ansatz 2: Direktes Einbetten eines Bildes in eine Zelle**

Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Methode `Cell.setEmbeddedImage(byte[])`. Durch Zuweisen von Bildbytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Funktionsweise eingebetteter Bilder**

- Das Bild wird als Teil des Zellinhalts gespeichert und nicht als Form auf der Zeichnungsebene.
- Das Bild wird automatisch skaliert, um in den Anzeigebereich der Zelle zu passen. Es sind keine Anker-Koordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen zellbezogenen Operationen verwendet werden kann.

Dies macht `setEmbeddedImage()` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das sich innerhalb dieser Zelle befindet" ist.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `byte[]`-Array ein (z. B. durch Lesen der Datei über `Files.readAllBytes()` aus `java.nio.file`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.getCells().get("C6")` oder `worksheet.getCells().get(5, 2)`.
5. Weisen Sie das Byte-Array der Zelle mit `cell.setEmbeddedImage(bytes)` zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte an, um dem eingebetteten Bild ein auffälligeres Erscheinungsbild zu verleihen.
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

// Die Bilddatei in ein Byte-Array lesen
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

Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch in der Art, wie das Bild gespeichert wird und wie es sich verhält:

- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Steuerung der Platzierung, der Schichtung oder der Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild wie eine Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Anker-Koordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.

- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie das einfachstmögliche Einfügen eines Bildes in eine Zelle wünschen.
  - Das Bild sich wie jeder andere Zellinhalt mit der Zelle mitbewegen soll.
  - Sie das Bild nicht als Form bearbeiten müssen.

{{% alert color="primary" %}}

Beide Ansätze können in derselben Arbeitsmappe koexistieren. Sie können schwebende Bilder über einer Reihe von Zellen platzieren und Bilder direkt in andere Zellen einbetten, da die beiden Mechanismen unterschiedliche Speicherebenen in der Datei verwenden.

{{% /alert %}}



{{< app/cells/assistant language="java" >}}