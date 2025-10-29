---
title: Trouver le maximum de lignes et de colonnes supporté par les formats XLS et XLSX avec C++
linktitle: Trouver le maximum de lignes et de colonnes
type: docs
weight: 20
url: /fr/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Apprenez comment trouver le maximum de lignes et de colonnes supporté par les formats XLS et XLSX en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Il y a différentes quantités de lignes et de colonnes supportées par les formats Excel. Par exemple, XLS supporte 65536 lignes et 256 colonnes tandis que XLSX supporte 1048576 lignes et 16384 colonnes. Si vous souhaitez connaître le nombre de lignes et de colonnes supportées par un format donné, vous pouvez utiliser les propriétés [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) et [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX**

Le code d'exemple suivant crée d'abord un classeur au format XLS puis en XLSX. Après la création, il affiche les valeurs des propriétés [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) et [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). Veuillez consulter la sortie console du code ci-dessous pour référence.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Print message about XLS format.
    std::cout << "Maximum Rows and Columns supported by XLS format." << std::endl;

    // Create workbook in XLS format.
    Workbook wb(FileFormatType::Excel97To2003);

    // Print the maximum rows and columns supported by XLS format.
    int maxRows = wb.GetSettings().GetMaxRow() + 1;
    int maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;
    std::cout << std::endl;

    // Print message about XLSX format.
    std::cout << "Maximum Rows and Columns supported by XLSX format." << std::endl;

    // Create workbook in XLSX format.
    wb = Workbook(FileFormatType::Xlsx);

    // Print the maximum rows and columns supported by XLSX format.
    maxRows = wb.GetSettings().GetMaxRow() + 1;
    maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
