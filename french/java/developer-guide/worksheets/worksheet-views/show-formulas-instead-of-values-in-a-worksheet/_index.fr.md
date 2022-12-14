---
title: Afficher des formules au lieu de valeurs dans une feuille de calcul
type: docs
weight: 100
url: /fr/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

Il est possible d'afficher des formules au lieu de valeurs calculées dans Microsoft Excel en utilisant t*Afficher les formules* option de la**Formules**ruban. Lorsque les formules sont affichées, Microsoft Excel affiche les formules dans la feuille de calcul. Vous pouvez obtenir la même chose en utilisant Aspose.Cells.

{{% /alert %}} 

Aspose.Cells fournit un[**Feuille de calcul.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) propriété. Réglez ceci sur**vrai**pour définir Microsoft Excel pour afficher les formules.

L'image suivante montre la feuille de calcul qui contient une formule dans la cellule A3 : =Sum(A1:A2).

**Feuille de calcul avec formule dans la cellule A3**

![tâche : image_autre_texte](show-formulas-instead-of-values-in-a-worksheet_1.png)

 L'image suivante montre la formule au lieu de la valeur calculée, activée en définissant le[**Feuille de calcul.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) propriété à**vrai** au Aspose.Cells.

**La feuille de calcul affiche maintenant la formule au lieu de la valeur calculée**

![tâche : image_autre_texte](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
