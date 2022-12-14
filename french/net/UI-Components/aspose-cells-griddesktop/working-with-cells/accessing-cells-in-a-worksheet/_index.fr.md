---
title: Accéder à Cells dans une feuille de calcul
type: docs
weight: 10
url: /fr/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

Jusqu'à présent, nous avons discuté de l'utilisation de feuilles de calcul, de lignes et de colonnes, mais il est temps d'approfondir et de parler des cellules. Ainsi, dans cette rubrique, nous commencerions notre discussion sur les cellules avec une fonctionnalité de base d'accès aux cellules.

{{% /alert %}} 
## **Accéder à Cells dans une feuille de calcul**
Nous pouvons accéder à n'importe quelle cellule d'une feuille de calcul en utilisant le API de Aspose.Cells.GridDesktop. Il pourrait y avoir trois façons possibles d'accéder aux cellules comme suit :

- **Utilisation du nom Cell**
- **Utilisation des indices de ligne et de colonne de Cell**
- **Se concentrer Cell**

Discutons de toutes les trois approches ci-dessus une par une.
### **Utilisation du nom Cell**
 Toutes les cellules d'une feuille de calcul ont un nom unique. Par exemple, A1, A2, B1, B2 etc. Aspose.Cells.GridDesktop permet aux développeurs d'accéder à n'importe quelle cellule souhaitée en utilisant son nom de cellule. Tout ce que nous avons à faire est de simplement passer le nom de la cellule (en tant qu'index) au**Cells** collecte de la**Feuille de travail**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Utilisation des indices de ligne et de colonne de Cell**
 Une cellule d'une feuille de calcul peut également être reconnue à l'aide de son emplacement en termes d'indices de ligne et de colonne. Tout ce que nous avons à faire est de simplement passer les indices de ligne et de colonne de la cellule au**Cells** collecte de la**Feuille de travail**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **Se concentrer Cell**
 Si vous ne savez pas exactement quelle cellule doit être accessible. Ensuite, Aspose.Cells.GridDesktop vous permet également d'accéder à une cellule qui est actuellement au centre d'un utilisateur. À l'aide de cette fonctionnalité, vous pouvez autoriser un utilisateur à sélectionner n'importe quelle cellule, puis vous pouvez accéder à cette cellule au niveau du backend. Il peut être obtenu simplement en utilisant**GetFocusedCell** méthode de la**Feuille de travail**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
