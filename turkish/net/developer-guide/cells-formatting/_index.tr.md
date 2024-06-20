---
title: Hücreleri Biçimlendirin
description: Aspose.Cells for .NET de hücre biçimlendirme ve stili hakkında bilgi edinin, sayı biçimlendirme, tarih biçimlendirme, font stilleri ve diğer hücre stili seçeneklerini içerir. Rehberimiz size çekici ve profesyonel görünümlü elektronik tablolar oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, hücre biçimlendirme, stil, sayı biçimlendirme, tarih biçimlendirme, font stili, hücre stili seçenekleri, elektronik tablo, oluştur, profesyonel görünüm, satırları ve sütunları biçimlendir.
linktitle: Hücreleri Biçimlendirin
type: docs
weight: 120
url: /tr/net/cells-formatting/
---

## **Giriş**

{{% alert color="primary" %}}

Aspose.Cells, [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının formatlama stili almak/ayarlamak için kullanılan [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metotlarını sağlar. Aspose.Cells ayrıca bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) sınıfı sağlar.

{{% /alert %}}

## **GetStyle ve SetStyle Metodları Kullanılarak Hücreleri Biçimlendirme**

Hücrelere arka plan veya ön plan renkleri, kenarlıklar, fontlar, yatay ve dikey hizalamalar, girinti düzeyi, yazı yönü, döndürme açısı ve çok daha fazlası için farklı türde biçimlendirme stilleri uygulayın.

### **GetStyle ve SetStyle Metodlarını Kullanma**

Geliştiricilerin farklı hücrelere farklı biçimlendirme stilleri uygulamaları gerekiyorsa, hücrenin {0} ve {1} metotlarını kullanarak hücrenin {2} özniteliklerini belirtip sonra {3} metodunu kullanarak biçimlendirme uygulamak daha iyidir. Aşağıda, bu yaklaşımın farklı biçimlendirmeyi bir hücrede uygulamak için bir örnek verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Farklı Hücreleri Biçimlendirmek İçin Stil Nesnesini Kullanma**

Farklı hücrelere aynı biçimlendirme stilini uygulamak istiyorsanız, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesini kullanabilirsiniz. Aşağıdaki adımları izleyin ve [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesini kullanmak için aşağıdaki adımları izleyin:

1. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) metodunu çağırarak bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi ekleyin
1. Yeni eklenen [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesine erişin
1. Düzenlenmiş [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin istenen özellik/özniteliklerini ayarlayın ve istenen biçimlendirme ayarlarını uygulayın
1. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesini istenen hücrelere atayın

Bu yaklaşım uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve aynı zamanda bellek tasarrufu sağlayabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Microsoft Excel 2007 Önceden Tanımlanmış Stilleri Nasıl Kullanılır**

Microsoft Excel 2007 için farklı biçimlendirme stilleri uygulamanız gerekiyorsa, Aspose.Cells API'sını kullanarak stilleri uygulayın. Aşağıdaki örnek, bir hücreye önceden tanımlanmış bir stil uygulamanın bu yaklaşımını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Bir Hücredeki Seçili Karakterleri Biçimlendirme**

Yazı tipi ayarlarıyla ilgilenmek, hücre içindeki metni biçimlendirmeyi açıklar, ancak sadece hücre içeriğinin tümünü biçimlendirmeyi açıklar. Seçili karakterleri biçimlendirmek istiyorsanız ne yapacaksınız?

Aspose.Cells bu özelliği de destekler. Bu konu, bu özelliği nasıl etkili bir şekilde kullandığımızı açıklar.

### **Seçili Karakterleri Biçimlendirmek**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sunar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

The [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfı, hücre içindeki karakterlerin bir aralığını seçmek için aşağıdaki parametreleri alan [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) metodunu sağlar:

- **Başlangıç İndeksi**, seçimin nereden başlayacağı karakterin indeksi.
- **Karakter Sayısı**, seçilecek karakterlerin sayısı.

[**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) metodu, karakterleri hücrede olduğu gibi biçimlendirmek için geliştiricilere izin veren [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) sınıfının bir örneğini döndürür. Aşağıdaki kod örneğinde gösterildiği gibi, çıktı dosyasında A1 hücresinde, 'Ziyaret' kelimesi varsayılan yazı tipiyle biçimlendirilecek ancak 'Aspose!' kalın ve mavi renkte olacaktır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Bir hücredeki Zengin Metnin bir kısmını biçimlendirmek istiyorsanız, [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) ve [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodlarını kullanmayı düşünebilirsiniz. [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) metodu metnin bölümlerine erişmek için kullanılır ve ardından değişiklikler [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodu kullanılarak yapılabilirken **Get** metodu, değişikliklerin yapılmasına izin veren [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) nesnelerinin bir dizisini döndürür ve **Set** metodu değişikliklerin uygulanmasında kullanılabilir.

{{% /alert %}}

## **Satırları ve Sütunları Nasıl Biçimlendirilir**

Bazı durumlarda, geliştiricilerin satırlara veya sütunlara aynı biçimlendirmeyi uygulamaları gerekebilir. Hücrelere tek tek biçimlendirme uygulamak genellikle daha uzun sürer ve iyi bir çözüm değildir.
Bu sorunu ele almak için, Aspose.Cells bu makalede detaylı bir şekilde tartışılan basit ve hızlı bir yol sağlar.

### **Satırları ve Sütunları Biçimlendirme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu bir [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) koleksiyonu sağlar.

### **Bir Satırı Nasıl Biçimlendirirsiniz**

[**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) koleksiyonundaki her öğe, bir [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) nesnesini temsil eder. [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) nesnesi, satırın biçimlendirmesini ayarlamak için kullanılan [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metodunu sunar. Bir satıra aynı biçimlendirmeyi uygulamak için, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesini kullanın. Aşağıdaki adımlar nasıl kullanılacağını gösterir.

1. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesini, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfına [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) metodunu çağırarak ekleyin.
1. Biçimlendirme ayarlarını uygulamak için [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin özelliklerini ayarlayın.
1. İlgili özellikleri [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) nesnesi için AÇIK hale getirin.
1. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesini, [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) nesnesine atayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Bir Sutunu Nasıl Biçimlendirirsiniz**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu ayrıca bir [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) koleksiyonu sağlar. [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) koleksiyonundaki her öğe, bir [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column) nesnesini temsil eder. Bir [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) nesnesine benzer şekilde, [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column) nesnesi de sütunu biçimlendirmek için [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metodunu sunar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Gelişmiş Konular**
- [Hizalama Ayarları](/cells/tr/net/cells-alignment-settings/)
- [Kenarlık Ayarları](/cells/tr/net/cells-border-settings/)
- [Excel ve ODS dosyalarının Koşullu Biçimleri ayarlanması.](/cells/tr/net/conditional-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/net/excel-themes-and-colors/)
- [Doldurma Ayarları](/cells/tr/net/cells-fill-settings/)
- [Font Ayarları](/cells/tr/net/cells-font-settings/)
- [Bir İşkitapta Hücreleri Biçimlendirme](/cells/tr/net/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sistemi Uygulama](/cells/tr/net/implement-1904-date-system/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/net/merging-and-unmerging-cells/)
- [Sayı Ayarları](/cells/tr/net/cells-number-settings/)
- [Hücreler için Stili Getirme ve Ayarlama](/cells/tr/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

