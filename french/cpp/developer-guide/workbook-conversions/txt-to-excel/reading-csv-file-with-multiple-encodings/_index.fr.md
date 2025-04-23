---
title: Lecture d un fichier CSV avec plusieurs encodages avec C++
linktitle: Lecture du fichier CSV avec plusieurs encodages
type: docs
weight: 200
url: /fr/cpp/reading-csv-file-with-multiple-encodings/
description: Découvrez comment lire des fichiers CSV avec plusieurs encodages en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells vous permet de charger ces fichiers CSV et de les convertir dans d'autres formats, par exemple, PDF ou XLSX.

{{% /alert %}}

Aspose.Cells fournit la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/), que vous devez définir à **true** pour charger correctement votre fichier CSV avec plusieurs encodages.

La capture d'écran suivante montre un fichier CSV d'exemple contenant deux lignes. La première ligne est en encodage **ANSI** et la seconde en **Unicode**.

|**Fichier d'entrée**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus sans définir la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) à **true**. Comme vous pouvez le voir, le texte Unicode n'a pas été converti correctement.

|**Fichier de sortie 1: aucune adaptation pour plusieurs encodages**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus après avoir réglé la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) à **true**. Comme vous pouvez le voir, le texte Unicode est désormais converti correctement.

|**Fichier de sortie 2: IsMultiEncoded est défini sur true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ci-dessous se trouve le code d'exemple qui convertit le fichier CSV ci-dessus en format XLSX correctement.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"MultiEncoded.csv";

    // Create TxtLoadOptions and set MultiEncoded property to true
    TxtLoadOptions options;
    options.SetIsMultiEncoded(true);

    // Load the CSV file into Workbook with the specified options
    Workbook workbook(filePath, options);

    // Save the workbook in XLSX format
    workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Articles Connexes

- [Ouverture des fichiers CSV](/cells/fr/cpp/opening-files-with-different-formats/#opening-csv-files)
