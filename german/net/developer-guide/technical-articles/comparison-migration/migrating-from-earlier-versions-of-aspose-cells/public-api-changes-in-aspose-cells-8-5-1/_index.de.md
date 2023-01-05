---
title: Öffentlich API Änderungen in Aspose.Cells 8.5.1
type: docs
weight: 170
url: /de/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.5.0 zu 8.5.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-5-1/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Methode Workbook.Dispose Hinzugefügt**
Das Workbook-Objekt implementiert jetzt die System.IDisposable-Schnittstelle, die über eine einzige Dispose-Methode verfügt. Sie können die Workbook.Dispose-Methode entweder direkt aufrufen oder ein Workbook-Objekt in einer Using-Struktur erstellen, um diese Methode automatisch aufzurufen.

**C#**

{{< highlight "csharp" >}}

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


### **Methode Cell.GetHeightOfValue hinzugefügt**
 Aspose.Cells for .NET 8.5.1 hat die Methode Cell.GetHeightOfValue bereitgestellt, um die Höhe des Zellenwerts abzurufen. Mit dieser Methode können Sie die Höhe des Zellenwerts berechnen und dann die Höhe der Zeile dieser Zelle festlegen. Überprüfen Sie den ausführlichen Artikel auf[wie man die Zellenhöhe und -breite berechnet](/cells/de/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Enumeration TableDataSourceType hinzugefügt**
Aspose.Cells for .NET 8.5.1 hat die Enumeration Aspose.Cells.Tables.TableDataSourceType verfügbar gemacht, um den Datenquellentyp eines ListObject abzurufen. Die TableDataSourceType-Enumeration als folgende Felder.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Arbeitsblatt
1. TableDataSourceType.XML
### **Eigenschaft ListObject.DataSourceType hinzugefügt**
Mit der Veröffentlichung von v8.5.1 hat Aspose.Cells API die schreibgeschützte ListObject.DataSourceType-Eigenschaft verfügbar gemacht, die verwendet werden kann, um den Datenquellentyp eines ListObject zu erkennen.

Hier ist das einfachste Anwendungsszenario.

**C#**

{{< highlight "csharp" >}}

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
