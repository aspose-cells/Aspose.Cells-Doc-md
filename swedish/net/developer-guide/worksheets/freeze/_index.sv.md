---
title: Frysa rader i Excel ark
linktitle: Frysa rader
type: docs
weight: 190
url: /sv/net/how-to-freeze-panes-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur man fryser rader i Excel ark programmatiskt med C# bibliotek med .NET API.
keywords: Frysa rader, frysa fönster.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man fryser rutor. När du har en enorm mängd data under en gemensam rubrik kan du inte se rubriken när du scrollar ner i kalkylarket. Och varje post innehåller många data. Du kan frysa rutor så att du kan se den frysta delen även när resten av datorna rullas. Du kan enkelt se rubriker i de översta raderna eller första kolumnerna. Att frysa och avfrysa rutor ändrar endast visningen av datan utan att ändra datan själv.

## **I Excel**

**![Frys rader i Excel](Frys-panor.png)**


1. Om du vill frysa rader, frysa rader och kolumner, välj först en cell (t.ex. B2)
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn klickar du på Frysa rader.
4. Om du rullar ned eller till höger är den första raden och kolumnen frysta.

**![Frysta rader](Frysta-rutor.png)**

Som du kan se är 1: a raden och kolumn A frysta, den andra raden är 32 och den andra synliga kolumnen är D. 

Frysa rader låter dig visa din stora data utan att behöva hålla reda på rad- eller kolumnetikett.




## **Frysa rader med Aspose.Cells för .Net**
Det är enkelt att frysa rader med Aspose.Cells för .Net. Använd [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)-metoden för att frysa rader vid den valda cellen.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frysta rader med Worksheet.FreezePanes() metod.
3. Spara filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

Bifogad [provkälla Excel-fil](Frys.xlsx).
