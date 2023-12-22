---
title: Hücreleri biçimlendirme
description: Sayı biçimlendirmesi, tarih biçimlendirmesi, yazı tipi stilleri ve diğer hücre stili seçenekleri dahil olmak üzere, Aspose.Cells for .NET numaralı telefondan hücreleri nasıl biçimlendireceğinizi ve stillendireceğinizi öğrenin. Kılavuzumuz çekici ve profesyonel görünümlü e-tablolar oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: Hücreleri biçimlendirme
type: docs
weight: 120
url: /tr/net/cells-formatting/
---
##  **giriiş**

{{% alert color="primary" %}}

 Aspose.Cells şunları sağlar[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) yöntemleri[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf, bir hücrenin biçimlendirme stilini almak/ayarlamak için kullanılır. Aspose.Cells ayrıca bir de sağlar[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)sınıf.

{{% /alert %}}

##  **GetStyle ve SetStyle Yöntemlerini Kullanarak Cells Nasıl Biçimlendirilir**

Arka plan veya ön plan renklerini, kenarlıkları, yazı tiplerini, yatay ve dikey hizalamaları, girinti düzeyini, metin yönünü, döndürme açısını ve çok daha fazlasını ayarlamak için hücrelere farklı biçimlendirme stilleri uygulayın.

###  **GetStyle ve SetStyle Yöntemleri Nasıl Kullanılır?**

 Geliştiricilerin farklı hücrelere farklı biçimlendirme stilleri uygulaması gerekiyorsa, o zaman[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) kullanarak hücrenin[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) yöntemini kullanarak stil niteliklerini belirtin ve ardından aşağıdakileri kullanarak biçimlendirmeyi uygulayın:[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)yöntem. Bir hücreye çeşitli biçimlendirmeler uygulamak için bu yaklaşımı göstermek amacıyla aşağıda bir örnek verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **Farklı Biçimlendirmek İçin Stil Nesnesi Nasıl Kullanılır Cells**

 Geliştiricilerin aynı biçimlendirme stilini farklı hücrelere uygulaması gerekiyorsa bunu kullanabilirler.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne. Kullanmak için lütfen aşağıdaki adımları izleyin.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne:

1.  Ekle[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) çağırarak nesneyi[**Stil Oluştur**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf
1.  Yeni eklenenlere erişin[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1.  İstediğiniz özellikleri/nitelikleri ayarlayın[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)İstenilen biçimlendirme ayarlarının uygulanacağı nesne
1.  Yapılandırılmış olanı ata[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)İstediğiniz hücrelere itiraz edin

Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve bellekten de tasarruf sağlayabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **Microsoft Excel 2007 Önceden Tanımlanmış Stiller Nasıl Kullanılır**

Microsoft Excel 2007 için farklı biçimlendirme stilleri uygulamanız gerekiyorsa, Aspose.Cells API'i kullanarak stilleri uygulayın. Bir hücreye önceden tanımlanmış bir stil uygulamak için bu yaklaşımı göstermek amacıyla aşağıda bir örnek verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **Cell'de Seçilen Karakterler Nasıl Biçimlendirilir**

Yazı Tipi Ayarlarıyla İlgilenmek, hücrelerdeki metnin nasıl biçimlendirileceğini açıklar, ancak yalnızca tüm hücre içeriğinin nasıl biçimlendirileceğini açıklar. Yalnızca seçilen karakterleri biçimlendirmek istiyorsanız ne olur?

Aspose.Cells de bu özelliği destekliyor. Bu konu, bu özelliği nasıl etkili bir şekilde kullanabileceğimizi açıklamaktadır.

###  **Seçilen Karakterler Nasıl Formatlanır**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf şunları içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf şunları sağlar[**Karakterler**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)Bir hücrenin içindeki bir karakter aralığını seçmek için aşağıdaki parametreleri alan yöntem:

- *Başlangıç Dizini**, seçimin başlayacağı karakterin dizini.
- *Karakter Sayısı**, seçilecek karakter sayısı.

[**Karakterler**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) yöntem bir örneğini döndürür[**Yazı Tipi Ayarı**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)Geliştiricilerin, aşağıda kod örneğinde gösterildiği gibi karakterleri bir hücrede olduğu gibi biçimlendirmelerine olanak tanıyan sınıf. Çıkış dosyasındaki A1 hücresindeki 'Ziyaret' kelimesi varsayılan yazı tipiyle ancak 'Aspose!' ile biçimlendirilecektir. cesur ve mavidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Bir hücredeki Zengin Metin'in bir bölümünü biçimlendirmekle ilgileniyorsanız,[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemler.[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) Metnin bazı bölümlerine erişmek için yöntem kullanılacaktır ve daha sonra bu yöntem kullanılarak değişiklikler yapılabilir.[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntem ise**Elde etmek** yöntem bir dizi döndürür[**Yazı Tipi Ayarı**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) yazı tipi adı, yazı tipi rengi, kalınlık vb. gibi çeşitli özellikleri ayarlamak için değiştirilebilen nesneler ve**Ayarlamak** Değişiklikleri uygulamak için yöntem kullanılabilir.

{{% /alert %}}

##  **Satır ve Sütunlar Nasıl Biçimlendirilir?**

Bazen geliştiricilerin aynı formatı satırlara veya sütunlara uygulaması gerekir. Hücrelere tek tek biçimlendirme uygulamak genellikle daha uzun sürer ve iyi bir çözüm değildir.
Bu sorunu çözmek için Aspose.Cells, bu makalede ayrıntılı olarak tartışılan basit ve hızlı bir yol sağlar.

###  **Satırları ve Sütunları Biçimlendirme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon sağlar[**Satırlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)Toplamak.

###  **Satır Nasıl Biçimlendirilir**

 İçindeki her öğe[**Satırlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) koleksiyon bir temsil eder[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row) nesne.[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row)nesne şunları sunar[**Stili Uygula**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) satırın biçimlendirmesini ayarlamak için kullanılan yöntem. Aynı formatı bir satıra uygulamak için[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne. Aşağıdaki adımlar nasıl kullanılacağını göstermektedir.

1.  Ekle[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) itiraz[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını çağırarak[**Stil Oluştur**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)yöntem.
1.  Yı kur[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Biçimlendirme ayarlarını uygulamak için nesnenin özelliklerini kullanın.
1.  İlgili öznitelikleri AÇIK duruma getirin[**StilBayrak**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)nesne.
1.  Yapılandırılmış olanı ata[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) itiraz[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row)nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **Sütun Nasıl Biçimlendirilir**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon aynı zamanda bir[**Sütunlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) Toplamak. İçindeki her öğe[**Sütunlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) koleksiyon bir temsil eder[**Kolon**](https://reference.aspose.com/cells/net/aspose.cells/column) nesne. Benzeri[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row) nesne,[**Kolon**](https://reference.aspose.com/cells/net/aspose.cells/column) nesne aynı zamanda şunları da sunar:[**Stili Uygula**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)Bir sütunu biçimlendirme yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **İleri konular**
- [Hizalama Ayarları](/cells/tr/net/cells-alignment-settings/)
- [Kenarlık Ayarları](/cells/tr/net/cells-border-settings/)
- [Excel ve ODS dosyalarının Koşullu Formatlarını ayarlayın.](/cells/tr/net/conditional-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/net/excel-themes-and-colors/)
- [Doldurma Ayarları](/cells/tr/net/cells-fill-settings/)
- [Yazı Tipi Ayarları](/cells/tr/net/cells-font-settings/)
- [Çalışma Kitabındaki Çalışma Sayfası Cells'i Biçimlendirme](/cells/tr/net/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sisteminin Uygulanması](/cells/tr/net/implement-1904-date-system/)
- [Birleştirme ve Ayrılma Cells](/cells/tr/net/merging-and-unmerging-cells/)
- [Numara Ayarları](/cells/tr/net/cells-number-settings/)
- [Hücreler için Stil Alma ve Ayarlama](/cells/tr/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

