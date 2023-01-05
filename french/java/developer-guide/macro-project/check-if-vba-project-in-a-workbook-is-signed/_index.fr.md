---
title: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 40
url: /fr/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

 Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel via**Outils > Signatures numériques...** commande de menus. De même, vous pouvez le vérifier par programme en utilisant Aspose.Cells[**Classeur.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) méthode.

{{% /alert %}}

## **Vérifier si le projet VBA dans un classeur est signé**

 Le code suivant charge le classeur et vérifie si son projet VBA est signé à l'aide[**Classeur.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) la propriété. La propriété reviendra**vrai** si le projet est signé sinon il reviendra**faux**.

## Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
