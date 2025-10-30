---
title: Maximale Zeilen und Spalten unterstützen, die vom XLS und XLSX Format mit Golang via C++ unterstützt werden
linktitle: Maximale Zeilen und Spalten finden
type: docs
weight: 20
url: /de/go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Erfahren Sie, wie Sie die maximale Zeilen und Spaltenzahl der XLS und XLSX Formate mit Aspose.Cells for C++ ermitteln.
---

## **Mögliche Verwendungsszenarien**

Es gibt unterschiedliche Zeilen- und Spaltenzahlen, die von Excel-Formaten unterstützt werden. Zum Beispiel unterstützt XLS 65536 Zeilen und 256 Spalten, während XLSX 1048576 Zeilen und 16384 Spalten unterstützt. Wenn Sie wissen möchten, wie viele Zeilen und Spalten ein bestimmtes Format unterstützt, können Sie die Eigenschaften [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) und [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) verwenden.

## **Suchen Sie die maximale Anzahl von Zeilen und Spalten, die von den XLS- und XLSX-Formaten unterstützt werden**

Der folgende Beispielcode erstellt zunächst eine Arbeitsmappe im XLS-Format und anschließend im XLSX-Format. Nach der Erstellung werden die Werte der Eigenschaften [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) und [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) ausgegeben. Bitte siehe die Konsolenausgabe des unten angegebenen Codes zu Ihrer Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
