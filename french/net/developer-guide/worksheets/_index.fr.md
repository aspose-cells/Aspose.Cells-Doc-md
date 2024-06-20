---
title: Gérer les feuilles de calcul des fichiers Microsoft Excel
linktitle: Feuilles de calcul
type: docs
weight: 90
url: /fr/net/manage-worksheets/
description: Ajouter une feuille de calcul, supprimer une feuille de calcul et activer une feuille à l aide d Aspose.Cells.
---


{{% alert color="primary" %}}

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans les fichiers Microsoft Excel de manière programmatique en utilisant l'API flexible d'Aspose.Cells. Ce sujet décrit les approches pour ajouter et supprimer des feuilles de calcul dans les fichiers Microsoft Excel.

{{% /alert %}}

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul.

## **Ajout de feuilles de calcul à un nouveau fichier Excel**

Pour créer un nouveau fichier Excel de manière programmatique:

1. Créez un objet de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Appelez la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Une feuille de calcul vide est ajoutée au fichier Excel automatiquement. Elle peut être référencée en passant l'index de la feuille de calcul nouvellement créée à la collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets).
1. Obtenez une référence de feuille de calcul.
1. Travaillez sur les feuilles de calcul.
1. Enregistrez le nouveau fichier Excel avec les nouvelles feuilles de calcul en appelant la méthode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Ajout de feuilles de calcul à une feuille de calcul Designer**

Le processus d'ajout de feuilles de calcul à une feuille de calcul Design est le même que celui de l'ajout d'une nouvelle feuille de calcul, sauf que le fichier Excel existe déjà et doit être ouvert avant d'ajouter des feuilles de calcul. Une feuille de calcul Design peut être ouverte par la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Accéder aux feuilles de calcul en utilisant le nom de la feuille**

Accédez à n'importe quelle feuille de calcul en spécifiant son nom ou son index.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Suppression des feuilles de calcul en utilisant le nom de la feuille**

Pour supprimer des feuilles de calcul d'un fichier, appelez la méthode [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Passez le nom de la feuille à la méthode [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) pour supprimer une feuille de calcul spécifique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Suppression des feuilles de calcul en utilisant l'indice de la feuille**

La suppression des feuilles de calcul par nom fonctionne bien lorsque le nom de la feuille de calcul est connu. Si vous ne connaissez pas le nom de la feuille de calcul, utilisez une version surchargée de la méthode [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) qui prend l'index de la feuille de calcul au lieu de son nom de feuille.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Activation des feuilles et mise en place d'une cellule active dans la feuille de calcul**

Parfois, vous avez besoin qu'une feuille de calcul spécifique soit active et affichée lorsque l'utilisateur ouvre un fichier Microsoft Excel dans Excel. De même, vous voudrez peut-être activer une cellule spécifique et définir les barres de défilement pour afficher la cellule active.
Aspose.Cells est capable d'effectuer toutes ces tâches.

Une **feuille active** est une feuille sur laquelle vous travaillez : le nom de la feuille active sur l'onglet est en gras par défaut.

Une **cellule active** est une cellule sélectionnée, la cellule dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est mise en évidence par une bordure épaisse.

### **Activation des feuilles et mise en avant d'une cellule**

Aspose.Cells fournit des appels API spécifiques pour activer une feuille et une cellule. Par exemple, la propriété [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) est utile pour définir la feuille active dans un classeur.
De même, la propriété [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) est utilisée pour définir et obtenir une cellule active dans la feuille de calcul.

Pour vous assurer que les barres de défilement horizontales ou verticales se trouvent à la position de l'index de ligne et de colonne que vous souhaitez afficher des données spécifiques, utilisez les propriétés [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) et [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn).

L'exemple suivant montre comment activer une feuille de calcul et mettre en avant une cellule active. Dans la sortie générée, les barres de défilement seront scrollées pour que la 2ème ligne et la 2ème colonne soient leur première ligne et colonne visibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Sujets avancés**
- [Copier et Déplacer des Feuilles de calcul](/cells/fr/net/copying-and-moving-worksheets/)
- [Compter le nombre de cellules dans la feuille de calcul](/cells/fr/net/count-number-of-cells-in-the-worksheet/)
- [Détection des Feuilles de calcul vides](/cells/fr/net/detecting-empty-worksheets/)
- [Trouver si la Feuille de calcul est une Feuille de dialogue](/cells/fr/net/find-if-the-worksheet-is-dialog-sheet/)
- [Obtenir l'identifiant unique de la feuille de calcul](/cells/fr/net/get-worksheet-unique-id/)
- [Créer, Manipuler ou Supprimer des Scénarios des Feuilles de calcul](/cells/fr/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestion des Sauts de Page](/cells/fr/net/managing-page-breaks/)
- [Fonctionnalités de Configuration de Page](/cells/fr/net/page-setup-features/)
- [Imprimer plusieurs copies d'une feuille de calcul](/cells/fr/net/print-multiple-copies-of-a-worksheet/)
- [Utiliser la propriété Sheet.SheetId d'OpenXml en utilisant Aspose.Cells](/cells/fr/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Vues de Feuille de calcul](/cells/fr/net/worksheet-views/)

