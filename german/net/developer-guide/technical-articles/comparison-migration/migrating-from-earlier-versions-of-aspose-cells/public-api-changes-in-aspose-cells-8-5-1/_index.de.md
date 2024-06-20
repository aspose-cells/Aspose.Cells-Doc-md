---
title: Öffentliche API Änderungen in Aspose.Cells 8.5.1
type: docs
weight: 170
url: /de/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

In diesem Dokument werden die Änderungen an der Aspose.Cells-API von Version 8.5.0 auf 8.5.1 beschrieben, die für Modul-/Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-5-1/), sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Methode Workbook.Dispose hinzugefügt**
Das Workbook-Objekt implementiert nun das System.IDisposable-Interface, das eine einzelne Dispose-Methode hat. Sie können entweder direkt die Workbook.Dispose-Methode aufrufen oder ein Workbook-Objekt in einer Using-Struktur erstellen, um diese Methode automatisch aufzurufen.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **Hinzugefügt Cell.GetHeightOfValue Methode**
Aspose.Cells for .NET 8.5.1 hat die Methode Cell.GetHeightOfValue freigegeben, um die Höhe des Zellwerts zu erhalten. Mit dieser Methode können Sie die Höhe des Zellwerts berechnen und dann die Höhe der Zeile dieser Zelle entsprechend festlegen. Prüfen Sie den ausführlichen Artikel zu [wie man die Höhe und Breite der Zellwerte berechnet](/cells/de/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Hinzugefügt TableDataSourceType Enumeration**
Aspose.Cells for .NET 8.5.1 hat die Enumeration Aspose.Cells.Tables.TableDataSourceType freigegeben, um den Datenquellentyp eines ListObjects abzurufen. Die Enumeration TableDataSourceType hat folgende Felder.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Hinzugefügtes ListObject.DataSourceType-Eigenschaft**
Mit der Veröffentlichung von v8.5.1 hat die Aspose.Cells-API die schreibgeschützte ListObject.DataSourceType-Eigenschaft freigelegt, die dazu verwendet werden kann, den Datentyp der Datenquelle eines ListObjects zu erkennen.

Hier ist das einfachste Anwendungsszenario.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
