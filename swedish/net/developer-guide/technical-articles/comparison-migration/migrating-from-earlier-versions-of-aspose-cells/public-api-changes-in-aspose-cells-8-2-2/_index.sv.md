---
title: Offentlig API Ändringar i Aspose.Cells 8.2.2
type: docs
weight: 90
url: /sv/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.2.1 till 8.2.2 som kan vara av intresse för modul-/applikationsutvecklare.

{{% /alert %}} 
## **Lade till API:er**
### **Property BuiltInDocumentPropertyCollection.Version tillagd**
Den nya egenskapen Version har lagts till i klassen BuiltInDocumentPropertyCollection för att göra det möjligt för utvecklare att hämta versionen av programmet som skapade ett visst kalkylblad.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln[Hämta versionen av programmet som skapade kalkylarket](/cells/sv/net/get-the-version-number-of-the-application-that-created-the-excel-document/) för mer information.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Egenskapsdiagram. Arbetsblad tillagt**
Före lanseringen av Aspose.Cells 8.2.2 var det inte möjligt att hämta instansen av arbetsbladet från ett diagramobjekt som det innehåller. Aspose.Cells 8.2.2 har fyllt upp denna lucka genom att tillhandahålla egenskapen Chart.Worksheet.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln[Skaffa arbetsblad av diagrammet](/cells/sv/net/get-worksheet-of-the-chart/) för mer information.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
