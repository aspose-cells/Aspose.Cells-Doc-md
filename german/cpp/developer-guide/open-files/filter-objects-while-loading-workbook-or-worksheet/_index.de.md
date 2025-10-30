---
title: Objekte beim Laden der Arbeitsmappe oder des Arbeitsblatts mit C++ filtern
linktitle: Filterobjekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 330
url: /de/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Erfahren Sie, wie Sie Objekte wie Diagramme, Formen und bedingte Formatierungen beim Laden von Arbeitsmappen oder Arbeitsblättern mit Aspose.Cells for C++ filtern.
---

## **Mögliche Verwendungsszenarien**
Bitte verwenden Sie während des Filterns von Daten aus der Arbeitsmappe die Eigenschaft [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/). Wenn Sie Daten aus einzelnen Arbeitsblättern filtern möchten, müssen Sie die Methode [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/) überschreiben. Geben Sie beim Erstellen oder Arbeiten mit [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/) einen geeigneten Wert aus der [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) Enumeration an.

Die Enumeration [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) hat die folgenden möglichen Werte.

- Alle
- Bucheinstellungen
- Zelle Leer
- Zelle Bool
- Zelldaten
- Zellenfehler
- Zellnumerisch
- Zellenzeichenfolge
- Zellwert
- Chart
- Bedingte Formatierung
- Datenvalidierung
- Definierte Namen
- Dokumenteigenschaften
- Formel
- Hyperlinks
- Zusammengeführter Bereich
- Pivot-Tabelle
- Einstellungen
- Form
- Tabellendaten
- Tabelleneinstellungen
- Struktur
- Stil
- Tabelle
- VBA
- XmlMap

## **Filterobjekte beim Laden der Arbeitsmappe**
Der folgende Beispielcode veranschaulicht, wie Diagramme aus der Arbeitsmappe gefiltert werden. Bitte überprüfen Sie die [Beispiel-Excel-Datei](5115258.xlsx), die in diesem Code verwendet wird, und das [Ausgabe-PDF](5115257.pdf), das von ihm generiert wurde. Wie Sie im Ausgabe-PDF sehen können, wurden alle Diagramme aus der Arbeitsmappe gefiltert.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Filterobjekte beim Laden des Arbeitsblatts**
Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115255.xlsx) und filtert die folgenden Daten aus ihren Arbeitsblättern mithilfe eines benutzerdefinierten Filters.

- Es filtert Diagramme aus dem Arbeitsblatt mit dem Namen NoCharts.
- Es filtert Formen aus dem Arbeitsblatt mit dem Namen NoShapes.
- Es filtert bedingte Formatierungen aus dem Arbeitsblatt mit dem Namen NoConditionalFormatting.

Sobald es die [Quell-Excel-Datei](5115255.xlsx) mit einem benutzerdefinierten Filter lädt, nimmt es die Bilder aller Arbeitsblätter nacheinander. Hier sind die Ausgabe-Bilder zur Referenz. Wie Sie sehen können, hat das erste Bild keine Diagramme, das zweite Bild hat keine Formen und das dritte Bild hat keine bedingte Formatierung.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

So verwenden Sie die Klasse CustomLoadFilter gemäß der Arbeitsblattnamen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
