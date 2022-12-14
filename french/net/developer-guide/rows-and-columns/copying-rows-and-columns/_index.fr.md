---
title: Copier des lignes et des colonnes
type: docs
weight: 40
url: /fr/net/copying-rows-and-columns/
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

## **Coller des lignes et des colonnes à l'aide des options de collage avec Microsoft Excel**

1. Sélectionnez les cellules qui contiennent les données ou d'autres attributs que vous souhaitez copier.
1.  Dans l'onglet Accueil, cliquez sur**Copie**.
1.  Cliquez sur la première cellule de la zone où vous souhaitez**pâte** ce que vous avez copié.
1.  Dans l'onglet Accueil, cliquez sur la flèche à côté de**Pâte** , puis sélectionnez**Pâte** Spécial.
1.  Sélectionnez le**choix** tu veux.

## **En utilisant Aspose.Cells**

## **Copier des lignes uniques**

 Aspose.Cells fournit le[**CopieRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classer. Cette méthode copie tous les types de données, y compris les formules, les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets de dessin de la ligne source vers la ligne de destination.

 La[**CopieRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)méthode prend les paramètres suivants :

-  la source[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objet,
- l'index de la ligne source, et
- l'index de la ligne de destination.

 Utilisez cette méthode pour copier une ligne dans une feuille ou dans une autre feuille. La[**CopieRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)La méthode fonctionne de la même manière que Microsoft Excel. Ainsi, par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un modèle de fichier Excel Microsoft et copie la deuxième ligne (complète avec les données, le formatage, les commentaires, les images, etc.) et le colle à la 12e ligne de la même feuille de calcul.

 Vous pouvez ignorer l'étape qui obtient la hauteur de la ligne source à l'aide de la[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) puis définit la hauteur de la ligne de destination à l'aide de la méthode[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) méthode comme la[**CopieRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)prend automatiquement en charge la hauteur de la ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Lors de la copie de lignes, il est important de noter les images, graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :

1. Si l'index de ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'index de ligne de début est 4 et l'index de ligne de fin est 6).
1. Les images, graphiques, etc. existants dans la ligne de destination ne seront pas supprimés.

{{% /alert %}}

## **Copie de plusieurs lignes**

Vous pouvez également copier plusieurs lignes vers une nouvelle destination tout en utilisant le[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)méthode qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de lignes source à copier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Copier des colonnes**

 Aspose.Cells fournit le[**CopierColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe, cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets de dessin de la colonne source vers la colonne de destination.

 La[**CopierColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)méthode prend les paramètres suivants :

-  la source[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objet,
- index de colonne source, et
- l'index de la colonne de destination.

 Utilisez le[**CopierColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)méthode pour copier une colonne dans une feuille ou vers une autre feuille.

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Copie de plusieurs colonnes**

 Semblable à[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) méthode, les API Aspose.Cells fournissent également la[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)méthode afin de copier plusieurs colonnes source vers un nouvel emplacement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Collage de lignes/colonnes avec les options de collage**

 Aspose.Cells fournit maintenant[**CollerOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) lors de l'utilisation des fonctions[**Copier les lignes**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) et[**CopierColonnes**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Il permet de définir l'option de collage appropriée similaire à Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

