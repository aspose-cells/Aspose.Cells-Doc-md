---
title: Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin
type: docs
weight: 230
url: /tr/net/check-if-workbook-contains-hidden-external-links/
---

## **Olası Kullanım Senaryoları**
Bazen çalışma kitabı, Microsoft Excel'de görünmeyen ve gizlenmiş harici bağlantıları içerebilir. Aspose.Cells, bunların hepsini alır, görünür veya gizli olsunlar. Ancak [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) özelliğini kontrol edebilir ve harici bağlantının görünür olup olmadığını kontrol edebilirsiniz.
## **Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin**
Aşağıdaki örnek kodu, Microsoft Excel'de görüntülenemeyen ancak çalışma kitabı içinde bulunan gizli harici bağlantılar içeren [kaynak excel dosyasını](5115413.xlsx) yükler. [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) ve [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) özelliklerini yazdırdıktan sonra [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) özelliğini yazdırır. Aşağıdaki konsol çıktısında, tüm harici bağlantılarının görünür olmadığını görebilirsiniz.
### **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Konsol Çıktısı**
Aşağıdaki örnek kodun, verilen [örnek excel dosyası](5115413.xlsx) ile çalıştırılması sonucu konsol çıktısı aşağıdaki gibidir.



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
{{< app/cells/assistant language="csharp" >}}
