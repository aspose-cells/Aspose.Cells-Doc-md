---
title: Paramétrage de formule partagée
type: docs
weight: 10
url: /fr/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

Supposons que vous ayez une feuille de calcul remplie de données dans le format qui ressemble à la feuille de calcul d'exemple suivante.

Fichier d'entrée avec une colonne ou des données 

![todo:image_alt_text](setting-shared-formula_1.png)

Vous souhaitez ajouter une fonction en B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est de **9%**. La formule qui calcule la taxe de vente est: **"=A2*0.09"**. Cet article explique comment appliquer cette formule avec Aspose.Cells.

{{% /alert %}} 

Aspose.Cells vous permet de spécifier une formule en utilisant la propriété [Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), spécifiquement [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) et [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Faites ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (`A3*0.09`, `A4*0.09`, `A5*0.09` et ainsi de suite). Cela nécessite la mise à jour des références de cellule pour chaque ligne. Cela nécessite également à Aspose.Cells de parser chaque formule individuellement, ce qui peut être chronophage pour les feuilles de calcul volumineuses et les formules complexes. Cela ajoute également des lignes de code supplémentaires, bien que des boucles puissent les réduire quelque peu.

Une autre approche consiste à utiliser une **formule partagée**. Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellules dans chaque ligne afin que la taxe soit calculée correctement. La méthode [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula-java.lang.String-int-int-) est plus efficace que la première méthode.

L'exemple suivant démontre comment l'utiliser. La capture d'écran ci-dessous montre le fichier de sortie.

**Fichier de sortie : formule partagée appliquée** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
