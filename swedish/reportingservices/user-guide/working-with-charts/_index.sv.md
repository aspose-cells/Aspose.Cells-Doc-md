---
title: Arbeta med diagram
type: docs
weight: 110
url: /sv/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells Rapportmall stöder Microsoft Excel-diagram. Varje gång du kör en rapport fylls diagrammet på med de senaste datorna. 

{{% /alert %}} 

För att lägga till ett diagram i rapportmall:

1. Skapa först datasetet som kommer att vara datakälla för diagrammet.
   Här använder vi exempelvis AdventureWorks provdatabas som följer med SQL Server Reporting Services 2005 och skapar ett dataset som heter Försäljning.
   Detta SQL definierar datasetet: 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



Se [Datakällor och frågor](/cells/sv/reportingservices/data-sources-and-queries/) för att lära dig mer om hur man skapar en datakälla och dataset i Aspose.Cells.Report.Designer.

1. Skapa en tabellrapport enligt instruktionerna i [Skapa en tabellrapport](/cells/sv/reportingservices/creating-tabular-report/). Rapporten vi har skapat för detta exempel är nedan. Tabellen är diagrammets datakälla. 

![todo:image_alt_text](working-with-charts_1.png)




1. I Microsoft Excel klickar du på **Infoga**-menyn och väljer **Diagram**.
1. Klicka på **Nästa**. 

![todo:image_alt_text](working-with-charts_2.png)




1. Klicka på fliken **Serie**. 

![todo:image_alt_text](working-with-charts_3.png)




1. Klicka på **Lägg till**. 

![todo:image_alt_text](working-with-charts_4.png)




1. I dialogrutan, ställ in värdet på Serie1 (Kvartalsserie) till tabellens första datafält.
   I exemplet är det "CompanySales!$C$3:$C$3". Det första $C$3 är det första radindexet för "Kvartal" och det andra $C$3 är en platsmarkör för sista radindex för "Kvartal" och kommer att ersättas med det riktiga radindexet för tabellens data vid renderingstid. Ställ in kategorin (X) axel etiketter till "=CompanySales!$C$3:$C$3". 

![todo:image_alt_text](working-with-charts_5.png)




1. Klicka på **Lägg till** för att lägga till en annan serie.
   I exemplet har vi lagt till försäljningsserien. 
1. Ställ in värdet på Serie2 (försäljningsserie) till tabellens andra datafält.
   I exemplet är det "CompanySales!$D$3:$D$3". Det första $D$3 är det första radindexet för "Försäljning" och det andra $D$3 är en platsmarkör för sista radindex för "Försäljning" och kommer att ersättas med tabellens data riktiga radindex vid renderingstid. 
1. Klicka på **Nästa** för att fortsätta. 

![todo:image_alt_text](working-with-charts_6.png)




1. I dialogrutan, ställ in diagramtiteln och kategorin (X) axeln.
1. Klicka på **Slutför** för att slutföra arbetet. 

![todo:image_alt_text](working-with-charts_7.png)



Mallen ser ut som nedan. 

![todo:image_alt_text](working-with-charts_8.png)




1. Spara rapporten och publicera den till Rapportservern.
1. Exportera rapporten från Rapportservern.
   Resultatet är som nedan. 

![todo:image_alt_text](working-with-charts_9.png)
