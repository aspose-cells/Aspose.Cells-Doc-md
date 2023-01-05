---
title: Veri Ekle ve Al
type: docs
weight: 20
url: /tr/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 İçinde[Bir Çalışma Sayfasının Cells'ine Erişme](/cells/tr/cpp/accessing-cells-of-a-worksheet/), bir çalışma sayfasındaki hücrelere erişim için temel yaklaşımları tartıştık. Bu makale, hücrelere farklı veri türleri eklemek için bu yaklaşımlardan birini kullanır.

{{% /alert %}} 
## **Cells'e Veri Ekleme**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[IÇalışma Sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf bir sağlar[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Toplamak. İçindeki her öğe[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyon bir nesneyi temsil eder[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)sınıf.

Aspose.Cells, geliştiricilerin çalışma sayfalarındaki hücrelere şunu çağırarak veri eklemesine olanak tanır:[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) sınıf[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) yöntem. Aspose.Cells, aşırı yüklenmiş sürümler sağlar.[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) geliştiricilerin hücrelere farklı türde veriler eklemesine olanak tanıyan bir yöntem. Bu aşırı yüklenmiş sürümlerini kullanarak[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)yöntemi ile hücreye Boolean, string, double, integer veya tarih/saat vb. değerler eklemek mümkündür.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Verimliliği Artırma**
 Eğer kullanırsan[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)Bir çalışma sayfasına büyük miktarda veri yerleştirme yöntemi olarak, hücrelere önce satırlara sonra sütunlara göre değerler eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.
## **Cells'den Veri Alınıyor**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[IÇalışma Sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) dosyadaki çalışma sayfalarına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf bir sağlar[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Toplamak. İçindeki her öğe[ICell'ler](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyon bir nesneyi temsil eder[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)sınıf.

 bu[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)class, geliştiricilerin veri türlerine göre hücrelerden değerler almasına izin veren çeşitli yöntemler sağlar. Bu yöntemler şunları içerir:

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), hücrenin dize değerini döndürür.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), hücrenin çift değerini döndürür.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), hücrenin boole değerini döndürür.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), hücrenin tarih/saat değerini döndürür.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), hücrenin kayan değerini döndürür.
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), hücrenin tamsayı değerini döndürür.

 Bir alan doldurulmadığında,[GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) veya[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)bir istisna atar.

 Bir hücrede bulunan veri türü kullanılarak da kontrol edilebilir.[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) sınıf[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) yöntem. Aslında,[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) sınıf[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) yöntemine dayanmaktadır[Hücre Değeri Türü](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)önceden tanımlanmış değerleri aşağıda listelenen numaralandırma:

|**Cell Değer Türleri**|**Açıklama**|
|:- |:- |
|CellValueType_IsBool|Hücre değerinin Boolean olduğunu belirtir.|
|CellValueType_IsDateTime|Hücre değerinin tarih/saat olduğunu belirtir.|
|CellValueType_IsNull|Boş bir hücreyi temsil eder.|
|CellValueType_IsNumeric|Hücre değerinin sayısal olduğunu belirtir.|
|CellValueType_IsString|Hücre değerinin dize olduğunu belirtir.|
|CellValueType_IsBilinmiyor|Hücre değerinin bilinmediğini belirtir.|
Her hücrede bulunan verilerin Türü ile karşılaştırmak için yukarıda önceden tanımlanmış hücre değeri türlerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
