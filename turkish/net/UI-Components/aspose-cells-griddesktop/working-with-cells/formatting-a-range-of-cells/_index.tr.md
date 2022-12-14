---
title: Cells Aralığını Biçimlendirme
type: docs
weight: 60
url: /tr/net/formatting-a-range-of-cells/
---
{{% alert color="primary" %}} 

Bu konu aynı zamanda hücrelerde yazı tipi ayarlarının ve diğer biçimlendirme stillerinin uygulanmasıyla ilgili konu dizisine aittir. Son konularımız, bu tür özelliklerin ele alınması hakkında iyi bir şekilde ele alınmıştır. Örneğin, başvurabilirsiniz[Cell'in Yazı Tipi ve Rengini Değiştirme](/cells/tr/net/changing-the-font-and-color-of-a-cell/) ve[Cells'de Stilleri Uygulamak](/cells/tr/net/applying-styles-on-cells/) aynı özellikler hakkında bilgi edinmek için konular. Öyleyse, bu kavramları zaten ele aldıysak, bu konudaki yenilikler nelerdir? Bu konunun öncekilerden tek farkı, biçimlendirme ayarlarını (yazı tipleri ve diğer stillerle ilgili) tek bir hücre yerine bir dizi hücreye uygulayacak olmamızdır. Bu konuyu yine de sizin için yararlı bulacağınızı umuyoruz.

{{% /alert %}} 
## **Cells Aralığının Yazı Tipi ve Stilini Ayarlama**
 Biçimlendirme ayarlarından bahsetmeden önce (önceki konularımızda çokça konuştuk), hücre aralığını nasıl oluşturacağımızı bilmeliyiz. Pekala, kullanarak bir hücre aralığı oluşturabiliriz.**Hücre Aralığı** yapıcısı hücre aralığını belirtmek için bazı parametreler alan sınıf. Kullanarak hücre aralığını belirtebiliriz.**İsimler** veya**Satır ve Sütun İndeksleri** başlangıç ve bitiş hücrelerinin sayısı.

 Bir kez oluşturduğumuzda**Hücre Aralığı** nesnenin aşırı yüklenmiş sürümlerini kullanabiliriz.**SetStyle**, **SetFont** & **SetFontColor** alabilen Çalışma Sayfası yöntemleri**Hücre Aralığı** biçimlendirme ayarlarını belirtilen hücre aralığında uygulamak için nesne.

Bu temel kavramı anlamak için bir örneğe bakalım.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
