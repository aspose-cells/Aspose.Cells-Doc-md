---
title: Frysa första kolumn(er) i Excel ark
linktitle: Frys kolumner
type: docs
weight: 190
url: /sv/python-net/how-to-freeze-columns-of-excel-worksheet
description: I den här artikeln lär du dig hur du låser vänstra kolumner i Excel arbetsblad programmässigt med hjälp av Aspose.Cells för Python via .NET API er.
keywords: Python Excel bibliotek, Python lås vänstra kolumner, Python lås första kolumnen, Python lås kolumner.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man fryser vänsterkolumn(er). När du har en stor mängd data i en rad så kan du inte se de vänstra kolumnerna när du horisontellt skrollar i arket. Du kan frysa och låsa den första kolumnen så att du kan se den frysta delen även när resten av datan skrollas. Du kan enkelt se rubriker i de vänstra kolumnerna.


## **Hur man låser kolumner i Excel**

**![Frys vänster kolumn(er) i Excel](freeze-columns.png)**


1. Om du vill frysa vänster kolumn(er), välj först kolumnen under kolumnen som ska frysas
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa första kolumn.
4. Om du skrollar ner är den första kolumnen alltid i vänster vy.

**![Fonzen kolumn](frozen-columns.png)**

Som du kan se är den första kolumnen frusen, den första kolumnen är alltid låst högst upp i vyn när du skrollar horisontellt.

Frys kolumner låter dig visa dina långa data utan att behöva hålla reda på den första kolumnen.




## **Hur man låser kolumner med Aspose.Cells för Python Excel-bibliotek**
Det är enkelt att låsa första kolumn(er) med Aspose.Cells för Python via .NET. Använd [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int)-metoden för att låsa kolumn(er) vid den valda kolumnen.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första kolumnen med Worksheet.FreezePanes()-metoden.
3. Spara filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

Bifogad [provkälla Excel-fil](Frys.xlsx).
{{< app/cells/assistant language="python-net" >}}
