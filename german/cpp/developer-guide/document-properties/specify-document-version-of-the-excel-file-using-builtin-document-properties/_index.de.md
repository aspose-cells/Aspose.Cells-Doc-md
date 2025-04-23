---
title: Spezifizieren Sie die Dokumentversion der Excel Datei mit den BuiltIn Dokumenteigenschaften in C++
linktitle: Dokumentversion angeben
type: docs
weight: 20
url: /de/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Erfahren Sie, wie Sie die Dokumentversion einer Excel Datei mit den integrierten Dokumenteigenschaften in Aspose.Cells for C++ angeben.
---

## **Mögliche Verwendungsszenarien**

Sie können die **Versionsnummer** einer Excel-Datei ändern, indem Sie mit der rechten Maustaste auf die Datei klicken, Eigenschaften > Details auswählen und dann das Feld **Versionsnummer** bearbeiten. Verwenden Sie [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) Eigenschaft, um sie programmgesteuert mit den APIs von Aspose.Cells zu ändern.

## **Festlegen der Dokumentversion der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften**

Der folgende Beispielcode erstellt eine Arbeitsmappe und ändert ihre integrierten Dokumenteigenschaften, einschließlich Titel, Autoren und Versionsnummer. Bitte sehen Sie sich die [Ausgabedatei Excel](64716811.xlsx) an, die vom Code erzeugt wurde, und den Screenshot, der die geänderte Versionsnummer mit der [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) Eigenschaft zeigt.

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Beispielcode**

```cpp
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

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
