---
title: Arbeiten mit Diagrammen
type: docs
weight: 110
url: /de/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

 Aspose.Cells Berichtsvorlage unterstützt Microsoft Excel-Diagramme. Jedes Mal, wenn Sie einen Bericht ausführen, wird das Diagramm mit den neuesten Daten gefüllt.

{{% /alert %}} 

So fügen Sie ein Diagramm zu einer Berichtsvorlage hinzu:

1. Erstellen Sie zunächst das Dataset, das als Datenquelle für das Diagramm dienen soll.
 Unten verwenden wir die AdventureWorks-Beispieldatenbank, die im Lieferumfang von SQL Server Reporting Services 2005 enthalten ist, und erstellen ein Dataset mit dem Namen „Sales“.
 Diese SQL definiert das Dataset:

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



 Bitte beziehen Sie sich auf[Datenquellen und Abfragen](/cells/de/reportingservices/data-sources-and-queries/) um mehr darüber zu erfahren, wie man eine Datenquelle und einen Datensatz in Aspose.Cells.Report.Designer erstellt.

1. Erstellen Sie einen tabellarischen Bericht gemäß den Anweisungen in[Tabellenbericht erstellen](/cells/de/reportingservices/creating-tabular-report/) . Der Bericht, den wir für dieses Beispiel erstellt haben, ist unten. Die Tabelle ist die Datenquelle des Diagramms.

![todo: Bild_alt_Text](working-with-charts_1.png)




1.  Klicken Sie in Microsoft Excel auf die**Einfügung** Menü und auswählen**Diagramm**.
1.  Klicken**Nächste**. 

![todo: Bild_alt_Text](working-with-charts_2.png)




1.  Drücke den**Serie** Tab.

![todo: Bild_alt_Text](working-with-charts_3.png)




1.  Klicken**Addieren**. 

![todo: Bild_alt_Text](working-with-charts_4.png)




1. Legen Sie im Dialogfeld den Wert von Series1 (Quarter Series) auf das erste Datenfeld der Tabelle fest.
 Im Beispiel ist das „CompanySales!$C$3:$C$3“. Das erste $C$3 ist der erste Zeilenindex von „Quarter“ und das zweite $C$3 ist ein Platzhalter für den letzten Zeilenindex von „Quarter“ und wird beim Rendern durch den echten Zeilenindex der Tabellendaten ersetzt. Legen Sie die Achsenbeschriftungen der Kategorie (X) auf „=CompanySales!$C$3:$C$3“ fest.

![todo: Bild_alt_Text](working-with-charts_5.png)




1.  Klicken**Addieren** um eine weitere Serie hinzuzufügen.
 Im Beispiel haben wir die Verkaufsserie hinzugefügt.
1. Setzen Sie den Wert von Series2 (Sales series) auf das zweite Datenfeld der Tabelle.
Im Beispiel ist es „CompanySales!$D$3:$D$3“. Das erste $D$3 ist der erste Zeilenindex von „Sales“ und das zweite $D$3 ist ein Platzhalter für den letzten Zeilenindex von „Sales“ und wird beim Rendern durch den echten Zeilenindex der Tabellendaten ersetzt.
1.  Klicken**Nächste** weitermachen.

![todo: Bild_alt_Text](working-with-charts_6.png)




1. Legen Sie im Dialogfeld den Diagrammtitel und die Kategorieachse (X) fest.
1.  Klicken**Fertig** um die Arbeit abzuschließen.

![todo: Bild_alt_Text](working-with-charts_7.png)



 Die Vorlage sieht wie folgt aus.

![todo: Bild_alt_Text](working-with-charts_8.png)




1. Speichern Sie den Bericht und veröffentlichen Sie ihn auf dem Berichtsserver.
1. Exportieren Sie den Bericht vom Berichtsserver.
 Das Ergebnis ist wie folgt.

![todo: Bild_alt_Text](working-with-charts_9.png)
