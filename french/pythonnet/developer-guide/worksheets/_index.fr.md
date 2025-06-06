---
title: Gérer les feuilles de calcul des fichiers Microsoft Excel
linktitle: Feuilles de calcul
type: docs
weight: 90
url: /fr/python-net/manage-worksheets/
description: Cet article montre comment gérer les feuilles de calcul des fichiers Microsoft Excel avec l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Gérer les feuilles de calcul des fichiers Microsoft Excel en Python, Ajouter une feuille de calcul en Python, Supprimer une feuille de calcul en Python, Comment ajouter des feuilles de calcul à un nouveau fichier Excel en Python, Comment ajouter des feuilles de calcul à une feuille de calcul prédéfinie en Python, Comment accéder aux feuilles de calcul en utilisant le nom de la feuille en Python, Comment supprimer des feuilles de calcul en utilisant le nom de la feuille en Python, Comment supprimer des feuilles de calcul en utilisant l index de la feuille en Python, Comment activer les feuilles et activer une cellule.
---


{{% alert color="primary" %}}

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans les fichiers Microsoft Excel de manière programmatique en utilisant l'API flexible d'Aspose.Cells. Ce sujet décrit les approches pour ajouter et supprimer des feuilles de calcul dans les fichiers Microsoft Excel.

{{% /alert %}}

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul.

## **Comment ajouter des feuilles de calcul à un nouveau fichier Excel**

Pour créer un nouveau fichier Excel de manière programmatique:

1. Créez un objet de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Appelez la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Une feuille de calcul vide est ajoutée au fichier Excel automatiquement. Elle peut être référencée en passant l'index de la feuille de calcul nouvellement créée à la collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/).
1. Obtenez une référence de feuille de calcul.
1. Travaillez sur les feuilles de calcul.
1. Enregistrez le nouveau fichier Excel avec les nouvelles feuilles de calcul en appelant la méthode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **Comment ajouter des feuilles de calcul à une feuille de calcul prédéfinie**

Le processus d'ajout de feuilles de calcul à une feuille de calcul Design est le même que celui de l'ajout d'une nouvelle feuille de calcul, sauf que le fichier Excel existe déjà et doit être ouvert avant d'ajouter des feuilles de calcul. Une feuille de calcul Design peut être ouverte par la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **Comment accéder aux feuilles de calcul en utilisant le nom de la feuille**

Accédez à n'importe quelle feuille de calcul en spécifiant son nom ou son index.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **Comment supprimer des feuilles de calcul en utilisant le nom de la feuille**

Pour supprimer des feuilles de calcul d'un fichier, appelez la méthode [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Passez le nom de la feuille à la méthode [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) pour supprimer une feuille de calcul spécifique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **Comment supprimer des feuilles de calcul en utilisant l'index de la feuille**

La suppression des feuilles de calcul par le nom fonctionne bien lorsque le nom de la feuille de calcul est connu. Si vous ne connaissez pas le nom de la feuille de calcul, utilisez la méthode [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int) qui prend l'index de la feuille de calcul au lieu de son nom de feuille.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **Comment activer les feuilles et rendre une cellule active dans la feuille de calcul**

Parfois, vous avez besoin qu'une feuille de calcul spécifique soit active et affichée lorsque l'utilisateur ouvre un fichier Microsoft Excel dans Excel. De même, vous voudrez peut-être activer une cellule spécifique et définir les barres de défilement pour afficher la cellule active.
Aspose.Cells est capable d'effectuer toutes ces tâches.

Une **feuille active** est une feuille sur laquelle vous travaillez : le nom de la feuille active sur l'onglet est en gras par défaut.

Une **cellule active** est une cellule sélectionnée, la cellule dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est mise en évidence par une bordure épaisse.

### **Comment activer les feuilles et rendre une cellule active**

Aspose.Cells fournit des appels API spécifiques pour activer une feuille et une cellule. Par exemple, la propriété [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) est utile pour définir la feuille active dans un classeur.
De même, la propriété [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) est utilisée pour définir et obtenir une cellule active dans la feuille de calcul.

Pour vous assurer que les barres de défilement horizontales ou verticales se trouvent à la position de l'index de ligne et de colonne que vous souhaitez afficher des données spécifiques, utilisez les propriétés [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) et [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/).

L'exemple suivant montre comment activer une feuille de calcul et mettre en avant une cellule active. Dans la sortie générée, les barres de défilement seront scrollées pour que la 2ème ligne et la 2ème colonne soient leur première ligne et colonne visibles.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

