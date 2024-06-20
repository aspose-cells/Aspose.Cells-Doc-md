---
title: Copier des lignes et des colonnes
type: docs
weight: 30
url: /fr/java/copying-rows-and-columns/
---

## **Introduction**
Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier toute la feuille de calcul. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes à l'intérieur ou entre les classeurs.

Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, la mise en forme, les cellules masquées, les images et autres objets graphiques sont également copiés.
## **Copie des lignes et des colonnes avec Microsoft Excel**
1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.
1. Pour copier des lignes ou des colonnes, cliquez sur **Copier** dans la barre d'outils **Standard**, ou appuyez sur **CTRL**+**C**.
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.
1. Lorsque vous copiez des lignes ou des colonnes, cliquez sur **Cellules copiées** dans le menu **Insérer**.

{{% alert color="primary" %}} 

Si vous cliquez sur **Coller** dans la barre d'outils **Standard** ou appuyez sur **CTRL**+**V** au lieu de cliquer sur une commande dans le menu **Insérer**, tout contenu des cellules de destination est remplacé.

{{% /alert %}} 

## **Copie d'une seule ligne**

Aspose.Cells fournit la méthode [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) de la classe [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Cette méthode copie tous les types de données, y compris les formules, les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets graphiques de la ligne source à la ligne de destination.

La méthode [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) prend les paramètres suivants :

- l'objet source [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells),
- l'indice de ligne source, et
- l'indice de ligne de destination.

Utilisez cette méthode pour copier une ligne dans une feuille ou vers une autre feuille. La méthode [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) fonctionne de la même manière que Microsoft Excel. Par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, car cette valeur est également copiée.

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un fichier modèle Microsoft Excel et copie la deuxième ligne (complète avec des données, un formatage, des commentaires, des images, etc.) et la colle dans la 12e ligne de la même feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



La sortie suivante est générée lorsque le code ci-dessous est exécuté.

**La ligne est copiée avec le plus haut degré de précision et d'exactitude** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Lors de la copie de lignes, il est important de noter les images, les graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :

1. Si l'indice de la ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'indice de début de la ligne est 4 et l'indice de fin de la ligne est 6).
1. Les images existantes, les graphiques, etc. dans la ligne de destination ne seront pas supprimés.

{{% /alert %}} 

## **Copier plusieurs lignes**

Vous pouvez également copier plusieurs lignes vers une nouvelle destination en utilisant la méthode [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de lignes source à copier.

Ci-dessous est un instantané de la feuille de calcul d'entrée contenant 3 lignes de données, tandis que l'extrait de code fourni ci-dessous copie les 3 lignes vers un nouvel emplacement en commençant à partir de la 7e ligne.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Voici la vue de la feuille de calcul résultante après l'exécution de l'extrait de code ci-dessus.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Copier une seule colonne**

Aspose.Cells fournit la méthode [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) de la classe [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, commentaires, formats de cellule, cellules masquées, images et autres objets graphiques depuis la colonne source vers la colonne de destination.

La méthode [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) prend les paramètres suivants :

- l'objet source [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells),
- indice de la colonne source, et
- indice de la colonne de destination.

Utilisez la méthode [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) pour copier une colonne dans une feuille ou vers une autre feuille.

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.

**Une colonne est copiée d'un classeur à un autre** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Copier plusieurs colonnes**

Similaire à la méthode [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)), les API Aspose.Cells fournissent également la méthode [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) pour copier plusieurs colonnes sources vers un nouvel emplacement.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Voici à quoi ressemblent les feuilles de calcul source et résultante dans Excel.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Coller des lignes/colonnes avec des options de collage**
Aspose.Cells propose désormais [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) lors de l'utilisation des fonctions [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) et [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Cela permet de définir des options de collage appropriées similaires à Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

