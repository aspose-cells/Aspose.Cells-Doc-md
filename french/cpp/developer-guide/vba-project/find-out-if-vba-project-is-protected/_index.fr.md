---  
title: Vérifier si le projet VBA est protégé avec C++  
linktitle: Vérifier si le projet VBA est protégé  
type: docs  
weight: 20  
url: /fr/cpp/find-out-if-vba-project-is-protected/  
description: Vérifiez si le projet VBA d un fichier Excel est protégé en utilisant Aspose.Cells avec C++.  
---  

## **Vérifiez si le projet VBA est protégé en C++**

Vous pouvez déterminer si le projet VBA (Visual Basic Applications) de votre fichier Excel est protégé ou non avec Aspose.Cells en utilisant la propriété [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/).

## **Code d'exemple**

Le code exemple suivant crée un classeur puis vérifie si son projet VBA est protégé ou non. Ensuite, il protège le projet VBA et vérifie de nouveau. Veuillez consulter la sortie de la console pour référence. Avant la protection, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) retourne **faux**, mais après, il retourne **vrai**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook wb;

    // Access the VBA project of the workbook.
    VbaProject vbaProj = wb.GetVbaProject();

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - Before Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    // Protect the VBA project.
    vbaProj.Protect(true, u"11");

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - After Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

Il s'agit de la sortie console du code d'exemple ci-dessus pour référence.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
