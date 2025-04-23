---
title: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 70
url: /fr/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel, via le menu **Outils > Signatures numériques...**. De même, il est possible de le vérifier par programmation en utilisant la propriété [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed) d’Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Vérifiez si le projet VBA d'un classeur est signé en Python**

Le code suivant charge le classeur et vérifie si son projet VBA est signé en utilisant la propriété [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed). La propriété renverra **true** si le projet est signé sinon elle renverra **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

