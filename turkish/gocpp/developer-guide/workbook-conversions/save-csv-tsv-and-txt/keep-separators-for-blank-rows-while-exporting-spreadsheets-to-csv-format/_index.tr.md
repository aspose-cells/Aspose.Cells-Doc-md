---
title: Boş Satırlar için Ayırıcıları koruyarak bu satırları CSV formatına aktarırken Golang ile C++ kullanın
linktitle: CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla
type: docs
weight: 160
url: /tr/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Boş satırlar için ayırıcıları koruyarak Excel dosyasını CSV ye aktarırken Aspose.Cells kullanarak Golang ile C++ öğrenin.
---

## **CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla**

Aspose.Cells, elektronik tabloları CSV'ye dönüştürürken satır ayırıcılarını tutma yeteneği sağlar. Bunun için, [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/) sınıfının [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) özelliğini kullanabilirsiniz. [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) boolean bir özelliktir. Excel dosyasını CSV'ye dönüştürürken boş satırlar için ayırıcıları tutmak için [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) özelliğini **true** olarak ayarlayın.

Aşağıdaki örnek kod, [kaynak Excel dosyasını](84378743.xlsx) yükler. [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) özelliğini **true** yapar ve [çıktı.csv](84378744.csv) olarak kaydeder. Ekran görüntüsü, kaynak Excel dosyası, varsayılan CSV'ye dönüştürme ve [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) ayarlamasıyla üretilen çıktı arasındaki karşılaştırmayı gösterir.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
