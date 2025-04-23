---
title: Afficher les formules au lieu des valeurs dans une feuille de calcul
type: docs
weight: 100
url: /fr/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

Il est possible d'afficher des formules au lieu des valeurs calculées dans Microsoft Excel en utilisant l'option *Afficher les formules* du ruban **Formules**. Lorsque les formules sont affichées, Microsoft Excel affiche les formules dans la feuille de calcul. Vous pouvez obtenir le même résultat en utilisant Aspose.Cells.

{{% /alert %}} 

Aspose.Cells fournit une propriété [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas). Définissez-la sur **true** pour demander à Microsoft Excel d'afficher les formules.

L'image suivante montre la feuille de calcul qui contient une formule dans la cellule A3 : =Somme(A1:A2).

**Feuille de calcul avec une formule dans la cellule A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

L'image suivante montre la formule au lieu de la valeur calculée, activée en définissant la propriété [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) sur **true** avec Aspose.Cells.

**La feuille de calcul affiche maintenant la formule au lieu de la valeur calculée**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
