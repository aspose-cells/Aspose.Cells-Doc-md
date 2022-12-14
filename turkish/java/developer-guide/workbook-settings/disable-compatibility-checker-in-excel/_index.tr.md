---
title: Excel'de Uyumluluk Denetleyicisini Devre Dışı Bırak
type: docs
weight: 270
url: /tr/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft Excel'in Uyumluluk Denetleyicisi, bir dosyayı daha önceki bir dosya biçiminde kaydederken, dosyayı kaydetmenin işlevsellik sorunlarına veya aslına uygunluk kaybına neden olabileceğini işaret ediyor. Uyumluluk Denetleyicisi, Microsoft Office Excel 2007, 2010 ve 2013'ün bir özelliğidir.

Excel 2007 veya Excel 2010'dan Excel 97'den Excel 2003'e kadar olan önceki bir sürümde bir çalışma kitabını kaydettiğinizde, Uyumluluk Denetleyicisi, çalışma kitabını önceki sürüm tarafından desteklenmeyen özellikler içerip içermediğini görmek için tarar. Uyumluluk sorunlarının nasıl ele alınacağına ilişkin kararlar almanıza yardımcı olmak için Uyumluluk Denetleyicisi, seçenekler içeren iletişim kutuları görüntüler. Çalışma kitabındaki herhangi bir sorun hakkında rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.

Bazen, belirli bir e-tablo için Uyumluluk Denetleyicisini devre dışı bırakmanız gerekir. Aspose.Cells' API'leri ile bunu dinamik olarak yapabilirsiniz, böylece kullanıcılar dosyayı Microsoft Excel'de manuel olarak yeniden kaydettiklerinde açılan Uyumluluk Denetleyicisi iletişim kutusundan rahatsız olmaz veya kafaları karışmaz.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel'de Uyumluluk Denetleyicisini devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):

-  (Excel 2007) Office düğmesinde,**HAZIRLAMA** , sonra**Uyumluluk Denetleyicisini Çalıştır** ve ardından temizleyin**Bu çalışma kitabını kaydettiğinizde uyumluluğu kontrol edin** seçenek.
-  (Excel 2010 & 2013) Dosya sekmesinde,**Bilgi** , sonra**Sorunları kontrol et** , Tıklayın**Uyumluluğu Kontrol Edin** , ve son olarak, temizleyin**Bu çalışma kitabını kaydettiğinizde uyumluluğu kontrol edin** seçenek.

## **Aspose.Cells API'leri kullanma**

 Yı kur[**WorkbookSettings.CheckComptiliblite**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) mülkiyet**Yanlış** Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için.

Bir şablon XLS dosyamız olduğunu varsayalım. Bir kullanıcı bunu MS Excel 2007/2010/2013'te kaydettiğinde veya yeniden kaydettiğinde, aşağıdaki ekran görüntüsünde gösterildiği gibi Uyumluluk Denetleyicisi iletişim kutusu görüntülenir.

![yapılacaklar:resim_alternatif_Metin](disable-compatibility-checker-in-excel_1.png)

Aşağıdaki kod, Uyumluluk Denetleyicisinin Aspose.Cells for Java ile nasıl devre dışı bırakılacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
