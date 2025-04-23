---
title: Mehrere Arbeitsmappen zu einer einzigen Arbeitsmappe mit C++ kombinieren
linktitle: Arbeitsmappen Zusammenführung
type: docs
weight: 66
url: /de/cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Erfahren, wie man mit Aspose.Cells und C++ mehrere Arbeitsmappen in eine einzelne zusammenfasst.
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsmappen mit verschiedenen Inhalten wie Bildern, Diagrammen und Daten in eine einzige Arbeitsmappe zusammenfügen. Aspose.Cells unterstützt diese Funktion. Dieser Artikel zeigt, wie man mit Visual Studio eine Konsolenanwendung erstellt und Arbeitsmappen mit wenigen Zeilen Code mit Aspose.Cells kombiniert.

{{% /alert %}}

## **Arbeitsbücher mit Bildern und Diagrammen kombinieren**

Der Beispielcode kombiniert mit Aspose.Cells zwei Arbeitsbücher zu einem einzigen Arbeitsbuch. Der Code lädt die Quell-Arbeitsbücher, verwendet die Methode [**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) zur Kombination und speichert das Ausgabearbeitsbuch.

### **Quell-Arbeitsbücher**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Ausgabearbeitsbücher**

- [combined.xlsx](5473095.xlsx)

### **Screenshots**

Nachfolgend finden Sie Screenshots der Quell- und Ausgabearbeitsbücher.

{{% alert color="primary" %}}

Sie können beliebige Quellarbeitsmappen verwenden. Diese Bilder dienen nur zur Veranschaulichung.

{{% /alert %}}

**Die erste Arbeitsblatt der Diagramme Arbeitsmappe - gestapelt** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Zweites Arbeitsblatt der Diagramme Arbeitsmappe - Linie** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Erstes Arbeitsblatt der Bild Arbeitsmappe - Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alle drei Arbeitsblätter in der kombinierten Arbeitsmappe - gestapelt, Linie, Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

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

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";

    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren](/cells/de/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dateien zusammenführen](/cells/de/cpp/merge-files/)
