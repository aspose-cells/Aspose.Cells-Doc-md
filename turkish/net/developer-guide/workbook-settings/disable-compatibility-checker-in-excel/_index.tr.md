---
title: Excel de Uyumluluk Denetimini Devre Dışı Bırakma
type: docs
weight: 170
url: /tr/net/disable-compatibility-checker-in-excel/
description: Bu makale, Aspose.Cells for .NET API aracılığıyla uyumluluk denetimini devre dışı bırakmanın nasıl yapıldığını göstermektedir.
keywords: Excel de Uyumluluk Denetimini Devre Dışı Bırakma, C# da Excel de Uyumluluk Denetimini Devre Dışı Bırakma, Çalışma Kitabında Uyumluluk Denetimini Devre Dışı Bırakma 
---

## C#'da Excel'de Uyumluluk Denetimini Devre Dışı Bırakma 

{{% alert color="primary" %}}

Microsoft Excel'in Uyumluluk Denetçisi, bir dosyayı önceki bir dosya biçiminde kaydedildiğinde işlevsellik sorunlarına veya sadelik kaybına neden olabilecek özellikleri tespit eder. Uyumluluk Denetçisi, Microsoft Office Excel 2007 ve Microsoft Excel 2010'un bir özelliğidir.

Excel 2007 veya 2003'ten Excel 2007 veya 2010'a kaydederken, Uyumluluk Denetçisi, daha önceki sürüm tarafından desteklenmeyen özellikleri içeren bir dosya olup olmadığını kontrol etmek için çalışma kitabını tarar. Uyumluluk sorunları hakkında kararlar vermenize yardımcı olmak için, Uyumluluk Denetçisi, seçenekleri içeren iletişim kutuları görüntüler. Ayrıca, çalışma kitabındaki herhangi bir sorun hakkında bir rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.

Bazen belirli bir elektronik tablo için Uyumluluk Denetçisini devre dışı bırakmanız gerekebilir. Aspose.Cells'ın API'ları sayesinde bu işlemi programlı olarak yapabilirsiniz, böylece kullanıcılar dosyayı Microsoft Excel'de manuel olarak yeniden kaydettiklerinde Uyumluluk Denetçisi ile ilgili bir iletişim kutusu çıkmaz ve kullanıcıların kafası karışmaz.

{{% /alert %}}

## **Microsoft Excel'de Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**

Microsoft Excel'de Uyumluluk Denetçisini devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):

- (Excel 2007) Office düğmesine tıklayın, **Hazırla**'yı tıklayın, ardından **Uyumluluk Denetleyicisini Çalıştır**'ı tıklayın ve **Bu çalışma kitabını kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.
- (Excel 2010) Dosya sekmesine tıklayın, sonra **Bilgi**'ye tıklayın, **Sorunları kontrol et**'i tıklayın, **Uyumluluğu Kontrol Et**'i tıklayın ve son olarak **Bu çalışbook'u kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.

## **Aspose.Cells API'ları kullanarak Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**

Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için **False** olarak [**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) özelliğini ayarlayın.

### **Kod Örnekleri**

Aşağıdaki kod örnekleri, Uyumluluk Denetleyicisini Aspose.Cells for .NET ile devre dışı bırakmanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
