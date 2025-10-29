---
title: Insérer des liens hypertexte dans Excel ou OpenOffice
linktitle: Gérer les liens hypertexte
type: docs
weight: 45
url: /fr/python-net/insert-hyperlinks-to-excel/
description: Comment insérer des liens hypertexte dans un fichier Excel avec la bibliothèque Aspose.Cells pour Python via .NET sans MS Excel.
keywords: Bibliothèque Python Excel, Insérer des Hyperliens en Excel avec Python, Ajouter ou Insérer des Hyperliens avec Python, Ajouter ou Insérer un lien vers une URL avec Python, Ajouter ou Insérer un Lien vers une Cellule avec Python, Ajouter un Lien vers un Fichier Externe avec Python
---

{{% alert color="primary" %}} 

Un lien hypertexte est utilisé pour créer un lien entre deux entités. Tout le monde est familier avec l'utilisation des liens hypertexte, en particulier sur les sites Internet.
En utilisant Aspose.Cells pour Python via .NET, les développeurs peuvent créer différents types d'hyperliens dans les fichiers Microsoft Excel. Ce sujet traite des types d'hyperliens pris en charge par Aspose.Cells pour Python via .NET et de la manière dont ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}} 
## **Comment ajouter des hyperliens**
Aspose.Cells pour Python via .NET permet aux développeurs d'ajouter des hyperliens aux fichiers Excel soit en utilisant l'API, soit en utilisant des feuilles de calcul créées manuellement et importées dans d'autres feuilles de calcul à l'aide d'Aspose.Cells pour Python via .NET.

Aspose.Cells pour Python via .NET fournit une classe, [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit différentes méthodes pour ajouter différents hyperliens aux fichiers Excel.

## **Comment ajouter un lien vers une URL**
La classe [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) contient une collection [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) . Chaque élément de la collection [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) représente un [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). Ajoutez des hyperliens vers des URL en appelant la méthode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) de la collection [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). La méthode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage d'hyperliens
- URL, l'adresse URL.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

Dans l'exemple ci-dessus, un lien hypertexte est ajouté à une URL dans une cellule vide, ** A1 **. Dans de tels cas, si une cellule est vide, l'adresse URL est également ajoutée à cette cellule vide en tant que sa valeur. Si la cellule n'est pas vide et qu'un lien hypertexte est ajouté, la valeur de la cellule ressemble à du texte brut. Pour le faire ressembler à un lien hypertexte, appliquez les paramètres de formatage appropriés sur cette cellule.

{{% /alert %}} 

## **Comment ajouter un lien vers une cellule dans le même fichier**
Il est possible d'ajouter des hyperliens vers des cellules dans le même fichier Excel en appelant la méthode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) de la collection [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). La méthode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) fonctionne pour les hyperliens internes et externes. Une version de la méthode surchargée prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **Comment ajouter un lien vers un fichier externe**
Il est possible d'ajouter des hyperliens vers des fichiers Excel externes en appelant la méthode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) de la collection [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). La méthode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Sujets avancés**
- [Ajouter des hyperliens d'image](/cells/fr/python-net/add-image-hyperlinks/)
- [Détecter le type de lien hypertexte](/cells/fr/python-net/detect-hyperlink-type/)
- [Modifier les hyperliens de la feuille de calcul](/cells/fr/python-net/editing-hyperlinks-of-worksheet/)
- [Obtenir des hyperliens dans la plage](/cells/fr/python-net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="python-net" >}}
