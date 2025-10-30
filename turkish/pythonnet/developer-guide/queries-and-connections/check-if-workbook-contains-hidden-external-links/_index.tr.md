---
title: Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin
type: docs
weight: 230
url: /tr/python-net/check-if-workbook-contains-hidden-external-links/
---

## **Olası Kullanım Senaryoları**
Bazen, çalışma kitabında gizli ve görünmeyen dış bağlantılar olabilir ve Microsoft Excel'de görüntülenemez. Aspose.Cells for Python via .NET, görünür veya gizli olsun dış bağlantıların tamamını alır. Ancak, [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) property’sini kullanarak dış bağlantının görünür olup olmadığını kontrol edebilirsiniz.

## **Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin**
Aşağıdaki örnek kod, gizli dış bağlantılar içeren [kaynak excel dosyasını](5115413.xlsx) yükler. Bu bağlantılar Microsoft Excel'de görüntülenemez, ancak çalışma kitabında bulunur. [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) ve [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred) özelliklerini ardından, [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) özelliği görüntülenir. Aşağıdaki konsol çıktısında, tüm dış bağlantıların görünmediği görülür.

### **Örnek Kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
