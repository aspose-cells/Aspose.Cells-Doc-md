---
title: Implementierung des 1904 Datumsystems mit C++
linktitle: Implementieren Sie das 1904 Datensystem
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Es unterstützt die Implementierung des 1904 Datumsystems, sodass Benutzer Berechnungen und Formatierungen basierend auf dem Datumssystem vom 1. Januar 1904 durchführen können. Dieser Artikel beschreibt, wie man das 1904 Datumsystem mit der Aspose.Cells Bibliothek implementiert.
keywords: Aspose.Cells, 1904 Datensystem, Tabelle, Berechnung, Formatierung
type: docs
weight: 7000
url: /de/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel unterstützt zwei Datensysteme: das 1900-Datensystem (das Standarddatensystem in Excel für Windows) und das 1904-Datensystem. Das 1904-Datensystem wird normalerweise verwendet, um die Kompatibilität mit Macintosh Excel-Dateien zu gewährleisten und ist das Standard-System, wenn Sie Excel für Macintosh verwenden. Sie können das 1904-Datensystem für Excel-Dateien mit Aspose.Cells einstellen.

{{% /alert %}}

Um das 1904-Datensystem in Microsoft Excel zu implementieren (zum Beispiel Microsoft Excel 2003):

1. Wählen Sie im **Extras**-Menü die Option **Optionen** und wählen Sie den Tab **Berechnung**.
1. Wählen Sie die Option **1904-Datensystem** aus.
1. Klicken Sie auf **OK**.

|**Auswählen des 1904-Datensystems in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Sehen Sie sich den folgenden Beispielcode an, wie Sie dies mit Aspose.Cells-APIs erreichen können.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
