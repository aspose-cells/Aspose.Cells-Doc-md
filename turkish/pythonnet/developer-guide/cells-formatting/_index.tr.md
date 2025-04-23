---
title: Hücreleri Biçimlendirin
description: Aspose.Cells for Python via .NET kullanarak hücreleri biçimlendirme ve stil verme yöntemlerini öğrenin, including sayısal biçimlendirme, tarih biçimlendirme, yazı tipi stilleri ve diğer hücre stilleri seçenekleri. Rehberimiz, çekici ve profesyonel görünümlü tablolar oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for Python via .NET, hücre biçimlendirme, stil verme, sayı biçimlendirme, tarih biçimlendirme, yazı tipi stili, hücre stili seçenekleri, elektronik tablo, oluşturma, profesyonel görünüm, satır ve sütunları biçimlendirme.
linktitle: Hücreleri Biçimlendirin
type: docs
weight: 120
url: /tr/python-net/cells-formatting/
---

## **Giriş**

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, hücrenin biçimlendirme stilini almak/ayarlamak için kullanılan [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) ve [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) metodlarını sağlar. Ayrıca, Aspose.Cells for Python via .NET [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) sınıfını da sağlar.

{{% /alert %}}

## **GetStyle ve SetStyle Metodları Kullanılarak Hücreleri Biçimlendirme**

Hücrelere arka plan veya ön plan renkleri, kenarlıklar, fontlar, yatay ve dikey hizalamalar, girinti düzeyi, yazı yönü, döndürme açısı ve çok daha fazlası için farklı türde biçimlendirme stilleri uygulayın.

### **GetStyle ve SetStyle Metodlarını Kullanma**

Geliştiricilerin farklı hücrelere farklı biçimlendirme stilleri uygulamaları gerekiyorsa, hücrenin {0} ve {1} metotlarını kullanarak hücrenin {2} özniteliklerini belirtip sonra {3} metodunu kullanarak biçimlendirme uygulamak daha iyidir. Aşağıda, bu yaklaşımın farklı biçimlendirmeyi bir hücrede uygulamak için bir örnek verilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **Farklı Hücreleri Biçimlendirmek İçin Stil Nesnesini Kullanma**

