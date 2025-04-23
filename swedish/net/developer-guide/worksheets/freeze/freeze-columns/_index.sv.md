---
title: Frysa första kolumn(er) i Excel ark
linktitle: Frys kolumner
type: docs
weight: 190
url: /sv/net/how-to-freeze-columns-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur man fryser vänstra kolumner i Excel ark programmatiskt med C# Library och .NET API.
keywords: Frys vänstra kolumner, Frys första kolumner, Lås kolumn(er)
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man fryser vänsterkolumn(er). När du har en stor mängd data i en rad så kan du inte se de vänstra kolumnerna när du horisontellt skrollar i arket. Du kan frysa och låsa den första kolumnen så att du kan se den frysta delen även när resten av datan skrollas. Du kan enkelt se rubriker i de vänstra kolumnerna.


## **Frys kolumner i Excel**

**![Frys vänster kolumn(er) i Excel](freeze-columns.png)**


1. Om du vill frysa vänster kolumn(er), välj först kolumnen under kolumnen som ska frysas
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa första kolumn.
4. Om du skrollar ner är den första kolumnen alltid i vänster vy.

**![Fonzen kolumn](frozen-columns.png)**

Som du kan se är den första kolumnen frusen, den första kolumnen är alltid låst högst upp i vyn när du skrollar horisontellt.

Frys kolumner låter dig visa dina långa data utan att behöva hålla reda på den första kolumnen.




## **Frys kolumner med Aspose.Cells för .Net**
Det är enkelt att frysa första kolumn(er) med Aspose.Cells för .Net. 
Använd [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)-metoden för att frysa kolumn(er) vid den valda kolumnen.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första kolumnen med Worksheet.FreezePanes()-metoden.
3. Spara filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

Bifogad [provkälla Excel-fil](Frys.xlsx).
{{< app/cells/assistant language="csharp" >}}
