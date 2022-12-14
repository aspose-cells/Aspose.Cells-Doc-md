---
title: Arbeta med diagram
type: docs
weight: 110
url: /sv/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

 Aspose.Cells Rapportmall stöder Microsoft Excel-diagram. Varje gång du kör en rapport fylls diagrammet i med de senaste uppgifterna.

{{% /alert %}} 

Så här lägger du till ett diagram i rapportmallen:

1. Skapa först datamängden som kommer att vara datakällan för diagrammet.
 Nedan använder vi exempeldatabasen AdventureWorks som levereras med SQL Server Reporting Services 2005 och skapar en datauppsättning som heter Sales.
 Denna SQL definierar datasetet:

**SQL**

{{< highlight "csharp" >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



 Vänligen hänvisa till[Datakällor och frågor](/cells/sv/reportingservices/data-sources-and-queries/) för att lära dig mer om hur du skapar en datakälla och datauppsättning i Aspose.Cells.Report.Designer.

1. Skapa en tabellrapport enligt instruktionerna i[Skapa tabellrapport](/cells/sv/reportingservices/creating-tabular-report/) . Rapporten vi har skapat för det här exemplet finns nedan. Tabellen är diagrammets datakälla.

![todo:image_alt_text](working-with-charts_1.png)




1.  I Microsoft Excel klickar du på**Föra in** menyn och välj**Diagram**.
1.  Klick**Nästa**. 

![todo:image_alt_text](working-with-charts_2.png)




1.  Klicka på**Serier** flik.

![todo:image_alt_text](working-with-charts_3.png)




1.  Klick**Lägg till**. 

![todo:image_alt_text](working-with-charts_4.png)




1. I dialogrutan ställer du in värdet för Series1 (Kvartalsserie) till tabellens första datafält.
 I exemplet är det "CompanySales!$C$3:$C$3". Den första $C$3 är den första radens index för "Quarter" och den andra $C$3 är en platshållare för sista radens index för "Quarter" och kommer att ersättas med tabelldatas verkliga radindex vid renderingstidpunkten. Ställ in kategori(X)-axeletiketterna till "=Företagsförsäljning!$C$3:$C$3".

![todo:image_alt_text](working-with-charts_5.png)




1.  Klick**Lägg till** för att lägga till ytterligare en serie.
 I provet har vi lagt till försäljningsserien.
1. Ställ in värdet för Series2 (Sales series) till tabellens andra datafält.
 exemplet är det "CompanySales!$D$3:$D$3". Den första $D$3 är den första radens index för "Försäljning" och den andra $D$3 är en platshållare för sista radens index för "Försäljning" och kommer att ersättas med tabelldatas verkliga radindex vid renderingstidpunkten.
1.  Klick**Nästa** att fortsätta.

![todo:image_alt_text](working-with-charts_6.png)




1. Ställ in diagramtiteln och kategori(X)-axeln i dialogrutan.
1.  Klick**Avsluta** för att slutföra arbetet.

![todo:image_alt_text](working-with-charts_7.png)



 Mallen ser ut som nedan.

![todo:image_alt_text](working-with-charts_8.png)




1. Spara rapporten och publicera den på rapportservern.
1. Exportera rapporten från rapportservern.
 Resultatet är som nedan.

![todo:image_alt_text](working-with-charts_9.png)
