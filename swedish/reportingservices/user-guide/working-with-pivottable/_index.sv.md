---
title: Arbete med PivotTabell
type: docs
weight: 100
url: /sv/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

En *pivottabell* är en interaktiv tabell som sammanfattar data och presenterar den på ett meningsfullt sätt. SQL Server Reporting Services kan inte exportera en rapport till formatet Microsft Excel medan en pivottabell behålls. Rapportanvändare måste manuellt skapa pivottabeller varje gång de exporterar en pivottabelrapport från Rapporteringstjänster till Microsoft Excel. Med Aspose.Cells for Reporting Services kan du utforma en pivottabell en gång vid rapportdesign. Varje gång rapporten körs exporterar Aspose.Cells for Reporting Services rapporten till Microsoft Excel och uppdaterar data i pivottabellen.

{{% /alert %}} 

För att skapa en pivottabelrapport:

1. Skapa en dataset som datakälla för pivottabellen.
   Nedan använder vi det exempeldatabasen AdventureWorks som levereras med SQL Server Reporting Services 2005 och skapar en datamängd med namnet "försäljning".
   SQL för datamängden är som följer: 

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

Se [Datakällor och frågor](/cells/sv/reportingservices/data-sources-and-queries/) för att lära dig mer om hur man skapar en datakälla och datamängd med Aspose.Cells.Report.Designer.

{{% /alert %}} 

1. Skapa en tabellrapport enligt instruktionen i [Skapa tabulär rapport](/cells/sv/reportingservices/creating-tabular-report/), enligt nedan.
   Tabellen kommer att vara datamängden för pivottabellen. 

![todo:image_alt_text](working-with-pivottable_1.png)




1. I Microsoft Excel, från menyn **Infoga**, välj **Namn** och sedan **Definiera**.
1. Definiera ett namn som "försäljning".
   Intervall för namnet börjar med den första cellen i huvudtiteln och slutar vid den sista cellen i tabellens datarad enligt nedan. 

![todo:image_alt_text](working-with-pivottable_2.png)




1. Klicka på **OK** för att avsluta.
1. Skapa ett nytt blad för pivottabellen.
1. Från menyn **Data** väljer du **PivotTable och PivotChart Report** för att lägga till en pivottabell.
   En dialogruta visas.
1. Välj **Microsoft Office Excel-lista eller databas** som datakälla och **pivottabell** som rapporttyp.
1. Klicka på **Nästa** för att fortsätta. 

![todo:image_alt_text](working-with-pivottable_3.png)




1. I dialogrutan, ange “försäljning”, det namn du definierade ovan.
1. Klicka på **Nästa** för att fortsätta. 

![todo:image_alt_text](working-with-pivottable_4.png)




1. Klicka på **Slutför**. 

![todo:image_alt_text](working-with-pivottable_5.png)




1. Designa pivottabellen i Excel. 

![todo:image_alt_text](working-with-pivottable_6.png)



Den designade pivottabellen visas nedan. 

![todo:image_alt_text](working-with-pivottable_7.png)




1. Högerklicka på pivottabellen och välj **Tabelloptioner**.
1. Se till att **Uppdatera vid öppning** är valt. 

![todo:image_alt_text](working-with-pivottable_8.png)




1. Spara rapporten och publicera den till Rapportservern.
1. Exportera rapporten från Rapportservern.
   Resultatet visas nedan. 

![todo:image_alt_text](working-with-pivottable_9.png)
