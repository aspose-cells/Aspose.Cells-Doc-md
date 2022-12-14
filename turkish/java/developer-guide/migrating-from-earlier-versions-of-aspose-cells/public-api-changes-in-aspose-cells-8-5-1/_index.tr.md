---
title: Genel API Aspose.Cells 8.5.1'deki değişiklikler
type: docs
weight: 180
url: /tr/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.5.0'dan 8.5.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-5-1/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yöntem Workbook.Dispose Eklendi**
Aspose.Cells for Java 8.5.1, Workbook nesnesinin yönetilmeyen kaynaklarını serbest bırakmak için Workbook.dispose yöntemini kullanıma sundu. Atma modeli yalnızca dosya ve yönlendirme tanıtıcıları, kayıt tanıtıcıları, bekleme tutamaçları veya yönetilmeyen bellek bloklarına yönelik işaretçiler gibi yönetilmeyen kaynaklara erişen nesneler için kullanılır. Bunun nedeni, çöp toplayıcının kullanılmayan yönetilen nesneleri geri alma konusunda çok verimli olmasına karşın yönetilmeyen nesneleri geri alamamasıdır.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Yöntem Cell.getHeightOfValue Eklendi**
 Aspose.Cells for Java 8.5.1, hücre değerinin yüksekliğini elde etmek için Cell.getHeightOfValue yöntemini kullanıma sundu. Bu yöntemi kullanarak hücre değerinin yüksekliğini hesaplayabilir ve ardından sırasıyla o hücrenin satır yüksekliğini ayarlayabilirsiniz. Ayrıntılı makaleyi kontrol edin[hücre yüksekliği ve genişliği nasıl hesaplanır](/cells/tr/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Numaralandırma TableDataSourceType Eklendi**
Aspose.Cells for Java 8.5.1, bir ListObject veri kaynağı türünü almak için com.aspose.cells.TableDataSourceType numaralandırmasını kullanıma sundu. Aşağıdaki alanlar olarak TableDataSourceType numaralandırması.

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Özellik ListObject.DataSourceType Eklendi**
v8.5.1 sürümüyle birlikte Aspose.Cells API, bir ListObject veri kaynağı türünü algılamak için kullanılabilecek salt okunur ListObject.DataSourceType özelliğini kullanıma sunmuştur.

İşte en basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
