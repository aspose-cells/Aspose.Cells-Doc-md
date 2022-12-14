---
title: Hücreleri biçimlendir
linktitle: Hücreleri biçimlendir
type: docs
weight: 120
url: /tr/net/cells-formatting/
description: .NET Framework, .NET Core, Mono veya Xamarin Platformlarında Excel dosyaları için sayı biçimini, kenarlığı ve arka plan rengini ayarlayın.
---
## **giriiş**

{{% alert color="primary" %}}

 Aspose.Cells şunları sağlar:[**Stil Al**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) yöntemleri[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf, bir hücrenin biçimlendirme stilini almak/ayarlamak için kullanılır. Aspose.Cells ayrıca bir[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)sınıf.

{{% /alert %}}

## **GetStyle ve SetStyle Yöntemlerini kullanarak Cells'i biçimlendirin**

Arka plan veya ön plan renkleri, kenarlıklar, yazı tipleri, yatay ve dikey hizalamalar, girinti düzeyi, metin yönü, döndürme açısı ve çok daha fazlasını ayarlamak için hücrelere farklı biçimlendirme stilleri uygulayın.

### **GetStyle ve SetStyle Yöntemlerini Kullanma**

 Geliştiricilerin farklı hücrelere farklı biçimlendirme stilleri uygulamaları gerekiyorsa,[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) kullanarak hücrenin[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) yöntemi, stil özniteliklerini belirtin ve ardından kullanarak biçimlendirmeyi uygulayın.[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)yöntem. Bir hücreye çeşitli biçimlendirmeler uygulamak için bu yaklaşımı göstermek üzere aşağıda bir örnek verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Farklı Biçimlendirmek İçin Stil Nesnesini Kullanma Cells**

 Geliştiricilerin aynı biçimlendirme stilini farklı hücrelere uygulamaları gerekiyorsa, kullanabilirler[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne. kullanmak için lütfen aşağıdaki adımları izleyin.[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne:

1.  Ekle[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) çağırarak nesne[**Stil Oluştur**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf
1.  Yeni eklenenlere erişin[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne
1.  İstenen özellikleri/öznitelikleri ayarlayın.[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)istenen biçimlendirme ayarlarını uygulamak için nesne
1. Yapılandırılanı ata[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)istediğiniz hücrelere itiraz edin

Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve bellek tasarrufu da sağlayabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Microsoft Excel 2007 Önceden Tanımlanmış Stilleri Kullanma**

Microsoft Excel 2007 için farklı biçimlendirme stilleri uygulamanız gerekirse, Aspose.Cells API'i kullanarak stilleri uygulayın. Hücreye önceden tanımlanmış bir stil uygulamak için bu yaklaşımı gösteren bir örnek aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Cell'de Seçili Karakterleri Biçimlendirme**

Yazı Tipi Ayarları ile ilgilenmek, hücrelerdeki metnin nasıl biçimlendirileceğini açıklar, ancak yalnızca tüm hücre içeriğinin nasıl biçimlendirileceğini açıklar. Yalnızca seçili karakterleri biçimlendirmek isterseniz ne olur?

Aspose.Cells bu özelliği de desteklemektedir. Bu konuda, bu özelliği nasıl etkili bir şekilde kullanacağımız açıklanmaktadır.

### **Seçilen Karakterleri Biçimlendirme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 bu[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf sağlar[**Karakterler**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)bir hücre içindeki bir karakter aralığını seçmek için aşağıdaki parametreleri alan yöntem:

- **Dizini başlat**, seçimin başladığı karakterin dizini.
- **Karakter sayısı**, seçilecek karakter sayısı.

 bu[**Karakterler**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) yöntemi örneğini döndürür[**Yazı Tipi Ayarı**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)geliştiricilerin karakterleri, aşağıda kod örneğinde gösterildiği gibi bir hücrede olduğu gibi biçimlendirmelerine izin veren sınıf. Çıktı dosyasında, A1 hücresinde, 'Ziyaret' sözcüğü varsayılan yazı tipiyle biçimlendirilecek ancak 'Aspose!' kalın ve mavidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 Bir hücredeki Zengin Metnin bir bölümünü biçimlendirmekle ilgileniyorsanız,[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemler. bu[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) Yöntem, metnin bölümlerine erişmek için kullanılacaktır ve daha sonra düzeltmeler kullanılarak yapılabilir.[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntem oysa**Almak**yöntem bir dizi döndürür[**Yazı Tipi Ayarı**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) yazı tipi adı, yazı tipi rengi, kalınlık vb. gibi çeşitli özellikleri ayarlamak için değiştirilebilen nesneler ve**Ayarlamak** Yöntem, değişiklikleri uygulamak için kullanılabilir.

{{% /alert %}}

## **Satırları ve Sütunları Biçimlendirme**

Bazen, geliştiricilerin aynı biçimlendirmeyi satırlara veya sütunlara uygulamaları gerekir. Hücrelere tek tek biçimlendirme uygulamak genellikle daha uzun sürer ve iyi bir çözüm değildir.
Bu sorunu çözmek için Aspose.Cells, bu makalede ayrıntılı olarak açıklanan basit ve hızlı bir yol sağlar.

### **Satırları ve Sütunları Biçimlendirme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)toplama sağlar[**Satırlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)Toplamak.

### **Satır Biçimlendirme**

 İçindeki her öğe[**Satırlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) koleksiyon temsil eder[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row) nesne. bu[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row)nesne şunları sunar:[**Stili Uygula**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) satırın biçimlendirmesini ayarlamak için kullanılan yöntem. Aynı biçimlendirmeyi bir satıra uygulamak için,[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne. Aşağıdaki adımlar nasıl kullanılacağını göstermektedir.

1.  Ekle[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) itiraz etmek[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını çağırarak[**Stil Oluştur**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)yöntem.
1.  Yı kur[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)biçimlendirme ayarlarını uygulamak için nesnenin özellikleri.
1.  için ilgili öznitelikleri AÇIK duruma getirin.[**Stil Bayrağı**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)nesne.
1. Yapılandırılanı ata[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) itiraz etmek[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row)nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Bir Sütunu Biçimlendirme**

 bu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) toplama ayrıca bir[**Sütunlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) Toplamak. İçindeki her öğe[**Sütunlar**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) koleksiyon temsil eder[**Kolon**](https://reference.aspose.com/cells/net/aspose.cells/column) nesne. benzer bir[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row) nesne,[**Kolon**](https://reference.aspose.com/cells/net/aspose.cells/column) nesne ayrıca şunları sunar:[**Stili Uygula**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)Bir sütunu biçimlendirme yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **ileri konular**
- [Hizalama Ayarları](/cells/tr/net/cells-alignment-settings/)
- [Kenarlık Ayarları](/cells/tr/net/cells-border-settings/)
- [Excel ve ODS dosyalarının Koşullu Biçimlerini ayarlayın.](/cells/tr/net/conditional-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/net/excel-themes-and-colors/)
- [Dolgu Ayarları](/cells/tr/net/cells-fill-settings/)
- [Yazı Tipi Ayarları](/cells/tr/net/cells-font-settings/)
- [Bir Çalışma Kitabında Çalışma Sayfasını Biçimlendir Cells](/cells/tr/net/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sistemini Uygulayın](/cells/tr/net/implement-1904-date-system/)
- [Birleşme ve Ayrılma Cells](/cells/tr/net/merging-and-unmerging-cells/)
- [Sayı Ayarları](/cells/tr/net/cells-number-settings/)
- [Hücreler için Stil Al ve Ayarla](/cells/tr/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

