---
title: Aspose.Cells in TrueType Font ları nasıl kullandığı
type: docs
weight: 10
url: /tr/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells, PDF, XPS ve görüntüler gibi formatlara elektronik tabloları renderlarken TrueType font'ları gerektirir.

Aspose.Cells bir elektronik tablo renderladığında, elektronik tabloda kullanılan TrueType font'larına erişim gerektirir. Bu, PDF, XPS ve görüntü oluşturma sırasında normal bir uygulamadır ve dönüştürülen belge veya görüntünün herhangi bir görüntüleyici için aynı görünmesini sağlar.

{{% /alert %}}

## **Fontlar Hakkında**

### **Font Erişilebilirliği ve Yedekleme**

Bir elektronik tablo, Arial, Times New Roman, Verdana ve diğer fontlar gibi çeşitli fontlar kullanılarak biçimlendirilebilir. Aspose.Cells bir elektronik tablo renderladığında, elektronik tabloda kullanılan fontları seçmeye çalışır. Ancak, tam font mevcut olmayabilecek durumlar vardır, bu durumda Aspose.Cells benzer bir font seçmek zorunda kalır.

Aşağıda, Aspose.Cells'in sahnenin arkasındaki süreci bulunmaktadır.

1. Aspose.Cells, elektronik tabloda kullanılan tam font adına eşleşen fontları dosya sisteminde bulmaya çalışır.
1. Aspose.Cells, aynı isimdeki fontları bulamazsa, Workbook'ün DefaultStyle.Font özelliği altında belirtilen varsayılan fontu kullanmaya çalışır.
1. Aspose.Cells, işlemine mevcut tüm fontlardan en uygun fontları seçmeye çalışır.
1. Son olarak, Aspose.Cells dosya sistemde hiçbir font bulamazsa, elektronik tabloyu Arial kullanarak renderler.

### **Aspose.Cells'in Font Aradığı Yerler**

Aspose.Cells, dosya sisteminden TrueType fontlarını otomatik olarak bulmaya çalışır. Genellikle TrueType fontlarını bulmak için Aspose.Cells'in varsayılan davranışına güvenebilirsiniz, ancak bazen TrueType font'larını içeren klasörleri FontConfigs.setFontFolder fabrika yöntemi kullanarak belirtmeniz gerekebilir.

### **Tipik Fontla İlgili Problemler ve Çözümler**

Bu tablo, Aspose.Cells kullanarak elektronik tabloları PDF'e renderlerken karşılaşabileceğiniz bazı problemleri ve çözümlerini listeler.

{{% alert color="primary" %}}

Herhangi bir font kopyalarken çoğu fontun telif hakkı olduğunu unutmayın. Bir fontun lisansını önceden bulun ve başka bir makineye serbestçe aktarılabilir olduklarını doğrulayın. 

{{% /alert %}}

|**Problem** |**Sebep** |**Çözüm** |
| :- | :- | :- |
|Render edilen belgedeki düzen ve fontlar orijinalden farklı. |Aspose.Cells'i Linux veya Mac OS'ta kullanıyorsunuz, burada TureType fontları varsayılan olarak bulunmadığından Aspose.Cells bilgisayarınızda fontları bulamıyor. |TrueType font dosyalarını Windows makinesinden kopyalayın veya TrueType font paketi yükleyin. TrueType font dosyalarının konumunu belirtmek için FontConfigs.setFontFolder fabrika yöntemini kullanın.|

{{% alert color="primary" %}}

Detaylı makaleleri kontrol edin

- [Linux'ta TrueType fontları nasıl yerleştireceğiniz](/cells/tr/java/how-to-install-truetype-fonts-on-linux/).
- [TrueType font'larının konumunu nasıl belirteceğiniz](/cells/tr/java/how-to-specify-truetype-fonts-location/).
- [TrueType font yedekleme gerçekleştiğinde uyarıları nasıl alırsınız](/cells/tr/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
