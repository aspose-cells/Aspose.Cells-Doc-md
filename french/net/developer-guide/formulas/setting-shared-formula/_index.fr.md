---
title: Définition d'une formule partagée
type: docs
weight: 10
url: /fr/net/setting-shared-formula/
---
{{% alert color="primary" %}}

Si vous souhaitez ajouter une fonction dans la feuille de calcul qui effectuera des calculs. Cet article explique comment réaliser cette tâche en utilisant Aspose.Cells.

{{% /alert %}}

## Définition de la formule partagée à l'aide de Aspose.Cells

Supposons que vous disposiez d'une feuille de calcul remplie de données au format qui ressemble à l'exemple de feuille de calcul suivant.

|**Fichier d'entrée avec une colonne ou des données**|
|:- |
|![tâche : image_autre_texte](setting-shared-formula_1.png)|

 Vous souhaitez ajouter une fonction dans B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est**9%** La formule qui calcule la taxe de vente est :**"=A2*0.09"**. Cet article explique comment appliquer cette formule avec le Aspose.Cells.

 Aspose.Cells vous permet de spécifier une formule à l'aide de la[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)la propriété. Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Faites ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (A3*0,09, A4*0,09, A5*0,09 et ainsi de suite). Cela nécessite que les références de cellule de chaque ligne soient mises à jour. Il nécessite également Aspose.Cells pour analyser chaque formule individuellement, ce qui peut prendre du temps pour les feuilles de calcul volumineuses et les formules complexes. Il ajoute également des lignes de codes supplémentaires bien que les boucles puissent les réduire quelque peu.

 Une autre approche consiste à utiliser un**formule partagée** Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellule dans chaque ligne afin que la taxe soit calculée correctement. Le[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)méthode est plus efficace que la première méthode.

L'exemple suivant montre comment l'utiliser.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
