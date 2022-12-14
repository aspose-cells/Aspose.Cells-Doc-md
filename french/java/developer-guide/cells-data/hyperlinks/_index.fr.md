---
title: Insérer des hyperliens dans Excel ou OpenOffice
linktitle: Gestion des hyperliens
type: docs
weight: 160
url: /fr/java/insert-hyperlinks-to-excel/
---
## **Ajout d'hyperliens aux données de lien**
{{% alert color="primary" %}} 

Un lien hypertexte permet de créer un lien entre deux entités. Tout le monde connaît l'utilisation des hyperliens, en particulier sur les sites Web.

En utilisant Aspose.Cells, les développeurs peuvent créer différents types d'hyperliens dans les fichiers Excel Microsoft. Cette rubrique explique quels types d'hyperliens sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}} 
## **Ajout d'hyperliens**
Trois types d'hyperliens peuvent être ajoutés à une cellule à l'aide du Aspose.Cells :

- [Ajouter un lien vers une URL](/cells/fr/java/working-with-hyperlinks-to-link-data/).
- [Ajouter un lien vers une autre cellule dans le même fichier](/cells/fr/java/working-with-hyperlinks-to-link-data/).
- [Ajouter un lien vers un fichier externe](/cells/fr/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells permet aux développeurs d'ajouter des liens hypertexte vers des fichiers Excel soit en utilisant le API ou[feuilles de calcul de concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/)(feuilles de calcul où les hyperliens sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles de calcul).

Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)La classe fournit différentes méthodes pour ajouter différents liens hypertexte aux fichiers Excel.
## **Ajouter un lien à une URL**
 La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe contient un[Hyperliens](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) le recueil. Chaque élément de la[Hyperliens](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) la collection représente un[Lien hypertexte](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . Ajoutez des hyperliens aux URL en appelant le[Hyperliens](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) de la collection[Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )méthode. La[Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes de cette plage de liens hypertexte
- URL, l'adresse URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 Dans l'exemple ci-dessus, un lien hypertexte est ajouté à une URL dans une cellule vide,**A1**Dans de tels cas, si une cellule est vide, l'adresse URL est également ajoutée à cette cellule vide en tant que valeur. Si la cellule n'est pas vide et qu'un lien hypertexte est ajouté, la valeur de la cellule ressemble à du texte brut. Pour le faire ressembler à un lien hypertexte, appliquez les paramètres de mise en forme appropriés sur cette cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Ajout d'un lien vers un Cell dans le même fichier**
 Il est possible d'ajouter des hyperliens vers des cellules d'un même fichier Excel en appelant le[Hyperliens](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) de la collection[Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )méthode. La[Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) fonctionne à la fois pour les hyperliens internes et externes. Une version de la méthode surchargée prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Ajouter un lien vers un fichier externe**
 Il est possible d'ajouter des hyperliens vers des fichiers Excel externes en appelant le[Hyperliens](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) de la collection[Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )méthode. La[Ajouter](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Sujets avancés**
- [Ajouter des hyperliens d'image](/cells/fr/java/add-image-hyperlinks/)
- [Détecter le type de lien hypertexte](/cells/fr/java/detect-hyperlink-type/)
- [Modification des liens hypertexte de la feuille de calcul](/cells/fr/java/editing-hyperlinks-of-worksheet/)
- [Obtenir des hyperliens dans la plage](/cells/fr/java/get-hyperlinks-in-range/)


