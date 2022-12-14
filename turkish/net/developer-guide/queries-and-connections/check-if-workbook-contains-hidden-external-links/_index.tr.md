---
title: Çalışma Kitabının gizli Dış Bağlantılar içerip içermediğini kontrol edin
type: docs
weight: 230
url: /tr/net/check-if-workbook-contains-hidden-external-links/
---
## **Olası Kullanım Senaryoları**
Bazen, çalışma kitabı gizli olan ve Microsoft Excel'de görüntülenemeyen dış bağlantılar içerir. Aspose.Cells, görünür veya gizli tüm harici bağlantıları alır. Ancak, kontrol edebilirsiniz[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)harici bağlantının görünür olup olmadığını kontrol etme özelliği
## **Çalışma Kitabının gizli Dış Bağlantılar içerip içermediğini kontrol edin**
 Aşağıdaki örnek kod,[kaynak excel dosyası](5115413.xlsx) hangi gizli dış bağlantılar içerir. Bu bağlantılar Microsoft Excel'de görüntülenemez ancak çalışma kitabının içinde bulunurlar. Yazdırdıktan sonra[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) ve[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) özellik, yazdırır[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)Emlak. Aşağıdaki konsol çıktısında, tüm dış bağlantılarının görünmediğini görüyorsunuz.
### **Basit kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Konsol Çıkışı**
 Verilen ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı aşağıdadır.[örnek excel dosyası](5115413.xlsx).



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
