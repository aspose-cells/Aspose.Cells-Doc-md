---
title: Définition d'une formule partagée
type: docs
weight: 10
url: /fr/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

Supposons que vous disposiez d'une feuille de calcul remplie de données au format qui ressemble à l'exemple de feuille de calcul suivant.

**Fichier d'entrée avec une colonne ou des données** 

![tâche : image_autre_texte](setting-shared-formula_1.png)

 Vous souhaitez ajouter une fonction dans B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est**9%** La formule qui calcule la taxe de vente est :**"=A2*0.09"**. Cet article explique comment appliquer cette formule avec le Aspose.Cells.

{{% /alert %}} 

 Aspose.Cells vous permet de spécifier une formule à l'aide de la[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) propriété, en particulier[Cell.setFormule()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) et[Cell.getFormule()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Faites ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (A3*0,09, A4*0,09, A5*0,09 et ainsi de suite). Cela nécessite que les références de cellule de chaque ligne soient mises à jour. Il nécessite également Aspose.Cells pour analyser chaque formule individuellement, ce qui peut prendre du temps pour les feuilles de calcul volumineuses et les formules complexes. Il ajoute également des lignes de codes supplémentaires bien que les boucles puissent les réduire quelque peu.

 Une autre approche consiste à utiliser un**formule partagée** Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellule dans chaque ligne afin que la taxe soit calculée correctement. Le[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) méthode est plus efficace que la première méthode.

L'exemple suivant montre comment l'utiliser. La capture d'écran ci-dessous montre le fichier de sortie.

**Fichier de sortie : formule partagée appliquée** 

![tâche : image_autre_texte](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
