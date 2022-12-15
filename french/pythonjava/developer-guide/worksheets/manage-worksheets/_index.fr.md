---
title: Gérer les feuilles de calcul
type: docs
weight: 10
url: /fr/python-java/manage-worksheets/
---
La gestion des feuilles de calcul à l'aide de Aspose.Cells for Python via Java est très simple. Dans cet article, nous allons démontrer l'ajout, l'accès et la suppression de feuilles de calcul à l'aide du Aspose.Cells API.
## **Ajout de feuilles de calcul à un nouveau fichier Excel**
 Pour créer un nouveau classeur, créez un objet du[Cahier](https://reference.aspose.com/cells/python/asposecells.api/Workbook) classer. La[Cahier](https://reference.aspose.com/cells/python/asposecells.api/Workbook) classe représente un fichier Excel. Puis en utilisant le[ajouter](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) méthode de la[WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) , de nouvelles feuilles de calcul sont ajoutées au fichier Excel. Enfin, pour enregistrer le fichier Excel nouvellement créé, appelez le[enregistrer](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) méthode de la[Cahier](https://reference.aspose.com/cells/python/asposecells.api/Workbook)classer.

L'extrait de code suivant illustre la création d'un nouveau fichier Excel et l'ajout d'une feuille de calcul.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Ajout de feuilles de calcul à une feuille de calcul Designer**
L'ajout de feuilles de calcul à une feuille de calcul de concepteur revient exactement à ajouter la feuille de calcul à un nouveau fichier Excel. La seule différence est qu'au lieu de créer un nouveau fichier Excel, nous ouvrons un fichier existant par le[Cahier](https://reference.aspose.com/cells/python/asposecells.api/Workbook)classer.

L'extrait de code suivant illustre l'ajout d'une feuille de calcul à une feuille de calcul de concepteur.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Accéder aux feuilles de calcul à l'aide du nom de la feuille**
Après avoir chargé un classeur, les développeurs peuvent accéder à n'importe quelle feuille de calcul en utilisant son index ou son nom. L'extrait de code suivant illustre l'accès à une feuille de calcul à l'aide de son nom.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Suppression de feuilles de calcul**
Il peut arriver que certaines feuilles se rencontrent pour être supprimées du classeur. Pour cela, le API fournit le[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) méthode. Vous pouvez lui passer l'index de la feuille ou le nom de la feuille à supprimer. Les exemples suivants illustrent la suppression de feuilles de calcul à l'aide de l'index et du nom de la feuille.
### **Suppression de feuilles de calcul à l'aide de l'index des feuilles**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Suppression de feuilles de calcul à l'aide du nom de la feuille**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
