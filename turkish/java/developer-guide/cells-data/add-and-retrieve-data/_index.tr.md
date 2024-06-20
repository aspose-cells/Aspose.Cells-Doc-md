---
title: Veri Eklemek ve Almak
type: docs
weight: 20
url: /tr/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

[Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/java/accessing-cells-of-a-worksheet/) konusunda, bir çalışma sayfasındaki hücrelere erişmek için temel yaklaşımları tartıştık. Bu makale, hücrelere farklı tiplerde veri eklemek için bu yaklaşımlardan birini kullanır.

{{% /alert %}} 
## **Hücrelere Veri Eklemek**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)'a sahiptir. Çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonundaki her öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, geliştiricilere [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) özelliğini çağırarak çalışma sayfasındaki hücrelere veri eklemelerine izin verir. [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) özelliğini kullanarak, hücreye Boolean, dize, çift, tamsayı veya tarih/saat vb. değerler eklemek mümkündür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Verimliliği Artırma**
{{% alert color="primary" %}} 

Eğer bir çalışma sayfasına büyük miktarda veri eklemek için [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) özelliğini kullanıyorsanız, değerleri öncelikle satırlara ve ardından sütunlara eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

{{% /alert %}} 

Çalışma sayfalarında çalışırken, kullanıcılar hücrelere farklı tiplerde veri ekleyebilir. Bu veri öğeleri, boolean, tamsayı, kayan noktalı, metin veya tarih/saat değerleri içerebilir. Aspose.Cells kullanarak hücrelerdeki uygun değerleri alabilirsiniz.
## **Hücrelerden Veri Alın**
Aspose.Cells, bir Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)'ı sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)'a sahiptir. Çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonundaki her öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir nesnesini temsil eder.

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfı, hücrelerden değerleri farklı veri türlerine göre almak için geliştiricilere izin veren birkaç özellik sağlar.

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), hücrenin dize değeri.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), hücrenin çift değeri.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), hücrenin boolean değeri.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), hücrenin tarih/saat değeri.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), hücrenin kayan noktalı değeri.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), hücrenin tamsayı değeri.

Ayrıca, hücrede bulunan verinin türü, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) özelliğini kullanarak kontrol edilebilir. Aslında, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) özelliği, [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) numaralandırmasına dayalıdır ve bu numaralandırmanın önceden tanımlanmış değerleri aşağıda listelenmiştir:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Hücre değerinin boolean olduğunu belirtir.
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Hücre değerinin tarih/saat olduğunu belirtir.
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Hücrenin bir hata değeri içerdiğini temsil eder
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Boş bir hücreyi temsil eder.
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Hücre değerinin sayısal olduğunu belirtir.
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Hücre değerinin bir dize olduğunu belirtir.
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Hücre değerinin bilinmeyen olduğunu belirtir.
Yukarıdaki önceden tanımlanmış hücre değeri türlerini, her hücrede bulunan verinin türüyle karşılaştırmak için de kullanabilirsiniz.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
