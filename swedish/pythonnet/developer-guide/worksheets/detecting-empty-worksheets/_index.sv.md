---
title: Upptäcka tomma kalkylblad
type: docs
weight: 410
url: /sv/python-net/detecting-empty-worksheets/
description: Denna artikel visar kodexempel som förklarar hur man detekterar tomma arbetsblad i Excel arbetsböcker programmatiskt med Aspose.Cells för Python via .NET bibliotek.
keywords: Python Excel bibliotek, detektera tomt arbetsblad med Python, hitta tomt Excel ark i Python.
---

## **Kontrollera Populerade celler**

Kalkylblad kan ha en eller flera celler som är befolkade med värden där ett värde kan vara enkelt (text, numerisk, datum / tid) eller en formel eller ett formelbaserat värde. I så fall är det lätt att upptäcka om ett visst kalkylblad är tomt eller inte. Flytta Kalkylblad inom Arbetsbok. Allt vi behöver kontrollera är [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) eller [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) egenskap. Om de nämnda egenskaperna returnerar noll eller positiva värden betyder det att en eller flera celler har fyllts i, men om någon av dessa egenskaper returnerar -1 indikerar det att inga av cellerna har fyllts i i det angivna kalkylbladet.

{{% alert color="primary" %}}

 Raderna och kolumnerna har index från noll därför betyder en cell på rad 0 och kolumn 0 den första cellen i kalkylbladet, vilket är A1.

{{% /alert %}}

## **Kontrollera toma initialiserade celler**

Alla celler som har värden är automatiskt initialiserade, men det finns en möjlighet att ett arbetsblad har celler endast med formatering. I ett sådant scenario kommer egenskapen [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) eller [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) att returnera -1, vilket indikerar att det inte finns några ifyllda värden, men initialiserade celler kan inte upptäckas med denna metod pga. cellformatet. För att kontrollera om ett arbetsblad har tomma initialiserade celler rekommenderas att använda IEnumerator.MoveNext-metoden på enumeratorn som erhållits från [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) samlingen. Om IEnumerator.MoveNext returnerar **true** betyder det att det finns en eller flera initialiserade celler i det angivna arbetsbladet.

## **Kontrollera former**

Det är möjligt att ett givet arbetsblad inte har några ifyllda celler, men det kan innehålla former och objekt såsom kontroller, diagram, bilder med mera. Om vi behöver kontrollera om ett arbetsblad innehåller några former kan vi göra det genom att inspektera [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) element. Ett positivt värde indikerar att det finns form(er) i arbetsbladet.

## **Programmeringsexempel**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
{{< app/cells/assistant language="python-net" >}}
