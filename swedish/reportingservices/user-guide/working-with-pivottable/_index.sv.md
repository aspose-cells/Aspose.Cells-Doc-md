---
title: Arbeta med PivotTable
type: docs
weight: 100
url: /sv/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 A*pivottabell* är en interaktiv tabell som sammanfattar data och presenterar den på ett meningsfullt sätt. SQL Server Reporting Services kan inte exportera en rapport till Microsft Excel-format samtidigt som en pivottabell bibehålls. Rapportanvändare måste manuellt skapa pivottabeller varje gång de exporterar en pivottabellsrapport från Reporting Services till Microsoft Excel. Med Aspose.Cells för Reporting Services kan du designa en pivottabell en gång vid rapportdesign. Varje gång rapporten körs exporterar Aspose.Cells för Reporting Services rapporten till Microsoft Excel och uppdaterar data till pivottabellen.

{{% /alert %}} 

Så här skapar du en pivottabellsrapport:

1. Skapa en datauppsättning som datakälla för pivottabellen.
Nedan använder vi exempeldatabasen AdventureWorks som levereras med SQL Server Reporting Services 2005 och skapar en datauppsättning med namnet "försäljning".
 SQL för datasetet är som följer:

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

 Vänligen hänvisa till[Datakällor och frågor](/cells/sv/reportingservices/data-sources-and-queries/) för att lära dig mer om hur du skapar en datakälla och datauppsättning med Aspose.Cells.Report.Designer.

{{% /alert %}} 

1.  Skapa en tabellrapport enligt instruktionen i[Skapa tabellrapport](/cells/sv/reportingservices/creating-tabular-report/), enligt nedanstående.
 Tabellen kommer att vara datakällan för pivottabellen.

![todo:image_alt_text](working-with-pivottable_1.png)




1.  I Microsoft Excel, från**Föra in** menyn, välj**namn** och då**Definiera**.
1. Definiera ett namn som "försäljning".
 Namnets område börjar med den första cellen i rubriktiteln och slutar vid den sista cellen i tabelldataraden som visas nedan.

![todo:image_alt_text](working-with-pivottable_2.png)




1.  Klick**OK** att avsluta.
1. Skapa ett nytt ark för pivottabellen.
1.  Från**Data** menyn, välj**Pivottabell och pivotdiagramrapport** för att lägga till en pivottabell.
 En dialogruta visas.
1.  Välj**Microsoft Office Excel-lista eller databas** som datakälla och**pivottabell** som rapporttyp.
1.  Klick**Nästa** att fortsätta.

![todo:image_alt_text](working-with-pivottable_3.png)




1. I dialogrutan anger du "försäljning", namnet du definierade ovan.
1.  Klick**Nästa** att fortsätta.

![todo:image_alt_text](working-with-pivottable_4.png)




1.  Klick**Avsluta**. 

![todo:image_alt_text](working-with-pivottable_5.png)




1.  Designa pivottabellen i Excel.

![todo:image_alt_text](working-with-pivottable_6.png)



Den designade pivottabellen visas nedan.

![todo:image_alt_text](working-with-pivottable_7.png)




1.  Högerklicka på pivottabellen och välj**Tabellalternativ**.
1.  Se till att**Uppdatera vid öppen** är vald.

![todo:image_alt_text](working-with-pivottable_8.png)




1. Spara rapporten och publicera den på rapportservern.
1. Exportera rapporten från rapportservern.
 Resultatet visas nedan.

![todo:image_alt_text](working-with-pivottable_9.png)
