---
title: Aspose.Cells 8.5.1 de Genel API Değişiklikleri
type: docs
weight: 180
url: /tr/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 8.5.0'dan 8.5.1'e Aspose.Cells API'sindeki değişiklikleri modül / uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklar. Bu, yeni ve güncellenmiş genel yöntemlerinin yanı sıra [eklenen sınıflara vs.](/cells/tr/java/public-api-changes-in-aspose-cells-8-5-1/) aynı zamanda Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Eklendi Workbook.Dispose Yöntemi**
Aspose.Cells for Java 8.5.1, Workbook.dispose yöntemini, Workbook nesnesinin yönetilmeyen kaynaklarını serbest bırakmak için açıklamıştır. Atık toplayıcısı, kullanılmayan yönetilen nesneleri kurtarma konusunda çok etkilidir, ancak yönetilmeyen nesneleri kurtaramaz.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Eklendi Cell.getHeightOfValue Yöntemi**
Aspose.Cells for Java 8.5.1, Cell.getHeightOfValue yöntemini hücre değerinin yüksekliğini almak için açıklamıştır. Bu yöntemi kullanarak hücre değerinin yüksekliğini hesaplayabilir ve ardından hücrenin satır yüksekliğini buna göre ayarlayabilirsiniz.
### **Numaralandırma TableDataSourceType Eklendi**
Aspose.Cells for Java 8.5.1, bir ListObject'in veri kaynağı türünü almak için enumeration com.aspose.cells.TableDataSourceType numaralandırmasını açıklamıştır. TableDataSourceType numaralandırması aşağıdaki alanlara sahiptir. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Eklendi ListObject.DataSourceType Özelliği**
v8.5.1 sürümüyle birlikte, Aspose.Cells API'si, bir ListObject'in veri kaynağı türünü algılamak için salt okunur ListObject.DataSourceType özelliğini açıklamıştır.

İşte en basit kullanım senaryosu.

**Java**

{{< highlight csharp >}}

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
