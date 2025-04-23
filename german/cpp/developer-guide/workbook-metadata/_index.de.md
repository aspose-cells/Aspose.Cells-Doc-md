---
title: Mit WorkbookMetadata in C++
linktitle: Metadaten der Arbeitsmappe
type: docs
weight: 320
url: /de/cpp/using-workbookmetadata/
description: Erfahren Sie, wie Sie WorkbookMetadata verwenden, um benutzerdefinierte Dokumenteigenschaften eines Arbeitsbuchs in C++ mit Aspose.Cells zu bearbeiten.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht das Laden einer leichten Version eines Arbeitsbuchs ins Speicher für die Bearbeitung seiner Metadaten. Bitte verwenden Sie die [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/)-Klasse, um das Arbeitsbuch zu laden.

{{% /alert %}}

Der folgende Beispielcode verwendet die [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/)-Klasse, um benutzerdefinierte Dokumenteigenschaften eines Arbeitsbuchs zu bearbeiten. Nachdem Sie das Arbeitsbuch mit der [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse geöffnet haben, können Sie die Dokumenteigenschaften lesen. Hier ist ein Beispielcode mit der [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/)-Klasse.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Metadata;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    MetadataOptions options(MetadataType::Document_Properties);
    WorkbookMetadata meta(srcDir + u"Sample1.xlsx", options);

    meta.GetCustomDocumentProperties().Add(u"test", u"test");

    meta.Save(srcDir + u"Sample2.out.xlsx");

    Workbook w(srcDir + u"Sample2.out.xlsx");

    std::cout << w.GetCustomDocumentProperties().Get(u"test").ToString().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```
