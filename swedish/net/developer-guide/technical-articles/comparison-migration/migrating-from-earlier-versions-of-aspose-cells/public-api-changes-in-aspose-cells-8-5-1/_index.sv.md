---
title: Offentliga API-ändringar i Aspose.Cells 8.5.1
type: docs
weight: 170
url: /sv/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.5.0 till 8.5.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-5-1/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Metod Workbook. Dispose tillagd**
Workbook-objekt implementerar nu System.IDisposable-gränssnittet som har en enda Dispose-metod. Du kan antingen anropa metoden Workbook.Dispose direkt eller skapa ett Workbook-objekt i en Using-struktur för att anropa den här metoden automatiskt.

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


### **Metod Cell.GetHeightOfValue Added**
 Aspose.Cells för .NET 8.5.1 har exponerat metoden Cell.GetHeightOfValue för att få höjden på cellvärdet. Genom att använda den här metoden kan du beräkna höjden på cellvärdet och sedan ställa in höjden på raden i den cellen. Kolla den detaljerade artikeln om[hur man beräknar cellens höjd och bredd](/cells/sv/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Enumeration TableDataSourceType tillagd**
Aspose.Cells för .NET 8.5.1 har avslöjat uppräkningen Aspose.Cells.Tables.TableDataSourceType för att hämta datakälltypen för ett ListObject. Uppräkningen av TableDataSourceType enligt följande fält.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Property ListObject.DataSourceType tillagd**
Med utgåvan av v8.5.1 har API:et Aspose.Cells avslöjat den skrivskyddade ListObject.DataSourceType-egenskapen som kan användas för att detektera datakällans typ av ett ListObject.

Här är det enklaste användningsscenariot.

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
