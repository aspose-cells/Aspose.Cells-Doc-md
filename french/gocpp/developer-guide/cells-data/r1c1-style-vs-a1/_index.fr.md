---  
title: Excel – Style de référence R1C1 vs. A1 avec Golang via C++  
linktitle: Style de référence Excel – R1C1 vs A1  
type: docs  
weight: 30  
url: /fr/go-cpp/r1c1-reference-style-vs-a1/  
description: Style de référence R1C1 versus Style A1 en utilisant Aspose.Cells avec Golang via C++.  
keywords: Style de référence R1C1 VS. A1, Style de référence R1C1, Comment basculer entre le style de référence R1C1 et le style de référence A1, Style de référence A1.  
---  

## **Introduction**

Dans Excel, R1C1 et A1 sont deux styles de référence différents utilisés pour identifier les cellules dans une feuille de calcul. Notez que le choix entre A1 et R1C1 relève en grande partie de la préférence personnelle. La plupart des utilisateurs sont plus familiers avec le style A1, mais le R1C1 peut être utile dans certaines situations, surtout lorsqu'il s'agit de formules et de calculs.

## **Style de référence A1**

C'est le style de référence par défaut dans Excel. En style A1, les colonnes sont identifiées par des lettres (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...), et les lignes par des chiffres (1, 2, 3, ...). Par exemple, la cellule dans la première colonne et la deuxième ligne est désignée comme A2.

## **Style de référence R1C1**

Dans le style R1C1, à la fois les lignes et les colonnes sont identifiées par des chiffres. La lettre "R" représente le numéro de la ligne, et la lettre "C" représente le numéro de la colonne. Par exemple, R2C1 fait référence à la cellule dans la deuxième ligne et la première colonne.

Tous les numéros entre crochets désignent la distance relative par rapport à la cellule actuelle. Contrairement à A1 qui fait référence aux colonnes suivies du numéro de ligne, R1C1 fait l'inverse : les lignes suivies des colonnes (ce qui nécessite un certain temps d'adaptation). Les nombres positifs désigneront les cellules en dessous et/ou à droite. Les nombres négatifs désigneront les cellules au-dessus et/ou à gauche.

Par exemple, R[2]C[3] est une cellule 2 lignes en dessous et 3 colonnes à droite. R[-1]C[-4] est une cellule 1 ligne au dessus et 4 colonnes à gauche. Si aucun chiffre n’est indiqué entre crochets, alors vous faites référence à la même ligne ou colonne, c’est-à-dire R[3]C sera une cellule 3 lignes en dessous de la cellule actuelle dans la même colonne.  
<br>  
<image src="2.png" width="70%" />  

## **Comparaison du style de référence R1C1 et du style de référence A1**  
Voici une comparaison rapide :  
|**Style A1**|**Style R1C1**|  
| :- | :- |  
|A1|R1C1  
|B3|R3C2  
|G10|R10C7  
|AA25|R25C27  

## **Comment passer du style de référence R1C1 au style de référence A1**  
Vous pouvez passer entre ces styles de référence dans les paramètres d'Excel. Pour changer le style de référence:

1. Allez dans l'onglet "Fichier".  
1. Sélectionnez "Options" en bas.  
1. Dans la boîte de dialogue Options Excel, allez dans la catégorie "Formules".  
1. Sous la section "Travailler avec des formules", cochez ou décochez l'option "Style de référence R1C1".  
1. Cliquez sur "OK" pour appliquer les modifications.  
<br>  
<image src="1.png" width="70%" />  

## **Comment utiliser le style de référence R1C1 et le style de référence A1 dans Excel**  
L'exemple suivant montre comment calculer la somme de deux valeurs de cellule dans deux styles.  
<br>  
Style de référence A1:  
<br>  
<image src="4.png" width="70%" />  

Style de référence R1C1:  
<br>  
<image src="3.png" width="70%" />  
