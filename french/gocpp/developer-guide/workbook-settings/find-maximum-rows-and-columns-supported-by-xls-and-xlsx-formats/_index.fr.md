---
title: Trouver le nombre maximum de lignes et de colonnes supportées par les formats XLS et XLSX avec Golang via C++
linktitle: Trouver le maximum de lignes et de colonnes
type: docs
weight: 20
url: /fr/go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Apprenez comment trouver le maximum de lignes et de colonnes supporté par les formats XLS et XLSX en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Il y a différentes quantités de lignes et de colonnes supportées par les formats Excel. Par exemple, XLS supporte 65536 lignes et 256 colonnes tandis que XLSX supporte 1048576 lignes et 16384 colonnes. Si vous souhaitez connaître le nombre de lignes et de colonnes supportées par un format donné, vous pouvez utiliser les propriétés [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) et [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX**

Le code d'exemple suivant crée d'abord un classeur au format XLS puis en XLSX. Après la création, il affiche les valeurs des propriétés [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) et [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). Veuillez consulter la sortie console du code ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **Sortie console**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
