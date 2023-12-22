---
title: Excel – Style de référence R1C1 par rapport à A1
type: docs
weight: 30
url: /fr/net/r1c1-reference-style-vs-a1/
description: Style de référence R1C1 VS. Style A1 en utilisant Aspose.Cells for Python via .NET API.
keywords: R1C1 Reference Style VS. A1 style, R1C1 Reference Style, How to switch between R1C1 Reference Style and A1 Reference Style, A1 Reference style.
---
{{% alert color="primary" %}}

Dans Excel, R1C1 et A1 sont deux styles de référence différents utilisés pour identifier les cellules d'une feuille de calcul. Notez que le choix entre A1 et R1C1 est en grande partie une question de préférence personnelle. La plupart des utilisateurs sont plus familiers avec le style A1, mais R1C1 peut être utile dans certaines situations, notamment lorsque vous travaillez avec des formules et des calculs.

{{% /alert %}}

##  **Style de référence A1**

Il s'agit du style de référence par défaut dans Excel. Dans le style A1, les colonnes sont identifiées par des lettres (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...) et les lignes sont identifiées par des chiffres (1, 2, 3, ...).
Par exemple, la cellule de la première colonne et de la deuxième ligne est appelée A2.

##  **Style de référence R1C1**

Dans le style R1C1, les lignes et les colonnes sont identifiées par des chiffres. La lettre « R » représente le numéro de ligne et la lettre « C » représente le numéro de colonne. Par exemple, R2C1 fait référence à la cellule de la deuxième ligne et de la première colonne.

Tous les nombres entre crochets font référence à la distance relative par rapport à la cellule actuelle. Contrairement à A1 qui fait référence à des colonnes suivies d'un numéro de ligne, R1C1 fait le contraire : des lignes suivies de colonnes (ce qui prend un certain temps pour s'y habituer). Les nombres positifs feront référence aux cellules ci-dessous et/ou à droite. Les nombres négatifs feront référence aux cellules situées au-dessus et/ou à gauche.

Par exemple, R[2]C[3] est une cellule 2 lignes vers le bas et 3 colonnes vers la droite. R[-1]C[-4] est une cellule 1 ligne vers le haut et 4 colonnes vers la gauche. Si aucun nombre n'est affiché entre parenthèses, vous faites référence à la même ligne ou colonne, c'est-à-dire que R[3]C sera une cellule 3 lignes en dessous de la cellule actuelle dans la même colonne.
<br>
<image src="2.png" width="70%" />

##  **Comparaison du style de référence R1C1 et du style de référence A1**
Voici une comparaison rapide :
|**Modèle A1**|**Modèle R1C1**|
| :- | :- |
|A1|
|B3|
|G10|
|AA25|

##  **Comment basculer entre le style de référence R1C1 et le style de référence A1**
Vous pouvez basculer entre ces styles de référence dans les paramètres Excel. Pour modifier le style de référence :

1. Allez dans l'onglet "Fichier".
1. Sélectionnez "Options" en bas.
1. Dans la boîte de dialogue Options Excel, accédez à la catégorie "Formules".
1. Dans la section "Travailler avec des formules", cochez ou décochez l'option "Style de référence R1C1".
1. Cliquez sur "OK" pour appliquer les modifications.
<br>
<image src="1.png" width="70%" />

##  **Comment utiliser le style de référence R1C1 et le style de référence A1 dans Excel**
L'exemple suivant montre comment calculer la somme de deux valeurs de cellule dans deux styles.
<br>
Style de référence A1 :
<br>
<image src="4.png" width="70%" />

Style de référence R1C1 :
<br>
<image src="3.png" width="70%" />
