---
title: Paramétrage de formule partagée
type: docs
weight: 10
url: /fr/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

Si vous souhaitez ajouter une fonction dans la feuille de calcul qui effectuera des calculs. Cet article explique comment réaliser cette tâche en utilisant Aspose.Cells pour Python via .NET.

{{% /alert %}}

## Définir une formule partagée avec Aspose.Cells pour Python via .NET

Supposons que vous ayez une feuille de calcul remplie de données dans le format qui ressemble à la feuille de calcul d'exemple suivante.

|**Fichier d'entrée avec une colonne de données**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Vous souhaitez ajouter une fonction dans B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est de **9%**. La formule qui calcule la taxe de vente est : **"=A2*0.09"**. Cet article explique comment appliquer cette formule avec Aspose.Cells pour Python via .NET.

Aspose.Cells pour Python via .NET vous permet de spécifier une formule en utilisant la propriété [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula). Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) dans la colonne.

Soit faites ce que vous avez fait pour la première cellule, en configurant effectivement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (A3*0.09, A4*0.09, A5*0.09, etc.). Cela nécessite que les références de cellules pour chaque ligne soient mises à jour. Cela nécessite également qu'Aspose.Cells pour Python via .NET analyse chaque formule individuellement, ce qui peut prendre du temps pour de grands tableaux et des formules complexes. Il ajoute également des lignes de code supplémentaires, bien que des boucles puissent réduire cela dans une certaine mesure.

Une autre approche est d'utiliser une **formule partagée**. Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellules dans chaque ligne afin que la taxe soit calculée correctement. La méthode [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) est plus efficace que la première méthode.

L'exemple suivant démontre comment l'utiliser.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

