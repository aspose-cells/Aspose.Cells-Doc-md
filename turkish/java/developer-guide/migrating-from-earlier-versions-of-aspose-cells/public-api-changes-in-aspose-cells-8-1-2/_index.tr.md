---
title: Genel API Aspose.Cells 8.1.2'deki değişiklikler
type: docs
weight: 70
url: /tr/java/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.1.1'den 8.1.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **Yazı Tipi Değiştirme Oluşursa Uyarı İçin Destek Eklendi**
Aspose.Cells for Java 8.1.2 ile, elektronik tabloları görüntülere, XPS & PDF biçimlerine dönüştürürken yazı tipi değişikliği meydana geldiğinde geliştiricilerin uyarı almasına izin vermek için WarningInfo ve WarningType sınıfları, IWarningCallback arayüzü ve SaveOptions.WarningCallback ve ImageOrPrintOptions.WarningCallback özellikleri eklendi.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Elektronik Tabloları İşlerken Yazı Tipi Değiştirme Uyarıları Alma](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) daha fazla bilgi için.

{{% /alert %}}
## **Eski PdfSaveOptions.ChartImageType Özelliği Silindi**
Aspose.Cells for Java 8.1.2, kullanılmayan PdfSaveOptions.ChartImageType özelliğini genel API'den kaldırdı.
