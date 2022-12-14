---
title: Öffentlich API Änderungen in Aspose.Cells 8.2.2
type: docs
weight: 100
url: /de/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.2.1 zu 8.2.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Eigenschaftsversion für die BuiltInDocumentPropertyCollection-Klasse hinzugefügt**
Die neue Eigenschaft Version wurde der Klasse BuiltInDocumentPropertyCollection hinzugefügt, damit Entwickler die Version der Anwendung für eine bestimmte Tabelle abrufen oder festlegen können.

{{% alert color="primary" %}} 

 Bitte überprüfen Sie den detaillierten Artikel auf[Rufen Sie die Version der Anwendung ab, die die Tabelle erstellt hat](/cells/de/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Property Chart.Arbeitsblatt hinzugefügt**
Vor der Veröffentlichung von Aspose.Cells 8.2.2 war es nicht möglich, die Instanz des Arbeitsblatts aus einem darin enthaltenen Diagrammobjekt abzurufen. Aspose.Cells 8.2.2 hat diese Lücke durch die Bereitstellung der Eigenschaft Chart.Worksheet geschlossen.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel[Holen Sie sich das Arbeitsblatt des Diagramms](/cells/de/java/get-worksheet-of-the-chart/) für mehr Informationen.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
