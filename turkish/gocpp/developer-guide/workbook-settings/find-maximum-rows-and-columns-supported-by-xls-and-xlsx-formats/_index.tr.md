---
title: Golang ile C++ üzerinden XLS ve XLSX formatlarının desteklediği maksimum Satır ve Sütunu bulun
linktitle: Maksimum Satır ve Sütunları Bul
type: docs
weight: 20
url: /tr/go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: XLS ve XLSX formatlarının desteklediği maksimum satır ve sütunları bulmak için Aspose.Cells for C++ kullanmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel formatlarının desteklediği satır ve sütun sayıları farklıdır. Örneğin, XLS 65536 satır ve 256 sütun desteklerken, XLSX 1048576 satır ve 16384 sütun destekler. Belirli bir formatın kaç satır ve sütunu desteklediğini öğrenmek için [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) ve [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) özelliklerini kullanabilirsiniz.

## **XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.**

Aşağıdaki örnek kod, ilk olarak XLS formatında, sonra XLSX formatında bir çalışma kitabı oluşturur. Oluşturulduktan sonra, [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) ve [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) özelliklerinin değerlerini yazdırır. Lütfen aşağıda verilen kodun konsol çıktılarına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **Konsol Çıktısı**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
