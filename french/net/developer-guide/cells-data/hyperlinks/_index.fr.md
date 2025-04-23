---
title: Insérer des liens hypertexte dans Excel ou OpenOffice
linktitle: Gérer les liens hypertexte
type: docs
weight: 45
url: /fr/net/insert-hyperlinks-to-excel/
description: Comment insérer des hyperliens dans un fichier Excel avec la bibliothèque Aspose.Cells sans MS Excel.
keywords: Insérer des hyperliens dans Excel, Ajouter ou insérer des hyperliens, Ajouter ou insérer un lien vers une URL, Ajouter ou insérer un lien vers une cellule, Ajouter un lien vers un fichier externe
---

{{% alert color="primary" %}} 

Un lien hypertexte est utilisé pour créer un lien entre deux entités. Tout le monde est familier avec l'utilisation des liens hypertexte, en particulier sur les sites Internet.
En utilisant Aspose.Cells, les développeurs peuvent créer différents types de liens hypertexte dans les fichiers Microsoft Excel. Ce sujet explique quels types de liens hypertexte sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}} 
## **Ajout de liens hypertexte**
Aspose.Cells permet aux développeurs d'ajouter des hyperliens aux fichiers Excel soit en utilisant l'API, soit des feuilles de calcul conçues (feuilles de calcul où les hyperliens sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles de calcul).

Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit différentes méthodes pour ajouter différents hyperliens aux fichiers Excel.
## **Ajout de lien vers une URL**
La classe [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) contient une collection [Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Chaque élément dans la collection [Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) représente un [Hyperlien](https://reference.aspose.com/cells/net/aspose.cells/hyperlink). Ajoutez des hyperliens vers des URL en appelant la méthode [Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) de la collection [Hyperliens](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). La méthode [Ajouter](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) prend les paramètres suivants:

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage d'hyperliens
- URL, l'adresse URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

Dans l'exemple ci-dessus, un lien hypertexte est ajouté à une URL dans une cellule vide, ** A1 **. Dans de tels cas, si une cellule est vide, l'adresse URL est également ajoutée à cette cellule vide en tant que sa valeur. Si la cellule n'est pas vide et qu'un lien hypertexte est ajouté, la valeur de la cellule ressemble à du texte brut. Pour le faire ressembler à un lien hypertexte, appliquez les paramètres de formatage appropriés sur cette cellule.

{{% /alert %}} 
## **Ajouter un lien vers une cellule dans le même fichier**
Il est possible d'ajouter des hyperliens aux cellules dans le même fichier Excel en appelant la méthode [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) de la collection [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). La méthode [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) fonctionne à la fois pour les hyperliens internes et externes. Une version de la méthode surchargée prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Ajouter un lien vers un fichier externe**
Il est possible d'ajouter des hyperliens à des fichiers Excel externes en appelant la méthode [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) de la collection [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). La méthode [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Sujets avancés**
- [Ajouter des hyperliens d'image](/cells/fr/net/add-image-hyperlinks/)
- [Détecter le type de lien hypertexte](/cells/fr/net/detect-hyperlink-type/)
- [Modifier les hyperliens de la feuille de calcul](/cells/fr/net/editing-hyperlinks-of-worksheet/)
- [Obtenir des hyperliens dans la plage](/cells/fr/net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="csharp" >}}
