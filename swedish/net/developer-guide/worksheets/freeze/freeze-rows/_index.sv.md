---
title: Frys översta rad(er) i Excel-kalkylblad
linktitle: Frys rader
type: docs
weight: 190
url: /sv/net/how-to-freeze-rows-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur du fryser översta raderna av Excel-kalkylblad programmatiskt med C# Library med .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

I den här artikeln kommer vi att lära oss hur man fryser översta rad(er).
När du har en enorm mängd data under en gemensam rubrik kan du inte se rubriken när du rullar ner i kalkylbladet. Du kan frysa översta rad(er) så att du kan se den frysta delen även när resten av data rullas. Du kan enkelt se rubriker i de översta raderna.

{{% /alert %}}

##  **Frys rader i Excel**

**![Frys översta rad(er) i Excel](Freeze-Rows.png)**


1. Om du vill frysa översta rad(er), välj först raden under raden som ska frysas
2. Klicka på Visa > Frys fönster.
3. Klicka på Frys översta raden i rullgardinsmenyn.
4. Om du bläddrar nedåt är den första raden alltid i toppvyn.

**![Fonzen row](Frozen-Row.png)**

Som du kan se är 1:a raden frusen, den första raden stannar alltid högst upp i vyn när du scrollar ner.

Frys rader låter dig se dina stora data utan att behöva hålla reda på radetiketten.




##  **Frys rader med Aspose.Cells för .Net**
 Det är enkelt att frysa rad(er) med Aspose.Cells för .Net.
 Vänligen använd[**Arbetsblad.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)metod för att feeze rad(er) vid den valda raden.
1. Konstruera arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första raden med metoden Worksheet.FreezePanes().
3. Spara filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

 Bifogad[exempel på Excel-källfil](../Freeze.xlsx).
