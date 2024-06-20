---
title: Gérer les feuilles de calcul
type: docs
weight: 10
url: /fr/python-java/manage-worksheets/
---

La gestion des feuilles de calcul à l'aide d'Aspose.Cells pour Python via Java est très facile. Dans cet article, nous allons démontrer comment ajouter, accéder et supprimer des feuilles de calcul en utilisant l'API Aspose.Cells.
## **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour créer un nouveau classeur, créez un objet de la classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook). La classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) représente un fichier Excel. Ensuite, en utilisant la méthode [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) de la classe [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection), de nouvelles feuilles de calcul sont ajoutées au fichier Excel. Enfin, pour enregistrer le fichier Excel nouvellement créé, appelez la méthode [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) de la classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

Le code suivant illustre la création d'un nouveau fichier Excel et l'ajout d'une feuille de calcul.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Ajout de feuilles de calcul à une feuille de calcul Designer**
Ajouter des feuilles de calcul à une feuille de calcul de concepteur est exactement la même que d'ajouter la feuille de calcul à un nouveau fichier Excel. La seule différence est qu'au lieu de créer un nouveau fichier Excel, nous ouvrons un fichier existant par la classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

Le code suivant illustre l'ajout d'une feuille de calcul à une feuille de calcul de concepteur.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Accéder aux feuilles de calcul en utilisant le nom de la feuille**
Après le chargement d'un classeur, les développeurs peuvent accéder à n'importe quelle feuille de calcul en utilisant son indice ou son nom. Le code suivant illustre l'accès à une feuille de calcul en utilisant son nom.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Suppression de feuilles de calcul**
Il peut arriver que certaines feuilles doivent être supprimées du classeur. Pour ce faire, l'API fournit la méthode [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)). Vous pouvez lui transmettre l'indice de la feuille ou le nom de la feuille à supprimer. Les exemples suivants montrent comment supprimer des feuilles de calcul en utilisant l'indice de la feuille et le nom de la feuille.
### **Suppression de feuilles de calcul en utilisant l'indice de feuille**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Suppression des feuilles de calcul en utilisant le nom de la feuille**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
