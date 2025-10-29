---
title: Vérifier si le projet VBA est protégé et verrouillé pour la visualisation avec C++
linktitle: Vérifier si le projet VBA est protégé et verrouillé pour consultation
type: docs
weight: 30
url: /fr/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Apprenez comment vérifier si un projet VBA est protégé et verrouillé pour la visualisation dans les fichiers Excel en utilisant Aspose.Cells for C++.
---

## Vérifier si le projet VBA est protégé et verrouillé pour la visualisation dans C++

Aspose.Cells vous permet de vérifier si le projet VBA (Visual Basic for Applications) d'un fichier Excel est protégé et verrouillé pour la visualisation. Pour cela, l'API fournit la propriété [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/). S'il est verrouillé pour la visualisation, alors la propriété [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) retourne **true**.

## **Code d'exemple**

Le code d'exemple suivant charge le [fichier Excel d'exemple](43352065.xlsm) et vérifie si le projet VBA (Visual Basic for Applications) du fichier Excel est protégé et verrouillé pour la visualisation. Veuillez également consulter sa sortie Console pour référence.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

Il s'agit de la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](43352065.xlsm) fourni.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
