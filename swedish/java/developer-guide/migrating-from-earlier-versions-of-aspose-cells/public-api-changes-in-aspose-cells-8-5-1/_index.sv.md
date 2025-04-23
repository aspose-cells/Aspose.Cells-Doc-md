---
title: Ändringar i offentlig API i Aspose.Cells 8.5.1
type: docs
weight: 180
url: /sv/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.5.0 till 8.5.1 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-5-1/), men även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Lade till Workbook.Dispose-metoden**
Aspose.Cells for Java 8.5.1 har exponerat Workbook.dispose-metoden för att frigöra de hanterade resurserna i Workbook-objektet. Dispose-mönstret används endast för objekt som har åtkomst till hanterade resurser, såsom fil- och rörhandtag, registerhandtag, väntehandtag eller pekare till block av ohanterat minne. Detta beror på att soptunnan är mycket effektiv på att återta oanvända hanterade objekt, men den kan inte återta ohanterade objekt.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Lade till Cell.getHeightOfValue-metoden**
Aspose.Cells for Java 8.5.1 har exponerat Cell.getHeightOfValue-metoden för att få höjden av cellvärdet. Genom att använda denna metod kan du beräkna höjden av cellvärdet och sedan ställa in radens höjd för den cellen respektive. Se den detaljerade artikeln om [hur man beräknar cellens höjd och bredd](/cells/sv/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Uppräkning TableDataSourceType tillagd**
Aspose.Cells for Java 8.5.1 har exponerat uppräkningen com.aspose.cells.TableDataSourceType för att hämta datatypen för en ListObject. TableDataSourceType-uppräkningen har följande fält. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Lade till ListObject.DataSourceType-egenskapen**
Med släppet av v8.5.1 har Aspose.Cells API exponerat den skrivskyddade ListObject.DataSourceType-egenskapen som kan användas för att upptäcka datatypen för en ListObject.

Här är det enklaste användningsscenario.

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
{{< app/cells/assistant language="java" >}}
