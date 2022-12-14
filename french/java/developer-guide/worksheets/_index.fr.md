---
title: Gérer les feuilles de travail
linktitle: Des feuilles de calcul
type: docs
weight: 60
url: /fr/java/manage-worksheets/
---
{{% alert color="primary" %}}

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans leurs fichiers Excel par programmation à l'aide du flexible API de Aspose.Cells. Dans cette rubrique, nous aborderons certaines approches pour ajouter et supprimer des feuilles de calcul dans des fichiers Excel.

{{% /alert %}}

La gestion des feuilles de calcul à l'aide de Aspose.Cells est aussi simple qu'ABC. Dans cette section, nous décrirons comment pouvons-nous :

1. Créez un nouveau fichier Excel à partir de zéro et ajoutez-y une feuille de calcul
1. Ajouter des feuilles de calcul aux feuilles de calcul du concepteur
1. Accéder aux feuilles de calcul à l'aide du nom de la feuille
1. Supprimer une feuille de calcul d'un fichier Excel en utilisant son nom de feuille
1. Supprimer une feuille de calcul d'un fichier Excel à l'aide de son index de feuille

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel.[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer.[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Voyons comment utiliser cet ensemble d'API de base.

## **Ajout de feuilles de calcul à un nouveau fichier Excel**

 Pour créer un nouveau fichier Excel par programmation, les développeurs doivent créer un objet de[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe qui représente un fichier Excel. Ensuite, les développeurs peuvent appeler[**ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) méthode de la[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Quand nous appelons[**ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ), une feuille de calcul vide est automatiquement ajoutée au fichier Excel, qui peut être référencée en transmettant l'index de feuille de la feuille de calcul nouvellement ajoutée à la[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Une fois la référence de la feuille de calcul obtenue, les développeurs peuvent travailler sur leurs feuilles de calcul en fonction de leurs besoins. Une fois le travail terminé sur les feuilles de calcul, les développeurs peuvent enregistrer leur fichier Excel nouvellement créé avec de nouvelles feuilles de calcul en appelant le[**enregistrer**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) méthode de la[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Ajout de feuilles de calcul à une feuille de calcul Designer**

Le processus d'ajout de feuilles de calcul à une feuille de calcul de concepteur est entièrement identique à celui de l'approche ci-dessus, sauf que le fichier Excel est déjà créé et que nous devons d'abord ouvrir ce fichier Excel avant d'y ajouter une feuille de calcul. Une feuille de calcul de concepteur peut être ouverte en transmettant le chemin d'accès au fichier ou le flux lors de l'initialisation du[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Accéder aux feuilles de calcul à l'aide du nom de la feuille**

Les développeurs peuvent accéder ou obtenir n'importe quelle feuille de calcul en spécifiant son nom ou son index.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Suppression de feuilles de calcul à l'aide du nom de la feuille**

 Parfois, les développeurs peuvent avoir besoin de supprimer des feuilles de calcul des fichiers Excel existants et cette tâche peut être effectuée en appelant le[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) méthode de la[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) le recueil. Nous pouvons passer le nom de la feuille au[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) méthode pour supprimer une feuille de calcul spécifique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Suppression de feuilles de calcul à l'aide de l'index des feuilles**

L'approche ci-dessus de suppression des feuilles de calcul fonctionne bien si les développeurs connaissent déjà les noms des feuilles de calcul à supprimer. Mais que se passe-t-il si vous ne connaissez pas le nom de la feuille de calcul que vous souhaitez supprimer de votre fichier Excel ?

 Eh bien, dans de telles circonstances, les développeurs peuvent utiliser une version surchargée de[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)méthode qui prend l'index de feuille de la feuille de calcul au lieu de son nom de feuille.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Sujets avancés**
- [Activation des feuilles et activation d'un Cell dans la feuille de calcul](/cells/fr/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Copier et déplacer des feuilles de calcul dans et entre des classeurs](/cells/fr/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Copier et déplacer des feuilles de calcul](/cells/fr/java/copying-and-moving-worksheets/)
- [Compter le nombre de cellules dans la feuille de calcul](/cells/fr/java/count-number-of-cells-in-the-worksheet/)
- [Détection des feuilles de calcul vides](/cells/fr/java/detecting-empty-worksheets/)
- [Rechercher si la feuille de calcul est une feuille de dialogue](/cells/fr/java/find-if-the-worksheet-is-dialog-sheet/)
- [Obtenir l'identifiant unique de la feuille de calcul](/cells/fr/java/get-worksheet-unique-id/)
- [Insérer une image d'arrière-plan dans Excel](/cells/fr/java/insert-background-image-to-excel/)
- [Créer, manipuler ou supprimer des scénarios des feuilles de travail](/cells/fr/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestion des sauts de page](/cells/fr/java/managing-page-breaks/)
- [Fonctionnalités de mise en page](/cells/fr/java/page-setup-features/)
- [Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant des colonnes et des lignes vides dans une feuille de calcul](/cells/fr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Utiliser la propriété Sheet.SheetId d'OpenXml en utilisant Aspose.Cells](/cells/fr/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Utilisation de l'arrière-plan dans les fichiers ODS](/cells/fr/java/working-with-background-in-ods-files/)
- [Vues de feuille de calcul](/cells/fr/java/worksheet-views/)
