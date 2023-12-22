---
title: Veri Ekleme ve Alma
type: docs
weight: 20
url: /tr/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 İçinde[Bir Çalışma Sayfasının Cells'ine erişme](/cells/tr/cpp/accessing-cells-of-a-worksheet/)çalışma sayfasındaki hücrelere erişmeye yönelik temel yaklaşımları tartıştık. Bu makalede, hücrelere farklı türde veriler eklemek için bu yaklaşımlardan biri kullanılmaktadır.

{{% /alert %}} 
##  **Cells'e Veri Ekleme**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf sağlar[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)sınıf.

 Aspose.Cells, geliştiricilerin çalışma sayfalarındaki hücrelere veri eklemesine olanak tanır.[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıf[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yöntem. Aspose.Cells aşırı yüklenmiş versiyonlarını sağlar[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) Geliştiricilerin hücrelere farklı türde veriler eklemesine olanak tanıyan yöntem. Bu aşırı yüklenmiş sürümlerini kullanarak[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)yöntemiyle hücreye Boolean, string, double, integer veya tarih/saat vb. değerler eklemek mümkündür.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **Verimliliği Artırma**
 Eğer kullanırsan[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)Bir çalışma sayfasına büyük miktarda veri yerleştirme yönteminde, hücrelere değerleri önce satırlar, sonra sütunlar halinde eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.
##  **Cells'den Veri Alma**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Microsoft Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) dosyadaki çalışma sayfalarına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf sağlar[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)sınıf.

[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)class, geliştiricilerin hücrelerden veri türlerine göre değer almasına olanak tanıyan çeşitli yöntemler sağlar. Bu yöntemler şunları içerir:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), hücrenin dize değerini döndürür.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), hücrenin çift değerini döndürür.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), hücrenin boole değerini döndürür.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), hücrenin tarih/saat değerini döndürür.
- [FloatValue'yu Getir](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), hücrenin kayan nokta değerini döndürür.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)hücrenin tamsayı değerini döndürür.

 Bir alan doldurulmadığında hücreler[GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) veya[FloatValue'yu Getir](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)bir istisna atar.

 Bir hücrede bulunan veri türü aynı zamanda kullanılarak da kontrol edilebilir.[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıf[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) yöntem. Aslında,[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıf[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) yöntem şuna dayanmaktadır:[Hücre Değeri Türü](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)önceden tanımlanmış değerleri aşağıda listelenen numaralandırma:

|**Cell Değer Türleri**|**Tanım**|
| :- | :- |
|CellValueType_IsBool|Hücre değerinin Boolean olduğunu belirtir.|
|CellValueType_IsDateTime|Hücre değerinin tarih/saat olduğunu belirtir.|
|CellValueType_IsNull|Boş bir hücreyi temsil eder.|
|CellValueType_IsNumeric|Hücre değerinin sayısal olduğunu belirtir.|
|CellValueType_IsString|Hücre değerinin dize olduğunu belirtir.|
|CellValueType_IsBilinmiyor|Hücre değerinin bilinmediğini belirtir.|
Ayrıca, her hücrede bulunan verilerin Türüyle karşılaştırmak için yukarıdaki önceden tanımlanmış hücre değeri türlerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
