---
title: Filtern Sie VBA Projekte beim Laden eines Arbeitsbuchs mit C++
linktitle: Filtern des VBA Projekts beim Laden einer Arbeitsmappe
type: docs
weight: 140
url: /de/cpp/filter-vba-project-while-loading-a-workbook/
description: Erfahren Sie, wie Sie VBA Projekte beim Laden eines Excel Arbeitsbuchs mit Aspose.Cells und C++ filtern.
---

## **Filtern Sie VBA-Projekte beim Laden eines Excel-Arbeitsbuchs in C++**

Einige .xlsm/.xslb Dateien haben eine extrem große Anzahl an Makros (oder sehr lange Makros). Aspose.Cells lädt diese (Meta-)Daten beim Öffnen solcher Arbeitsbücher unbeding. Sie müssen dies jedoch mit [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) kontrollieren, wenn Sie nur Sheet-Namen extrahieren möchten, um so unnötigen Inhalt zu überspringen. Dieser Filter wird durch die Einführung einer neuen Option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions), bereitgestellt.

## **Beispielcode**

Der folgende Beispielscode lädt eine Arbeitsmappe so, dass nur das VBA gefiltert wird. Eine Testdatei für dieses Feature können Sie über den folgenden Link herunterladen:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
