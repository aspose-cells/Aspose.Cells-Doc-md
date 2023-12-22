---
title: Hur man kontrollerar Frozen State utan Excel.
linktitle: Fryst tillstånd
type: docs
weight: 190
url: /sv/net/how-to-check-frozen-state-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur du kontrollerar det frusna tillståndet för Excel-kalkylbladet programmatiskt med C# Library med .NET API.
---
{{% alert color="primary" %}}

den här artikeln kommer vi att lära oss hur du kontrollerar det frusna tillståndet för Excel-kalkylbladet programmatiskt.
Vi kan helt enkelt ta reda på om kalkylbladet är fruset eller delat i MS Excel. Men finns det något sätt att ta reda på om den är fryst eller delad med CSharp.
Vi kan helt enkelt göra det med Aspose.Cells för .Net.
{{% /alert %}}

##  **Är fönsterrutorna frusna**
Med Aspose.Cells för .Net kan vi kontrollera om fönstret är fruset och hur många rader och kolumner som är låsta.

 Vänligen använd[**Arbetsblad.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) egenskap för att kontrollera tillståndet för fönsterrutor
 och får låsta rader och kolumner med[**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)metod.
1. Konstruera arbetsbok för att öppna filen.
2. Kontrollera om arbetsbladet är fruset.
3. Hämtar den låsta raden och kolumnerna

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}