---
title: Datei im Response Objekt mit C++ speichern
linktitle: Datei im Antwortobjekt speichern
type: docs
weight: 50
url: /de/cpp/saving-file-to-response-object/
description: Lernen Sie, wie man Dateien dynamisch speichert und sie direkt an einen Browser Client sendet mit Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, Dateien zu manipulieren. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien in einem Antwortobjekt gespeichert werden können.

{{% /alert %}}

## **Speichern der Datei im Antwortobjekt**

Es ist auch möglich, eine Datei dynamisch zu generieren und direkt an den Client-Browser zu senden. Verwenden Sie dazu eine spezielle überladene Version der [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode, die die folgenden Parameter akzeptiert:

- **HttpResponse**-Objekt.
- Dateiname.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/), der Inhalt-Dispositionstyp der Ausgabedatei.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), der Dateiformat-Typ.

Die [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) Enumeration bestimmt, ob die Datei, die an den Browser gesendet wird, die Option bietet, direkt im Browser oder in einer Anwendung mit der Erweiterung .xls/.xlsx oder einer anderen geöffnet zu werden.

Die Enumeration enthält die folgenden vordefinierten Speichertypen:

|**Typ**|**Beschreibung**|
| :- | :- |
|Anhang|Sendet die Tabelle an den Browser und öffnet sie in einer Anwendung als Anhang, der mit .xls/.xlsx oder anderen Erweiterungen verknüpft ist|
|Inline|Sendet das Dokument an den Browser und bietet die Option, die Tabelle auf der Festplatte zu speichern oder im Browser zu öffnen|

### **XLS-Dateien**

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

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **XLSX-Dateien**

```cpp
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PDF-Dateien**

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

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Hinweis**

Aufgrund des Objekts "System.Web.HttpResponse", das nicht in .NET5 und .Netstandard enthalten ist,
Existiert diese Funktion nicht in Aspose.Cells .NET5 und .Netstandard Version, Sie können sich auf den folgenden Code beziehen, um die Datei im Stream zu speichern und dann den Stream zu bearbeiten.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
