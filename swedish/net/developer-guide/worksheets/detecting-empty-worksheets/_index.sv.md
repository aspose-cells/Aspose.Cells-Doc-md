---
title: Upptäcka tomma kalkylblad
type: docs
weight: 410
url: /sv/net/detecting-empty-worksheets/
description: Denna artikel visar dig kod som förklarar hur man programmatiskt upptäcker tomma kalkylblad i Excel arbetsböcker med C# API med .NET bibliotek.
keywords: upptäcka tom kalkylblad c#, hitta tom excel kalkylblad c#
---

## **Kontrollera Populerade celler**

Kalkylblad kan ha en eller flera celler som är befolkade med värden där ett värde kan vara enkelt (text, numerisk, datum / tid) eller en formel eller ett formelbaserat värde. I så fall är det lätt att upptäcka om ett visst kalkylblad är tomt eller inte. Flytta Kalkylblad inom Arbetsbok. Allt vi behöver kontrollera är [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) eller [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) egenskap. Om de nämnda egenskaperna returnerar noll eller positiva värden betyder det att en eller flera celler har fyllts i, men om någon av dessa egenskaper returnerar -1 indikerar det att inga av cellerna har fyllts i i det angivna kalkylbladet.

{{% alert color="primary" %}}

 Raderna och kolumnerna har index från noll därför betyder en cell på rad 0 och kolumn 0 den första cellen i kalkylbladet, vilket är A1.

{{% /alert %}}

## **Kontrollera toma initialiserade celler**

Alla celler som har värden initialiseras automatiskt, det finns dock en möjlighet att ett kalkylblad har celler med endast formatering som tillämpas. I en sådan scen kan [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) eller [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) egenskaperna returnera -1 som indikerar frånvaron av några befolkade värden men initialiserade celler på grund av cellformatering som inte kan upptäckas med detta tillvägagångssätt. För att kontrollera om ett kalkylblad innehåller tomma initialiserade celler rekommenderas att använda IEnumerator.MoveNext-metoden på uppräknaren som förvärvats från [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-kollektionen. Om IEnumerator.MoveNext-metoden returnerar ** true ** betyder det att det finns en eller flera initialiserade celler i det angivna kalkylbladet.

## **Kontrollera former**

Det är möjligt att ett visst kalkylblad inte har några befolkade celler, men det kan innehålla former och objekt som styr element, diagram, bilder och så vidare. Om vi ​​behöver kontrollera om ett kalkylblad innehåller någon form kan vi göra det genom att inspektera [**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) egenskapen. Alla positiva värden indikerar närvaron av form(er) i kalkylbladet.

## **Programmeringsexempel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
