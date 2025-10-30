---
title: Kompatibilitätsprüfer in Excel mit C++ deaktivieren
linktitle: Kompatibilitätsprüfer deaktivieren
type: docs
weight: 170
url: /de/cpp/disable-compatibility-checker-in-excel/
description: Dieser Artikel zeigt, wie man den Kompatibilitätsprüfer über die Aspose.Cells for C++ API deaktiviert.
keywords: C++ Deaktivieren des Kompatibilitätsprüfers, Excel Deaktivieren des Kompatibilitätsprüfers in C++, Kompatibilitätsprüfer in Arbeitsmappen deaktivieren. 
---

## Deaktivieren des Kompatibilitätsprüfers in Excel-Arbeitsblättern in C++

{{% alert color="primary" %}}

Microsoft Excels Kompatibilitätsprüfer warnt, wenn das Speichern einer Datei in einem früheren Dateiformat zu Funktionsproblemen oder Qualitätsverlust führen könnte. Der Kompatibilitätsprüfer ist eine Funktion von Microsoft Office Excel 2007 und Microsoft Excel 2010.

Wenn Sie eine Arbeitsmappe in einer früheren Version, Excel 97 bis Excel 2003, von Excel 2007 oder Excel 2010 speichern, durchsucht der Kompatibilitätsprüfer die Arbeitsmappe, um festzustellen, ob sie Funktionen enthält, die von der früheren Version nicht unterstützt werden. Um Ihnen bei Entscheidungen über den Umgang mit Kompatibilitätsproblemen zu helfen, zeigt der Kompatibilitätsprüfer Dialogfelder mit Optionen an. Er kann auch verwendet werden, um einen Bericht über Probleme in der Arbeitsmappe zu erstellen oder das Feature zu deaktivieren.

Manchmal müssen Sie den Kompatibilitätsprüfer für eine bestimmte Arbeitsmappe deaktivieren. Mit den Aspose.Cells-APIs können Sie dies programmgesteuert tun, damit Benutzer nicht durch das Dialogfeld des Kompatibilitätsprüfers frustriert oder verwirrt werden, wenn sie die Datei manuell in Microsoft Excel erneut speichern.

{{% /alert %}}

## **Wie Sie den Kompatibilitätsprüfer in Microsoft Excel deaktivieren**

Um den Kompatibilitätsprüfer in Microsoft Excel zu deaktivieren (z.B. Microsoft Excel 2007/2010):

- (Excel 2007) Klicken Sie auf die Office-Schaltfläche, dann auf **Vorbereiten**, anschließend auf **Kompatibilitätsprüfung ausführen** und deaktivieren Sie die Option **Kompatibilität beim Speichern dieser Arbeitsmappe prüfen**.
- (Excel 2010) Klicken Sie auf die Registerkarte **Datei**, dann auf **Info**, klicken Sie auf **Nach Problemen suchen**, klicken Sie auf **Kompatibilität prüfen** und deaktivieren Sie anschließend die Option **Kompatibilität prüfen, wenn Sie diese Arbeitsmappe speichern**.

## **So deaktivieren Sie den Kompatibilitätsprüfer mithilfe von Aspose.Cells-APIs**

Setzen Sie die [**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcompatibility/)-Eigenschaft auf **False**, um den Kompatibilitätsprüfer von Microsoft Excel zu deaktivieren.

### **Codebeispiele**

Die folgenden Codebeispiele zeigen, wie man den Kompatibilitätsprüfer mit Aspose.Cells for C++ deaktiviert.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open a template file
    U16String templateFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(templateFilePath);

    // Disable the compatibility checker
    workbook.GetSettings().SetCheckCompatibility(false);

    // Path to save the output file
    U16String outputFilePath = srcDir + u"Output_BK_CompCheck.out.xlsx";

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
