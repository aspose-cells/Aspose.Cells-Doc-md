---
title: Trier les données de la feuille de calcul
type: docs
weight: 80
url: /fr/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb, trier
description: Cet article présente comment trier les données dans GridWeb.
---

{{% alert color="primary" %}} 

Le tri est une fonctionnalité très précieuse en matière de traitement des données. Les données non triées sont une douleur pour les utilisateurs lorsqu'ils recherchent des informations spécifiques. Aspose.Cells.GridWeb prend en charge de puissantes fonctionnalités de tri. Ce sujet traite du tri des données en utilisant l'API Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Tri de données**
Aspose.Cells.GridWeb permet aux développeurs de trier des données horizontalement et verticalement afin que les développeurs puissent trier des données de haut en bas ou de gauche à droite.
### **De haut en bas**
Pour trier les données de haut en bas :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la feuille de calcul que vous souhaitez trier.
1. Triez la plage de données dans n'importe quel ordre (croissant ou décroissant). Assurez-vous de sélectionner l'orientation de haut en bas.

L'exemple ci-dessous trie les données de quatre colonnes d'une feuille de calcul en ordre décroissant. Seules vingt lignes des quatre colonnes sont triées de haut en bas.

Avant d'appliquer le code, la feuille de calcul contient des données non triées.

![todo:image_alt_text](sort-worksheet-data_1.png)

Après l'exécution du code, les données sont triées par ordre croissant.

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **De gauche à droite**
Pour trier les données de gauche à droite :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à votre formulaire Web.
1. Accédez à la feuille de calcul que vous souhaitez trier.
1. Triez la plage de données dans n'importe quel ordre (croissant ou décroissant). Assurez-vous de sélectionner de gauche à droite.

L'exemple ci-dessous trie les données de quatre lignes dans l'ordre croissant. Seules quatre lignes sur sept colonnes sont triées de gauche à droite.

Avant d'appliquer le code, la feuille de calcul contient des données non triées.

![todo:image_alt_text](sort-worksheet-data_3.png)

Après l'exécution du code, les données sont triées par ordre croissant.

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Les exemples ci-dessus démontrent le tri des données sur la base d'une colonne (de haut en bas) ou d'une ligne (de gauche à droite). Aspose.Cells.GridWeb peut également trier les données en fonction de plusieurs colonnes ou lignes. Pour ce faire, passez un tableau d'indices de colonnes ou de lignes à la méthode de tri. Le tri des types de données hybrides est également pris en charge.

{{% /alert %}}
