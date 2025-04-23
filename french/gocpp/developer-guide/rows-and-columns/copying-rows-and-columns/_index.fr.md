---
title: Copier des lignes et des colonnes
type: docs
weight: 20
url: /fr/go-cpp/copying-rows-and-columns/
---

## **Introduction**

Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier la feuille de calcul entière. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes à l'intérieur ou entre des classeurs.
Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, le formatage, les cellules masquées, les images et autres objets graphiques sont également copiés.

## **Copie des lignes et des colonnes avec Microsoft Excel**

1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.
1. Pour copier des lignes ou des colonnes, cliquez sur **Copier** dans la barre d'outils **Standard**, ou appuyez sur **CTRL**+**C**.
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.
1. Lorsque vous copiez des lignes ou des colonnes, cliquez sur **Cellules copiées** dans le menu **Insérer**.

{{% alert color="primary" %}}

Si vous cliquez sur **Coller** dans la barre d'outils **Standard** ou appuyez sur **CTRL**+**V** au lieu de cliquer sur une commande dans le menu **Insertion**, le contenu des cellules de destination est remplacé.

{{% /alert %}}

## **Utilisation d'Aspose.Cells**

### **Copier des lignes**

Aspose.Cells fournit la méthode CopyRow de la classe Aspose::Cells::ICells. Cette méthode copie tous les types de données, y compris les formules, les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets graphiques de la ligne source à la ligne de destination.

La méthode CopyRow prend les paramètres suivants:

- l'objet Cells source,
- l'indice de ligne source, et
- l'indice de ligne de destination.

Utilisez cette méthode pour copier une ligne dans une feuille ou vers une autre feuille. La méthode CopyRow fonctionne de manière similaire à Microsoft Excel. Par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un fichier modèle Microsoft Excel et copie la deuxième ligne (avec des données, des formats, des commentaires, des images, etc.) et la colle dans la 12e ligne de la même feuille de calcul.

Vous pouvez ignorer l'étape qui récupère la hauteur de la ligne source en utilisant la méthode **GetRowHeigh** puis définit la hauteur de la ligne de destination en utilisant la méthode **SetRowHeight** car la méthode **CopyRow** prend automatiquement en charge la hauteur de la ligne.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyingRows.go" >}}

{{% alert color="primary" %}}

Lors de la copie de lignes, il est important de prendre en compte les images, graphiques ou autres objets de dessin associés, de la même manière qu'avec Microsoft Excel :

1. Si l'index de ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'index de ligne de départ est 4 et l'index de ligne de fin est 6).
1. Les images, graphiques, etc. existants dans la ligne de destination ne seront pas supprimés.

{{% /alert %}}

### **Copier des colonnes**

Aspose.Cells fournit la méthode CopyColumn de la classe ICells; cette méthode copie tous les types de données, y compris les formules — avec des références actualisées — et les valeurs, commentaires, formats de cellule, cellules cachées, images et autres objets de dessin de la colonne source vers la colonne de destination.

La méthode CopyColumn prend les paramètres suivants:

- l'objet Cells source,
- indice de la colonne source, et
- indice de la colonne de destination.

Utilisez la méthode CopyColumn pour copier une colonne dans une feuille ou vers une autre feuille.

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyingColumns.go" >}}
