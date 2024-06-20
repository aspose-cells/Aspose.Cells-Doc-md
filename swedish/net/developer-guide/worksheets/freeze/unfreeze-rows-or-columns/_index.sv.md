---
title: Avfrys rader eller kolumner
linktitle: Avfrys fönster
type: docs
weight: 190
url: /sv/net/unfreeze-rows-or-columns-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur man avfryser rader, kolumner eller fönster för Excel ark programmatiskt med C# biblioteket med .NET API.
keywords: Avfrys fönster, Avfrys rader, Avfrys kolumner, Avfrys fönster.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man avfryser rader, kolumner och delar. Om kalkylbladen i Excel-filerna är frysta vill vi ibland avfrysa kalkylarket eller justera frysta rader, kolumner eller delar.


## **I Excel**

1. Klicka på fliken Visa > Frys fönster > Avfrys fönster.

**![avfrysta fönster i Excel](Avfrys-Fönster.png)**




## **Avfrys rader, kolumner eller fönster med Aspose.Cells för .Net**
Det är enkelt att avfrysa fönster med Aspose.Cells för .Net. Använd [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)-metoden för att avfrysa fönster.

1. Konstruera arbetsboken för att öppna den frysta filen.
2. Avfrysa fönster med metoden Worksheet.UnFreezePanes().
3. Spara filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

Bifogad [provkälla för Excel-filen](Fryst.xlsx).
