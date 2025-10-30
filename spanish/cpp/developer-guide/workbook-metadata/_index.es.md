---
title: Uso de WorkbookMetadata con C++
linktitle: Metadatos del libro de trabajo
type: docs
weight: 320
url: /es/cpp/using-workbookmetadata/
description: Aprenda cómo usar WorkbookMetadata para editar las propiedades personalizadas de un documento en C++ con Aspose.Cells.
---

{{% alert color="primary" %}}

Aspose.Cells te permite cargar una versión ligera de un libro en memoria para editar su información de metadatos. Usa la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) para cargar el libro.

{{% /alert %}}

El siguiente código de ejemplo usa la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) para editar propiedades personalizadas de documentos de un libro. Una vez que abra el libro usando la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), podrá leer las propiedades del documento. Aquí hay un código de ejemplo usando la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/).

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
{{< app/cells/assistant language="cpp" >}}
