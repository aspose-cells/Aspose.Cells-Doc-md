---
title: Insérer des hyperliens dans Excel ou OpenOffice
linktitle: Gestion des hyperliens
type: docs
weight: 45
url: /fr/net/insert-hyperlinks-to-excel/
description: Comment insérer des hyperliens dans un fichier Excel avec la bibliothèque Aspose.Cells sans MS Excel.
---
{{% alert color="primary" %}} 

Un lien hypertexte permet de créer un lien entre deux entités. Tout le monde connaît l'utilisation des hyperliens, en particulier sur les sites Web.
En utilisant Aspose.Cells, les développeurs peuvent créer différents types d'hyperliens dans les fichiers Excel Microsoft. Cette rubrique explique quels types d'hyperliens sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}} 
## **Ajout d'hyperliens**
Aspose.Cells permet aux développeurs d'ajouter des hyperliens aux fichiers Excel à l'aide des feuilles de calcul API ou de concepteur (feuilles de calcul où les hyperliens sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles de calcul).

 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/net/aspose.cells/worksheet)La classe fournit différentes méthodes pour ajouter différents liens hypertexte aux fichiers Excel.
## **Ajouter un lien à une URL**
 La[Feuille de travail](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe contient un[Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) le recueil. Chaque élément de la[Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) la collection représente un[Lien hypertexte](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Ajoutez des hyperliens aux URL en appelant le[Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) de la collection[Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) méthode. La[Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)méthode prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte
- URL, l'adresse URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 Dans l'exemple ci-dessus, un lien hypertexte est ajouté à une URL dans une cellule vide,**A1**. Dans de tels cas, si une cellule est vide, l'adresse URL est également ajoutée à cette cellule vide en tant que valeur. Si la cellule n'est pas vide et qu'un lien hypertexte est ajouté, la valeur de la cellule ressemble à du texte brut. Pour le faire ressembler à un lien hypertexte, appliquez les paramètres de mise en forme appropriés sur cette cellule.

{{% /alert %}} 
## **Ajout d'un lien vers un Cell dans le même fichier**
 Il est possible d'ajouter des hyperliens vers des cellules d'un même fichier Excel en appelant le[Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) de la collection[Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) méthode. La[Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)La méthode fonctionne pour les hyperliens internes et externes. Une version de la méthode surchargée prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Ajouter un lien vers un fichier externe**
 Il est possible d'ajouter des hyperliens vers des fichiers Excel externes en appelant le[Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) de la collection[Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) méthode. La[Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)méthode prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Sujets avancés**
- [Ajouter des hyperliens d'image](/cells/fr/net/add-image-hyperlinks/)
- [Détecter le type de lien hypertexte](/cells/fr/net/detect-hyperlink-type/)
- [Modification des liens hypertexte de la feuille de calcul](/cells/fr/net/editing-hyperlinks-of-worksheet/)
- [Obtenir des hyperliens dans la plage](/cells/fr/net/get-hyperlinks-in-range/)

