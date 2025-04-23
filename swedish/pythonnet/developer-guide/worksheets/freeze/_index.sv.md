---
title: Frysa rader i Excel ark
linktitle: Frysa rader
type: docs
weight: 190
url: /sv/python-net/how-to-freeze-panes-of-excel-worksheet
description: I denna artikel lär du dig hur man fäster rutor i Excel ark programmatiskt med Aspose.Cells för Python via .NET API er.
keywords: Python Excel bibliotek, Python frysa rutor, frysa fönster i Python.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man fryser rutor. När du har en enorm mängd data under en gemensam rubrik kan du inte se rubriken när du scrollar ner i kalkylarket. Och varje post innehåller många data. Du kan frysa rutor så att du kan se den frysta delen även när resten av datorna rullas. Du kan enkelt se rubriker i de översta raderna eller första kolumnerna. Att frysa och avfrysa rutor ändrar endast visningen av datan utan att ändra datan själv.

## ***Hur man fryser rutor i Excel**

**![Frys rader i Excel](Frys-panor.png)**


1. Om du vill frysa rader, frysa rader och kolumner, välj först en cell (t.ex. B2)
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn klickar du på Frysa rader.
4. Om du rullar ned eller till höger är den första raden och kolumnen frysta.

**![Frysta rader](Frysta-rutor.png)**

Som du kan se är 1: a raden och kolumn A frysta, den andra raden är 32 och den andra synliga kolumnen är D. 

Frysa rader låter dig visa din stora data utan att behöva hålla reda på rad- eller kolumnetikett.




## **Hur man fryser rutor med Aspose.Cells för Python Excel-bibliotek**
Det är enkelt att frysa rutor med Aspose.Cells för Python via .NET. Använd [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)-metoden för att frysa rutor vid den valda cellen.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frysta rader med Worksheet.FreezePanes() metod.
3. Spara filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

Bifogad [provkälla Excel-fil](Frys.xlsx).
