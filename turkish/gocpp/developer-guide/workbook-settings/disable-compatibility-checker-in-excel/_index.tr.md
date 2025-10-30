---
title: Excel de Uyum Denetleyicisini Golang ile C++ üzerinden Devre dışı bırakın
linktitle: Uyumluluk Denetleyicisini Devre Dışı Bırak
type: docs
weight: 170
url: /tr/go-cpp/disable-compatibility-checker-in-excel/
description: Bu makale, Aspose.Cells for C++ API si aracılığıyla uyumluluk denetleyicisini nasıl devre dışı bırakacağınızı gösterir.
keywords: C++ Uyumluluk Denetleyicisini Devre Dışı Bırak, Excel de Uyumluluk Denetleyicisini Devre Dışı Bırak, WorkBook ta Uyumluluk Denetleyicisini Kapat. 
---

## C++ ile Excel Çalışma Sayfalarında Uyumluluk Denetleyicisini Devre Dışı Bırakma

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

Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için **False** olarak [**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcheckcompatibility/) özelliğini ayarlayın.

### **Kod Örnekleri**

Aşağıdaki kod örnekleri, Aspose.Cells for C++ ile Uyumluluk Denetleyicisini nasıl devre dışı bırakacağınızı gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCompatibilityCheckerInExcel.go" >}}
