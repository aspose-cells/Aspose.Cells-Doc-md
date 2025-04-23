---
title: Öffentliche API Änderungen in Aspose.Cells 8.2.2
type: docs
weight: 90
url: /de/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen in der Aspose.Cells-API von Version 8.2.1 auf 8.2.2, die für Modul-/Anwendungsentwickler von Interesse sein können.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzugefügte Eigenschaft BuiltInDocumentPropertyCollection.Version**
Die neue Eigenschaft Version wurde der BuiltInDocumentPropertyCollection-Klasse hinzugefügt, um Entwicklern die Abfrage der Version der Anwendung zu ermöglichen, die eine bestimmte Tabelle erstellt hat.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Abrufen der Version der Anwendung, die die Tabelle erstellt hat](/cells/de/net/get-the-version-number-of-the-application-that-created-the-excel-document/) für weitere Informationen.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Hinzufügen der Chart.Worksheet-Eigenschaft**
Vor der Veröffentlichung von Aspose.Cells 8.2.2 war es nicht möglich, die Instanz des Arbeitsblatts von einem Chart-Objekt abzurufen, das es enthält. Aspose.Cells 8.2.2 hat diese Lücke geschlossen, indem es die Eigenschaft Chart.Worksheet bereitgestellt hat.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Abrufen des Arbeitsblatts des Diagramms](/cells/de/net/get-worksheet-of-the-chart/) für weitere Informationen.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
