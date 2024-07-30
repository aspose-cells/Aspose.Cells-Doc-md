---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/python-net/managing-page-breaks/
description: Cet article fournit un code d exemple et explique comment ajouter des sauts de page, effacer des sauts de page ou supprimer des sauts de page spécifiques dans les feuilles Excel de manière programmable en utilisant Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, sauts de page Python, sauts de page Excel en Python, supprimer un saut de page en Python.
---

{{% alert color="primary" %}}

Selon la définition, un saut de page est un endroit dans un flux de texte où une page se termine et où la page suivante commence. Microsoft Excel permet aux utilisateurs d'ajouter des sauts de page dans n'importe quelle cellule sélectionnée d'une feuille de calcul.

L'emplacement de la cellule où le saut de page est ajouté, la page se termine et le reste des données après le saut de page est imprimé sur la page suivante lors de l'impression. En termes simples, les sauts de page divisent votre feuille de calcul en plusieurs pages selon vos spécifications. Vous pouvez également ajouter des sauts de page à vos feuilles de calcul en temps réel en utilisant Aspose.Cells pour Python via .NET. Aspose.Cells pour Python via .NET permet aux développeurs d'ajouter deux types de sauts de page:

- Saut de page horizontal
- Saut de page vertical

Dans le reste de la discussion, nous décrirons comment vous pouvez ajouter des sauts de page horizontaux ou verticaux dans vos feuilles de calcul en utilisant Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Sauts de page**

Aspose.Cells pour Python via .NET fournit une classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit un large éventail de propriétés et de méthodes utilisées pour gérer une feuille de calcul.

Pour ajouter les sauts de page, utilisez les propriétés de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) et [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks).

Les propriétés [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) et [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) sont des collections qui peuvent contenir plusieurs sauts de page. Chaque collection contient plusieurs méthodes pour gérer les sauts de page horizontaux et verticaux.

## **Comment Ajouter des Sauts de Page**

Pour ajouter un saut de page dans une feuille de calcul, insérez des sauts de page verticaux et horizontaux à la cellule spécifiée en appelant les méthodes [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) et [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str). Chaque méthode **ajout** prend le nom de la cellule où le saut doit être ajouté.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

En mode Aperçu des sauts de page ou Aperçu avant impression, vous pouvez voir comment fonctionnent ces sauts de page.

{{% /alert %}}


## **Important à savoir**

Lorsque vous définissez les propriétés **FitToPages** (c'est-à-dire [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) et [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) dans les paramètres de mise en page, les paramètres de saut de page sont affectés. Ainsi, si vous imprimez la feuille de calcul, les paramètres de saut de page ne sont pas pris en compte bien qu'ils soient toujours définis.
