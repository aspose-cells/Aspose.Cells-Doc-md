---
title: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells ist eine C++-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erläutert, wie ein Bild mithilfe zweier verschiedener Ansätze genau an die Größe einer einzelnen Zelle angepasst werden kann, durch Platzieren eines schwebenden Bildes über der Zelle oder durch direktes Einbetten des Bildes in die Zelle.
keywords: Aspose.Cells, C++-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in Zelle, Bild an Zelle anpassen, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /de/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild mit einer einzelnen Zelle zu verknüpfen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die visuell über einem Zellbereich liegt, während ein eingebettetes Bild in der Zelle selbst gespeichert wird und sich automatisch an den Anzeigebereich der Zelle anpasst. Wählen Sie den Ansatz, der am besten zu Ihren Layout-Anforderungen passt.

{{% /alert %}}

## **Einführung**

Ein Bild genau an eine einzelne Zelle anzupassen, ist eine häufige Anforderung beim Entwerfen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Bestandslisten dienen. Anstatt ein Bild über viele Zellen zu strecken oder es lose auf einem Arbeitsblatt zu platzieren, möchten Sie möglicherweise ein sauberes, zellgebundenes Bild, das mit der zugehörigen Zelle ausgerichtet bleibt.

Aspose.Cells unterstützt dieses Szenario auf zwei sich ergänzende Arten:

