---
title: Öffentliche API Änderungen in Aspose.Cells 8.2.2
type: docs
weight: 100
url: /de/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen in der Aspose.Cells-API von Version 8.2.1 auf 8.2.2, die für Modul-/Anwendungsentwickler von Interesse sein können.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Hinzufügen der Versionseigenschaft für die BuiltInDocumentPropertyCollection-Klasse**
Die neue Eigenschaft Version wurde der BuiltInDocumentPropertyCollection-Klasse hinzugefügt, um Entwicklern zu ermöglichen, die Version der Anwendung für eine bestimmte Tabelle zu erhalten oder festzulegen.

{{% alert color="primary" %}} 

Bitte lesen Sie den ausführlichen Artikel zu [Ermitteln der Version der Anwendung, die die Tabelle erstellt hat](/cells/de/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Hinzufügen der Chart.Worksheet-Eigenschaft**
Vor der Veröffentlichung von Aspose.Cells 8.2.2 war es nicht möglich, die Instanz des Arbeitsblatts aus einem Chart-Objekt abzurufen, das es enthält. Aspose.Cells 8.2.2 hat diese Lücke geschlossen, indem die Chart.Worksheet-Eigenschaft bereitgestellt wurde.

{{% alert color="primary" %}} 

Bitte prüfen Sie den ausführlichen Artikel [Arbeitsblatt des Diagramms erhalten](/cells/de/java/get-worksheet-of-the-chart/) für weitere Informationen.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
