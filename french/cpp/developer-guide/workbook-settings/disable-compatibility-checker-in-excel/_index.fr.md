---
title: Désactiver le vérificateur de compatibilité dans Excel avec C++
linktitle: Désactiver le vérificateur de compatibilité
type: docs
weight: 170
url: /fr/cpp/disable-compatibility-checker-in-excel/
description: Cet article montre comment désactiver le vérificateur de compatibilité via l API Aspose.Cells for C++.
keywords: C++ Désactivation du vérificateur de compatibilité, Excel Désactivation du vérificateur de compatibilité en C++, Désactiver le vérificateur de compatibilité dans le classeur. 
---

## Désactiver le vérificateur de compatibilité dans les feuilles Excel en C++

{{% alert color="primary" %}}

Le vérificateur de compatibilité de Microsoft Excel signale lorsque la sauvegarde d'un fichier dans un format de fichier antérieur pourrait entraîner des problèmes de fonctionnalité ou une perte de fidélité. Le vérificateur de compatibilité est une fonctionnalité de Microsoft Office Excel 2007 et de Microsoft Excel 2010.

Lorsque vous enregistrez un classeur dans une version antérieure, Excel 97 à Excel 2003, à partir d'Excel 2007 ou d'Excel 2010, le vérificateur de compatibilité analyse le classeur pour voir s'il contient des fonctionnalités qui ne sont pas prises en charge par la version antérieure. Pour vous aider à prendre des décisions sur la manière de gérer les problèmes de compatibilité, le vérificateur de compatibilité affiche des boîtes de dialogue avec des options. Il peut également être utilisé pour créer un rapport sur les problèmes dans le classeur, ou désactiver la fonctionnalité.

Parfois, vous devez désactiver le vérificateur de compatibilité pour une feuille de calcul particulière. Avec les API d'Aspose.Cells, vous pouvez le faire de manière programmée afin que les utilisateurs ne soient pas frustrés ou désorientés par la boîte de dialogue du vérificateur de compatibilité qui apparaît lorsqu'ils réenregistrent le fichier dans Microsoft Excel manuellement.

{{% /alert %}}

## **Comment désactiver le vérificateur de compatibilité à l'aide de Microsoft Excel**

Pour désactiver le vérificateur de compatibilité dans Microsoft Excel (par exemple Microsoft Excel 2007/2010) :

- (Excel 2007) Sur le bouton Office, cliquez sur **Préparer**, puis sur **Exécuter le vérificateur de compatibilité**, puis désactivez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.
- (Excel 2010) Sur l'onglet **Fichier**, cliquez sur **Informations**, puis **Vérifier les problèmes**, cliquez sur **Vérifier la compatibilité**, et enfin, désélectionnez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.

## **Comment désactiver le vérificateur de compatibilité à l'aide des API Aspose.Cells**

Définissez la propriété [**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcompatibility/) sur **False** pour désactiver le vérificateur de compatibilité de Microsoft Excel.

### **Exemples de code**

Les exemples de code suivants montrent comment désactiver le vérificateur de compatibilité avec Aspose.Cells for C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open a template file
    U16String templateFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(templateFilePath);

    // Disable the compatibility checker
    workbook.GetSettings().SetCheckCompatibility(false);

    // Path to save the output file
    U16String outputFilePath = srcDir + u"Output_BK_CompCheck.out.xlsx";

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
