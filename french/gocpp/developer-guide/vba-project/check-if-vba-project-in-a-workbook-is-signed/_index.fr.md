---
title: Vérifiez si le projet VBA dans un classeur est signé avec Golang via C++
linktitle: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 70
url: /fr/go-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Vérifiez si le projet VBA dans un classeur est signé en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel via la commande **Tools > Digital Signatures...** menu. De même, vous pouvez le vérifier de manière programmatique avec Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/issigned/).

{{% /alert %}}

## **Vérifier si le projet VBA d’un classeur est signé en C++**

Le code suivant charge le classeur et vérifie si son projet VBA est signé en utilisant la propriété [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/issigned/). La propriété retournera **true** si le projet est signé, sinon elle retournera **false**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfVbaProjectInAWorkbookIsSigned.go" >}}
