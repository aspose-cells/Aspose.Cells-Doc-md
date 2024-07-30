---
title: Upptäcka tomma kalkylblad
type: docs
weight: 410
url: /sv/python-net/detecting-empty-worksheets/
description: Den här artikeln visar dig kod som förklarar hur man upptäcker tomma kalkylblad i Excel arbetsböcker programmatoriskt med hjälp av Aspose.Cells för Python via .NET biblioteket.
keywords: Python Excel Library, upptäck tomt arbetsblad med python, hitta tomt excel kalkylblad i python.
---

## **Kontrollera Populerade celler**

Kalkylblad kan ha en eller flera celler som är befolkade med värden där ett värde kan vara enkelt (text, numerisk, datum / tid) eller en formel eller ett formelbaserat värde. I så fall är det lätt att upptäcka om ett visst kalkylblad är tomt eller inte. Flytta Kalkylblad inom Arbetsbok. Allt vi behöver kontrollera är [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) eller [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) egenskap. Om de nämnda egenskaperna returnerar noll eller positiva värden betyder det att en eller flera celler har fyllts i, men om någon av dessa egenskaper returnerar -1 indikerar det att inga av cellerna har fyllts i i det angivna kalkylbladet.

{{% alert color="primary" %}}

 Raderna och kolumnerna har index från noll därför betyder en cell på rad 0 och kolumn 0 den första cellen i kalkylbladet, vilket är A1.

{{% /alert %}}

## **Kontrollera toma initialiserade celler**

Alla celler som har värden initieras automatiskt, men det finns en möjlighet att ett kalkylblad har celler endast med formatering tillämpad. I ett sådant scenario kommer egenskaperna [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) eller [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) att returnera -1 vilket indikerar avsaknaden av några befolkade värden men initierade celler på grund av att cellformatering inte kan detekteras med denna metod. För att kontrollera om ett kalkylblad har tomma initierade celler rekommenderas det att använda IEnumerator.MoveNext-metoden på en Enumerator som förvärvats från [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) -samlingen. Om IEnumerator.MoveNext-metoden returnerar **true** betyder det att det finns en eller flera initierade celler i det angivna kalkylbladet.

## **Kontrollera former**

Det är möjligt att ett visst kalkylblad inte har några befolkade celler, men det kan innehålla former & objekt som kontroller, diagram, bilder och så vidare. Om vi behöver kontrollera om ett kalkylblad innehåller någon form, kan vi göra det genom att inspektera [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) elementen. Ett positivt värde indikerar närvaron av form(er) i kalkylbladet.

## **Programmeringsexempel**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
