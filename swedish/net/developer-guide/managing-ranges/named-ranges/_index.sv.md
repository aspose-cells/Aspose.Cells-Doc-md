---
title: Skapa arbetsbok och arbetsbladsspecifika namngivna intervall
linktitle: Namngivet intervall
type: docs
weight: 40
url: /sv/net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att definiera namngivna områden med två olika omfång: arbetsbok (också känt som globalt omfång) och arbetsblad.

- Namngivna områden med ett arbetsboksomfång kan kommas åt från vilket arbetsblad som helst inom den arbetsboken genom att helt enkelt använda dess namn.
- Arbetsbladscoped namngivna områden kommas åt med referensen till det specifika arbetsbladet där det skapades.

Aspose.Cells tillhandahåller samma funktionalitet som Microsoft Excel för att lägga till arbetsbok och arbetsbladscoped namngivna områden. Vid skapande av ett arbetsbladscoped namngivet område bör arbetsbladsreferensen användas i det namngivna området för att specificera det som ett arbetsbladscoped namngivet område.

{{% /alert %}} 
## **Lägga till ett namngivet intervall med arbetsboksuppsikt**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **Lägg till ett namngivet område med arbetsbladomfång**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **Fortsatta ämnen**
- [Skapa åtkomst och kopiera namngivna områden](/cells/sv/net/create-access-and-copy-named-ranges/)
- [Formatera och modifiera namngivna områden](/cells/sv/net/format-and-modify-named-ranges/)
- [Hämta intervall med externa länkar](/cells/sv/net/get-range-with-external-links/)
- [Implementera icke-sekventiella områden](/cells/sv/net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="csharp" >}}
