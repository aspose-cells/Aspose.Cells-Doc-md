---
title: Frysa översta rad(er) i Excel ark
linktitle: Frys rader
type: docs
weight: 190
url: /sv/python-net/how-to-freeze-rows-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur man fryser översta rader i Excel ark programmatiskt med Aspose.Cells för Python via .NET API er.
keywords: Python Excel bibliotek, Frysa översta rader i Python, Frysa översta raden i Python.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man fryser topprad(er). När du har en stor mängd data under en gemensam rubrik kan du inte se rubriken när du skrollar nedåt i arket. Du kan frysa topprad(er) så att du kan se den frysta delen även när resten av datan skrollas. Du kan enkelt se rubriker i de övre raderna.

## **Hur man fryser rader i Excel**

**![Frysa översta rad(er) i Excel](Freeze-Rows.png)**


1. Om du vill frysa översta rad(er), välj först raden under den rad som ska frysas
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa översta rad.
4. Om du rullar ner, är den första raden alltid i toppvy.

**![Fronzen row](Frozen-Row.png)**

Som du kan se är 1 raden frusen, den första raden stannar alltid överst i vyn när du bläddrar ner.

Frys rader låter dig se din stora data utan att behöva hålla koll på radmärket.




## **Hur man fryser rader med Aspose.Cells för Python Excel-bibliotek**
Det är enkelt att frysa rad(er) med Aspose.Cells för Python via .NET. Använd metoden [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) för att frysa rad(er) vid den valda raden.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första raden med Worksheet.FreezePanes() -metoden.
3. Spara filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Row.py" >}}

Bifogad [provkäll-Excel-fil](../Freeze.xlsx).
