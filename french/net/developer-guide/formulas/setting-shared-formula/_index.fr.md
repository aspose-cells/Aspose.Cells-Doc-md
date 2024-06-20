---
title: Paramétrage de formule partagée
type: docs
weight: 10
url: /fr/net/setting-shared-formula/
---

{{% alert color="primary" %}}

Si vous souhaitez ajouter une fonction dans une feuille de calcul qui effectuera des calculs. Cet article explique comment réaliser cette tâche avec Aspose.Cells.

{{% /alert %}}

## Paramétrage de formule partagée avec Aspose.Cells

Supposons que vous ayez une feuille de calcul remplie de données dans le format qui ressemble à la feuille de calcul d'exemple suivante.

|**Fichier d'entrée avec une colonne de données**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Vous souhaitez ajouter une fonction en B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est de **9%**. La formule qui calcule la taxe de vente est: **"=A2*0.09"**. Cet article explique comment appliquer cette formule avec Aspose.Cells.

Aspose.Cells vous permet de spécifier une formule en utilisant la propriété [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula). Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Soit vous faites ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (A3*0.09, A4*0.09, A5*0.09, etc.). Cela nécessite la mise à jour des références de cellule pour chaque ligne. Cela nécessite également à Aspose.Cells de parser chaque formule individuellement, ce qui peut être chronophage pour de grandes feuilles de calcul et des formules complexes. Cela ajoute également des lignes de code supplémentaires bien que les boucles puissent les réduire quelque peu.

Une autre approche est d'utiliser une **formule partagée**. Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellules dans chaque ligne afin que la taxe soit calculée correctement. La méthode [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) est plus efficace que la première méthode.

L'exemple suivant démontre comment l'utiliser.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
