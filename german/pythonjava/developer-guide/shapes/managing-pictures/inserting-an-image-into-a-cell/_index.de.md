---
title: Einfügen eines Bildes in eine Zelle
linktitle: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells for Python via Java ist eine Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild genau in eine einzelne Zelle eingefügt wird, entweder durch Platzieren eines schwebenden Bildes über der Zelle oder durch direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Python via Java Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die einen Zellbereich visuell überlagert, während ein eingebettetes Bild innerhalb der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.
{{% /alert %}}

## **Einführung**
Das exakte Anpassen eines Bildes an eine einzelne Zelle ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu spannen oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der ihm gehörenden Zelle ausgerichtet bleibt.
Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:
- **Ansatz 1 — Platzieren eines schwebenden Bildes über einer Zelle.** Fügen Sie dem Arbeitsblatt ein `Picture` hinzu, setzen Sie dessen `setPlacement` auf `MOVE_AND_SIZE` und passen Sie dessen Ankerzellen (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Direktes Einbetten eines Bildes in eine Zelle.** Weisen Sie der Eigenschaft `setEmbeddedImage` der Zelle Bildbytes zu. Das Bild skaliert automatisch, um in den Anzeigebereich der Zelle zu passen, und wandert mit der Zelle mit.
Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code eingesetzt werden.

## **Ansatz 1: Bild über einer Zelle platzieren**
Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.
Damit ein schwebendes Bild **genau eine Zelle** abdeckt, müssen Sie:
1. Das Bild mit `Worksheet.getPictures().add(int row, int column, InputStream stream)` hinzufügen, wodurch das neue Bild an der angegebenen Zelle verankert wird.
2. Die vier Ankereigenschaften so setzen, dass das umgebende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. `Picture.setPlacement` auf `PlacementType.MOVE_AND_SIZE` setzen, damit das Bild mit der darunterliegenden Zelle verschoben und in der Größe verändert wird, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Das Bild an einer einzelnen Zelle verankern**
Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:
- `setUpperLeftRow` — der Zeilenindex der oberen Kante des Bildes.
- `setUpperLeftColumn` — der Spaltenindex der linken Kante des Bildes.
- `setLowerRightRow` — der Zeilenindex der unteren Kante des Bildes. Damit die untere Kante des Bildes am unteren Rand der Zeile `r` liegt, setzen Sie diesen Wert auf `r + 1`.
- `setLowerRightColumn` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` liegt, setzen Sie diesen Wert auf `c + 1`.

{{% alert color="primary" %}}
Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

### **Platzierungsverhalten steuern**
`getPlacement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die darunterliegende Zeile oder Spalte in der Größe ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MOVE_AND_SIZE`, wodurch das Bild zusammen mit seiner darunterliegenden Zelle verschoben und in der Größe verändert wird, sodass die exakte Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen `InputStream` (typischerweise ein `FileInputStream`), damit der Stream ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.getPictures().add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Setzen Sie die vier Ankerkoordinaten so, dass das Bild nur Zelle C6 abdeckt: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Setzen Sie `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`, damit das Bild an C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe verändert wird.
7. Optional können Sie Beispieltext zu umgebenden Zellen hinzufügen, um zu zeigen, dass nur Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Ansatz 2: Bild direkt in eine Zelle einbetten**
Aspose.Cells stellt außerdem einen einfacheren Mechanismus für zellgebundene Bilder bereit: die Eigenschaft `Cell.setEmbeddedImage`. Durch Zuweisen von Bildbytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Wie eingebettete Bilder funktionieren**
- Das Bild wird als Teil des Zellinhalts gespeichert, nicht als Form auf der Zeichnungsebene.
- Das Bild skaliert automatisch so, dass es in die gerenderten Grenzen der Zelle passt. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, auf die durch Formeln verwiesen werden kann, die als Teil einer Zeile sortiert werden kann oder die in anderen zellenbezogenen Operationen verwendet werden kann.
Dies macht `Cell.setEmbeddedImage` zur knappsten Option, wenn Ihr Ziel einfach „ein Bild, das innerhalb dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `byte[]`-Array (zum Beispiel durch Verwendung eines `Files.readAllBytes`-Aufrufs aus `java.nio.file.Files`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.getCells().get("C6")` oder `worksheet.getCells().get(5, 2)`.
5. Weisen Sie das Byte-Array der Eigenschaft `setEmbeddedImage` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Den richtigen Ansatz wählen**
Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:
- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Steuerung der Platzierung, der Schichtung oder der Ausrichtung an anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass das Bild als Form fungiert, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.
- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie die einfachstmögliche Einfügung eines Bildes in eine Zelle wünschen.
  - Das Bild wie jeder andere Zelleninhalt mit der Zelle mitwandern soll.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}