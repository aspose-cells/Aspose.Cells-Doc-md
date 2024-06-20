---
title: Upptäcka tomma kalkylblad
type: docs
weight: 710
url: /sv/java/detecting-empty-worksheets/
---

## **Kontrollera Populerade celler**
Arbetsbladen kan ha en eller flera celler som är ifyllda med värden, där ett värde kan vara enkelt (text, numeriskt, datum/tid) eller en formel eller ett värdet baserat på en formel. I så fall är det enkelt att upptäcka om ett visst arbetsblad är tomt eller inte. Allt vi behöver kontrollera är [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) eller [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) egenskaperna. Om ovanstående egenskaper returnerar noll eller positiva värden innebär det att en eller flera celler har fyllts i, men om någon av dessa egenskaper returnerar -1 indikerar det att inga av cellerna har fyllts i på det givna arbetsbladet.

{{% alert color="primary" %}} 

Rad- och kolumnsamlingarna har en nollbaserad index, därför innebär en cell på rad 0 & kolumn 0 den första cellen i arbetsbladet, dvs. A1.

{{% /alert %}} 
## **Kontrollera toma initialiserade celler**
Alla celler som har värden initialiseras automatiskt, men det finns en möjlighet att ett arbetsblad har celler med endast formatering applicerad. I sådant scenario kommer [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) eller [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) egenskaperna att returnera -1 vilket indikerar frånvaron av några ifyllda värden men initialiserade celler på grund av att cellformateringen inte kan upptäckas med detta tillvägagångssätt. För att kontrollera om ett arbetsblad har tomma initialiserade celler rekommenderas det att använda metoden *Iterator.hasNext* på iteratorn som hämtats från cellsamlingen. Om metoden *iterator.hasNext* returnerar true innebär det att det finns en eller flera initialiserade celler på det givna arbetsbladet.

{{% alert color="primary" %}} 

Det finns ett antal sätt att erhålla cellräknaren som detaljeras i [Hur & Var man använder Iterators](/cells/sv/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Kontrollera former**
Det är möjligt att ett givet arbetsblad inte har några ifyllda celler, men det kan innehålla former & objekt såsom kontroller, diagram, bilder osv. Om vi behöver kontrollera om ett arbetsblad innehåller någon form, kan vi göra det genom att inspektera egenskapen [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count). Ett positivt värde indikerar närvaron av form(er) på arbetsbladet.
## **Programmeringsexempel**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
