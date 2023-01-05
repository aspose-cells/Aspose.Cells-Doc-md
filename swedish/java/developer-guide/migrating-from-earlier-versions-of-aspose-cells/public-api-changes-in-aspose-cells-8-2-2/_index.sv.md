---
title: Offentlig API Ändringar i Aspose.Cells 8.2.2
type: docs
weight: 100
url: /sv/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.2.1 till 8.2.2 som kan vara av intresse för modul-/applikationsutvecklare.

{{% /alert %}} 
## **Lade till API:er**
### **Egenskapsversion tillagd för klassen BuiltInDocumentPropertyCollection**
Den nya egenskapsversionen har lagts till i klassen BuiltInDocumentPropertyCollection för att göra det möjligt för utvecklare att hämta eller ställa in versionen av applikationen för ett visst kalkylblad.

{{% alert color="primary" %}} 

 Vänligen kontrollera detaljerad artikel om[Hämta versionen av programmet som skapade kalkylarket](/cells/sv/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Egenskapsdiagram. Arbetsblad tillagt**
Före lanseringen av Aspose.Cells 8.2.2 var det inte möjligt att hämta instansen av arbetsbladet från ett diagramobjekt som det innehåller. Aspose.Cells 8.2.2 har fyllt upp denna lucka genom att tillhandahålla egenskapen Chart.Worksheet.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln[Skaffa arbetsblad av diagrammet](/cells/sv/java/get-worksheet-of-the-chart/) för mer information.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
