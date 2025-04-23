---
title: Offentliga API ändringar i Aspose.Cells 8.2.2
type: docs
weight: 100
url: /sv/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.2.1 till 8.2.2 som kan vara av intresse för modul/tillämpningsutvecklare.

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagd Versionsegenskap för BuiltInDocumentPropertyCollection Class**
Den nya egenskapen Version har lagts till BuiltInDocumentPropertyCollection-klassen för att låta utvecklare hämta eller ange versionen av programmet för ett givet kalkylblad.

{{% alert color="primary" %}} 

Se detaljerad artikel om [Hämta Version av Programmet som Skapade Kalkylbladet](/cells/sv/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Lade till Chart.Worksheet Egenskap**
Innan utgåvan av Aspose.Cells 8.2.2 var det inte möjligt att hämta instansen av Worksheet från ett Chart-objekt den innehåller. Aspose.Cells 8.2.2 har fyllt detta gap genom att tillhandahålla egenskapen Chart.Worksheet.

{{% alert color="primary" %}} 

Se den detaljerade artikeln [Hämta Kalkylbladet för Diagrammet](/cells/sv/java/get-worksheet-of-the-chart/) för mer information.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
