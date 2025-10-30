---
title: Veri Eklemek ve Almak
type: docs
weight: 20
url: /tr/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

[Bir Çalışma Sayfasının Hücrelerine Erişim](/cells/tr/cpp/accessing-cells-of-a-worksheet/) bölümünde, bir çalışma sayfasındaki hücrelere erişim için temel yaklaşımları tartıştık. Bu makale, bu yaklaşımlardan birini kullanarak hücrelere farklı türde veri eklemeyi ele almaktadır.

{{% /alert %}} 
## **Hücrelere Veri Eklemek**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunu sağlar. [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) içindeki her öğe, [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir nesnesini temsil eder.

Aspose.Cells, geliştiricilere hücrelere veri eklemek için [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yöntemini çağırarak veri eklemeyi sağlar. Aspose.Cells, [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yönteminin aşırı yüklenmiş sürümlerini sunar, bu sayede geliştiriciler farklı türde verileri hücrelere ekleyebilir. [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yönteminin bu aşırı yüklenmiş sürümlerini kullanarak, bir hücreye mantıksal, string, double, tamsayı veya tarih/zaman vs. gibi farklı türde veriler eklemek mümkündür.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **Verimliliği Artırma**
Eğer [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yöntemini kullanarak bir çalışma sayfasına büyük miktarda veri eklerseniz, verileri hücrelere önce satır bazında ardından sütun bazında eklemeniz gerekmektedir. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde arttırır.
## **Hücrelerden Veri Alın**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, dosyadaki çalışma sayfalarına erişim sağlar. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunu sağlar. Koleksiyondaki her öğe, [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir nesnesini temsil eder.

[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfı, geliştiricilere hücrelerden veri almak için verilerin veri türlerine göre alınmasına izin veren birkaç yöntem sağlar. Bu yöntemler şunları içerir:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), hücrenin dize değerini döndürür.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), hücrenin double değerini döndürür.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/) , hücrenin boolean değerini döndürür.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), hücrenin tarih/saat değerini döndürür.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), hücrenin float değerini döndürür
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/), hücrenin tam sayı değerini döndürür.

Bir alan doldurulmadığında, [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) veya [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) hücreleri bir istisna fırlatır.

Hücrede bulunan verinin türü ayrıca [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) metodunu kullanarak kontrol edilebilir. Aslında, [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) metodu, önceden tanımlanmış değerlerin listelendiği [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) numaralandırmasına dayanmaktadır:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|CellValueType_IsBool|Hücre değerinin Boolean olduğunu belirtir.
|CellValueType_IsDateTime|Hücre değerinin tarih/saat olduğunu belirtir.
|CellValueType_IsNull|Boş bir hücreyi temsil eder.
|CellValueType_IsNumeric|Hücre değerinin sayısal olduğunu belirtir.
|CellValueType_IsString|Hücre değerinin dize olduğunu belirtir.
|CellValueType_IsUnknown|Hücre değerinin bilinmeyen olduğunu belirtir.
Ayrıca, yukarıda önceden tanımlanmış hücre değer türlerini, her hücrede bulunan verinin Türü ile karşılaştırmak için de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
