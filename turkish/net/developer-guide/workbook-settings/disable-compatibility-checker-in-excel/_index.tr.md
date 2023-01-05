---
title: Excel'de Uyumluluk Denetleyicisini Devre Dışı Bırak
type: docs
weight: 170
url: /tr/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## C#'de Excel Çalışma Sayfalarında Uyumluluk Denetleyicisini Devre Dışı Bırak

{{% alert color="primary" %}}

Microsoft Excel'in Uyumluluk Denetleyicisi, bir dosyayı daha eski bir dosya biçiminde kaydederken işaretler, işlevsellik sorunlarına veya aslına uygunluk kaybına neden olabilir. Uyumluluk Denetleyicisi, Microsoft Office Excel 2007 ve Microsoft Excel 2010'un bir özelliğidir.

Excel 2007 veya Excel 2010'dan Excel 97'den Excel 2003'e kadar olan önceki bir sürümde bir çalışma kitabını kaydettiğinizde, Uyumluluk Denetleyicisi, çalışma kitabını önceki sürüm tarafından desteklenmeyen özellikler içerip içermediğini görmek için tarar. Uyumluluk sorunlarının nasıl ele alınacağına ilişkin kararlar almanıza yardımcı olmak için Uyumluluk Denetleyicisi, seçenekler içeren iletişim kutuları görüntüler. Çalışma kitabındaki herhangi bir sorun hakkında rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.

Bazen, belirli bir e-tablo için Uyumluluk Denetleyicisini devre dışı bırakmanız gerekir. Aspose.Cells' API'leri ile bunu programlı olarak yapabilirsiniz, böylece kullanıcılar dosyayı Microsoft Excel'de manuel olarak yeniden kaydettiklerinde açılan Uyumluluk Denetleyicisi iletişim kutusundan rahatsız olmaz veya kafaları karışmaz.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel'de Uyumluluk Denetleyicisini devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):

-  (Excel 2007) Office düğmesinde,**Hazırlamak** , o zamanlar**Uyumluluk Denetleyicisini Çalıştır** ve ardından temizleyin**Bu çalışma kitabını kaydettiğinizde uyumluluğu kontrol edin** seçenek.
-  (Excel 2010) Dosya sekmesinde,**Bilgi** , o zamanlar**Sorunları kontrol et** , Tıklayın**Uyumluluğu Kontrol Edin** , ve son olarak, temizleyin**Bu çalışma kitabını kaydettiğinizde uyumluluğu kontrol edin** seçenek.

## **Aspose.Cells API'leri kullanma**

 Yı kur[**Workbook.Settings.CheckComptiliblite**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) mülkiyet**YANLIŞ** Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için.

### **Kod Örnekleri**

Aşağıdaki kod örnekleri, Uyumluluk Denetleyicisinin Aspose.Cells for .NET ile nasıl devre dışı bırakılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
