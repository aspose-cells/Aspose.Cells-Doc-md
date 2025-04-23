---
title: Hücrelerde öncü apostrofu gösterme
type: docs
weight: 20
url: /tr/java/show-leading-apostrophe-in-cells/
---

## **Hücrelerde Öncü Apostrof Göster**

Microsoft Excel'de, hücrenin değerindeki öncü apostrof gizlidir. Aspose.Cells, varsayılan olarak apostrofu görüntülemek için özellik sağlar. Bu amaçla API, [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle) özelliğini sağlar. Bu özellik, hücreye tek tırnakla başlayan dize değeri girilirken [**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix) özelliğini ayarlayıp ayarlamamamızı gösterir. [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle) özelliğini **false** olarak ayarlamak, çıktı Excel dosyasında öncü apostrofu gösterir.

Aşağıdaki ekran görüntüsü, çıkış excel dosyasını görünen öncü apostrofla göstermektedir.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Aşağıdaki kod parçası, kaynak excel dosyasına Akıllı İmlerle veri ekleyerek bunu gösterir. Kaynak ve çıkış excel dosyaları referans için ekte verilmiştir.

[Kaynak Dosya](AllowLeadingApostropheSample.xlsx)

[Çıktı Dosyası](AllowLeadingApostropheSample_out.xlsx)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

*DataObject* sınıfının uygulaması aşağıda verilmiştir

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
{{< app/cells/assistant language="java" >}}
