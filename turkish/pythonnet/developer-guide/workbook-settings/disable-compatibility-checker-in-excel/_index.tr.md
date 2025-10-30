---
title: Excel de Uyumluluk Denetimini Devre Dışı Bırakma
type: docs
weight: 170
url: /tr/python-net/disable-compatibility-checker-in-excel/
description: Bu makale, Aspose.Cells for Python via .NET API aracılığıyla uyumluluk denetleyicisini devre dışı bırakmayı gösterir.
keywords: Python Dağıtımı Uyumluluk Denetleyicisini Devre Dışı Bırak, Excel Uyumluluk Denetleyicisini C# ta Devre Dışı Bırak, Çalışma Kitabında Uyumluluk Denetleyicisini Devre Dışı Bırak. 
---

## Python ile Excel Çalışma Sayfası Sekmesi Çubuğunu Devre Dışı Bırakma 

{{% alert color="primary" %}}

Microsoft Excel'in Uyumluluk Denetçisi, bir dosyayı önceki bir dosya biçiminde kaydedildiğinde işlevsellik sorunlarına veya sadelik kaybına neden olabilecek özellikleri tespit eder. Uyumluluk Denetçisi, Microsoft Office Excel 2007 ve Microsoft Excel 2010'un bir özelliğidir.

Excel 2007 veya 2003'ten Excel 2007 veya 2010'a kaydederken, Uyumluluk Denetçisi, daha önceki sürüm tarafından desteklenmeyen özellikleri içeren bir dosya olup olmadığını kontrol etmek için çalışma kitabını tarar. Uyumluluk sorunları hakkında kararlar vermenize yardımcı olmak için, Uyumluluk Denetçisi, seçenekleri içeren iletişim kutuları görüntüler. Ayrıca, çalışma kitabındaki herhangi bir sorun hakkında bir rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.

Bazen, belirli bir elektronik tablo için Uyumluluk Denetleyicisini devre dışı bırakmanız gerekebilir. Aspose.Cells for Python via .NET API’leri ile bunu programlı olarak yapabilir ve kullanıcıların Microsoft Excel'de dosyayı tekrar kaydederken Uyumluluk Denetleyicisi iletişim kutusunun ortaya çıkmasıyla hayal kırıklığına uğramalarını veya karışıklık yaşamalarını önleyebilirsiniz.

{{% /alert %}}

## **Microsoft Excel'de Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**

Microsoft Excel'de Uyumluluk Denetçisini devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):

- (Excel 2007) Office düğmesine tıklayın, **Hazırla**'yı tıklayın, ardından **Uyumluluk Denetleyicisini Çalıştır**'ı tıklayın ve **Bu çalışma kitabını kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.
- (Excel 2010) Dosya sekmesine tıklayın, sonra **Bilgi**'ye tıklayın, **Sorunları kontrol et**'i tıklayın, **Uyumluluğu Kontrol Et**'i tıklayın ve son olarak **Bu çalışbook'u kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.

## **Aspose.Cells API'ları kullanarak Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**

Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için **False** olarak [**Workbook.settings.check_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_compatibility) özelliğini ayarlayın.

### **Kod Örnekleri**

Takip eden kod örnekleri, Aspose.Cells for Python via .NET kullanarak Uyumluluk Denetleyicisini nasıl devre dışı bırakacağınızı gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-DisableCompatibilityChecker-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
