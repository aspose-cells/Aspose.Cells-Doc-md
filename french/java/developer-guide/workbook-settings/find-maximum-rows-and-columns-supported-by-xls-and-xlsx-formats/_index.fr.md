---
title: Trouver le maximum de lignes et de colonnes prises en charge par les formats XLS et XLSX
type: docs
weight: 60
url: /fr/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Scénarios d'utilisation possibles**
Il existe différents nombres de lignes et de colonnes prises en charge par les formats Excel. Par exemple, XLS prend en charge 65536 lignes et 256 colonnes tandis que XLSX prend en charge 1048576 lignes et 16384 colonnes. Si vous voulez savoir combien de lignes et de colonnes sont prises en charge par un format donné, vous pouvez utiliser[Classeur.Paramètres.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)et[Classeur.Paramètres.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)Propriétés.
## **Trouver le maximum de lignes et de colonnes prises en charge par les formats XLS et XLSX**
L'exemple de code suivant crée d'abord un classeur au format XLS, puis au format XLSX. Après la création, il imprime les valeurs de[Classeur.Paramètres.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)et[Classeur.Paramètres.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)Propriétés. Veuillez consulter la sortie de la console du code ci-dessous pour votre référence.
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Sortie console

{{< highlight "java" >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
