---
title: Öffentlich API Änderungen in Aspose.Cells 8.5.1
type: docs
weight: 180
url: /de/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.5.0 zu 8.5.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-5-1/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Methode Workbook.Dispose Hinzugefügt**
Aspose.Cells for Java 8.5.1 hat die Workbook.dispose-Methode verfügbar gemacht, um die nicht verwalteten Ressourcen des Workbook-Objekts freizugeben. Das Dispose-Muster wird nur für Objekte verwendet, die auf nicht verwaltete Ressourcen zugreifen, z. B. Datei- und Pipe-Handles, Registrierungshandles, Wait-Handles oder Zeiger auf Blöcke von nicht verwaltetem Speicher. Dies liegt daran, dass der Garbage Collector beim Zurückgewinnen nicht verwendeter verwalteter Objekte sehr effizient ist, aber nicht in der Lage ist, nicht verwaltete Objekte zurückzugewinnen.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Methode Cell.getHeightOfValue hinzugefügt**
 Aspose.Cells for Java 8.5.1 hat die Methode Cell.getHeightOfValue bereitgestellt, um die Höhe des Zellenwerts abzurufen. Mit dieser Methode können Sie die Höhe des Zellenwerts berechnen und dann die Höhe der Zeile dieser Zelle festlegen. Überprüfen Sie den ausführlichen Artikel auf[wie man die Zellenhöhe und -breite berechnet](/cells/de/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Enumeration TableDataSourceType hinzugefügt**
Aspose.Cells for Java 8.5.1 hat die Enumeration com.aspose.cells.TableDataSourceType verfügbar gemacht, um den Datenquellentyp eines ListObject abzurufen. Die TableDataSourceType-Enumeration als folgende Felder.

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Eigenschaft ListObject.DataSourceType hinzugefügt**
Mit der Veröffentlichung von v8.5.1 hat Aspose.Cells API die schreibgeschützte ListObject.DataSourceType-Eigenschaft verfügbar gemacht, die verwendet werden kann, um den Datenquellentyp eines ListObject zu erkennen.

Hier ist das einfachste Anwendungsszenario.

**Java**

{{< highlight "csharp" >}}

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
