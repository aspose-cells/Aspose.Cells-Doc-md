---
title: Öffentliche API Änderungen in Aspose.Cells 8.5.1
type: docs
weight: 180
url: /de/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.5.0 auf 8.5.1, die für Modul-/Anwendungsentwickler interessant sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen etc.](/cells/de/java/public-api-changes-in-aspose-cells-8-5-1/), sondern auch eine Beschreibung von Änderungen im Verhalten im Hintergrund von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Methode Workbook.Dispose hinzugefügt**
Aspose.Cells for Java 8.5.1 hat die Methode Workbook.dispose freigegeben, um die nicht verwalteten Ressourcen des Workbook-Objekts freizugeben. Das Dispose-Muster wird nur für Objekte verwendet, die auf nicht verwaltete Ressourcen wie Datei- und Pipe-Handles, Registrierungsgriffe, Wartegriffe oder Zeiger auf Blöcke nicht verwalteten Speichers zugreifen. Dies liegt daran, dass der Garbage Collector sehr effizient darin ist, nicht genutzte verwaltete Objekte zurückzugewinnen, jedoch keine unverwalteten Objekte zurückgewinnen kann.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Methode Cell.getHeightOfValue hinzugefügt**
Aspose.Cells for Java 8.5.1 hat die Methode Cell.getHeightOfValue freigegeben, um die Höhe des Zellenwerts zu erhalten. Mit dieser Methode können Sie die Höhe des Zellenwerts berechnen und dann entsprechend die Höhe der Zeile dieser Zelle festlegen. Prüfen Sie den ausführlichen Artikel über [die Berechnung der Zellenhöhe und -breite](/cells/de/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Aufzählung TableDataSourceType hinzugefügt**
Aspose.Cells for Java 8.5.1 hat die Aufzählung com.aspose.cells.TableDataSourceType freigegeben, um den Datentyp der Datenquelle eines ListObject abzurufen. Die Aufzählung TableDataSourceType mit folgenden Feldern. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Hinzugefügtes ListObject.DataSourceType-Eigenschaft**
Mit der Veröffentlichung von v8.5.1 hat die Aspose.Cells-API die schreibgeschützte ListObject.DataSourceType-Eigenschaft freigelegt, die dazu verwendet werden kann, den Datentyp der Datenquelle eines ListObjects zu erkennen.

Hier ist das einfachste Anwendungsszenario.

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
