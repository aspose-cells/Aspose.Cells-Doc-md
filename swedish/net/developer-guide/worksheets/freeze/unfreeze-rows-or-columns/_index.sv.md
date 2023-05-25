---
title: Frigör rader eller kolumner
linktitle: Frigör rutor
type: docs
weight: 190
url: /sv/net/unfreeze-rows-or-columns-of-excel-worksheet
description: den här artikeln kommer du att lära dig hur du låser upp rader, kolumner eller rutor i Excel-kalkylblad programmatiskt med hjälp av C# Library med .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

I den här artikeln kommer vi att lära oss hur man låser upp rader, kolumner och rutor.
Om kalkylblad i Excel-filer är frysta vill vi ibland frysa upp dem eller justera frysta rader, kolumner eller rutor.

{{% /alert %}}

##  **I Excel**

1. Klicka på fliken Visa > Frys rutor > Unfreeze Panes.

**![unfreeze rutor i Excel](Unfreeze-Panes.png)**




##  **Avfrysa rader, kolumner eller rutor med Aspose.Cells för .Net**
 Det är enkelt att låsa upp rutor med Aspose.Cells för .Net. Vänligen använd[**Arbetsblad.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)metod för att frigöra rutor.

1. Konstruera arbetsbok för att öppna den frysta filen.
2. Lås upp rutor med metoden Worksheet.UnFreezePanes().
3. Spara filen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Bifogad[exempel på Excel-källfil](Frozen.xlsx).
