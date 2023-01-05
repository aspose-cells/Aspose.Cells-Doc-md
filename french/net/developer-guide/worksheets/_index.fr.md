---
title: Gérer les feuilles de calcul des fichiers Excel Microsoft.
linktitle: Feuilles de travail
type: docs
weight: 90
url: /fr/net/manage-worksheets/
description: Ajouter une feuille de calcul, supprimer une feuille de calcul et une feuille active à l'aide de Aspose.Cells.
---
{{% alert color="primary" %}}

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans des fichiers Excel Microsoft par programme à l'aide de Aspose.Cells' flexible API. Cette rubrique décrit les approches pour ajouter et supprimer des feuilles de calcul dans des fichiers Excel Microsoft.

{{% /alert %}}

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul.

## **Ajout de feuilles de calcul à un nouveau fichier Excel**

Pour créer un nouveau fichier Excel par programmation :

1.  Créer un objet du[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe.
1.  Appeler le[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) méthode de la[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) classe. Une feuille de calcul vide est automatiquement ajoutée au fichier Excel. Il peut être référencé en passant l'index de feuille de la nouvelle feuille de calcul au[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) le recueil.
1. Obtenir une référence de feuille de travail.
1. Effectuer des travaux sur les feuilles de travail.
1.  Enregistrez le nouveau fichier Excel avec de nouvelles feuilles de calcul en appelant le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**Sauver**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Ajout de feuilles de calcul à une feuille de calcul Designer**

 Le processus d'ajout de feuilles de calcul à une feuille de calcul de concepteur est le même que celui d'ajout d'une nouvelle feuille de calcul, sauf que le fichier Excel existe déjà et doit donc être ouvert avant l'ajout des feuilles de calcul. Une feuille de calcul de concepteur peut être ouverte par le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Accéder aux feuilles de calcul à l'aide du nom de la feuille**

Accédez à n'importe quelle feuille de calcul en spécifiant son nom ou son index.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Suppression de feuilles de calcul à l'aide du nom de la feuille**

Pour supprimer des feuilles de calcul d'un fichier, appelez le[**Supprimer à**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) méthode de[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) classe. Transmettez le nom de la feuille au[**Supprimer à**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)méthode pour supprimer une feuille de calcul spécifique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Suppression de feuilles de calcul à l'aide de l'index des feuilles**

 La suppression de feuilles de calcul par nom fonctionne bien lorsque le nom de la feuille de calcul est connu. Si vous ne connaissez pas le nom de la feuille de calcul, utilisez une version surchargée du[**Supprimer à**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)méthode qui prend l'index de feuille de la feuille de calcul au lieu de son nom de feuille.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Activer des feuilles et rendre actif Cell dans la feuille de calcul**

Parfois, vous avez besoin qu'une feuille de calcul spécifique soit active et affichée lorsqu'un utilisateur ouvre un fichier Excel Microsoft dans Excel. De même, vous souhaiterez peut-être activer une cellule spécifique et définir les barres de défilement pour afficher la cellule active.
Aspose.Cells est capable de faire toutes ces tâches.

 Un**feuille active** est une feuille sur laquelle vous travaillez : le nom de la feuille active sur l'onglet est en gras par défaut.

 Un**cellule active** est une cellule sélectionnée, la cellule dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est mise en évidence par une bordure épaisse.

### **Activer les feuilles et rendre un Cell actif**

Aspose.Cells fournit des appels spécifiques API pour activer une feuille et une cellule. Par exemple, le[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)La propriété est utile pour définir la feuille active dans un classeur.
De la même manière,[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)La propriété est utilisée pour définir et obtenir une cellule active dans la feuille de calcul.

Pour vous assurer que les barres de défilement horizontales ou verticales se trouvent à la position d'index de ligne et de colonne où vous souhaitez afficher des données spécifiques, utilisez la[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) et[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)Propriétés.

L'exemple suivant montre comment activer une feuille de calcul et y rendre une cellule active. Dans la sortie générée, les barres de défilement défileront pour faire de la 2e ligne et de la 2e colonne leur première ligne et colonne visibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Sujets avancés**
- [Copier et déplacer des feuilles de calcul](/cells/fr/net/copying-and-moving-worksheets/)
- [Compter le nombre de cellules dans la feuille de calcul](/cells/fr/net/count-number-of-cells-in-the-worksheet/)
- [Détection des feuilles de calcul vides](/cells/fr/net/detecting-empty-worksheets/)
- [Rechercher si la feuille de calcul est une feuille de dialogue](/cells/fr/net/find-if-the-worksheet-is-dialog-sheet/)
- [Obtenir l'identifiant unique de la feuille de calcul](/cells/fr/net/get-worksheet-unique-id/)
- [Créer, manipuler ou supprimer des scénarios des feuilles de travail](/cells/fr/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestion des sauts de page](/cells/fr/net/managing-page-breaks/)
- [Fonctionnalités de mise en page](/cells/fr/net/page-setup-features/)
- [Imprimer plusieurs copies d'une feuille de calcul](/cells/fr/net/print-multiple-copies-of-a-worksheet/)
- [Utiliser la propriété Sheet.SheetId d'OpenXml en utilisant Aspose.Cells](/cells/fr/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Vues de feuille de calcul](/cells/fr/net/worksheet-views/)

