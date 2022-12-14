---
title: Çalışma Kitabının gizli Dış Bağlantılar içerip içermediğini kontrol edin
type: docs
weight: 950
url: /tr/java/check-if-workbook-contains-hidden-external-links/
---
## **Olası Kullanım Senaryoları**
Bazen, çalışma kitabı gizli olan ve Microsoft Excel'de görüntülenemeyen dış bağlantılar içerir. Aspose.Cells, görünür veya gizli tüm harici bağlantıları alır. Ancak, kontrol edebilirsiniz[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)harici bağlantının görünür olup olmadığını kontrol etme özelliği
## **Çalışma Kitabının gizli Dış Bağlantılar içerip içermediğini kontrol edin**
 Aşağıdaki örnek kod,[kaynak excel dosyası](5472525.xlsx) hangi gizli dış bağlantılar içerir. Bu bağlantılar Microsoft Excel'de görüntülenemez ancak çalışma kitabının içinde bulunurlar. Yazdırdıktan sonra[ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) ve[ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) özellik, yazdırır[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)Emlak. Aşağıdaki konsol çıktısında, tüm dış bağlantılarının görünmediğini görüyorsunuz.
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Konsol Çıkışı**
 Verilen ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı aşağıdadır.[örnek excel dosyası](5472525.xlsx).



{{< highlight "java" >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
