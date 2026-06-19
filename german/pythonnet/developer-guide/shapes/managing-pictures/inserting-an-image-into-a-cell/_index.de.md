---
title: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine Python-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild exakt an die Größe einer einzelnen Zelle angepasst werden kann, und zwar mit zwei verschiedenen Ansätzen: Platzieren eines schwebenden Bildes über der Zelle oder direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Python-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die visuell über einem Zellbereich liegt, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.

{{% /alert %}}

## **Einführung**

Ein Bild exakt an eine einzelne Zelle anzupassen, ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu strecken oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der zugehörigen Zelle ausgerichtet bleibt.

Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:

- **Ansatz 1 — Platzieren Sie ein schwebendes Bild über einer Zelle.** Fügen Sie ein `Picture` zum Arbeitsblatt hinzu, setzen Sie dessen `placement` auf `MOVE_AND_SIZE`, und passen Sie dessen Ankerzellen (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Betten Sie ein Bild direkt in eine Zelle ein.** Weisen Sie Bildbytes der Eigenschaft `embedded_image` der Zelle zu. Das Bild skaliert automatisch, um in den Anzeigebereich der Zelle zu passen, und bewegt sich mit der Zelle mit.

Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Platzieren eines Bildes über einer Zelle**

Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine oberen linken und unteren rechten Ecken — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.

Um ein schwebendes Bild **genau eine Zelle** abdecken zu lassen, müssen Sie:

1. Das Bild mit `Worksheet.pictures.add(row, column, stream)` hinzufügen, wodurch das neue Bild an der angegebenen Zelle verankert wird.
2. Die vier Anker-Eigenschaften so festlegen, dass das umgebende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. `Picture.placement` auf `PlacementType.MOVE_AND_SIZE` setzen, damit sich das Bild beim Ändern der Spaltenbreite oder Zeilenhöhe durch den Benutzer mit der darunterliegenden Zelle bewegt und seine Größe ändert.

### **Verankerung des Bildes an einer einzelnen Zelle**

Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:

- `Picture.upper_left_row` — der Zeilenindex der oberen Kante des Bildes.
- `Picture.upper_left_column` — der Spaltenindex der linken Kante des Bildes.
- `Picture.lower_right_row` — der Zeilenindex der unteren Kante des Bildes. Damit die untere Kante des Bildes am unteren Rand der Zeile `r` sitzt, setzen Sie diesen auf `r + 1`.
- `Picture.lower_right_column` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` sitzt, setzen Sie diesen auf `c + 1`.

Um das Bild beispielsweise genau in die Zelle **C6** (Zeilenindex `5`, Spaltenindex `2`) einzupassen, setzen Sie `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6` und `lower_right_column = 3`.

{{% alert color="primary" %}}

Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Die Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim Anker für die untere rechte Ecke sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle hineinragen.

{{% /alert %}}

### **Steuerung des Platzierungsverhaltens**

`Picture.placement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die darunterliegende Zeile oder Spalte in der Größe ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MOVE_AND_SIZE`, wodurch sich das Bild gemeinsam mit der darunterliegenden Zelle bewegt und seine Größe ändert, wobei die exakte Passform erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.worksheets[0]` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einem Dateistrom (oder einem `BytesIO`-Objekt) mithilfe eines `with`-Blocks, damit der Strom ordnungsgemäß geschlossen wird.
4. Rufen Sie `worksheet.pictures.add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Legen Sie die vier Ankerkoordinaten so fest, dass das Bild nur die Zelle C6 abdeckt: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Setzen Sie `picture.placement = PlacementType.MOVE_AND_SIZE`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe geändert wird.
7. Optional können Sie Beispieltext zu umgebenden Zellen hinzufügen, um zu zeigen, dass nur die Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den gesamten Ansatz.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE

workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Ansatz 2: Direktes Einbetten eines Bildes in eine Zelle**

Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `Cell.embedded_image`. Das Zuweisen von Bildbytes zu dieser Eigenschaft hängt das Bild an die Zelle selbst an, als wäre es Inline-Inhalt.

### **Wie eingebettete Bilder funktionieren**

- Das Bild wird als Teil des Zellinhalts gespeichert und nicht als Form auf der Zeichnungsebene.
- Das Bild skaliert automatisch, um in die gerenderten Grenzen der Zelle zu passen. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen zellbezogenen Operationen verwendet werden kann.

Dies macht `Cell.embedded_image` zur kompaktesten Option, wenn Ihr Ziel einfach ein „Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.worksheets[0]` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `bytes`-Objekt (zum Beispiel durch Öffnen der Datei im Binärmodus und Aufrufen von `.read()`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.cells["C6"]` oder `worksheet.cells[5, 2]`.
5. Weisen Sie das bytes-Objekt der Eigenschaft `embedded_image` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den gesamten Ansatz.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Die Zielzelle C6 abrufen
cell = worksheet.cells["C6"]

# Die Bilddatei in ein Byte-Array einlesen
with open("logo.png", "rb") as f:
    imageData = f.read()

# Das Bild direkt in die Zelle einbetten
cell.embedded_image = imageData

# Optional die Zeilenhöhe und Spaltenbreite anpassen, damit das eingebettete Bild besser sichtbar ist
worksheet.cells.set_column_width(2, 30)   # Spalte C (Index 2)
worksheet.cells.set_row_height(5, 100)     # Zeile 6 (Index 5)

# Die resultierende Arbeitsmappe als .xlsx-Datei speichern
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Den richtigen Ansatz wählen**

Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:

- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Kontrolle über Platzierung, Schichtung oder Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild wie eine Form verhält, die ausgewählt, umgeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `pictures`-Sammlungen arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblatt-Layout berechnen müssen.

- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie die einfachstmögliche Einfügung eines Bildes in eine Zelle wünschen.
  - Das Bild sich wie jeder andere Zellinhalt mit der Zelle bewegen soll.
  - Sie das Bild nicht als Form bearbeiten müssen.

{{% alert color="primary" %}}

Beide Ansätze können in derselben Arbeitsmappe koexistieren. Sie können schwebende Bilder über einem Satz von Zellen platzieren und Bilder direkt in andere Zellen einbetten, da die beiden Mechanismen unterschiedliche Speicherebenen in der Datei verwenden.

{{% /alert %}}

## **Verwandte Artikel**

- [Wie man ein Bild in eine Zelle einfügt](/cells/de/python-net/how-to-place-image-to-cell/)
- [Bild-Hyperlinks hinzufügen](/cells/de/python-net/add-image-hyperlinks/)
- [Laden eines Webbildes von einer URL in ein Excel-Arbeitsblatt](/cells/de/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Position, Größe und Designer-Diagramm bearbeiten](/cells/de/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}