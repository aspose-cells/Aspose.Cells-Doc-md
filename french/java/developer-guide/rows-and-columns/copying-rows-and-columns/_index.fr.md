---
title: Copier des lignes et des colonnes
type: docs
weight: 30
url: /fr/java/copying-rows-and-columns/
---
## **Introduction**
Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier la totalité de la feuille de calcul. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes dans ou entre des classeurs.

Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, le formatage, les cellules masquées, les images et d'autres objets de dessin sont également copiés.
## **Copier des lignes et des colonnes avec Microsoft Excel**
1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.
1.  Pour copier des lignes ou des colonnes, cliquez sur**Copie** sur le**Standard** barre d'outils ou appuyez sur**CTRL**+**C**.
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.
1.  Lorsque vous copiez des lignes ou des colonnes, cliquez sur**Copié Cells** sur le**Insérer** menu.

{{% alert color="primary" %}} 

 Si vous cliquez**Pâte** sur le**Standard** barre d'outils ou appuyez sur**CTRL**+** V** au lieu de cliquer sur une commande sur le**Menu Insertion**, tout contenu des cellules de destination est remplacé.

{{% /alert %}} 

## **Copie d'une seule ligne**

 Aspose.Cells fournit le[copierRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) méthode de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)classer. Cette méthode copie tous les types de données, y compris les formules, les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets de dessin de la ligne source vers la ligne de destination.

 La[copierRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) prend les paramètres suivants :

-  la source[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)objet,
- l'index de la ligne source, et
- l'index de la ligne de destination.

 Utilisez cette méthode pour copier une ligne dans une feuille ou dans une autre feuille. La[copierRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) fonctionne de manière similaire à Microsoft Excel. Ainsi, par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un modèle de fichier Excel Microsoft et copie la deuxième ligne (complète avec les données, le formatage, les commentaires, les images, etc.) et le colle à la 12e ligne de la même feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



La sortie suivante est générée lorsque le code ci-dessous est exécuté.

**La ligne est copiée avec le plus haut degré de précision et d'exactitude** 

![tâche : image_autre_texte](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Lors de la copie de lignes, il est important de noter les images, graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :

1. Si l'index de ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'index de ligne de début est 4 et l'index de ligne de fin est 6).
1. Les images, graphiques, etc. existants dans la ligne de destination ne seront pas supprimés.

{{% /alert %}} 

## **Copie de plusieurs lignes**

 Vous pouvez également copier plusieurs lignes vers une nouvelle destination tout en utilisant le[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de lignes source à copier.

Vous trouverez ci-dessous un instantané de la feuille de calcul d'entrée contenant 3 lignes de données, tandis que l'extrait de code fourni ci-dessous copie les 3 lignes vers un nouvel emplacement à partir de la 7e ligne.

![tâche : image_autre_texte](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Voici la vue de feuille de calcul résultante après l'exécution de l'extrait de code ci-dessus.

![tâche : image_autre_texte](copy-rows-and-columns_4.png)

## **Copie d'une seule colonne**

 Aspose.Cells fournit le[copierColonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) méthode de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)classe, cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets de dessin de la colonne source vers la colonne de destination.

 La[copierColonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) prend les paramètres suivants :

-  la source[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)objet,
- index de colonne source, et
- l'index de la colonne de destination.

 Utilisez le[copierColonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) pour copier une colonne dans une feuille ou dans une autre feuille.

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.

**Une colonne est copiée d'un classeur à un autre** 

![tâche : image_autre_texte](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Copie de plusieurs colonnes**

 Semblable à[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) ), les API Aspose.Cells fournissent également la[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) afin de copier plusieurs colonnes source vers un nouvel emplacement.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Voici à quoi ressemblent les feuilles de calcul source et résultante dans Excel.

![tâche : image_autre_texte](copy-rows-and-columns_7.png)

![tâche : image_autre_texte](copy-rows-and-columns_8.png)


## **Collage de lignes/colonnes avec les options de collage**
 Aspose.Cells fournit maintenant[CollerOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) lors de l'utilisation des fonctions[Copier les lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) et[CopierColonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Il permet de définir des options de collage appropriées similaires à Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

