---
title: Festlegen der Sprache der Excel Datei mithilfe der BuiltIn Dokumenteigenschaften mit C++
linktitle: Festlegen der Sprache der Excel Datei
type: docs
weight: 30
url: /de/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Erfahren Sie, wie Sie die Sprache einer Excel Datei programmatisch mit Aspose.Cells for C++ ändern.
---

## **Mögliche Verwendungsszenarien**

Sie können die Sprache einer Excel-Datei ändern, indem Sie mit der rechten Maustaste auf die Datei klicken, Eigenschaften > Details auswählen und dann das Sprachfeld bearbeiten. Verwenden Sie [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) Eigenschaft, um sie programmgesteuert mit den APIs von Aspose.Cells zu ändern.

## **Festlegen der Sprache der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften**

Der folgende Beispielcode erstellt eine Arbeitsmappe und ändert die interne Dokumenteigenschaft Sprache. Bitte sehen Sie sich die [Ausgabedatei Excel](64716891.xlsx) an, die vom Code erzeugt wurde, und den Screenshot, der das modifizierte Sprachfeld mit der [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) Eigenschaft zeigt.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