Farklı hücrelere aynı biçimlendirme stilini uygulamak istiyorsanız, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesini kullanabilirsiniz. Aşağıdaki adımları izleyin ve [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesini kullanmak için aşağıdaki adımları izleyin:

1. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) metodunu çağırarak bir [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesi ekleyin
1. Yeni eklenen [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesine erişin
1. Düzenlenmiş [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin istenen özellik/özniteliklerini ayarlayın ve istenen biçimlendirme ayarlarını uygulayın
1. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesini istenen hücrelere atayın

Bu yaklaşım uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve aynı zamanda bellek tasarrufu sağlayabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **Microsoft Excel 2007 Önceden Tanımlanmış Stilleri Nasıl Kullanılır**

Microsoft Excel 2007 için farklı biçimlendirme stilleri uygulamanız gerekiyorsa, Aspose.Cells for Python via .NET API'sini kullanarak stiller uygulayabilirsiniz. Bu yaklaşıma örnek olarak, bir hücreye önceden tanımlanmış bir stil uygulama süreçlerini gösteren aşağıdaki örnek verilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **Bir Hücredeki Seçili Karakterleri Biçimlendirme**

Yazı tipi ayarlarıyla ilgilenmek, hücre içindeki metni biçimlendirmeyi açıklar, ancak sadece hücre içeriğinin tümünü biçimlendirmeyi açıklar. Seçili karakterleri biçimlendirmek istiyorsanız ne yapacaksınız?

Aspose.Cells for Python via .NET bu özelliği de destekler. Bu konu, bu özelliğin etkili nasıl kullanılacağını açıklar.

### **Seçili Karakterleri Biçimlendirmek**

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ise [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu içindeki her öğe, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı nesnesini temsil eder.

The [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı, hücre içindeki karakterlerin bir aralığını seçmek için aşağıdaki parametreleri alan [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) metodunu sağlar:

- **Başlangıç İndeksi**, seçimin nereden başlayacağı karakterin indeksi.
- **Karakter Sayısı**, seçilecek karakterlerin sayısı.

[**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) metodu, karakterleri hücrede olduğu gibi biçimlendirmek için geliştiricilere izin veren [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) sınıfının bir örneğini döndürür. Aşağıdaki kod örneğinde gösterildiği gibi, çıktı dosyasında A1 hücresinde, 'Ziyaret' kelimesi varsayılan yazı tipiyle biçimlendirilecek ancak 'Aspose!' kalın ve mavi renkte olacaktır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

Bir hücredeki Zengin Metnin bir bölümünü biçimlendirmekle ilgileniyorsanız, [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) ve [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters) metodlarını kullanmayı düşünün. [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) metodu, metnin bölümlerine erişmek için kullanılmalıdır ve ardından düzenlemeler [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters) metodu kullanılarak yapılabilir. Ayrıca, **Get** metodu, font adı, font rengi, kalın yapma gibi çeşitli özellikleri ayarlamak için manipüle edilebilecek [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) nesneler dizisi dönerken, **Set** metodu bu değişiklikleri uygulamak için kullanılır.

{{% /alert %}}

## **Satırları ve Sütunları Nasıl Biçimlendirilir**

Bazı durumlarda, geliştiricilerin satırlara veya sütunlara aynı biçimlendirmeyi uygulamaları gerekebilir. Hücrelere tek tek biçimlendirme uygulamak genellikle daha uzun sürer ve iyi bir çözüm değildir.
Bu sorunu çözmek için, Aspose.Cells for Python via .NET bu makalede detaylıca tartışılan basit ve hızlı bir yöntem sağlar.

### **Satırları ve Sütunları Biçimlendirme**

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişmek için kullanılan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ise [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu ise [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) koleksiyonunu sağlar.

### **Bir Satırı Nasıl Biçimlendirirsiniz**

[**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) koleksiyonundaki her öğe, bir [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) nesnesini temsil eder. [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) nesnesi, satırın biçimlendirmesini ayarlamak için kullanılan [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) metodunu sunar. Bir satıra aynı biçimlendirmeyi uygulamak için, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesini kullanın. Aşağıdaki adımlar nasıl kullanılacağını gösterir.

1. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesini, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfına [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) metodunu çağırarak ekleyin.
1. Biçimlendirme ayarlarını uygulamak için [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin özelliklerini ayarlayın.
1. İlgili özellikleri [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) nesnesi için AÇIK hale getirin.
1. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesini, [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) nesnesine atayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **Bir Sutunu Nasıl Biçimlendirirsiniz**

[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu ayrıca bir [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns) koleksiyonu sağlar. [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns) koleksiyonundaki her öğe, bir [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) nesnesini temsil eder. Bir [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) nesnesine benzer şekilde, [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) nesnesi de sütunu biçimlendirmek için [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) metodunu sunar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Gelişmiş Konular**
- [Hizalama Ayarları](/cells/tr/python-net/cells-alignment-settings/)
- [Kenarlık Ayarları](/cells/tr/python-net/cells-border-settings/)
- [Excel ve ODS dosyalarının Koşullu Biçimleri ayarlanması.](/cells/tr/python-net/conditional-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/python-net/excel-themes-and-colors/)
- [Doldurma Ayarları](/cells/tr/python-net/cells-fill-settings/)
- [Font Ayarları](/cells/tr/python-net/cells-font-settings/)
- [Bir İşkitapta Hücreleri Biçimlendirme](/cells/tr/python-net/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sistemi Uygulama](/cells/tr/python-net/implement-1904-date-system/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/python-net/merging-and-unmerging-cells/)
- [Sayı Ayarları](/cells/tr/python-net/cells-number-settings/)
- [Hücreler için Stili Getirme ve Ayarlama](/cells/tr/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

