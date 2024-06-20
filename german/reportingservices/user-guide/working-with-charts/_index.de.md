---
title: Arbeiten mit Diagrammen
type: docs
weight: 110
url: /de/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells Report-Vorlage unterstützt Microsoft Excel-Diagramme. Jedes Mal, wenn ein Bericht ausgeführt wird, wird das Diagramm mit den aktuellsten Daten befüllt. 

{{% /alert %}} 

Um einem Berichtsvorlagen ein Diagramm hinzuzufügen:

1. Erstellen Sie zuerst das Dataset, das die Datenquelle für das Diagramm sein wird.
   Nachfolgend verwenden wir die AdventureWorks-Beispieldatenbank, die mit SQL Server Reporting Services 2005 ausgeliefert wird, und erstellen ein Dataset namens Sales.
   Dieses SQL definiert das Dataset: 

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



Bitte beachten Sie [Datenquellen und Abfragen](/cells/de/reportingservices/data-sources-and-queries/), um mehr darüber zu erfahren, wie Sie eine Datenquelle und ein Dataset in Aspose.Cells.Report.Designer erstellen können.

1. Erstellen Sie einen tabellarischen Bericht gemäß den Anweisungen in [Tabellarischen Bericht erstellen](/cells/de/reportingservices/creating-tabular-report/). Der Bericht, den wir für dieses Beispiel erstellt haben, ist unten. Die Tabelle ist die Datenquelle für das Diagramm. 

![todo:image_alt_text](working-with-charts_1.png)




1. Klicken Sie in Microsoft Excel auf das **Einfügen**-Menü und wählen Sie **Diagramm** aus.
1. Klicken Sie auf **Weiter**. 

![todo:image_alt_text](working-with-charts_2.png)




1. Klicken Sie auf die Registerkarte **Reihen**. 

![todo:image_alt_text](working-with-charts_3.png)




1. Klicken Sie auf **Hinzufügen**. 

![todo:image_alt_text](working-with-charts_4.png)




1. Setzen Sie in dem Dialogfeld den Wert von Serie1 (Quartalsserie) auf das erste Datenfeld der Tabelle.
   In dem Beispiel lautet dies “CompanySales!$C$3:$C$3”. Das erste $C$3 ist der erste Zeilenindex des “Quartal” und das zweite $C$3 ist ein Platzhalter für den letzten Zeilenindex des “Quartals” und wird zur Laufzeit durch den realen Zeilenindex der Tabellendaten ersetzt. Setzen Sie die Kategorie(X)-Achsenbeschriftungen auf “=CompanySales!$C$3:$C$3”. 

![todo:image_alt_text](working-with-charts_5.png)




1. Klicken Sie auf **Hinzufügen**, um eine weitere Serie hinzuzufügen.
   Im Beispiel haben wir die Verkaufsserie hinzugefügt. 
1. Setzen Sie den Wert von Serie2 (Verkaufsserie) auf das zweite Datenfeld der Tabelle.
   Im Beispiel heißt es “CompanySales!$D$3:$D$3”. Das erste $D$3 ist der erste Zeilenindex des “Umsatzes” und das zweite $D$3 ist ein Platzhalter für den letzten Zeilenindex des “Umsatzes” und wird zur Laufzeit durch den realen Zeilenindex der Tabellendaten ersetzt. 
1. Klicken Sie auf **Weiter**, um fortzufahren. 

![todo:image_alt_text](working-with-charts_6.png)




1. Setzen Sie im Dialogfeld den Diagrammtitel und die Kategorie(X)-Achse.
1. Klicken Sie auf **Fertigstellen**, um die Arbeit abzuschließen. 

![todo:image_alt_text](working-with-charts_7.png)



Die Vorlage sieht wie folgt aus: 

![todo:image_alt_text](working-with-charts_8.png)




1. Speichern Sie den Bericht und veröffentlichen Sie ihn auf dem Report Server.
1. Exportieren Sie den Bericht vom Report Server.
   Das Ergebnis sieht wie folgt aus. 

![todo:image_alt_text](working-with-charts_9.png)
