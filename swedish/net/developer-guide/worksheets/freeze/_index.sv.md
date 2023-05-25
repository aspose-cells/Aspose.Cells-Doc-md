---
title: Frys rutor i Excel-kalkylblad
linktitle: Frys rutor
type: docs
weight: 190
url: /sv/net/how-to-freeze-panes-of-excel-worksheet
description: den här artikeln kommer du att lära dig hur du fryser rutor i Excel-kalkylblad programmatiskt med C# Library med .NET API.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

I den här artikeln kommer vi att lära oss hur man fryser rutor.
När du har en enorm mängd data under en gemensam rubrik kan du inte se rubriken när du rullar ner i kalkylbladet. Och varje post innehåller många data. Du kan frysa rutor så att du kan se den frysta delen även när resten av data rullas. Du kan enkelt se rubriker i de översta raderna eller första kolumnerna. Frysning och avfrysning av rutor ändrar bara datavyn utan att själva data ändras.

{{% /alert %}}

##  **I Excel**

**![frysa rutor i Excel](Freeze-panes.png)**


1. Om du vill frysa rutor för att frysa rader och kolumner, välj först en cell (som B2)
2. Klicka på Visa > Frys fönster.
3. Klicka på Frys rutor i rullgardinsmenyn.
4. Om du bläddrar nedåt eller höger, fryses den första raden och kolumnen.

**![Fonzen panges](Frozen-Panes.png)**

Som du kan se är första raden och kolumn A frysta, den andra raden som visas är 32 och den andra synliga kolumnen är D.

Frys rutor låter dig se dina stora data utan att behöva hålla reda på rad- eller kolumnetikett.




##  **Frys rutor med Aspose.Cells för .Net**
 Det är enkelt att frysa rutor med Aspose.Cells för .Net. Vänligen använd[**Arbetsblad.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)metod för att skjuta upp rutor vid den valda Cell.
1. Konstruera arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys rutor med metoden Worksheet.FreezePanes().
3. Spara filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Bifogad[exempel på Excel-källfil](Freeze.xlsx).
