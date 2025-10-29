---  
title: Vérifier si le code VBA est signé avec C++  
linktitle: Vérifier si le code VBA est signé  
type: docs  
weight: 100  
url: /fr/cpp/check-if-vba-code-is-signed/  
description: Apprenez comment vérifier si le code VBA dans les fichiers Excel est signé en utilisant Aspose.Cells avec C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells permet à l'utilisateur de vérifier si le projet de code VBA est signé ou non. Veuillez utiliser la propriété [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) pour vérifier si le projet de code VBA est signé ou non.  

{{% /alert %}}  

Le code suivant explique comment vérifier si le code VBA est signé ou non en utilisant la propriété [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/). Vous pouvez utiliser n'importe quel de vos fichiers Excel pour tester ce code. Pour les tests, vous pouvez utiliser [ce fichier Excel utilisé dans le code](5115032.xlsm).  

## **Vérifier si le code VBA est signé en C++**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## Sortie de la console  

Ci-dessous se trouve la sortie de la console du code ci-dessus en utilisant le [fichier excel d'exemple](5115032.xlsm) fourni par le lien.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
