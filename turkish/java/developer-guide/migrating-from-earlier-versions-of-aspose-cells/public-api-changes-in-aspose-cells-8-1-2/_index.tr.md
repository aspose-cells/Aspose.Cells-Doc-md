---
title: Aspose.Cells 8.1.2 de Genel API Değişiklikleri
type: docs
weight: 70
url: /tr/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için ilgi çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.1.1'den 8.1.2'ye, yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki değişikliklerin açıklamasını da içermektedir.

{{% /alert %}} 
## **Yedekleme Yapılması Durumunda Uyarı Desteği Eklendi**
Aspose.Cells for Java 8.1.2 ile, font yedekleme durumunda uyarı almak için  WarningInfo ve WarningType sınıfları, IWarningCallback arayüzü ve SaveOptions.WarningCallback ve ImageOrPrintOptions.WarningCallback özellikleri eklenmiştir. Bu değişiklikler, elektronik tabloların resimlere, XPS ve PDF formatlarına dönüştürülürken font yedekleme durumunda geliştiricilerin uyarı almasına olanak tanımaktadır. 

{{% alert color="primary" %}} 

Font Değiştirme Uyarılarını Almak için Detaylı Makaleye bakın [Spreadsheets Rendelerken Font Değiştirme Uyarılarını Almak](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) daha fazla bilgi için.

{{% /alert %}}
## **Artık Kullanılmayan PdfSaveOptions.ChartImageType Özelliği Silindi**
Aspose.Cells for Java8.1.2, PdfSaveOptions.ChartImageType özelliğini genel API'dan kaldırdı.
{{< app/cells/assistant language="java" >}}
