---
title: Avfrys rader eller kolumner
linktitle: Avfrys fönster
type: docs
weight: 190
url: /sv/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur man låser upp rader, kolumner eller rutor i Excels kalkylblad programmatiskt med hjälp av Aspose.Cells för Python via .NET APIer.
keywords: Python Excel bibliotek, Python Lås upp rutor, Python Hur man låser upp rader, Python hur man låser upp kolumner, Python hur man lossar fönster.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man avfryser rader, kolumner och delar. Om kalkylbladen i Excel-filerna är frysta vill vi ibland avfrysa kalkylarket eller justera frysta rader, kolumner eller delar.


## **Hur man låser upp rader eller kolumner i Excel**

1. Klicka på fliken Visa > Frys fönster > Avfrys fönster.

**![avfrysta fönster i Excel](Avfrys-Fönster.png)**




## **Hur man låser upp rader, kolumner eller rutor med Aspose.Cells för Python Excel bibliotek**
Det är enkelt att låsa upp rutor med Aspose.Cells för Python via .NET. Använd gärna [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) metoden för att låsa upp rutor.

1. Konstruera arbetsboken för att öppna den frysta filen.
2. Avfrysa fönster med metoden Worksheet.UnFreezePanes().
3. Spara filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Bifogad [provkälla för Excel-filen](Fryst.xlsx).
