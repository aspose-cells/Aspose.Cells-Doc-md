---
title: Boş Çalışma Sayfalarını Algılama
type: docs
weight: 410
url: /tr/net/detecting-empty-worksheets/
---
## **Doldurulmuş olup olmadığını kontrol edin Cells**

Çalışma sayfalarında, bir değerin basit (metin, sayısal, tarih/saat) veya bir formül veya formül tabanlı bir değer olabileceği değerlerle doldurulmuş bir veya daha fazla hücre olabilir. Böyle bir durumda verilen bir çalışma sayfasının boş olup olmadığını anlamak kolaydır. Kontrol etmemiz gereken tek şey[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) veya[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)özellikleri. Yukarıda belirtilen özellikler sıfır veya pozitif değerler döndürürse, bu bir veya daha fazla hücrenin doldurulduğu anlamına gelir, ancak bu özelliklerden herhangi biri -1 döndürürse, bu, verilen çalışma sayfasında hiçbir hücrenin doldurulmadığını gösterir.

{{% alert color="primary" %}}

Satırlar ve sütunlar koleksiyonları sıfır tabanlı dizine sahiptir, bu nedenle satır 0 ve sütun 0'daki bir hücre, çalışma sayfasındaki A1 olan ilk hücre anlamına gelir.

{{% /alert %}}

## **Boş Başlatılmış olup olmadığını kontrol edin Cells**

 Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışma sayfasında yalnızca biçimlendirmenin uygulanmış hücrelere sahip olma olasılığı vardır. Böyle bir senaryoda,[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)veya[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) özellikler, doldurulan herhangi bir değerin olmadığını belirten -1 döndürür, ancak hücre biçimlendirmesi nedeniyle başlatılan hücreler bu yaklaşım kullanılarak algılanamaz. Bir çalışma sayfasında boş başlatılmış hücreler olup olmadığını kontrol etmek için, şu adresten alınan numaralandırıcıda IEnumerator.MoveNext yönteminin kullanılması önerilir:[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. IEnumerator.MoveNext yöntemi dönerse**doğru** bu, verilen çalışma sayfasında bir veya daha fazla başlatılmış hücre olduğu anlamına gelir.

## **Şekilleri Denetle**

 Belirli bir çalışma sayfasında doldurulmuş hücreler olmayabilir, ancak kontroller, çizelgeler, resimler vb. gibi şekiller ve nesneler içerebilir. Bir çalışma sayfasının herhangi bir şekil içerip içermediğini kontrol etmemiz gerekirse, bunu[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)Emlak. Herhangi bir pozitif değer, çalışma sayfasında şekil(ler)in varlığını gösterir.

## **Programlama Örneği**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
