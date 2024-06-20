---
title: Hur man kontrollerar fruset tillstånd utan Excel.
linktitle: Fruset tillstånd
type: docs
weight: 190
url: /sv/net/how-to-check-frozen-state-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur du kontrollerar det frusna tillståndet i Excel ark programmatiskt med C# bibliotek med .NET API.

---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man kontrollerar det frysta tillståndet för Excel-arket programmatiskt. Vi kan enkelt avgöra om arket är fruset eller delat i MS Excel. Men finns det ett sätt att ta reda på om det är fryst eller delat med CSharp. Vi kan enkelt göra det med Aspose.Cells for .Net.

## **Är fönsterfönster frysta**
Med Aspose.Cells for .Net kan vi kontrollera om fönstret är fruset och hur många rader och kolumner som är låsta.

Använd [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) egenskapen för att kontrollera tillståndet för fönsterfönster 
och få låsta rader och kolumner med [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/) metoden.
1. Konstruera Arbetsbok för att öppna filen.
2. Kontrollera om arbetsbladet är fruset.
3. Få de låsta rad och kolumnerna

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
