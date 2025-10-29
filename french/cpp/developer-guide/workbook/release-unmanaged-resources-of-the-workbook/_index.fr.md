---
title: Libérer les ressources non gérées du classeur avec C++
linktitle: Libérer les ressources non gérées du classeur
type: docs
weight: 310
url: /fr/cpp/release-unmanaged-resources-of-the-workbook/
description: Apprenez comment libérer les ressources non gérées du classeur en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells fournit la méthode [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) pour libérer les ressources non managées de l'objet [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Le modèle de libération est utilisé uniquement pour les objets qui accèdent à des ressources non managées, telles que des poignées de fichiers et de tubes, des poignées de registre, des poignées d'attente ou des pointeurs vers des blocs de mémoire non gérée. C'est parce que le collecteur de vidanges est très efficace pour récupérer les objets managés inutilisés, mais qu'il est incapable de récupérer les objets non managés.

{{% /alert %}}

L'objet [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) implémente maintenant l'interface *IDisposable* qui a une seule méthode [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/). Vous pouvez soit appeler directement la méthode [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) ou utiliser l'instruction *Using* pour appeler cette méthode automatiquement.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
