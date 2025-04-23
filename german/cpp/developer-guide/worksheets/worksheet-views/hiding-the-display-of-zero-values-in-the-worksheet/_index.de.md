---
title: Ausblenden der Anzeige von Nulwerten im Arbeitsblatt mit C++
linktitle: Ausblenden der Anzeige von Nullwerten im Arbeitsblatt
type: docs
weight: 50
url: /de/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Dieser Artikel zeigt Ihnen Beispielcode, der erklärt, wie man mit der C++ Bibliothek oder API Nulwerte in einer Excel Tabelle programmatisch ausblendet.
keywords: Nulwerte im Excel Arbeitsblatt in C++ ausblenden
---

{{% alert color="primary" %}} 

Manchmal müssen Sie Nullwerte in einer Tabelle ausblenden. Es könnte eine persönliche Vorliebe oder ein Formatierungsstandard sein.

{{% /alert %}} 

Um Nullwerte in einem Arbeitsblatt in Microsoft Excel zu verstecken (z. B. Microsoft Excel 2003):

1. Wählen Sie im Menü **Extras** die Option **Optionen** und dann den Tab **Ansicht** aus.
1. Deaktivieren Sie die Option **Nullwerte**.
1. Klicken Sie auf **OK**.

Bitte beachten Sie den folgenden Beispielscode, der das Ausblenden von Nullen mit Aspose.Cells demonstriert.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
