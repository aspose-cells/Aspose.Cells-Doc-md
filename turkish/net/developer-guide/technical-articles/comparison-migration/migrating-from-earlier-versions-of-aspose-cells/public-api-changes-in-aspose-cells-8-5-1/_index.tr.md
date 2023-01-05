---
title: Genel API Aspose.Cells 8.5.1'deki değişiklikler
type: docs
weight: 170
url: /tr/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.5.0'dan 8.5.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-5-1/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yöntem Workbook.Dispose Eklendi**
Çalışma kitabı nesnesi artık tek bir Dispose yöntemi olan System.IDisposable arabirimini uygular. Bu yöntemi otomatik olarak çağırmak için Workbook.Dispose yöntemini doğrudan çağırabilir veya bir Workingbook nesnesini bir using yapısında oluşturabilirsiniz.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **Yöntem Cell.GetHeightOfValue Eklendi**
 Aspose.Cells for .NET 8.5.1, hücre değerinin yüksekliğini almak için Cell.GetHeightOfValue yöntemini kullanıma sundu. Bu yöntemi kullanarak hücre değerinin yüksekliğini hesaplayabilir ve ardından sırasıyla o hücrenin satır yüksekliğini ayarlayabilirsiniz. Ayrıntılı makaleyi kontrol edin[hücre yüksekliği ve genişliği nasıl hesaplanır](/cells/tr/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Numaralandırma TableDataSourceType Eklendi**
Aspose.Cells for .NET 8.5.1, bir ListObject veri kaynağı türünü almak için Aspose.Cells.Tables.TableDataSourceType numaralandırmasını kullanıma sundu. Aşağıdaki alanlar olarak TableDataSourceType numaralandırması.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Özellik ListObject.DataSourceType Eklendi**
v8.5.1 sürümüyle birlikte Aspose.Cells API, bir ListObject veri kaynağı türünü algılamak için kullanılabilecek salt okunur ListObject.DataSourceType özelliğini kullanıma sunmuştur.

İşte en basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
