---
title: Offentliga API-ändringar i Aspose.Cells 8.5.1
type: docs
weight: 180
url: /sv/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.5.0 till 8.5.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-5-1/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Metod Workbook. Dispose tillagd**
Aspose.Cells för Java 8.5.1 har exponerat metoden Workbook.dispose för att frigöra de ohanterade resurserna för Workbook-objektet. Avyttringsmönstret används endast för objekt som har åtkomst till ohanterade resurser, såsom fil- och pipe-handtag, registerhandtag, väntehandtag eller pekare till block av ohanterat minne. Detta beror på att sopsamlaren är mycket effektiv på att återta oanvända hanterade objekt, men den kan inte återta oanvända hanterade objekt.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Metod Cell.getHeightOfValue Added**
 Aspose.Cells för Java 8.5.1 har exponerat metoden Cell.getHeightOfValue för att få höjden på cellvärdet. Genom att använda den här metoden kan du beräkna höjden på cellvärdet och sedan ställa in höjden på raden i den cellen. Kolla den detaljerade artikeln om[hur man beräknar cellens höjd och bredd](/cells/sv/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Enumeration TableDataSourceType tillagd**
Aspose.Cells för Java 8.5.1 har avslöjat uppräkningen com.aspose.cells.TableDataSourceType för att hämta datakälltypen för ett ListObject. Uppräkningen av TableDataSourceType enligt följande fält.

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Property ListObject.DataSourceType tillagd**
Med utgåvan av v8.5.1 har API:et Aspose.Cells avslöjat den skrivskyddade ListObject.DataSourceType-egenskapen som kan användas för att detektera datakällans typ av ett ListObject.

Här är det enklaste användningsscenariot.

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
