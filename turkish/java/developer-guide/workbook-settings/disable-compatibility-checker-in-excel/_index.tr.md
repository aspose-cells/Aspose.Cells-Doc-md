---
title: Excel de Uyumluluk Denetimini Devre Dışı Bırakma
type: docs
weight: 270
url: /tr/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Microsoft Excel'in Uyumluluk Denetçisi, bir dosyayı daha önceki bir dosya biçiminde kaydederken, dosyayı daha önceki bir sürümde kaydetmenin işlevsellik sorunlarına veya sadakatin kaybolmasına neden olabileceği konularında uyarı verir. Uyumluluk Denetçisi, Microsoft Office Excel 2007, 2010 ve 2013'ün bir özelliğidir.

Excel 2007 veya 2003'ten Excel 2007 veya 2010'a kaydederken, Uyumluluk Denetçisi, daha önceki sürüm tarafından desteklenmeyen özellikleri içeren bir dosya olup olmadığını kontrol etmek için çalışma kitabını tarar. Uyumluluk sorunları hakkında kararlar vermenize yardımcı olmak için, Uyumluluk Denetçisi, seçenekleri içeren iletişim kutuları görüntüler. Ayrıca, çalışma kitabındaki herhangi bir sorun hakkında bir rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.

Bazen, belirli bir elektronik tabloyu Uyumluluk Denetçisini devre dışı bırakmanız gerekir. Aspose.Cells'ı kullanarak kullanıcıların dosyayı Microsoft Excel'de el ile yeniden kaydettiklerinde, Uyumluluk Denetçisi ile ilgili bir iletişim kutusunun karşısına çıkması nedeniyle sinir bozucu veya kafa karıştırıcı hale gelmemesi için bunu dinamik olarak yapabilirsiniz.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de Uyumluluk Denetçisini devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):

- (Excel 2007) Office düğmesine tıklayın, **Hazırla**'yı tıklayın, ardından **Uyumluluk Denetleyicisini Çalıştır**'ı tıklayın ve **Bu çalışma kitabını kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.
- (Excel 2010 ve 2013) Dosya sekmesine tıklayın, **Bilgi**'yi tıklayın, **Sorunları kontrol et**'i tıklayın, **Uyumluluğu Kontrol Et**'i tıklayın ve son olarak **Bu çalışma kitabını kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.

## **Aspose.Cells API'larını Kullanma**

Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için **False** olarak [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) özelliğini ayarlayın.

Bir şablon XLS dosyamız olduğunu varsayalım. Kullanıcı MS Excel 2007/2010/2013'te dosyayı kaydettiğinde veya tekrar kaydettiğinde, Uyumluluk Denetleyicisi iletişim kutusu gösterilir, aşağıdaki ekran resminde gösterildiği gibi.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

Aşağıdaki kod, Uyumluluk Denetleyicisini Aspose.Cells for Java ile devre dışı bırakma işlemini göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
