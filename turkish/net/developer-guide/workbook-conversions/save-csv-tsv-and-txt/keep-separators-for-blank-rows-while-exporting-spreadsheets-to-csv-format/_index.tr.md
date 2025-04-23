---
title: CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla
type: docs
weight: 160
url: /tr/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla**

Aspose.Cells, elektronik tablolardan CSV formatına dönüştürürken satır ayraçlarını koruma olanağı sağlar. Bunun için, [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) sınıfının [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions) özelliğini kullanabilirsiniz. [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) bir boolean özelliğidir. Excel Dosyasını CSV'ye dönüştürürken boş satırlar için ayraçları saklamak için [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) özelliğini **true** olarak ayarlayın.

Aşağıdaki örnek kod, [kaynak Excel dosyasını](84378743.xlsx) yükler. [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) özelliğini **true** olarak ayarlar ve [çıktı.csv](84378744.csv)'olarak kaydeder. Ekran görüntüsü, kaynak Excel dosyası, CSV'ye dönüştürülürken oluşturulan öntanımlı çıktı ve [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) özelliğinin **true** olarak ayarlanmasıyla oluşturulan çıktı arasındaki karşılaştırmayı gösterir.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
