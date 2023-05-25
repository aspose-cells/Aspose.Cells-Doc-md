---
title: Upptäcka tomma arbetsblad
type: docs
weight: 410
url: /sv/net/detecting-empty-worksheets/
description: Den här artikeln visar kod som förklarar hur du upptäcker tomma kalkylblad i Excel-arbetsböcker programmatiskt med C# API med .NET-biblioteket.
keywords: detect empty worksheet c#, find empty excel worksheet c#
---
##  **Kontrollera efter befolkad Cells**

Kalkylblad kan ha en eller flera celler fyllda med värden där ett värde kan vara enkelt (text, numeriskt, datum/tid) eller en formel eller ett formelbaserat värde. I ett sådant fall är det lätt att upptäcka om ett visst kalkylblad är tomt eller inte. Allt vi behöver kontrollera är[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) eller[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)egenskaper. Om de ovan nämnda egenskaperna returnerar noll eller positiva värden betyder det att en eller flera celler har fyllts i, men om någon av dessa egenskaper returnerar -1 som indikerar att ingen av cellerna har fyllts i det givna kalkylbladet.

{{% alert color="primary" %}}

Rad- och kolumnsamlingarna har ett nollbaserat index, därför betyder en cell på rad 0 och kolumn 0 den första cellen i kalkylbladet, som är A1.

{{% /alert %}}

##  **Kontrollera om det är tomt initierat Cells**

 Alla celler som har värden initieras automatiskt, men det finns en möjlighet att ett kalkylblad har celler med endast formatering tillämpad. I ett sådant scenario är[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)eller[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)egenskaper returnerar -1 vilket indikerar frånvaron av några ifyllda värden men initierade celler på grund av cellformateringen kan inte upptäckas med detta tillvägagångssätt. För att kontrollera om ett kalkylblad har tomma initierade celler, rekommenderas det att använda metoden IEnumerator.MoveNext på enumeratorn som hämtas från[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling. Om metoden IEnumerator.MoveNext returnerar**Sann** det betyder att det finns en eller flera initierade celler i det givna kalkylbladet.

##  **Kolla efter former**

 Det är möjligt att ett visst kalkylblad inte har några fyllda celler, men det kan innehålla former och objekt som kontroller, diagram, bilder och så vidare. Om vi behöver kontrollera om ett kalkylblad innehåller någon form kan vi göra det genom att inspektera[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)fast egendom. Alla positiva värden indikerar förekomsten av form(er) i kalkylbladet.

##  **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
