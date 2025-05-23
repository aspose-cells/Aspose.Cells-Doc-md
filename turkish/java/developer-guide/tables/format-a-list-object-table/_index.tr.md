---
title: Liste Nesnesini Biçimlendirme  Tablo
type: docs
weight: 50
url: /tr/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

İlgili veri grubunu yönetmek ve analiz etmek için, hücre aralığını bir liste nesnesine (aynı zamanda bir Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Bir tablo, ilişkili verileri içeren bir dizi satır ve sütun, diğer satır ve sütunlardaki veriden bağımsız olarak yönetilir. Varsayılan olarak, tablodaki her sütunun başlık satırında filtreleme etkinleştirilir, böylece listeniz nesnesi verilerinizi hızlı bir şekilde filtreleyebilir veya sıralayabilir. Listeniz nesnesine (sayısal verilerle çalışmak için faydalı olan bir listede özel bir satır) toplam satır ekleyebilirsiniz. Bu toplam satırın her hücresi için bir toplama işlevlerinin açılır menüsünü sağlayan özel bir satır. Aspose.Cells, listelerin (veya tabloların) oluşturulması ve yönetilmesi için seçenekler sunar.

{{% /alert %}}

## **Liste Nesnesini Biçimlendirme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) koleksiyonu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntemler yelpazesi sağlar. Bir çalışma sayfasında [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) oluşturmak için, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject), aslında, [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection) sınıfının bir nesnesidir ve bu sınıf, bir Liste nesnesi eklemek ve kapsaması gereken hücre aralığını belirtmek için add yöntemini sağlar. Belirtilen hücre aralığına göre, Aspose.Cells ile bir [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) çalışma sayfasında oluşturulur. Tabloyu ihtiyaçlarınıza göre biçimlendirmek için öznitelikleri (örneğin, [**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType-)) kullanın.

Aşağıdaki örnek, bir çalışma sayfasına örnek veriler ekler, bir [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ekler ve ona varsayılan stilleri uygular. Bu işlem için Microsoft Excel 2007/2010 tarafından desteklenen [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) stili vardır.

Kod çalıştırıldığında aşağıdaki çıktı oluşturulur.

**Çalışma sayfasında biçimlendirilmiş bir tablo oluşturulur** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
{{< app/cells/assistant language="java" >}}
