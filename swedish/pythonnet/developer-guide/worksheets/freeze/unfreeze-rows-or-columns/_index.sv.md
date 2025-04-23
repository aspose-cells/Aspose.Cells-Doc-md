---
title: Avfrys rader eller kolumner
linktitle: Avfrys fönster
type: docs
weight: 190
url: /sv/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: I denna artikel kommer du att lära dig hur man avfräser rader, kolumner eller fönster i Excel arbetsblad programmässigt med Aspose.Cells för Python via .NET API er.
keywords: Python Excel bibliotek, Python avfrysning av fönster, Python Hur man avfryser rader, Python Hur man avfryser kolumner, Python Hur man avfryser fönster.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man avfryser rader, kolumner och delar. Om kalkylbladen i Excel-filerna är frysta vill vi ibland avfrysa kalkylarket eller justera frysta rader, kolumner eller delar.


## **Hur man avfryser rader eller kolumner i Excel**

1. Klicka på fliken Visa > Frys fönster > Avfrys fönster.

**![avfrysta fönster i Excel](Avfrys-Fönster.png)**




## **Hur man avfryser rader, kolumner eller fönster med Aspose.Cells för Python Excel bibliotek**
Det är enkelt att avfrysa fönster med Aspose.Cells för Python via .NET. Använd [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) metoden för att avfrysa fönster .

1. Konstruera arbetsboken för att öppna den frysta filen.
2. Avfrysa fönster med metoden Worksheet.UnFreezePanes().
3. Spara filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Bifogad [provkälla för Excel-filen](Fryst.xlsx).
