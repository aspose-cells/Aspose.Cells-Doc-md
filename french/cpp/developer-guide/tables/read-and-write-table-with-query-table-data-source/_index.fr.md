---
title: Lire et écrire une table avec une source de données QueryTable avec C++
linktitle: Lire et écrire un tableau avec la source de données de table de requête
type: docs
weight: 30
url: /fr/cpp/read-and-write-table-with-query-table-data-source/
description: Apprenez comment lire et écrire des tables avec QueryTable comme source de données en utilisant Aspose.Cells for C++.
---

## **Lire et Écrire un Tableau avec une Source de Données de Table de Requête**
Avec Aspose.Cells, vous pouvez lire et écrire une table qui a une QueryTable comme source de données. La prise en charge de cette fonctionnalité existe également pour les fichiers XLS. Le code suivant montre comment lire et écrire une telle table en la lisant d'abord et en la modifiant pour ajouter la ligne des totaux.

```cpp
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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

Les fichiers Excel source et de sortie sont joints à titre de référence.

[Fichier source](96928091.xls)

[Fichier de sortie](96928092.xls)
{{< app/cells/assistant language="cpp" >}}
