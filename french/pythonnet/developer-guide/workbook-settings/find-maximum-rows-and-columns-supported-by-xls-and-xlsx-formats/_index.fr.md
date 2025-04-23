---
title: Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX
type: docs
weight: 20
url: /fr/python-net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Scénarios d'utilisation possibles**

Il existe un nombre différent de lignes et de colonnes pris en charge par les formats Excel. Par exemple, XLS prend en charge 65536 lignes et 256 colonnes tandis que XLSX prend en charge 1048576 lignes et 16384 colonnes. Si vous voulez savoir combien de lignes et de colonnes sont pris en charge par un format donné, vous pouvez utiliser les propriétés [**WorkbookSettings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) et [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column).

## **Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX**

Le code d'exemple suivant crée d'abord un classeur en format XLS puis en format XLSX. Après la création, il imprime les valeurs des propriétés [**Workbook.settings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) et [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column). Veuillez consulter la sortie de la console du code ci-dessous pour votre référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.py" >}}

## **Sortie console**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}

