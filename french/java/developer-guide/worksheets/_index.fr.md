---
title: Gérer les feuilles de calcul
linktitle: Feuilles de calcul
type: docs
weight: 60
url: /fr/java/manage-worksheets/
---

{{% alert color="primary" %}}

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans leurs fichiers Excel de manière programmatique en utilisant l'API flexible d'Aspose.Cells. Dans ce sujet, nous discuterons de certaines approches pour ajouter et supprimer des feuilles de calcul dans les fichiers Excel.

{{% /alert %}}

La gestion des feuilles de calcul avec Aspose.Cells est un jeu d'enfant. Dans cette section, nous décrirons comment nous pouvons :

1. Créer un nouveau fichier Excel à partir de zéro et y ajouter une feuille de calcul
1. Ajouter des feuilles de calcul à des feuilles de calcul déjà conçues
1. Accéder aux feuilles de calcul en utilisant le nom de la feuille
1. Supprimer une feuille de calcul d'un fichier Excel en utilisant son nom de feuille
1. Supprimer une feuille de calcul d'un fichier Excel en utilisant son indice de feuille

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Voyons comment nous pouvons utiliser cet ensemble de bases d'API.

## **Ajout de feuilles de calcul à un nouveau fichier Excel**

Pour créer un nouveau fichier Excel de manière programmatique, les développeurs auraient besoin de créer un objet de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel. Ensuite, les développeurs peuvent appeler la méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) du [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Lorsque nous appelons la méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--), une feuille de calcul vide est ajoutée au fichier Excel automatiquement, qui peut être référencée en passant l'index de feuille de la nouvelle feuille de calcul au [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Après avoir obtenu la référence de la feuille de calcul, les développeurs peuvent travailler sur leurs feuilles de calcul selon leurs besoins. Après avoir travaillé sur les feuilles de calcul, les développeurs peuvent enregistrer leur fichier Excel nouvellement créé avec de nouvelles feuilles de calcul en appelant la méthode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Ajout de feuilles de calcul à une feuille de calcul Designer**

Le processus d'ajout de feuilles de calcul à une feuille de calcul déjà conçue est entièrement le même que celui de l'approche ci-dessus, sauf que le fichier Excel est déjà créé et que nous devons d'abord ouvrir ce fichier Excel avant d'ajouter une feuille de calcul. Une feuille de calcul déjà conçue peut être ouverte en passant le chemin du fichier ou le flux lors de l'initialisation de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Accéder aux feuilles de calcul en utilisant le nom de la feuille**

Les développeurs peuvent accéder ou obtenir n'importe quelle feuille de calcul en spécifiant son nom ou son indice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Suppression des feuilles de calcul en utilisant le nom de la feuille**

Parfois, les développeurs peuvent avoir besoin de supprimer des feuilles de calcul de fichiers Excel existants et cette tâche peut être effectuée en appelant la méthode [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) de la collection [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Nous pouvons passer le nom de la feuille à la méthode [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) pour supprimer une feuille de calcul spécifique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Suppression des feuilles de calcul en utilisant l'indice de la feuille**

L'approche ci-dessus pour supprimer des feuilles de calcul fonctionne bien si les développeurs connaissent déjà les noms des feuilles de calcul à supprimer. Mais, que faire si vous ne connaissez pas le nom de la feuille que vous souhaitez supprimer de votre fichier Excel?

Eh bien, dans de tels cas, les développeurs peuvent utiliser une version surchargée de la méthode [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)) qui prend l'index de la feuille de calcul au lieu de son nom de feuille.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Sujets avancés**
- [Activation des feuilles et activation d'une cellule dans une feuille de calcul](/cells/fr/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Copier et déplacer des feuilles de calcul à l'intérieur et entre les classeurs](/cells/fr/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Copier et Déplacer des Feuilles de calcul](/cells/fr/java/copying-and-moving-worksheets/)
- [Compter le nombre de cellules dans la feuille de calcul](/cells/fr/java/count-number-of-cells-in-the-worksheet/)
- [Détection des Feuilles de calcul vides](/cells/fr/java/detecting-empty-worksheets/)
- [Trouver si la Feuille de calcul est une Feuille de dialogue](/cells/fr/java/find-if-the-worksheet-is-dialog-sheet/)
- [Obtenir l'identifiant unique de la feuille de calcul](/cells/fr/java/get-worksheet-unique-id/)
- [Insérer une image d'arrière-plan dans Excel](/cells/fr/java/insert-background-image-to-excel/)
- [Créer, Manipuler ou Supprimer des Scénarios des Feuilles de calcul](/cells/fr/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestion des Sauts de Page](/cells/fr/java/managing-page-breaks/)
- [Fonctionnalités de Configuration de Page](/cells/fr/java/page-setup-features/)
- [Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul](/cells/fr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Utiliser la propriété Sheet.SheetId d'OpenXml en utilisant Aspose.Cells](/cells/fr/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Travailler avec l'arrière-plan dans les fichiers ODS](/cells/fr/java/working-with-background-in-ods-files/)
- [Vues de Feuille de calcul](/cells/fr/java/worksheet-views/)