- **Ansatz 1 — Platzieren Sie ein schwebendes Bild über einer Zelle.** Fügen Sie dem Arbeitsblatt eine `Picture` hinzu, setzen Sie deren `Placement` auf `MoveAndSize`, und passen Sie die Ankerzellen (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Betten Sie ein Bild direkt in eine Zelle ein.** Weisen Sie Bild-Bytes der `EmbeddedImage`-Eigenschaft der Zelle zu. Das Bild wird automatisch skaliert, um in den Anzeigebereich der Zelle zu passen, und bewegt sich mit der Zelle mit.

Der Rest dieses Artikels führt durch beide Ansätze, erläutert die relevanten APIs und zeigt, wie sie im Code verwendet werden.

## **Ansatz 1: Platzieren eines Bildes über einer Zelle**

Ein schwebendes Bild ist ein `Picture`-Objekt, das sich auf der Zeichnungsebene des Arbeitsblatts befindet. Obwohl es nicht Teil einer einzelnen Zelle ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine visuelle Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein neu hinzugefügtes Bild über mehrere Zellen.

Um ein schwebendes Bild so zu platzieren, dass es **genau eine Zelle** abdeckt, müssen Sie:

1. Fügen Sie das Bild mit `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)` hinzu, wodurch das neue Bild an die angegebene Zelle verankert wird.
2. Legen Sie die vier Anker-Eigenschaften so fest, dass das Begrenzungsrechteck des Bildes mit der Zielzelle übereinstimmt.
3. Setzen Sie `Picture.Placement` auf `PlacementType.MoveAndSize`, damit sich das Bild mit der darunterliegenden Zelle bewegt und seine Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Verankerung des Bildes an einer einzelnen Zelle**

Der Anker des Bildes wird durch vier nullbasierte Index-Eigenschaften definiert:

- `Picture.UpperLeftRow` — der Zeilenindex der oberen Kante des Bildes.
- `Picture.UpperLeftColumn` — der Spaltenindex der linken Kante des Bildes.
- `Picture.LowerRightRow` — der Zeilenindex der unteren Kante des Bildes. Um die untere Kante des Bildes am unteren Rand der Zeile `r` zu positionieren, setzen Sie diesen Wert auf `r + 1`.
- `Picture.LowerRightColumn` — der Spaltenindex der rechten Kante des Bildes. Um die rechte Kante des Bildes am rechten Rand der Spalte `c` zu positionieren, setzen Sie diesen Wert auf `c + 1`.

Um das Bild beispielsweise genau in Zelle **C6** (Zeilenindex `5`, Spaltenindex `2`) einzupassen, setzen Sie `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` und `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-One-Fehler beim unteren rechten Anker sind die häufigste Ursache dafür, dass Bilder in eine benachbarte Zelle hineinzuragen scheinen.

{{% /alert %}}

### **Steuerung des Platzierungsverhaltens**

`Picture.Placement` ist eine Aufzählung vom Typ `PlacementType`, die steuert, wie sich das Bild verhält, wenn der Benutzer die darunterliegende Zeile oder Spalte in der Größe ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MoveAndSize`, wodurch sich das Bild zusammen mit der darunterliegenden Zelle bewegt und seine Größe ändert, sodass die genaue Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.Worksheets[0]` zu.
3. Lesen Sie die Bilddatei von der Festplatte in einen `Vector<uint8_t>`-Byte-Puffer ein, damit die Bild-Bytes für die API verfügbar sind.
4. Rufen Sie `worksheet.Pictures.Add(5, 2, imageData)` auf, um ein Bild hinzuzufügen, das an Zelle C6 verankert ist. Erfassen Sie die zurückgegebene `Picture`-Referenz.
5. Legen Sie die vier Ankerkoordinaten so fest, dass das Bild nur Zelle C6 abdeckt: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Setzen Sie `picture.Placement = PlacementType.MoveAndSize`, damit das Bild mit C6 ausgerichtet bleibt, wenn die Spalte oder Zeile in der Größe geändert wird.
7. Optional können Sie Beispieltext in umliegende Zellen einfügen, um zu zeigen, dass nur Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den vollständigen Ansatz.

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();

    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));

    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);

    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ansatz 2: Bild direkt in eine Zelle einbetten**

Aspose.Cells bietet außerdem einen einfacheren Mechanismus für zellgebundene Bilder: die `Cell.EmbeddedImage`-Eigenschaft. Durch das Zuweisen von Bild-Bytes zu dieser Eigenschaft wird das Bild an die Zelle selbst angehängt, als wäre es Inline-Inhalt.

### **Funktionsweise eingebetteter Bilder**

- Das Bild wird als Teil des Zellinhalts und nicht als Form auf der Zeichnungsebene gespeichert.
- Das Bild wird automatisch skaliert, um in die gerenderten Grenzen der Zelle zu passen. Es sind keine Ankerkoordinaten oder Platzierungseinstellungen erforderlich.
- Die Zelle bleibt eine echte Zelle mit einer echten Adresse, die von Formeln referenziert, als Teil einer Zeile sortiert oder in anderen Zelloperationen verwendet werden kann.

Dies macht `Cell.EmbeddedImage` zur kompaktesten Option, wenn Ihr Ziel einfach „ein Bild, das in dieser Zelle lebt" ist.

### **Schritt-für-Schritt-Anleitung**

1. Erstellen Sie eine neue `Workbook` (oder öffnen Sie eine vorhandene).
2. Greifen Sie auf das Ziel-`Worksheet` über `workbook.Worksheets[0]` zu.
3. Lesen Sie die Bilddatei von der Festplatte in ein `Vector<uint8_t>`-Byte-Array ein.
4. Holen Sie sich eine Referenz auf die Zielzelle — entweder über `worksheet.Cells["C6"]` oder `worksheet.Cells[5, 2]`.
5. Weisen Sie das Byte-Array der `EmbeddedImage`-Eigenschaft der Zelle zu.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und -spalte an, um dem eingebetteten Bild ein prominenteres Erscheinungsbild zu verleihen.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.

Der folgende Code demonstriert den vollständigen Ansatz.

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(u"C6");

    // Liest die Bilddatei in ein Byte-Array
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // Konvertiert std::vector zu Aspose::Cells::Vector mit Zeiger+Größe-Konstruktor
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // Bettet das Bild direkt in die Zelle ein
    cell.SetEmbeddedImage(imageData);

    // Optional die Zeilenhöhe und Spaltenbreite anpassen, damit das eingebettete Bild besser sichtbar ist
    worksheet.GetCells().SetColumnWidth(2, 30);   // Spalte C (Index 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Zeile 6 (Index 5)

    // Speichert die resultierende Arbeitsmappe als .xlsx-Datei
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Den richtigen Ansatz wählen**

Beide Ansätze erzeugen ein Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch in der Art und Weise, wie das Bild gespeichert wird, und wie es sich verhält:

- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Steuerung der Platzierung, der Schichtung oder der Ausrichtung mit anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild wie eine Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie Legacy-Kompatibilität mit Code benötigen, der bereits mit `PictureCollection` arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Arbeitsblatt-Layout berechnen müssen.

- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie das einfachstmögliche Einfügen eines Bildes in eine Zelle wünschen.
  - Das Bild sich wie jeder andere Zelleninhalt mit der Zelle bewegen soll.
  - Sie das Bild nicht als Form bearbeiten müssen.

{{% alert color="primary" %}}

Beide Ansätze können in derselben Arbeitsmappe nebeneinander bestehen. Sie können schwebende Bilder über einem Satz von Zellen platzieren und Bilder direkt in andere Zellen einbetten, da die beiden Mechanismen unterschiedliche Speicherebenen in der Datei verwenden.

{{% /alert %}}

## **Verwandte Artikel**

- [Wie man ein Bild in eine Zelle einfügt](/cells/de/cpp/how-to-place-image-to-cell/)
- [Bild-Hyperlinks hinzufügen](/cells/de/cpp/add-image-hyperlinks/)
- [Laden eines Webbildes von einer URL in ein Excel-Arbeitsblatt](/cells/de/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Position, Größe und Designer-Diagramm bearbeiten](/cells/de/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}