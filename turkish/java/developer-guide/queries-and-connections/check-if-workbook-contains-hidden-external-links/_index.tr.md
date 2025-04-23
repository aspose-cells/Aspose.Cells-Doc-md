---
title: Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin
type: docs
weight: 950
url: /tr/java/check-if-workbook-contains-hidden-external-links/
---

## **Olası Kullanım Senaryoları**
Bazen çalışma kitabı, Microsoft Excel'de görünemeyen gizli harici bağlantıları içerir. Aspose.Cells, görünür veya görünmez olsun tüm harici bağlantıları alır. Ancak harici bağlantının görünür olup olmadığını kontrol etmek için [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) özelliğini kontrol edebilirsiniz
## **Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin**
Aşağıdaki örnek kod, Microsoft Excel'de görülemeyen ancak çalışma kitabının içinde bulunan gizli harici bağlantıları içeren [kaynak excel dosyasını](5472525.xlsx) yükler. [ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) ve [ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) özelliklerini yazdırdıktan sonra [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) özelliğini yazdırır. Aşağıdaki konsol çıktısında, tüm harici bağlantıların görünür olmadığını görürsünüz.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun, verilen [örnek excel dosyası](5472525.xlsx) ile çalıştırıldığında konsol çıktısı aşağıdaki gibidir.



{{< highlight java >}}

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
{{< app/cells/assistant language="java" >}}
