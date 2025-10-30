---
title: Arbeitsmappe mit C++ drucken und Vorschau anzeigen
linktitle: Drucken und Vorschau
type: docs
weight: 70
url: /de/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells unterstützt das Drucken und die Vorschau von Excel Dateien ohne die Installation von Microsoft Excel mit C++.
---

{{% alert color="primary" %}}

Nachdem Sie ein Arbeitsblatt erstellt haben, möchten Sie oft eine gedruckte Kopie davon haben. Dieser Artikel erklärt, wie Sie Tabellenkalkulationen mit Aspose.Cells drucken können.

{{% /alert %}}

## **Drucken-Einführung**

Microsoft Excel geht davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben eine Auswahl an. Um mit Aspose.Cells zu drucken, importieren Sie zuerst den Aspose.Cells.Rendering-Namespace in das Programm. Es enthält mehrere nützliche Klassen, z.B. [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) und [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **Druckvorschau**

Es kann Fälle geben, in denen Excel-Dateien mit Millionen von Seiten in PDF oder Bilder konvertiert werden müssen. Solche Dateien zu verarbeiten, wird viel Zeit und Ressourcen in Anspruch nehmen. In solchen Fällen könnte die Arbeitsbuch- und Arbeitsblatt-Druckvorschau nützlich sein. Bevor solche Dateien konvertiert werden, kann der Benutzer die Gesamtzahl der Seiten überprüfen und dann entscheiden, ob die Datei konvertiert werden soll oder nicht. Dieser Artikel konzentriert sich auf die Verwendung der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/), um die Gesamtzahl der Seiten zu ermitteln.

Aspose.Cells bietet die Druckvorschau-Funktion. Dazu stellt die API die Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) und [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) bereit. Um die Druckvorschau des gesamten Arbeitsbuchs zu erstellen, erstellen Sie eine Instanz der Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/), indem Sie [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) Objekte an den Konstruktor übergeben. Die Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) bietet eine [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt. Ähnlich wie bei der Klasse [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) wird die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) verwendet, um eine Druckvorschau für ein bestimmtes Arbeitsblatt zu generieren. Erstellen Sie zum Erstellen der Druckvorschau eines Arbeitsblatts eine Instanz der Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/), indem Sie [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) Objekte an den Konstruktor übergeben. Die Klasse [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) bietet ebenfalls eine [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/)-Methode, die die Anzahl der Seiten in der generierten Vorschau zurückgibt.

Der folgende Codeausschnitt zeigt die Verwendung sowohl der Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) als auch [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/), indem die [Beispiel-Excel-Datei](94896177.xlsx) verwendet wird.

### **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Das folgende ist die Ausgabe, die durch das Ausführen des obigen Codes generiert wird.

### **Konsolenausgabe**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Erweiterte Themen**
- [Konfiguration von Schriftarten für die Darstellung von Tabellenkalkulationen](/cells/de/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Arbeitsblatt in Bild konvertieren - Leerraum um Daten entfernen](/cells/de/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Arbeitsblatt in Bild und Arbeitsblatt in Bild nach Seite konvertieren](/cells/de/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Arbeitsblatt in Bild mit den Optionen Bild oder Druck konvertieren](/cells/de/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren](/cells/de/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extrahieren von Bildern aus Arbeitsblättern mit ImageOrPrintOptions](/cells/de/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generieren einer Miniaturansicht des Arbeitsblatts](/cells/de/cpp/generate-thumbnail-of-the-worksheet/)
- [Leeres Blatt ausgeben, wenn nichts gedruckt werden muss](/cells/de/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Seiteneinrichtungs- und Druckoptionen](/cells/de/cpp/page-setup-and-printing-options/)
- [Sequenz von Seiten rendern mithilfe der Eigenschaften PageIndex und PageCount von ImageOrPrintOptions](/cells/de/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Arbeitsblatt in Grafikkontext rendern](/cells/de/cpp/render-worksheet-to-graphic-context/)
- [Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben](/cells/de/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
{{< app/cells/assistant language="cpp" >}}
