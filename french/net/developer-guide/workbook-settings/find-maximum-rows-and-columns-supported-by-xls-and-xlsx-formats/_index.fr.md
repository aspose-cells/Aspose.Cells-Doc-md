---
title: Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX
type: docs
weight: 20
url: /fr/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Scénarios d'utilisation possibles**

Il existe un nombre différent de lignes et de colonnes pris en charge par les formats Excel. Par exemple, XLS prend en charge 65536 lignes et 256 colonnes tandis que XLSX prend en charge 1048576 lignes et 16384 colonnes. Si vous voulez savoir combien de lignes et de colonnes sont pris en charge par un format donné, vous pouvez utiliser les propriétés [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) et [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn).

## **Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX**

Le code d'exemple suivant crée d'abord un classeur en format XLS puis en format XLSX. Après la création, il imprime les valeurs des propriétés [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) et [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn). Veuillez consulter la sortie de la console du code ci-dessous pour votre référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Sortie console**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
