---
title: Insérer des liens hypertexte dans Excel ou OpenOffice
linktitle: Gérer les liens hypertexte
type: docs
weight: 160
url: /fr/java/insert-hyperlinks-to-excel/
---

## **Ajout de liens hypertexte pour lier des données**
{{% alert color="primary" %}} 

Un lien hypertexte est utilisé pour créer un lien entre deux entités. Tout le monde est familier avec l'utilisation des liens hypertexte, en particulier sur les sites Internet.

En utilisant Aspose.Cells, les développeurs peuvent créer différents types de liens hypertexte dans les fichiers Microsoft Excel. Ce sujet explique quels types de liens hypertexte sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}} 
## **Ajout de liens hypertexte**
Trois types de liens hypertexte peuvent être ajoutés à une cellule à l'aide d'Aspose.Cells :

- [Ajout d'un lien vers une URL](/cells/fr/java/working-with-hyperlinks-to-link-data/).
- [Ajout d'un lien vers une autre cellule dans le même fichier](/cells/fr/java/working-with-hyperlinks-to-link-data/).
- [Ajout d'un lien vers un fichier externe](/cells/fr/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells permet aux développeurs d'ajouter des liens hypertexte aux fichiers Excel soit en utilisant l'API soit des [feuilles de calcul conçues](/cells/fr/java/what-is-a-designer-spreadsheet/) (feuilles de calcul où les liens hypertexte sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles de calcul).

Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit différentes méthodes pour ajouter différents liens hypertexte aux fichiers Excel.
## **Ajout de lien vers une URL**
La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) contient une collection [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). Chaque élément dans la collection [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) représente un [Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink). Ajoutez des liens hypertexte vers des URLs en appelant la méthode [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) de la collection [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks). La méthode [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes de cette plage de liens hypertexte
- URL, l'adresse URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


Dans l'exemple ci-dessus, un lien hypertexte est ajouté à une URL dans une cellule vide, **A1**. Dans de tels cas, si une cellule est vide, alors l'adresse URL est également ajoutée à cette cellule vide en tant que valeur. Si la cellule n'est pas vide et qu'un lien hypertexte est ajouté, la valeur de la cellule ressemble à du texte normal. Pour qu'elle ressemble à un lien hypertexte, appliquez les paramètres de mise en forme appropriés sur cette cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Ajouter un lien vers une cellule dans le même fichier**
Il est possible d'ajouter des liens hypertexte à des cellules dans le même fichier Excel en appelant la méthode [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) de la collection [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). La méthode [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) fonctionne à la fois pour les liens hypertexte internes et externes. Une version de la méthode surchargée prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Ajouter un lien vers un fichier externe**
Il est possible d'ajouter des hyperliens vers des fichiers Excel externes en appelant la méthode [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) de la collection [Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)). La méthode [Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) prend les paramètres suivants:

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Sujets avancés**
- [Ajouter des hyperliens d'image](/cells/fr/java/add-image-hyperlinks/)
- [Détecter le type de lien hypertexte](/cells/fr/java/detect-hyperlink-type/)
- [Modifier les hyperliens de la feuille de calcul](/cells/fr/java/editing-hyperlinks-of-worksheet/)
- [Obtenir des hyperliens dans la plage](/cells/fr/java/get-hyperlinks-in-range/)


