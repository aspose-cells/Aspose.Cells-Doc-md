---
title: Skapa arbetsbok och arbetsbladsspecifika namngivna intervall
linktitle: Namngivet intervall
type: docs
weight: 40
url: /sv/python-net/create-workbook-and-worksheet-scoped-named-ranges/
description: Den här artikeln visar hur du skapar arbetsbok och arbetsbladsspecifika namngivna intervall med Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python Skapa arbetsbok och arbetsbladsspecifika namngivna intervall, Python Lägg till ett namngivet intervall med arbetsboksscope, Python Lägg till ett namngivet intervall med arbetsbladsscope.
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att definiera namngivna områden med två olika omfång: arbetsbok (också känt som globalt omfång) och arbetsblad.

- Namngivna områden med ett arbetsboksomfång kan kommas åt från vilket arbetsblad som helst inom den arbetsboken genom att helt enkelt använda dess namn.
- Arbetsbladscoped namngivna områden kommas åt med referensen till det specifika arbetsbladet där det skapades.

Aspose.Cells for Python via .NET erbjuder samma funktionalitet som Microsoft Excel för att lägga till arbetsbok- och arbetsbladsspecifika namngivna intervall. Vid skapande av ett arbetsbladsspecifikt namngivet intervall ska arbetsbladsreferensen användas i det namngivna intervallet för att ange det som ett arbetsbladsspecifikt namngivet intervall.


{{% /alert %}} 
## **Hur man lägger till ett namngivet intervall med arbetsboksscope**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.py" >}}
## **Hur man lägger till ett namngivet intervall med arbetsbladsscope**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-WorksheetNamedRange-1.py" >}}

## **Fortsatta ämnen**
- [Skapa åtkomst och kopiera namngivna områden](/cells/sv/python-net/create-access-and-copy-named-ranges/)
- [Formatera och modifiera namngivna områden](/cells/sv/python-net/format-and-modify-named-ranges/)
- [Hämta intervall med externa länkar](/cells/sv/python-net/get-range-with-external-links/)
- [Implementera icke-sekventiella områden](/cells/sv/python-net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="python-net" >}}
