---
title: Excel'de Uyumluluk Denetleyicisini Devre Dışı Bırak
type: docs
weight: 170
url: /tr/net/disable-compatibility-checker-in-excel/
description: Bu makalede uyumluluk denetleyicisinin Aspose.Cells for .NET API aracılığıyla nasıl devre dışı bırakılacağı gösterilmektedir.
keywords: C# Disable Compatibility Checker, Excel Disable Compatibility Checker in C#, Disable Compatibility Checker in Workbook. 
---
##  C#'deki Excel Çalışma Sayfalarında Uyumluluk Denetleyicisini Devre Dışı Bırakma

{{% alert color="primary" %}}

Microsoft Bir dosyayı daha önceki bir dosya biçiminde kaydederken Excel'in Uyumluluk Denetleyicisi işaretleri, işlevsellik sorunlarına veya aslına uygunluk kaybına neden olabilir. Uyumluluk Denetleyicisi, Microsoft Office Excel 2007 ve Microsoft Excel 2010'un bir özelliğidir.

Bir çalışma kitabını Excel 97'den Excel 2003'e, Excel 2007 veya Excel 2010'dan önceki bir sürüme kaydettiğinizde, Uyumluluk Denetleyicisi çalışma kitabını tarayarak önceki sürüm tarafından desteklenmeyen özellikler içerip içermediğini kontrol eder. Uyumluluk sorunlarını nasıl çözeceğiniz konusunda karar vermenize yardımcı olmak için Uyumluluk Denetleyicisi seçeneklerin bulunduğu iletişim kutularını görüntüler. Ayrıca çalışma kitabındaki herhangi bir sorunla ilgili rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.

Bazen belirli bir e-tablo için Uyumluluk Denetleyicisini devre dışı bırakmanız gerekir. Aspose.Cells' API'leri ile bunu programlı olarak yapabilirsiniz; böylece kullanıcılar, dosyayı Microsoft Excel'de manuel olarak yeniden kaydettiklerinde açılan Uyumluluk Denetleyicisi iletişim kutusu nedeniyle hayal kırıklığına uğramaz veya kafaları karışmaz.

{{% /alert %}}

##  **Microsoft Excel kullanarak Uyumluluk Denetleyicisi Nasıl Devre Dışı Bırakılır**

Microsoft Excel'de Uyumluluk Denetleyicisi'ni devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):

-  (Excel 2007) Office düğmesinde**Hazırlayın**, ardından **Uyumluluk Denetleyicisini Çalıştırın** ve ardından **Bu çalışma kitabını kaydederken uyumluluğu denetleyin** seçeneğinin işaretini kaldırın.** seçenek.
-  (Excel 2010) Dosya sekmesinde,**Bilgi**'yi, ardından **Sorunları kontrol edin**, **Uyumluluğu Denetle**'yi tıklayın ve son olarak **Bu çalışma kitabını kaydederken uyumluluğu denetle' seçeneğinin işaretini kaldırın.** seçenek.

##  **Aspose.Cells API'lerini kullanarak Uyumluluk Denetleyicisi Nasıl Devre Dışı Bırakılır**

 Yı kur[**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) mülkiyet**YANLIŞ** Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için.

###  **Kod Örnekleri**

Aşağıdaki kod örnekleri, Uyumluluk Denetleyicisi'nin Aspose.Cells for .NET ile nasıl devre dışı bırakılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
