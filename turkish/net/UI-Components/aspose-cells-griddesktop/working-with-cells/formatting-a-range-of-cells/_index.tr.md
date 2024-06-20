---
title: Hücre Aralığının Biçimlendirilmesi
type: docs
weight: 60
url: /tr/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop,format,stil,hücreler
description: Bu makale, GridDesktop taki hücrelere stil formatı uygulamanın nasıl yapılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konu ayrıca, hücrelere yazı tipi ayarları ve diğer biçimlendirme stilleri uygulama konulu konu serisine aittir. Geçmiş konularımız bu özellikleri ele almıştır. Örneğin, [Hücrenin Yazı Tipi ve Rengini Değiştirme](/hücreler/tr/net/hücrenin-yazı-tipi-ve-rengini-değiştirme/) ve [Hücrelere Stil Uygulama](/hücreler/tr/net/hücrelere-stil-uygulama/) konularına aynı özellikler hakkında bilgi edinmek için başvurabilirsiniz. Peki, eğer bu kavramları zaten ele aldıysak, bu konuda yeni olan nedir. İşte farklılık, sadece bir tek hücre yerine bir hücre aralığına biçimlendirme ayarları (yazı tipleri ve diğer stillerle ilgili) uygulayacağız. Umuyoruz ki bu konunun yine de sizin için faydalı olacağını düşüneceğiz.

{{% /alert %}} 
## **Bir Hücre Aralığının Yazı Tipi ve Stil Ayarı**
Önce, hücre aralığı oluşturmak hakkında (ki zaten önceki konularımızda çok konuştuk), biçimlendirme ayarlarından bahsetmeden önce hücre aralığı nasıl oluşturulacağını bilmeliyiz. Peki, **CellRange** sınıfını kullanarak bir hücre aralığı oluşturabiliriz. Bu sınıfın yapıcı fonksiyonu, hücrelerin aralığını belirtmek için bazı parametreleri alır. Hücre aralığını başlangıç ve bitiş hücrelerinin **Adları** veya **Satır ve Sütun İndeksleri** kullanarak belirleyebiliriz.

Bir **CellRange** nesnesini oluşturduktan sonra, **Worksheet**'ın **SetStyle**, **SetFont** ve **SetFontColor** metodlarının aşırı yüklenmiş sürümlerini kullanabiliriz. Bu metodlar, belirtilen hücre aralığına biçimlendirme ayarları uygulamak için **CellRange** nesnesi alabilir.

Bu temel kavramı anlamak için bir örneğe bakalım.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
