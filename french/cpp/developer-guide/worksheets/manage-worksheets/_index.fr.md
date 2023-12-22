---
title: Gérer les feuilles de calcul
type: docs
weight: 20
url: /fr/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans des fichiers Excel Microsoft par programmation à l'aide de Aspose.Cells flexible API. Cette rubrique décrit les approches permettant d'ajouter et de supprimer des feuilles de calcul dans des fichiers Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d’accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fournit un large éventail de méthodes pour gérer les feuilles de calcul.
##  **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour créer un nouveau fichier Excel par programme :

1.  Créer un objet du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe.
1.  Appeler le[Ajouter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) méthode du[Collection de feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection. Une feuille de calcul vide est automatiquement ajoutée au fichier Excel. Il peut être référencé en passant l'index de la nouvelle feuille de calcul au[Collection de feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection.
1. Obtenez une référence de feuille de travail.
1. Effectuer le travail sur les feuilles de travail.
1. Enregistrez le nouveau fichier Excel avec les nouvelles feuilles de calcul en appelant le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) classe[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **Accéder aux feuilles de calcul à l'aide de l'index des feuilles**
L'exemple de code suivant montre comment accéder ou obtenir n'importe quelle feuille de calcul en spécifiant son index.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **Suppression de feuilles de calcul à l'aide de l'index de feuilles**
 La suppression de feuilles de calcul par nom fonctionne bien lorsque le nom de la feuille de calcul est connu. Si vous ne connaissez pas le nom de la feuille de calcul, utilisez une version surchargée du[Supprimer à](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)méthode qui prend l'index de la feuille de calcul au lieu de son nom de feuille.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
