---
title: Lecture et écriture de la table de requête d une feuille de calcul avec C++
linktitle: Lecture et écriture de table de requêtes de feuille de calcul
type: docs
weight: 40
url: /fr/cpp/reading-and-writing-query-table-of-worksheet/
description: Apprenez comment lire et écrire des tables de requête dans les feuilles Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells fournit la collection `Worksheet.QueryTables`, qui retourne un objet de type `QueryTable` par index. Elle possède les deux propriétés suivantes :

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

Ce sont deux valeurs booléennes. Vous pouvez les voir dans Microsoft Excel via **Données > Connexions > Propriétés**.

{{% /alert %}}

## Lecture et écriture de table de requêtes de feuille de calcul

Le code d'exemple suivant lit la première `QueryTable` de la première feuille de calcul, puis affiche ses deux propriétés. Ensuite, il définit `QueryTable.PreserveFormatting` à `true`.

Vous pouvez télécharger le fichier Excel source utilisé dans ce code et le fichier Excel de sortie généré par le code à partir des liens suivants.

- [Fichier Excel Source](5115533.xlsx)
- [Fichier Excel de Sortie](5115537.xlsx)

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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Sortie de la Console

Voici la sortie de la console pour le code ci-dessus :

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Récupérer la plage de résultats de la table de requête

Aspose.Cells offre une option pour lire l'adresse (c'est-à-dire la plage de résultats des cellules) d'une table de requête. Le code suivant illustre cette fonctionnalité en lisant l'adresse de la plage de résultats d'une requête. Le fichier d'exemple peut être téléchargé [ici](72417290.xlsx).

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
