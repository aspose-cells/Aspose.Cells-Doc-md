---
title: Implémenter des plages non séquentielles avec C++
linktitle: Mise en œuvre de plages non séquentielles
type: docs
weight: 700
url: /fr/cpp/implementing-non-sequential-ranges/
description: Apprenez comment créer des plages nommées avec des cellules non adjacentes en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}} 

Normalement, les plages nommées sont rectangulaires avec des cellules continues et adjacentes les unes aux autres. Mais parfois, vous pouvez avoir besoin d'utiliser une plage de cellules non séquentielle dans laquelle les cellules ne sont pas adjacentes. Aspose.Cells prend en charge la création d'une plage nommée avec des cellules non adjacentes.

{{% /alert %}} 

L'extrait de code ci-dessous montre comment créer une plage nommée non séquentielle avec Aspose.Cells for C++.

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

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
