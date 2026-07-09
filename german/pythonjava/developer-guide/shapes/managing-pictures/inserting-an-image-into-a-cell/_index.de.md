---
title: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells for Python via Java ist eine Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild genau auf eine einzelne Zellengröße angepasst wird, und zwar mit zwei verschiedenen Ansätzen, Platzieren eines schwebenden Bildes über der Zelle oder direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Python via Java Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die visuell über einem Zellenbereich liegt, während ein eingebettetes Bild innerhalb der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.

{{% /alert %}}

## **Einführung**

Ein Bild genau an eine einzelne Zelle anzupassen, ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu spannen oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der zugehörigen Zelle ausgerichtet bleibt.

Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:

- **Ansatz 1 — Platzieren Sie ein schwebendes Bild über einer Zelle.** Fügen Sie dem Arbeitsblatt ein `Picture` hinzu, setzen Sie dessen `setPlacement` auf `MOVE_AND_SIZE` und passen Sie dessen Ankerzellen (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Betten Sie ein Bild direkt in eine Zelle ein.** Weisen Sie Bild-Bytes der Eigenschaft `setEmbeddedImage` der Zelle zu. Das Bild wird automatisch so skaliert, dass es in den Anzeigebereich der Zelle passt, und wandert mit der Zelle mit.

Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Platzieren eines Bildes über einer Zelle**

Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellenbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen sein visuelles Ausmaß auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.

Um ein schwebendes Bild so zu positionieren, dass es **genau eine Zelle** abdeckt, müssen Sie:

1. Fügen Sie das Bild mit `Worksheet.getPictures().add(int row, int column, InputStream stream)` hinzu, wodurch das neue Bild an die angegebene Zelle verankert wird.
2. Legen Sie die vier Anker-Eigenschaften so fest, dass das umschließende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. Setzen Sie `Picture.setPlacement` auf `PlacementType.MOVE_AND_SIZE`, damit sich das Bild zusammen mit der zugrunde liegenden Zelle bewegt und in der Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Verankern des Bildes an einer einzelnen Zelle**

Der Anker des Bildes wird durch vier nullbasierte Index-Eigenschaften definiert:

- `setUpperLeftRow` — der Zeilenindex der oberen Kante des Bildes.
- `setUpperLeftColumn` — der Spaltenindex der linken Kante des Bildes.
- `setLowerRightRow` — der Zeilenindex der unteren Kante des Bildes. Um die untere Kante des Bildes an der Unterseite der Zeile `r` zu platzieren, setzen Sie diesen Wert auf `r + 1`.
- `setLowerRightColumn` — der Spaltenindex der rechten Kante des Bildes. Um die rechte Kante des Bildes an der rechten Seite der Spalte `c` zu platzieren, setzen Sie diesen Wert auf `c + 1`.

Um beispielsweise das Bild genau in die Zelle **C6** (Zeilenindex `5`, Spaltenindex `2`) einzupassen, setzen Sie `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` und `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

{{% /alert %}}

### **Steuerung des Platzierungsverhaltens**

`getPlacement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die Zeile oder Spalte darunter in der Größe ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MOVE_AND_SIZE`, wodurch sich das Bild zusammen mit seiner zugrunde liegenden Zelle bewegt und in der Größe ändert, wobei die genaue Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen `InputStream` (typischerweise ein `FileInputStream`), damit der Stream ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.getPictures().add(5, 2, stream)` auf, um ein Bild hinzuzufügen, das an Zelle C6 verankert ist. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Setzen Sie die vier Ankerkoordinaten so, dass das Bild nur die Zelle C6 abdeckt: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Setzen Sie `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe geändert wird.
7. Optional können Sie Beispieltext in umgebende Zellen einfügen, um zu zeigen, dass nur Zelle C6 das Bild enthält.
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

## **Ansatz 2: Direktes Einbetten eines Bildes in eine Zelle**

Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `Cell.setEmbeddedImage`. Durch Zuweisen von Bild-Bytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Funktionsweise eingebetteter Bilder**

- Das Bild wird als Teil des Zelleninhalts und nicht als Form auf der Zeichnungsebene gespeichert.
- Das Bild wird automatisch so skaliert, dass es in die gerenderten Grenzen der Zelle passt. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die durch Formeln referenziert, als Teil einer Zeile sortiert oder in anderen zellenbezogenen Operationen verwendet werden kann.

Dies macht `Cell.setEmbeddedImage` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.getWorksheets().get(0)` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `byte[]`-Array (z. B. durch einen Aufruf von `Files.readAllBytes` aus `java.nio.file.Files`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.getCells().get("C6")` oder `worksheet.getCells().get(5, 2)`.
5. Weisen Sie das Byte-Array der Eigenschaft `setEmbeddedImage` der Zelle zu.
6. Optional können Sie die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte anpassen, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den vollständigen Ansatz.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# Portierter Code hier
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Zielzelle C6 abrufen
cell = worksheet.getCells().get("C6")

# Bilddatei in ein Byte-Array einlesen
imageData = open("logo.png", "rb").read()

# Bild direkt in die Zelle einbetten
cell.setEmbeddedImage(imageData)

# Optional Zeilenhöhe und Spaltenbreite anpassen, damit das eingebettete Bild besser sichtbar ist
worksheet.getCells().setColumnWidth(2, 30)   # Spalte C (Index 2)
worksheet.getCells().setRowHeight(5, 100)    # Zeile 6 (Index 5)

# Speichern der resultierenden Arbeitsmappe als .xlsx-Datei
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Die richtige Vorgehensweise wählen**

Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:

- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Kontrolle über Platzierung, Schichtung oder Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild als Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblattlayout berechnen müssen.

- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie die einfachstmögliche Einfügung eines Bildes in eine Zelle wünschen.
  - Das Bild wie jeder andere Zelleninhalt mit der Zelle mitwandern soll.
  - Sie das Bild nicht als Form bearbeiten müssen.

{{% alert color="primary" %}}

Beide Ansätze können in derselben Arbeitsmappe nebeneinander bestehen. Sie können schwebende Bilder über einem Satz von Zellen platzieren und Bilder direkt in andere Zellen einbetten, da die beiden Mechanismen unterschiedliche Speicherebenen in der Datei verwenden.

{{% /alert %}}



{{< app/cells/assistant language="python" >}}