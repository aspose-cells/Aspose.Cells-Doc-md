---
title: Copier des lignes et des colonnes
type: docs
weight: 40
url: /fr/net/copying-rows-and-columns/
description: Cet article montre comment copier des lignes et des colonnes à l aide de l API Aspose.Cells for .NET.
keywords: C# Comment copier des lignes et des colonnes, Copier des lignes en C#, Copier des colonnes en utilisant C#, Comment coller des lignes et des colonnes en utilisant Aspose.Cells for .NET, Coller plusieurs lignes et colonnes, Comment copier et coller une seule ligne ou une colonne.
---

## **Introduction**

Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier toute la feuille de calcul. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes à l'intérieur ou entre les classeurs.
Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, la mise en forme, les cellules masquées, les images et autres objets graphiques sont également copiés.

## **Comment copier des lignes et des colonnes avec Microsoft Excel**

1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.
1. Pour copier des lignes ou des colonnes, cliquez sur **Copier** dans la barre d'outils **Standard**, ou appuyez sur **CTRL**+**C**.
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.
1. Lorsque vous copiez des lignes ou des colonnes, cliquez sur **Cellules copiées** dans le menu **Insérer**.

{{% alert color="primary" %}}

Si vous cliquez sur **Coller** dans la barre d'outils **Standard** ou appuyez sur **CTRL**+**V** au lieu de cliquer sur une commande dans le menu **Insérer**, tout contenu des cellules de destination est remplacé.

{{% /alert %}}

## **Comment coller des lignes et des colonnes en utilisant les options de collage avec Microsoft Excel**

1. Sélectionnez les cellules contenant les données ou autres attributs que vous souhaitez copier.
1. Sur l'onglet Accueil, cliquez sur **Copier**.
1. Cliquez sur la première cellule dans la zone où vous souhaitez **coller** ce que vous avez copié.
1. Sur l'onglet Accueil, cliquez sur la flèche à côté de **Coller**, puis sélectionnez **Collage** spécial.
1. Sélectionnez les **options** que vous souhaitez.

## **Comment copier des lignes et des colonnes en utilisant Aspose.Cells for .NET**

## **Comment copier des lignes uniques**

Aspose.Cells fournit la méthode [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Cette méthode copie tous types de données y compris les formules, les valeurs, les commentaires, les formats de cellules, les cellules masquées, les images et autres objets graphiques de la ligne source à la ligne de destination.

La méthode [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) prend les paramètres suivants :

- l'objet de la source [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells),
- l'indice de ligne source, et
- l'indice de ligne de destination.

Utilisez cette méthode pour copier une ligne dans une feuille de calcul, ou vers une autre feuille. La méthode [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) fonctionne de manière similaire à Microsoft Excel. Par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un fichier modèle Microsoft Excel et copie la deuxième ligne (complète avec des données, un formatage, des commentaires, des images, etc.) et la colle dans la 12e ligne de la même feuille de calcul.

Vous pouvez sauter l'étape qui obtient la hauteur de la ligne source en utilisant la méthode [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) et ensuite définir la hauteur de la ligne de destination en utilisant la méthode [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) car la méthode [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) prend automatiquement soin de la hauteur de la ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Lors de la copie de lignes, il est important de noter les images, les graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :

1. Si l'indice de la ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'indice de début de la ligne est 4 et l'indice de fin de la ligne est 6).
1. Les images existantes, les graphiques, etc. dans la ligne de destination ne seront pas supprimés.

{{% /alert %}}

## **Comment copier plusieurs lignes**

Vous pouvez également copier plusieurs lignes sur une nouvelle destination tout en utilisant la méthode [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de lignes sources à copier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Comment copier des colonnes**

Aspose.Cells fournit la méthode [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, les formats de cellules, les cellules masquées, les images et autres objets de dessin de la colonne source à la colonne de destination.

La méthode [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) prend les paramètres suivants :

- l'objet de la source [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells),
- indice de la colonne source, et
- indice de la colonne de destination.

Utilisez la méthode [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) pour copier une colonne dans une feuille de calcul ou vers une autre feuille.

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Comment copier plusieurs colonnes**

Similaire à la méthode [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index), les API Aspose.Cells fournissent également la méthode [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) pour copier plusieurs colonnes sources vers un nouvel emplacement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Comment coller des lignes et des colonnes avec des options de collage**

Aspose.Cells fournit maintenant [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) tout en utilisant les fonctions [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) et [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Il permet de définir une option de collage appropriée similaire à Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
