---
title: Offentliga API ändringar i Aspose.Cells 8.2.2
type: docs
weight: 90
url: /sv/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.2.1 till 8.2.2 som kan vara av intresse för modul/tillämpningsutvecklare.

{{% /alert %}} 
## **Tillagda API:er**
### **Lade till BuiltInDocumentPropertyCollection.Version Egenskap**
Den nya egenskapen Version har lagts till BuiltInDocumentPropertyCollection-klassen för att möjliggöra för utvecklare att hämta versionen av programmet som skapade ett givet kalkylblad.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln [Få den version av applikationen som skapade kalkylarket](/cells/sv/net/get-the-version-number-of-the-application-that-created-the-excel-document/) för mer information.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Lade till Chart.Worksheet Egenskap**
Före släppet av Aspose.Cells 8.2.2 var det inte möjligt att hämta instansen av Worksheet från ett Chart-objekt den innehåller. Aspose.Cells 8.2.2 har fyllt i denna lucka genom att tillhandahålla Chart.Worksheet-egenskapen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln [Hämta arbetsbladet i diagrammet](/cells/sv/net/get-worksheet-of-the-chart/) för mer information.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
