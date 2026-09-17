---
title: Excel-Kamera in Aspose.Cells for C++
linktitle: Excel-Kamera
description: Erfahren Sie, wie Sie die Excel-Kamera in Aspose.Cells for C++ verwenden, um ein dynamisches Bild zu erstellen, das mit einem Zellbereich verknüpft ist, sich mit den Quelldaten aktualisiert und die gesamte Quellformatierung beibehält.
keywords: Aspose.Cells, C++, Excel-Kamera, dynamisches Bild, verknüpftes Bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /de/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblattobjekt, das ein Live-Bild eines Zellbereichs rendert und wie ein gewöhnliches Bild auf der Zeichnungsebene schwebt. Aspose.Cells unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, und ein statisches Bild, das einen einmaligen Schnappschuss eines Bereichs erfasst. Dieser Artikel führt durch beide Ansätze, damit Sie denjenigen auswählen können, der zu Ihrem Layout passt.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das an einer bestimmten Zeile und Spalte auf der Zeichnungsebene des Arbeitsblatts verankert ist. Im Gegensatz zu einem normal eingefügten Bild ist die Kamera über eine Formel im A1-Stil, wie z. B. `"A1:F10"`, mit einem Quellbereich verknüpft. Immer wenn sich eine Zelle innerhalb dieses Bereichs ändert, wird das Bild der Kamera automatisch aktualisiert, um den neuen Inhalt wiederzugeben. Die Kamera bewahrt die gesamte Formatierung des Quellbereichs – Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate –, sodass alles, was innerhalb der Zellen sichtbar ist, auch im Bild der Kamera erscheint. Dies macht die Kamera besonders nützlich für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts, bei denen Sie eine sichtbare Vorschau eines entfernten Bereichs wünschen, ohne zu scrollen oder Daten zu wiederholen. Zwei Einschränkungen gelten: Sie müssen `UpdateSelectedValue()` vor dem Speichern der Arbeitsmappe aufrufen, und die Datei wird nach HTML oder PDF exportiert, da diese Formate auf den eingebetteten Bilddaten basieren und nicht auf einer Live-Neuberechnung.

## Methode 1 – Hinzufügen eines dynamischen Kamerabilds
Die dynamische Kamera ist der häufigste Ansatz und entspricht am ehesten dem in Excel integrierten Kamera-Tool. Sie funktioniert, indem ein Bild ohne anfänglichen Bildinhalt hinzugefügt und anschließend eine `Formula` zugewiesen wird, die auf den Quellbereich verweist. Nachdem die Formel zugewiesen wurde, aktualisiert der Aufruf von `UpdateSelectedValue()` die eingebetteten Bilddaten, sodass sie mit den Zellen synchron sind, die sie spiegeln. Die Kamera wird nicht über eine eigene Klasse implementiert – sie wird vollständig auf dem Standardtyp `Picture` aufgebaut.
Die wichtigsten APIs sind:
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` – fügt ein an der angegebenen Zeile und Spalte verankertes Bild hinzu. Das Übergeben eines leeren `Vector<uint8_t>()` erstellt ein leeres Bild, das als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index des neuen Bilds zurück.
- `worksheet.GetPictures().Get(int index)` – ruft ein bestimmtes `Picture` aus der Sammlung über den Index ab.
- `Picture.SetFormula(U16String value)` – legt die Referenz im A1-Stil auf den Quellbereich fest, den die Kamera spiegelt, z. B. `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` – aktualisiert die eingebetteten Bilddaten aus den Zellen, auf die `Formula` verweist.

{{% alert color="primary" %}}
`UpdateSelectedValue()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten und die Kamera erscheint in der gerenderten Ausgabe leer.
{{% /alert %}}

Der folgende Code erstellt eine Arbeitsmappe, fügt ein leeres Bild verankert an Zeile 10, Spalte 6 hinzu, verknüpft es über die Eigenschaft `Formula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.

## Methode 2 – Hinzufügen eines statischen Kamerabilds
Die statische Kamera ist im Wesentlichen eine einmal gerenderte Vorschau eines Zellbereichs. Anstatt eine Live-Verknüpfung beizubehalten, rendern Sie den Bereich einmal in einen Bytepuffer `Vector<uint8_t>` und übergeben diesen Puffer direkt an `Pictures.Add(row, col, data)`. Der Bildinhalt wird zum Zeitpunkt der Erstellung fixiert und aktualisiert sich nicht automatisch, wenn sich die Quellzellen ändern.
Die wichtigsten APIs sind:
- `Cells.CreateRange(U16String address)` – erstellt ein `Range`-Objekt aus einer Adresse im A1-Stil, z. B. `U16String("A1:F10")`.
- `Range.ToImage(ImageOrPrintOptions options)` – rendert den Bereich in einen Bytepuffer `Vector<uint8_t>`. Das Übergeben von `nullptr` verwendet die Standard-Renderingoptionen; es existieren Überladungen für eine feinere Steuerung der Ausgabe.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` – fügt das an der angegebenen Zeile und Spalte verankerte Bild hinzu, diesmal unter Übergabe des von `Range.ToImage` erzeugten Bytepuffers.
Der folgende Code erstellt eine Arbeitsmappe, baut einen `Range` für `A1:F10` auf, rendert ihn über `Range.ToImage(nullptr)` in Bildbytes, fügt das an Zeile 10, Spalte 6 verankerte Bild hinzu und speichert die Arbeitsmappe.

## Wahl zwischen dynamisch und statisch
- **Dynamische Kamera:** aktualisiert sich bei jeder Neuberechnung, unterstützt den HTML- und PDF-Export nach `UpdateSelectedValue()` und bewahrt das Verhalten der Live-Verknüpfung über die gesamte Lebensdauer der Datei.
- **Statische Kamera:** ein einmaliges Rendering, das nie aktualisiert wird, nützlich, wenn Sie einen fixen visuellen Schnappschuss einbetten möchten, der zur Build-Zeit erstellt wird, anstatt eine Live-Spiegelung der Daten.
Aspose.Cells unterstützt sowohl eine dynamische, sich automatisch aktualisierende Kamera, die auf `Picture.Formula` plus `UpdateSelectedValue()` aufbaut, als auch eine statische, einmalige Kamera, die auf `Range.ToImage` plus `Vector<uint8_t>` aufbaut. Wählen Sie den dynamischen Ansatz, wenn Ihre Ausgabe mit den Quellzellen synchron bleiben muss, und wählen Sie den statischen Ansatz, wenn Sie lediglich einen fixen visuellen Schnappschuss zur Build-Zeit benötigen.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Static Camera: build Range, render to bytes, add as picture
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}