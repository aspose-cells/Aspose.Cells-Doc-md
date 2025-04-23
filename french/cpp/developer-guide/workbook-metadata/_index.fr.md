---
title: Utilisation de WorkbookMetadata avec C++
linktitle: Métadonnées du classeur
type: docs
weight: 320
url: /fr/cpp/using-workbookmetadata/
description: Apprenez à utiliser WorkbookMetadata pour modifier les propriétés personnalisées d un document dans C++ avec Aspose.Cells.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de charger une version légère d'un classeur en mémoire pour modifier ses informations de métadonnées. Veuillez utiliser la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) pour charger le classeur.

{{% /alert %}}

Le code d'exemple suivant utilise la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) pour modifier les propriétés personnalisées d'un classeur. Une fois que vous avez ouvert le classeur en utilisant la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), vous pourrez lire les propriétés du document. Voici un exemple de code utilisant la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/).

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
