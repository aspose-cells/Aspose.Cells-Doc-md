---
title: Boş Çalışma Sayfalarını Algılama
type: docs
weight: 710
url: /tr/java/detecting-empty-worksheets/
---
## **Doldurulmuş olup olmadığını kontrol edin Cells**
Çalışma sayfalarında, bir değerin basit (metin, sayısal, tarih/saat) veya bir formül veya formül tabanlı bir değer olabileceği değerlerle doldurulmuş bir veya daha fazla hücre olabilir. Böyle bir durumda verilen bir çalışma sayfasının boş olup olmadığını anlamak kolaydır. Kontrol etmemiz gereken tek şey[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)özellikler. Yukarıda belirtilen özellikler sıfır veya pozitif değerler döndürürse, bu, bir veya daha fazla hücrenin doldurulduğu anlamına gelir, ancak bu özelliklerden herhangi biri -1 döndürürse, bu, verilen çalışma sayfasında hiçbir hücrenin doldurulmadığını gösterir.

{{% alert color="primary" %}} 

Satırlar ve sütunlar koleksiyonlarının sıfır tabanlı bir dizini vardır, bu nedenle satır 0 ve sütun 0'daki bir hücre, çalışma sayfasındaki A1 olan ilk hücre anlamına gelir.

{{% /alert %}} 
## **Boş Başlatılmış olup olmadığını kontrol edin Cells**
 Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışma sayfasında yalnızca biçimlendirmenin uygulanmış hücrelere sahip olma olasılığı vardır. Böyle bir senaryoda,[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)özellikler, doldurulan herhangi bir değerin olmadığını belirten -1 döndürür, ancak hücre biçimlendirmesi nedeniyle başlatılan hücreler bu yaklaşım kullanılarak algılanamaz. Bir çalışma sayfasının boş başlatılmış hücrelere sahip olup olmadığını kontrol etmek için,*Iterator.hasSonraki* Cells koleksiyonundan edinilen yineleyicideki yöntem. Eğer*iterator.hasSonraki*yöntem true döndürür, bu, verilen çalışma sayfasında bir veya daha fazla başlatılmış hücre olduğu anlamına gelir.

{{% alert color="primary" %}} 

 Ayrıntılı olarak hücre numaralandırıcısını edinmenin birkaç yolu vardır.[Yineleyiciler Nasıl ve Nerede Kullanılır?](/cells/tr/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Şekilleri Denetle**
 Belirli bir çalışma sayfasında doldurulmuş hücreler olmayabilir, ancak kontroller, çizelgeler, resimler vb. gibi şekiller ve nesneler içerebilir. Bir çalışma sayfasının herhangi bir şekil içerip içermediğini kontrol etmemiz gerekirse, bunu[ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count)Emlak. Herhangi bir pozitif değer, çalışma sayfasında şekil(ler)in varlığını gösterir.
## **Programlama Örneği**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
