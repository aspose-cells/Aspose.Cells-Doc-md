---
title: Aspose.Cells 8.5.1 de Genel API Değişiklikleri
type: docs
weight: 170
url: /tr/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Bu belge, 8.5.0 sürümünden 8.5.1 sürümüne Aspose.Cells API'sindeki değişiklikleri, modül/uygulama geliştiricilerin ilgisini çekebilecek şekilde açıklamaktadır. Yeni ve güncellenmiş genel yöntemlerin yanı sıra [eklenen sınıflar vb](/cells/tr/net/public-api-changes-in-aspose-cells-8-5-1/)'nin yanı sıra, Aspose.Cells'in arka planda herhangi bir değişikliğinin de açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Eklendi Workbook.Dispose Yöntemi**
Workbook nesnesi artık System.IDisposable arabirimini uygular ve tek bir Dispose yöntemine sahiptir. Workbook.Dispose yöntemini doğrudan çağırabilir veya bu yöntemi otomatik olarak çağırmak için bir Using yapısı içinde Workbook nesnesi oluşturabilirsiniz.

**C#**

{{< highlight csharp >}}

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


### **Eklenen Cell.GetHeightOfValue Yöntemi**
Aspose.Cells for .NET 8.5.1, Cell.GetHeightOfValue yöntemini ortaya çıkardı ve hücre değerinin yüksekliğini almak için kullanılır. Bu yöntemi kullanarak hücre değerinin yüksekliğini hesaplayabilir ve ardından o hücrenin satır yüksekliğini ayarlayabilirsiniz.
### **TableDataSourceType Numaralandırması Eklendi**
Aspose.Cells for .NET 8.5.1, bir ListObject'in veri kaynağı türünü almak için Anenumerasyon Aspose.Cells.Tables.TableDataSourceType'ı ortaya çıkardı. TableDataSourceType numaralandırması aşağıdaki alanlara sahiptir.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Eklendi ListObject.DataSourceType Özelliği**
v8.5.1 sürümüyle birlikte, Aspose.Cells API'si, bir ListObject'in veri kaynağı türünü algılamak için salt okunur ListObject.DataSourceType özelliğini açıklamıştır.

İşte en basit kullanım senaryosu.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
