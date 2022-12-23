---
title: Hücrelerde baştaki kesme işaretini göster
type: docs
weight: 20
url: /tr/java/show-leading-apostrophe-in-cells/
---
## **Hücrelerde baştaki kesme işaretini göster**

Microsoft Excel'de, hücrenin değerindeki baştaki kesme işareti gizlenmiştir. Aspose.Cells kesme işaretini varsayılan olarak görüntüleme özelliği sağlar. Bunun için API şunları sağlar:[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)Emlak. Bu özellik, ayarlanıp ayarlanmadığını gösterir.[**AlıntıÖnek**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)hücreye tek bir alıntı ile başlayan dize değeri girerken özelliği. ayarlamak[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)mülkiyet**YANLIŞ**çıktı excel dosyasında önde gelen kesme işaretini görüntüler.

Aşağıdaki ekran görüntüsü, görünür kesme işaretiyle çıktı excel dosyasını gösterir.

![yapılacaklar:resim_alternatif_metin](show-leading-apostrophe-in-cells_1.jpg)

Aşağıdaki kod parçacığı, kaynak excel dosyasına Akıllı İşaretleyiciler ile veri ekleyerek bunu gösterir. Kaynak ve çıktı excel dosyaları referans için eklenmiştir.

[Kaynak dosyası](AllowLeadingApostropheSample.xlsx)

[Çıktı dosyası](AllowLeadingApostropheSample_out.xlsx)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

uygulanması*Veri Nesnesi*sınıf aşağıda verilmiştir

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
