---
title: Libérer les ressources non gérées du classeur avec Golang via C++
linktitle: Libérer les ressources non gérées du classeur
type: docs
weight: 310
url: /fr/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Apprenez à libérer les ressources non gérées du classeur en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells fournit la méthode [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) pour libérer les ressources non managées de l'objet [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Le modèle de libération est utilisé uniquement pour les objets qui accèdent à des ressources non managées, telles que des poignées de fichiers et de tubes, des poignées de registre, des poignées d'attente ou des pointeurs vers des blocs de mémoire non gérée. C'est parce que le collecteur de vidanges est très efficace pour récupérer les objets managés inutilisés, mais qu'il est incapable de récupérer les objets non managés.

{{% /alert %}}

L'objet [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) implémente maintenant l'interface *IDisposable* qui a une seule méthode [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/). Vous pouvez soit appeler directement la méthode [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) ou utiliser l'instruction *Using* pour appeler cette méthode automatiquement.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
