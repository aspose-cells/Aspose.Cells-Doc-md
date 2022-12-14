---
title: Aspose.Cells, TrueType Yazı Tiplerini nasıl kullanır?
type: docs
weight: 10
url: /tr/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells, elektronik tabloları PDF, XPS ve resimler gibi biçimlerde işlerken TrueType yazı tiplerini gerektirir.

Aspose.Cells bir elektronik tablo oluşturduğunda, elektronik tabloda kullanılan TrueType yazı tiplerine erişim gerektirir. Bu, PDF, XPS ve görüntü oluşturma sırasında normal bir uygulamadır ve dönüştürülen belgenin veya görüntünün herhangi bir izleyici için aynı görünmesini sağlar.

{{% /alert %}}

## **Yazı Tipleri Hakkında**

### **Yazı Tipi Kullanılabilirliği ve Değiştirme**

Bir elektronik tablo, Arial, Times New Roman, Verdana ve diğerleri gibi çeşitli yazı tipleri kullanılarak biçimlendirilebilir. Aspose.Cells bir elektronik tablo oluşturduğunda, elektronik tabloda kullanılan yazı tiplerini seçmeye çalışır. Ancak, tam yazı tipinin mevcut olmadığı durumlar vardır, bu nedenle Aspose.Cells bunun yerine benzer bir yazı tipini değiştirmek zorunda kalır.

Aspose.Cells'in perde arkasından takip ettiği süreç aşağıdadır.

1. Aspose.Cells, dosya sisteminde elektronik tabloda kullanılan yazı tipi adıyla tam olarak eşleşen yazı tiplerini bulmaya çalışır.
1. Aspose.Cells tam olarak aynı ada sahip yazı tiplerini bulamazsa, Workbook'un DefaultStyle.Font özelliği altında belirtilen varsayılan yazı tipini kullanmayı dener.
1. Aspose.Cells, çalışma kitabının DefaultStyle.Font özelliği altında tanımlanan yazı tipini bulamazsa, mevcut tüm yazı tiplerinden en uygun yazı tiplerini seçmeye çalışır.
1. Son olarak, Aspose.Cells dosya sisteminde herhangi bir yazı tipi bulamazsa, elektronik tabloyu Arial kullanarak işler.

### **Aspose.Cells Yazı Tiplerini Nerede Arar?**

Aspose.Cells, dosya sisteminde TrueType yazı tiplerini otomatik olarak bulmaya çalışır. TrueType yazı tiplerini bulmak için çoğu zaman Aspose.Cell'in varsayılan davranışına güvenebilirsiniz, ancak bazen FontConfigs.setFontFolder fabrika yöntemini kullanarak TrueType yazı tiplerini içeren klasörleri belirtmeniz gerekebilir.

### **Yazı Tipiyle İlgili Tipik Sorunlar ve Çözümler**

Bu tablo, Aspose.Cells'i kullanarak elektronik tabloları PDF'ye dönüştürürken karşılaşabileceğiniz bazı sorunları ve çözümlerini listeler.

{{% alert color="primary" %}}

 Herhangi bir yazı tipini kopyalarken çoğu yazı tipinin telif hakkına sahip olduğunu unutmayın. Önce bir yazı tipinin lisansını önceden bulun ve başka bir makineye serbestçe aktarılabildiğini doğrulayın.

{{% /alert %}}

|**Sorun** |**Sebep** |**Çözüm** |
|:- |:- |:- |
| İşlenen belgedeki düzen ve yazı tipleri orijinalinden farklı.| TureType yazı tiplerinin varsayılan olarak bulunmadığı Linux veya Mac OS'de Aspose.Cells kullanıyorsunuz, bu nedenle Aspose.Cells, bilgisayarınızda yazı tiplerini bulamıyor.|TrueType yazı tipi dosyalarını bir Windows makinesinden kopyalayın veya bir TrueType yazı tipi paketi kurun. Yazı tipi dosyalarının konumunu belirtmek için FontConfigs.setFontFolder fabrika yöntemini kullanın.|

{{% alert color="primary" %}}

Ayrıntılı makaleleri kontrol edin

- [TrueType yazı tiplerini Linux'a nasıl yerleştirebilirim?](/cells/tr/java/how-to-install-truetype-fonts-on-linux/).
- [TrueType yazı tiplerinin konumu nasıl belirlenir](/cells/tr/java/how-to-specify-truetype-fonts-location/).
- [Yazı tipi değişikliği gerçekleştiğinde nasıl uyarı alınır?](/cells/tr/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
