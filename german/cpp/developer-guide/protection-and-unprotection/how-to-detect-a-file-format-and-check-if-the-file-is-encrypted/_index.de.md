---
title: So erkennen Sie ein Dateiformat und prüfen, ob die Datei mit C++ verschlüsselt ist
linktitle: Wie man ein Dateiformat erkennt und überprüft, ob die Datei verschlüsselt ist
type: docs
weight: 2700
url: /de/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Lernen Sie, wie Sie das Format einer Datei erkennen und prüfen, ob sie mit Aspose.Cells in C++ verschlüsselt ist.
---

{{% alert color="primary" %}}

Manchmal müssen Sie das Format einer Datei erkennen, bevor Sie sie öffnen, weil die Dateierweiterung nicht garantiert, dass der Inhalt der Datei geeignet ist. Die Datei könnte verschlüsselt sein (passwortgeschützte Datei), sodass sie nicht direkt gelesen werden kann, oder wir sollten sie nicht lesen. Aspose.Cells bietet die statische Methode [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) und einige relevante APIs, die Sie zur Verarbeitung von Dokumenten verwenden können.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie man ein Dateiformat (unter Verwendung des Dateipfads) erkennt und ihre Erweiterung überprüft. Sie können auch feststellen, ob die Datei verschlüsselt ist.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Detect file format
    FileFormatInfo info = FileFormatUtil::DetectFileFormat(srcDir + u"Book1.xlsx");

    // Gets the detected load format
    std::cout << "The spreadsheet format is: " << FileFormatUtil::LoadFormatToExtension(info.GetLoadFormat()).ToUtf8() << std::endl;

    // Check if the file is encrypted
    std::cout << "The file is encrypted: " << (info.IsEncrypted() ? "true" : "false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
