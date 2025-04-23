---
title: Libérer les ressources non gérées du classeur avec Python via .NET
linktitle: Libérer les ressources non gérées
type: docs
weight: 310
url: /fr/python-net/release-unmanaged-resources-of-the-workbook/
description: Découvrez comment libérer correctement les ressources non gérées lors de la manipulation de classeurs Excel avec Aspose.Cells pour Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells fournit la méthode [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) pour libérer les ressources non gérées de l'objet [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Ce modèle est crucial pour gérer des ressources non gérées telles que les poignées de fichiers, les flux ou les allocations mémoire qui ne sont pas automatiquement gérées par le ramasse-miettes de Python.

{{% /alert %}}

La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) implémente le protocole du gestionnaire de contexte de Python pour la gestion des ressources. Vous pouvez soit appeler explicitement la méthode [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) ou utiliser l'instruction `with` de Python pour assurer un nettoyage approprié.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
