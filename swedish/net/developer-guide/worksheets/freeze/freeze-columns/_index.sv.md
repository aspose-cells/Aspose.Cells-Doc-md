---
title: Frys första kolumn(erna) i Excel-kalkylblad
linktitle: Frys kolumner
type: docs
weight: 190
url: /sv/net/how-to-freeze-columns-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur du fryser vänstra kolumner i Excel-kalkylblad programmatiskt med C# Library med .NET API.
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

I den här artikeln kommer vi att lära oss hur man fryser vänster kolumn(er).
När du har en enorm mängd data i rad, så att du inte kan se de vänstra kolumnerna när du rullar horisontellt ner i kalkylbladet. Du kan frysa och låsa första kolumn(erna) så att du kan se den frysta delen även när resten av data rullas. Du kan enkelt se rubriker i de vänstra kolumnerna.

{{% /alert %}}

##  **Frys kolumner i Excel**

**![Frys vänster kolumn(er) i Excel](freeze-columns.png)**


1. Om du vill frysa vänster kolumn(er), välj först kolumnen under kolumnen som ska frysas
2. Klicka på Visa > Frys fönster.
3. Klicka på Frys första kolumnen i rullgardinsmenyn.
4. Om du bläddrar nedåt är den första kolumnen alltid i vyn till vänster.

**![Fonzen kolumn](frozen-columns.png)**

Som du kan se är den första kolumnen frusen, den första kolumnen är alltid låst högst upp i vyn när du rullar horisontellt.

Frys kolumner låter dig se dina långa data utan att behöva hålla reda på den första kolumnen.




##  **Frys kolumner med Aspose.Cells för .Net**
Det är enkelt att frysa första kolumn(erna) med Aspose.Cells för .Net.
 Vänligen använd[**Arbetsblad.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)metod för att feeze kolumn(er) vid den valda kolumnen.
1. Konstruera arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första kolumnen med metoden Worksheet.FreezePanes().
3. Spara filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

 Bifogad[exempel på Excel-källfil](Freeze.xlsx).
