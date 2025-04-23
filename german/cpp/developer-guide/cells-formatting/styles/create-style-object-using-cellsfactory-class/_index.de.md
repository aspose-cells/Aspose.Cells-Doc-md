---  
title: Erstelle Style Objekt mit der CellsFactory Klasse in C++  
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die ein Style Objekt zum Stylen von Zellen bereitstellt. Dieser Artikel zeigt, wie man mit der CellsFactory Klasse in Aspose.Cells ein Zellstil Objekt erstellt, damit Benutzer das Aussehen der Zellen nach Bedarf anpassen können.  
keywords: Aspose.Cells, C++ Bibliothek, elektronische Tabelle, Style Objekt, Zellenstil, Anpassung  
type: docs  
weight: 70  
url: /de/cpp/create-style-object-using-cellsfactory-class/  
---  

## **Erstellen Sie Style-Objekt mit der Klasse CellsFactory**  
Das folgende Beispiel erstellt ein [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) Objekt mit der [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory) Klasse und setzt dann den Standardstil des Arbeitsbuchs. Laden Sie die [Ausgabedatei](5115153.xlsx) herunter, um die Ergebnisse dieses Codes zu sehen.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
