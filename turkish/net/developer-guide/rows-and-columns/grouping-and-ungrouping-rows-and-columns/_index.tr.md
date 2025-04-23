---
title: Satır ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 50
url: /tr/net/grouping-and-ungrouping-rows-and-columns/
---

## **Giriş**

Bir Microsoft Excel dosyasında, veriler için bir biçim oluşturarak tek bir fare tıklamasıyla ayrıntı seviyelerini gösterip gizleyebilirsiniz.

Yalnızca özetler veya başlıkların bulunduğu satırları veya sütunları hızlı bir şekilde görüntülemek için **Özet Sembolleri**, 1,2,3, + ve - simgelerine tıklayabilirsiniz veya simgeleri kullanarak bir çalışma sayfasındaki bir bölümün altındaki ayrıntıları görebilirsiniz, aşağıdaki şekilde gösterildiği gibi:

|**Satır ve Sütun Gruplama.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Satır ve Sütun Grubu Yönetimi**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu sağlar.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için birkaç yöntem sağlar, bunlardan bazıları aşağıda daha detaylı olarak tartışılmıştır.

### **Satır ve Sütun Gruplama**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) ve [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) yöntemlerini çağırarak satırları veya sütunları gruplamak mümkündür. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun indeksi, grup içindeki ilk satır veya sütun.
- Son satır/sütun indeksi, grup içindeki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Grup Ayarları**

Microsoft Excel, görüntüleme için grup ayarlarını yapılandırmanıza izin verir:

- Detayın altında özet satırlar.
- Ayrıntının sağında özet sütunlar.

Geliştiriciler, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) özelliğini kullanarak bu grup ayarlarını yapılandırabilir.

### **Detaydan Aşağı Özet Satırlar**

Özet satırların detayın altında gösterilip gösterilmeyeceğini kontrol etmek de **true** veya **false** olarak [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) sınıfının [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) özelliğini ayarlayarak mümkündür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Detayın Sağına Özet Sütunlar**

Geliştiriciler, ayrıntının sağında özet sütunları göstermek veya gizlemek için [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) sınıfının [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) özelliğini **true** veya **false** olarak ayarlayabilirler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Satır ve Sütunların Gruplandırılmasını Kaldırma**

Gruplanmış herhangi bir satır veya sütunu ayırmak için, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) ve [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) metodlarını çağırın. Her iki metod da iki parametre alır:

- İlk satır veya sütun dizini, ayrılmak istenen ilk satır/sütun.
- Son satır veya sütun dizini, ayrılmak istenen son satır/sütun.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index), üçüncü bir Boolean parametresi alan bir aşırı yüklemesi vardır. **true** olarak ayarlayarak tüm gruplanmış bilgileri kaldırabilirsiniz. Aksi takdirde, yalnızca dış grup bilgileri kaldırılır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
