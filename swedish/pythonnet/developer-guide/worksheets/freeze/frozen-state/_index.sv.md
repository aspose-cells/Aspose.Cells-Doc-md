---
title: Hur man kontrollerar frysstatus utan Excel
linktitle: Fruset tillstånd
type: docs
weight: 190
url: /sv/python-net/how-to-check-frozen-state-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur man kontrollerar frysstatus för Excel ark programmatiskt med Aspose.Cells för Python via .NET API er.
keywords: Python Excel bibliotek, Python Så här kontrollerar du frysstatus utan Excel, Kontrollera frysstatus utan Excel i Python.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man kontrollerar frysstatus för Excel-ark programmatiskt. Vi kan enkelt hitta om arbetsbladet är nedfryst eller delat i MS Excel. Men finns det ett sätt att ta reda på om det är frys eller delat med CSharp. Vi kan enkelt göra det med Aspose.Cells för Python via .NET.

## **Hur man kontrollerar frysstatus**
Med Aspose.Cells för Python via .NET kan vi kontrollera om fönstret är fryst och hur många rader och kolumner som är låsta.

Använd [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) egenskapen för att kontrollera tillståndet för fönsterfönster 
och få låsta rader och kolumner med [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any) metoden.
1. Konstruera Arbetsbok för att öppna filen.
2. Kontrollera om arbetsbladet är fruset.
3. Få de låsta rad och kolumnerna

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
