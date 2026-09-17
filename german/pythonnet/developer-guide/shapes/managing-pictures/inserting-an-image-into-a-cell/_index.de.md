---
title: Einfügen eines Bildes in eine Zelle
linktitle: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine Python-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erklärt, wie ein Bild genau an eine einzelne Zelle angepasst werden kann, entweder durch Platzieren eines schwebenden Bildes über der Zelle oder durch direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, Python-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild einer einzelnen Zelle zuzuordnen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die einen Zellbereich visuell überlagert, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der Ihren Layout-Anforderungen am besten entspricht.

## **Einführung**
Ein Bild genau an eine einzelne Zelle anzupassen ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Inventarlisten dienen. Anstatt ein Bild über viele Zellen zu strecken oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der zugehörigen Zelle ausgerichtet bleibt.
Aspose.Cells unterstützt dieses Szenario auf zwei komplementäre Arten:
- **Ansatz 1 — Platzieren eines schwebenden Bildes über einer Zelle.** Fügen Sie ein `Picture` zum Arbeitsblatt hinzu, setzen Sie dessen `placement` auf `MOVE_AND_SIZE` und passen Sie die Ankerzellen (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Direktes Einbetten eines Bildes in eine Zelle.** Weisen Sie der Eigenschaft `embedded_image` der Zelle Bildbytes zu. Das Bild wird automatisch so skaliert, dass es in den Anzeigebereich der Zelle passt, und es wird mit der Zelle verschoben.
Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Bild über einer Zelle platzieren**
Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seinen visuellen Umfang auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.
Damit ein schwebendes Bild **genau eine Zelle** abdeckt, müssen Sie:
1. Fügen Sie das Bild mit `Worksheet.pictures.add(row, column, stream)` hinzu, wodurch das neue Bild an die angegebene Zelle verankert wird.
2. Legen Sie die vier Anker-Eigenschaften so fest, dass das umgebende Rechteck des Bildes mit der Zielzelle übereinstimmt.
3. Setzen Sie `Picture.placement` auf `PlacementType.MOVE_AND_SIZE`, damit sich das Bild mit der darunter liegenden Zelle bewegt und in der Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Verankern des Bildes an einer einzelnen Zelle**
Der Anker des Bildes wird durch vier nullbasierte Indexeigenschaften definiert:
- `Picture.upper_left_row` — der Zeilenindex der oberen Kante des Bildes.
- `Picture.upper_left_column` — der Spaltenindex der linken Kante des Bildes.
- `Picture.lower_right_row` — der Zeilenindex der unteren Kante des Bildes. Damit die untere Kante des Bildes am unteren Rand der Zeile `r` liegt, setzen Sie diesen auf `r + 1`.
- `Picture.lower_right_column` — der Spaltenindex der rechten Kante des Bildes. Damit die rechte Kante des Bildes am rechten Rand der Spalte `c` liegt, setzen Sie diesen auf `c + 1`.

{{% alert color="primary" %}}
Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler am unteren rechten Anker sind die häufigste Ursache für Bilder, die scheinbar in eine benachbarte Zelle überlappen.

### **Steuerung des Platzierungsverhaltens**
`Picture.placement` ist eine Enumeration vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die Zeile oder Spalte darunter in der Größe ändert. Der empfohlene Wert für ein Einzelzellbild ist `PlacementType.MOVE_AND_SIZE`, wodurch sich das Bild zusammen mit seiner darunter liegenden Zelle bewegt und in der Größe ändert, sodass die genaue Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie über `workbook.worksheets[0]` auf das Ziel-`Worksheet` zu.
3. Öffnen Sie die Bilddatei von der Festplatte in einen Dateistream (oder ein `BytesIO`-Objekt) mithilfe eines `with`-Blocks, damit der Stream ordnungsgemäß freigegeben wird.
4. Rufen Sie `worksheet.pictures.add(5, 2, stream)` auf, um ein an Zelle C6 verankertes Bild hinzuzufügen. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Legen Sie die vier Anker-Koordinaten so fest, dass das Bild nur Zelle C6 abdeckt: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Setzen Sie `picture.placement = PlacementType.MOVE_AND_SIZE`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe geändert wird.
7. Fügen Sie optional Beispieltext zu umgebenden Zellen hinzu, um zu zeigen, dass nur Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

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

## **Ansatz 2: Bild direkt in eine Zelle einbetten**
Aspose.Cells bietet auch einen einfacheren Mechanismus für zellgebundene Bilder: die Eigenschaft `Cell.embedded_image`. Durch Zuweisen von Bildbytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Wie eingebettete Bilder funktionieren**
- Das Bild wird als Teil des Zellinhalts gespeichert und nicht als Form auf der Zeichnungsebene.
- Das Bild wird automatisch so skaliert, dass es in die gerenderten Grenzen der Zelle passt. Es sind keine Anker-Koordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen Operationen auf Zellebene verwendet werden kann.
Damit ist `Cell.embedded_image` die kompakteste Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie über `workbook.worksheets[0]` auf das Ziel-`Worksheet` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `bytes`-Objekt (zum Beispiel durch Öffnen der Datei im Binärmodus und Aufrufen von `.read()`).
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.cells["C6"]` oder `worksheet.cells[5, 2]`.
5. Weisen Sie das Bytes-Objekt der Eigenschaft `embedded_image` der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code demonstriert den vollständigen Ansatz.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Den richtigen Ansatz wählen**
Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch darin, wie das Bild gespeichert wird und wie es sich verhält:
- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Steuerung über Platzierung, Schichtung oder Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild wie eine Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `pictures`-Sammlungen funktioniert.
  - Sie Anker-Koordinaten dynamisch basierend auf dem Arbeitsblatt-Layout berechnen müssen.
- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie die einfachstmögliche Einfügung eines Bildes in eine Zelle wünschen.
  - Das Bild mit der Zelle wie jeder andere Zellinhalt mitwandern soll.
  - Sie das Bild nicht als Form manipulieren müssen.
{{% /alert %}}

{{% /alert %}}

## Verwandte Artikel
- [Excel-Kamera in Aspose.Cells for Python via .NET](/cells/de/python-net/excel-camera/)
- [Hinzufügen von Filterfeldern zu einer Pivot-Tabelle in Aspose.Cells for Python via .NET](/cells/de/python-net/add-page-field-in-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen in Aspose.Cells for Python via .NET](/cells/de/python-net/apply-style-to-pivot-table/)
- [Ändern des Seitenfeldlayouts in einer Pivot-Tabelle](/cells/de/python-net/change-page-field-layout/)
- [Konvertieren einer Sparkline in Bild und HTML in Aspose.Cells for Python via .NET](/cells/de/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}