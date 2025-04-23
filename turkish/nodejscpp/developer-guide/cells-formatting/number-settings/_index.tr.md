---  
title: Sayı Ayarları
linktitle: Sayı Ayarları  
description: Aspose.Cells, çeşitli hücre sayı ayarlarını destekleyen spreadsheet dosyalarıyla çalışmak için Node.js kütüphanesidir. Bu makale, hücrelerin sayı ayarlarını yönetmek ve spreadsheet lerde sayı biçimlerini ayarlamak için Aspose.Cells kütüphanesinin nasıl kullanılacağını anlatmaktadır.  
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablolar, hücre sayı ayarları, biçimlendirme, yönetim, Sayı ve Tarih Formatları  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/cells-number-settings/  
---  

## **Sayı ve Tarih Formatlarının Görüntülemesini Nasıl Ayarlayabilirsiniz**  

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntüleme biçimlerini ayarlamalarına izin vermesidir. Sayısal verilerin, ondalık, para birimi, yüzde, kesir veya muhasebe değerleri gibi çeşitli farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Bu sayısal tüm değerler, temsil ettikleri bilgi türüne göre farklı biçimlerde görüntülenir. Benzer şekilde, bir tarih veya zamanın gösterilebileceği birçok format mevcuttur.  
Aspose.Cells bu işlevselliği destekler ve geliştiricilere bir numaranın veya tarihin herhangi bir görüntüleme formatını ayarlama izni verir.  

### **Microsoft Excel'de Görüntüleme Formatlarını Nasıl Ayarlayabilirsiniz**  

Microsoft Excel'de görüntüleme formatlarını ayarlamak için:  

1. Herhangi bir hücreye sağ tıklayın.  
2. **Hücreleri Biçimlendir** seçeneğini tıklayın. Herhangi bir değer türünün görüntüleme biçimlerini ayarlamak için kullanılan bir ileti kutusu açılır.  

İletişim kutusunun sol tarafında, **Genel**, **Sayı**, **Para Birimi**, **Muhasebe**, **Tarih**, **Saat**, **Yüzde** gibi birçok değer kategorisi vardır. Aspose.Cells, tüm bu görüntüleme biçimlerini destekler.  

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir modül sağlar; bu, bir Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) modülü, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) modülü tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) modülü, bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) modülünün bir nesnesini temsil eder.  

Aspose.Cells, [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) ve [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) yöntemleri sağlar; bunlar, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) modülü içindir. Bu yöntemler, bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) modülü, sayıların ve tarihlerinin görüntüleme biçimleriyle ilgilenmek için kullanışlı bazı özellikler sağlar.  

### **Dahili Sayı Formatlarının Nasıl Kullanılacağı**  

Aspose.Cells, sayıların ve tarihlerin görüntüleme biçimlerini yapılandırmak için bazı yerleşik sayı biçimleri sunar. Bu yerleşik sayı biçimleri, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) yöntemi kullanılarak uygulanabilir. Tüm yerleşik sayı biçimlerine özgü sayısal değerler atanmıştır. Geliştiriciler, bu biçimi uygulamak için, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) yöntemine istedikleri herhangi bir sayısal değeri atayabilirler. Bu yöntem hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı biçimleri aşağıda listelenmiştir.  

|**Değer**|**Tür**|**Biçim Dizesi**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **Özel Sayı Formatları Nasıl Kullanılır**  

Görüntüleme biçimi için kendi özelleştirilmiş biçim dizesini tanımlamak için, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) yöntemini kullanın. Bu yaklaşım, önceden ayarlanmış biçimleri kullanmaktan daha yavaş olsa da, daha esnektir.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

Sayısal formatı ayarlamak için [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) yöntemini kullanırsanız, daha önce [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) yöntemi kullanılarak ayarlanmış herhangi bir biçim üzerine yazılır ve tersi de geçerlidir.  

{{% /alert %}}  

## **Gelişmiş Konular**  
- [Stil.Oluştur Özelliğini Ayarlayarak Özel Sayı Formatını Kontrol Edin](/cells/tr/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Desteklenen Sayı Formatları Listesi](/cells/tr/nodejs-cpp/list-of-supported-number-formats/)  
- [Özel Tarih Format Deseni g ve ge mm dd'yi Dönüştürme](/cells/tr/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Çalışmabook için Özel Sayı Ondalık ve Grup Ayraçlarını Belirleme](/cells/tr/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [DBNum Özel Desen Biçimlendirmesini Belirleme](/cells/tr/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
