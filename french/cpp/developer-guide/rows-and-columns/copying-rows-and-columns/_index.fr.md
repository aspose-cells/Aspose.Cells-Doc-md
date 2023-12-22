---
title: Copie de lignes et de colonnes
type: docs
weight: 20
url: /fr/cpp/copying-rows-and-columns/
---
##  **Introduction**
Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier l'intégralité de la feuille de calcul. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes dans ou entre des classeurs.
Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec les références mises à jour - et les valeurs, les commentaires, le formatage, les cellules masquées, les images et autres objets de dessin sont également copiés.
##  **Copie de lignes et de colonnes avec Microsoft Excel**
1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.
1.  Pour copier des lignes ou des colonnes, cliquez sur**Copie** sur le**Standard** barre d'outils ou appuyez sur**CTRL**+*C**.
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.
1.  Lorsque vous copiez des lignes ou des colonnes, cliquez sur**Copié Cells** sur le**Insérer** menu.

{{% alert color="primary" %}} 

 Si vous cliquez**Pâte** sur le**Standard** barre d'outils ou appuyez sur**CTRL**+**V** au lieu de cliquer sur une commande sur **Insérer** menu, tout le contenu des cellules de destination est remplacé.

{{% /alert %}} 
##  **En utilisant le Aspose.Cells**
###  **Copie de lignes**
Aspose.Cells fournit la méthode CopyRow de la classe Aspose :: Cells :: ICells. Cette méthode copie tous les types de données, y compris les formules, valeurs, commentaires, formats de cellules, cellules masquées, images et autres objets de dessin, de la ligne source vers la ligne de destination.

La méthode CopyRow prend les paramètres suivants :

- l'objet source Cells,
- l'index de la ligne source, et
- l'index de la ligne de destination.

Utilisez cette méthode pour copier une ligne dans une feuille ou vers une autre feuille. La méthode CopyRow fonctionne de la même manière que Microsoft Excel. Ainsi, par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un modèle de fichier Excel Microsoft et copie la deuxième ligne (avec les données, le formatage, les commentaires, les images, etc.) et la colle dans la 12e ligne de la même feuille de calcul.

 Vous pouvez ignorer l'étape permettant d'obtenir la hauteur de la ligne source à l'aide de l'option**ObtenirRowHeigh** méthode, puis définit la hauteur de la ligne de destination à l'aide de la**Définir la hauteur de la ligne** méthode comme le**Copier la ligne** La méthode prend automatiquement en charge la hauteur de la ligne.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

Lors de la copie de lignes, il est important de noter les images, graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :

1. Si l'index de la ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'index de la ligne de départ est 4 et l'index de la ligne de fin est 6).
1. Les images, graphiques, etc. existants dans la ligne de destination ne seront pas supprimés.

{{% /alert %}} 
###  **Copie de colonnes**
Aspose.Cells fournit la méthode CopyColumn de la classe Aspose::Cells::ICells, cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, commentaires, formats de cellules, cellules masquées, images et autres objets de dessin à partir de la source colonne vers la colonne de destination.

La méthode CopyColumn prend les paramètres suivants :

- l'objet source Cells,
- index de la colonne source, et
- l'index de la colonne de destination.

Utilisez la méthode CopyColumn pour copier une colonne dans une feuille ou vers une autre feuille.

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
