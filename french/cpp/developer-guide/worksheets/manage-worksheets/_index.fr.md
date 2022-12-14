---
title: Gérer les feuilles de travail
type: docs
weight: 20
url: /fr/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans des fichiers Excel Microsoft par programmation à l'aide de Aspose.Cells flexible API. Cette rubrique décrit les approches permettant d'ajouter et de supprimer des feuilles de calcul dans des fichiers Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel. La[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)La classe fournit un large éventail de méthodes de gestion des feuilles de calcul.
## **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour créer un nouveau fichier Excel par programmation :

1.  Créer un objet du[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classer.
1.  Appeler le[Ajouter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) méthode de la[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) le recueil. Une feuille de calcul vide est automatiquement ajoutée au fichier Excel. Il peut être référencé en passant l'index de feuille de la nouvelle feuille de calcul au[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)le recueil.
1. Obtenir une référence de feuille de travail.
1. Effectuer des travaux sur les feuilles de travail.
1.  Enregistrez le nouveau fichier Excel avec de nouvelles feuilles de calcul en appelant le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classer[sauvegarder](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Accéder aux feuilles de calcul à l'aide de l'index des feuilles**
L'exemple de code suivant montre comment accéder ou obtenir une feuille de calcul en spécifiant son index.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Suppression de feuilles de calcul à l'aide de l'index des feuilles**
 La suppression de feuilles de calcul par nom fonctionne bien lorsque le nom de la feuille de calcul est connu. Si vous ne connaissez pas le nom de la feuille de calcul, utilisez une version surchargée du[Supprimer à](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)méthode qui prend l'index de feuille de la feuille de calcul au lieu de son nom de feuille.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
