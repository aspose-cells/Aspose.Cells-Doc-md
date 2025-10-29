---
title: Implémenter le système de date 1904 avec C++
linktitle: Implémenter le système de date 1904
description: Aspose.Cells est une bibliothèque C++ pour le travail avec des fichiers de tableur. Elle supporte l implémentation du système de date 1904, permettant aux utilisateurs de calculer et de formater selon ce système basé sur le 1er janvier 1904. Cet article explique comment implémenter le système de date 1904 en utilisant la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, système de date 1904, tableur, calcul, formatage
type: docs
weight: 7000
url: /fr/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel prend en charge deux systèmes de dates : le système de date 1900 (le système de date par défaut implémenté dans Excel pour Windows) et le système de date 1904. Le système de date 1904 est généralement utilisé pour assurer la compatibilité avec les fichiers Excel Macintosh et est le système par défaut si vous utilisez Excel pour Macintosh. Vous pouvez définir le système de date 1904 pour les fichiers Excel en utilisant Aspose.Cells.

{{% /alert %}}

Pour implémenter le système de date 1904 dans Microsoft Excel (par exemple Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Calcul**.
1. Sélectionnez l'option **Système de date 1904**.
1. Cliquez sur **OK**.

|**Sélection du système de date 1904 dans Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Consultez le code source suivant sur la manière d'accomplir ceci en utilisant les API Aspose.Cells.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
