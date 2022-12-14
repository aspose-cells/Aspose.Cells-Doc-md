---
title: Öffentlich API Änderungen in Aspose.Cells 8.2.2
type: docs
weight: 90
url: /de/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.2.1 zu 8.2.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Eigenschaft BuiltInDocumentPropertyCollection.Version hinzugefügt**
Die neue Eigenschaft Version wurde der Klasse BuiltInDocumentPropertyCollection hinzugefügt, damit Entwickler die Version der Anwendung abrufen können, die eine bestimmte Tabelle erstellt hat.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel[Rufen Sie die Version der Anwendung ab, die die Tabelle erstellt hat](/cells/de/net/get-the-version-number-of-the-application-that-created-the-excel-document/) für mehr Informationen.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Property Chart.Arbeitsblatt hinzugefügt**
Vor der Veröffentlichung von Aspose.Cells 8.2.2 war es nicht möglich, die Instanz des Arbeitsblatts aus einem darin enthaltenen Diagrammobjekt abzurufen. Aspose.Cells 8.2.2 hat diese Lücke durch die Bereitstellung der Eigenschaft Chart.Worksheet geschlossen.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel[Holen Sie sich das Arbeitsblatt des Diagramms](/cells/de/net/get-worksheet-of-the-chart/) für mehr Informationen.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
