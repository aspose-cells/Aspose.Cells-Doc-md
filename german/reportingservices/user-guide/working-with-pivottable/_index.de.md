---
title: Arbeiten mit PivotTable
type: docs
weight: 100
url: /de/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

Ein *Pivot-Table* ist eine interaktive Tabelle, die Daten zusammenfasst und sie auf sinnvolle Weise präsentiert. SQL Server Reporting Services können einen Bericht nicht im Microsft Excel-Format exportieren, während ein Pivot-Table erhalten bleibt. Benutzer von Berichten müssen jedes Mal manuell Pivot-Tables erstellen, wenn sie einen Pivot-Table-Bericht aus den Reporting Services in Microsoft Excel exportieren. Mit Aspose.Cells for Reporting Services können Sie einmalig zur Entwurfszeit einen Pivot-Table entwerfen. Jedes Mal, wenn der Bericht ausgeführt wird, exportiert Aspose.Cells for Reporting Services den Bericht in Microsoft Excel und aktualisiert die Daten des Pivot-Table.

{{% /alert %}} 

Um einen Pivot-Table-Bericht zu erstellen:

1. Erstellen Sie ein Dataset als Datenquelle für das Pivot-Table.
   Im Folgenden verwenden wir die Beispieldatenbank AdventureWorks, die mit SQL Server Reporting Services 2005 ausgeliefert wird, und erstellen ein Dataset namens "Sales".
   Der SQL für das Dataset lautet wie folgt: 

**SQL**

{{< highlight csharp >}}

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

Bitte lesen Sie [Datenquellen und Abfragen](/cells/de/reportingservices/data-sources-and-queries/) um mehr darüber zu erfahren, wie Sie eine Datenquelle und ein Dataset mit Aspose.Cells.Report.Designer erstellen können.

{{% /alert %}} 

1. Erstellen Sie einen Tabellenbericht gemäß der Anleitung in [Erstellen eines tabellarischen Berichts](/cells/de/reportingservices/creating-tabular-report/), wie unten gezeigt.
   Die Tabelle wird die Datenquelle für den Pivot-Tabellen sein. 

![todo:image_alt_text](working-with-pivottable_1.png)




1. In Microsoft Excel, wählen Sie im **Einfügen**-Menü **Name** und dann **Definieren**.
1. Definieren Sie einen Namen als “Umsatz”.
   Der Bereich des Namens beginnt mit der ersten Zelle des Überschriftstitels und endet an der letzten Zelle der Tabellendatenzeile wie unten gezeigt. 

![todo:image_alt_text](working-with-pivottable_2.png)




1. Klicken Sie auf **OK**, um abzuschließen.
1. Erstellen Sie ein neues Blatt für die Pivot-Tabelle.
1. Wählen Sie im **Daten**-Menü **PivotTable und PivotChart-Bericht**, um eine Pivot-Tabelle hinzuzufügen.
   Es wird ein Dialogfeld angezeigt.
1. Wählen Sie **Microsoft Office Excel-Liste oder -Datenbank** als Datenquelle und **Pivot-Tabelle** als Berichtstyp.
1. Klicken Sie auf **Weiter**, um fortzufahren. 

![todo:image_alt_text](working-with-pivottable_3.png)




1. Geben Sie im Dialogfeld “Umsatz” ein, den Sie oben definiert haben.
1. Klicken Sie auf **Weiter**, um fortzufahren. 

![todo:image_alt_text](working-with-pivottable_4.png)




1. Klicken Sie auf **Fertig stellen**. 

![todo:image_alt_text](working-with-pivottable_5.png)




1. Entwerfen Sie die Pivot-Tabelle in Excel. 

![todo:image_alt_text](working-with-pivottable_6.png)



Die entworfene Pivot-Tabelle ist unten gezeigt. 

![todo:image_alt_text](working-with-pivottable_7.png)




1. Klicken Sie mit der rechten Maustaste auf die Pivot-Tabelle und wählen Sie **Tabellenoptionen**.
1. Stellen Sie sicher, dass **Aktualisierung beim Öffnen** ausgewählt ist. 

![todo:image_alt_text](working-with-pivottable_8.png)




1. Speichern Sie den Bericht und veröffentlichen Sie ihn auf dem Report Server.
1. Exportieren Sie den Bericht vom Report Server.
   Das Ergebnis ist unten gezeigt. 

![todo:image_alt_text](working-with-pivottable_9.png)
