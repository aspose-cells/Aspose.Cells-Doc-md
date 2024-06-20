---
title: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 40
url: /fr/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel via la commande de menu **Outils > Signatures numériques...**. De même, vous pouvez le vérifier de manière programmatique en utilisant la méthode [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) d'Aspose.Cells.

{{% /alert %}}

## **Vérifier si le projet VBA dans un classeur est signé**

Le code suivant charge le classeur et vérifie si son projet VBA est signé en utilisant la propriété [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned). La propriété renverra **true** si le projet est signé sinon elle renverra **false**.

## Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
