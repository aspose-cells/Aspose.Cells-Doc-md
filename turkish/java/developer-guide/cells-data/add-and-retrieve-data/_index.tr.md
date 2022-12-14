---
title: Veri Ekle ve Al
type: docs
weight: 20
url: /tr/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 İçinde[Bir Çalışma Sayfasının Cells'ine Erişme](/cells/tr/java/accessing-cells-of-a-worksheet/)bir çalışma sayfasındaki hücrelere erişim için temel yaklaşımları tartıştık. Bu makale, hücrelere farklı veri türleri eklemek için bu yaklaşımlardan birini kullanır.

{{% /alert %}} 
## **Cells'e Veri Ekleme**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf.

 Aspose.Cells, geliştiricilerin şunu çağırarak çalışma sayfalarındaki hücrelere veri eklemesine olanak tanır:[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf'[değer ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Emlak. kullanarak[değer ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)özelliği ile hücreye Boolean, string, double, integer veya tarih/saat vb. değerler eklemek mümkündür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Verimliliği Artırma**
{{% alert color="primary" %}} 

 Eğer kullanırsan[değer ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Çalışma sayfasına büyük miktarda veri eklemek için, hücrelere değerleri önce satırlara sonra sütunlara göre eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

{{% /alert %}} 

Çalışma sayfaları üzerinde çalışırken, kullanıcılar hücrelere farklı türde veriler ekleyebilir. Bu veri öğeleri, boolean, tamsayı, kayan nokta, metin veya tarih/saat değerlerini içerebilir. Aspose.Cells ile hücrelerden veri türlerine göre uygun değerleri alabilirsiniz.
## **Cells'den Veri Alınıyor**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Bu bir Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf.

 bu[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)class, geliştiricilerin veri türlerine göre hücrelerden değerler almasına izin veren çeşitli özellikler sağlar. Bu özellikler şunları içerir:

- [Dize değeri](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), hücrenin dize değeri.
- [Çift Değer](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), hücrenin çift değerini döndürür.
- [BoolDeğeri](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), hücrenin Boolean değeri.
- [TarihSaatDeğeri](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), hücrenin tarih/saat değeri.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), hücrenin kayan değeri.
- [İç Değer](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), hücrenin tamsayı değeri.

 Ayrıca, bir hücrede bulunan veri türü kullanılarak da kontrol edilebilir.[Tip](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) mülkiyeti[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf. Aslında,[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf'[Tip](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) mülkiyet dayanmaktadır[Hücre Değeri Türü](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)önceden tanımlanmış değerleri aşağıda listelenen numaralandırma:

|**Cell Değer Türleri**|**Tanım**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Hücre değerinin Boolean olduğunu belirtir.|
|[DIR-DİR_TARİH_ZAMAN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Hücre değerinin tarih/saat olduğunu belirtir.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Hücrenin bir hata değeri içerdiğini temsil eder|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Boş bir hücreyi temsil eder.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Hücre değerinin sayısal olduğunu belirtir.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Hücre değerinin bir dize olduğunu belirtir.|
|[BİLİNMEYEN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Hücre değerinin bilinmediğini belirtir.|
Her hücrede bulunan veri tipiyle karşılaştırmak için yukarıda önceden tanımlanmış hücre değeri tiplerini de kullanabilirsiniz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
