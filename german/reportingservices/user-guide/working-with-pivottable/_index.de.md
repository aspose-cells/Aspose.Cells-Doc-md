---
title: Arbeiten mit PivotTable
type: docs
weight: 100
url: /de/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 EIN*Pivot-Tabelle* ist eine interaktive Tabelle, die Daten zusammenfasst und sinnvoll darstellt. SQL Server Reporting Services kann einen Bericht nicht in das Microsoft Excel-Format exportieren, während eine Pivot-Tabelle beibehalten wird. Berichtsbenutzer müssen Pivot-Tabellen jedes Mal manuell erstellen, wenn sie einen Pivot-Tabellenbericht von Reporting Services nach Microsoft Excel exportieren. Mit Aspose.Cells for Reporting Services können Sie einmalig zur Entwurfszeit des Berichts eine Pivot-Tabelle entwerfen. Jedes Mal, wenn der Bericht ausgeführt wird, exportiert Aspose.Cells for Reporting Services den Bericht nach Microsoft Excel und aktualisiert die Daten in der Pivot-Tabelle.

{{% /alert %}} 

So erstellen Sie einen Pivot-Tabellenbericht:

1. Erstellen Sie ein Dataset als Datenquelle für die Pivot-Tabelle.
 Unten verwenden wir die AdventureWorks-Beispieldatenbank, die im Lieferumfang von SQL Server Reporting Services 2005 enthalten ist, und erstellen ein Dataset mit dem Namen „Sales“.
Die SQL für das Dataset lautet wie folgt:

**SQL**

{{< highlight "csharp" >}}

 SELECT  PC.Name AS ProdCat,

	    PS.Name AS SubCat,

	    DATEPART(yy, SOH.OrderDate) AS OrderYear,

	    'Q' + DATENAME(qq, SOH.OrderDate) AS OrderQtr,

         SUM(SOD.UnitPrice * SOD.OrderQty) AS Sales

FROM    Production.ProductSubcategory PS INNER JOIN

         Sales.SalesOrderHeader SOH INNER JOIN

         Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID INNER JOIN

         Production.Product P ON SOD.ProductID = P.ProductID ON PS.ProductSubcategoryID = P.ProductSubcategoryID INNER JOIN

         Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID

WHERE   (SOH.OrderDate BETWEEN '1/1/2002' AND '12/31/2003')

GROUP BY  DATEPART(yy, SOH.OrderDate), PC.Name, PS.Name, 'Q' + DATENAME(qq, SOH.OrderDate), PS.ProductSubcategoryID



{{< /highlight >}}



{{% alert color="primary" %}} 

 Bitte beziehen Sie sich auf[Datenquellen und Abfragen](/cells/de/reportingservices/data-sources-and-queries/) um mehr über das Erstellen einer Datenquelle und eines Datensatzes mit Aspose.Cells.Report.Designer zu erfahren.

{{% /alert %}} 

1.  Erstellen Sie einen Tabellenbericht gemäß der Anleitung in[Tabellenbericht erstellen](/cells/de/reportingservices/creating-tabular-report/), Wie nachfolgend dargestellt.
 Die Tabelle dient als Datenquelle für die Pivot-Tabelle.

![todo: Bild_alt_Text](working-with-pivottable_1.png)




1.  In Microsoft Excel, von der**Einfügung** Menü, auswählen**Name** und dann**Definieren**.
1. Definieren Sie einen Namen als „Verkäufe“.
 Der Bereich des Namens beginnt mit der ersten Zelle des Kopfzeilentitels und endet mit der letzten Zelle der Tabellendatenzeile, wie unten gezeigt.

![todo: Bild_alt_Text](working-with-pivottable_2.png)




1.  Klicken**OK** beenden.
1. Erstellen Sie ein neues Blatt für die Pivot-Tabelle.
1.  Von dem**Daten** Menü, auswählen**PivotTable- und PivotChart-Bericht** um eine Pivot-Tabelle hinzuzufügen.
 Ein Dialogfeld wird angezeigt.
1.  Auswählen**Microsoft Office Excel-Liste oder -Datenbank** als Datenquelle u**Pivot-Tabelle** als Berichtstyp.
1.  Klicken**Nächste** weitermachen.

![todo: Bild_alt_Text](working-with-pivottable_3.png)




1. Geben Sie im Dialogfeld „Umsatz“ ein, den oben definierten Namen.
1.  Klicken**Nächste** weitermachen.

![todo: Bild_alt_Text](working-with-pivottable_4.png)




1.  Klicken**Fertig**. 

![todo: Bild_alt_Text](working-with-pivottable_5.png)




1.  Entwerfen Sie die Pivot-Tabelle in Excel.

![todo: Bild_alt_Text](working-with-pivottable_6.png)



 Die entworfene Pivot-Tabelle ist unten dargestellt.

![todo: Bild_alt_Text](working-with-pivottable_7.png)




1.  Klicken Sie mit der rechten Maustaste auf die Pivot-Tabelle und wählen Sie sie aus**Tabellenoptionen**.
1.  Stelle sicher das**Beim Öffnen aktualisieren** ist ausgewählt.

![todo: Bild_alt_Text](working-with-pivottable_8.png)




1. Speichern Sie den Bericht und veröffentlichen Sie ihn auf dem Berichtsserver.
1. Exportieren Sie den Bericht vom Berichtsserver.
 Das Ergebnis ist unten gezeigt.

![todo: Bild_alt_Text](working-with-pivottable_9.png)
