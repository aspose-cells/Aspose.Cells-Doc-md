---
title: Ändringar i offentlig API i Aspose.Cells 8.5.1
type: docs
weight: 170
url: /sv/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Dokumentet beskriver ändringarna i Aspose.Cells API från version 8.5.0 till 8.5.1, som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-5-1/), utan beskriver också eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Lade till Workbook.Dispose-metoden**
Arbetsbokobjektet implementerar nu System.IDisposable-gränssnittet som har en enda Dispose-metod. Du kan antingen direkt anropa Workbook.Dispose-metoden eller skapa ett Workbook-objekt i en Using-struktur för att automatiskt anropa denna metod.

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


### **Tillagd Cell.GetHeightOfValue-metod**
Aspose.Cells for .NET 8.5.1 har exponerat metoden Cell.GetHeightOfValue för att få höjden av cellvärdet. Genom att använda denna metod kan du beräkna höjden av cellvärdet och sedan ange höjden för raden för den cellen respektive. Kolla den detaljerade artikeln om [hur man beräknar cellens höjd och bredd](/cells/sv/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Tillagd uppräkningen TableDataSourceType**
Aspose.Cells for .NET 8.5.1 har exponerat uppräkningen Aspose.Cells.Tables.TableDataSourceType för att hämta datakälltypen för en ListObject. Uppräkningen TableDataSourceType har följande fält.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Lade till ListObject.DataSourceType-egenskapen**
Med släppet av v8.5.1 har Aspose.Cells API exponerat den skrivskyddade ListObject.DataSourceType-egenskapen som kan användas för att upptäcka datatypen för en ListObject.

Här är det enklaste användningsscenario.

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
