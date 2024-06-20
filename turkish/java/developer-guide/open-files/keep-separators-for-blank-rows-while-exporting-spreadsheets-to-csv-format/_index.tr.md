---
title: CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla
type: docs
weight: 110
url: /tr/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla**

Aspose.Cells, elektronik tablolardan CSV formatına dönüştürürken satır ayraçlarını koruma olanağı sağlar. Bunun için, [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) sınıfının [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions) özelliğini kullanabilirsiniz. [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) bir boolean özelliğidir. Excel Dosyasını CSV'ye dönüştürürken boş satırlar için ayraçları saklamak için [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) özelliğini **true** olarak ayarlayın.

Aşağıdaki örnek kod, [kaynak Excel dosyasını](KeepSeparatorsForBlankRow.xlsx) yükler. [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) özelliğini **true** olarak ayarlar ve [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv) olarak kaydeder. Ekran görüntüsü, Excel dosyasının orijinal hali, elektronik tabloyu CSV'ye dönüştürürken oluşturulan varsayılan çıktı ve **true** olarak ayarlama sonucunda oluşturulan çıktıyı göstermektedir.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
