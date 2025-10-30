---
title: Skapa arbetsbok och kalkylbladspecifika namngivna intervall med Golang via C++
linktitle: Namngivet intervall
type: docs
weight: 40
url: /sv/go-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Lär dig att skapa arbetsboks och kalkylbladspecifika namngivna intervall med Golang via C++ med Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att definiera namngivna områden med två olika omfång: arbetsbok (också känt som globalt omfång) och arbetsblad.

- Namngivna områden med ett arbetsboksomfång kan kommas åt från vilket arbetsblad som helst inom den arbetsboken genom att helt enkelt använda dess namn.
- Arbetsbladscoped namngivna områden kommas åt med referensen till det specifika arbetsbladet där det skapades.

Aspose.Cells tillhandahåller samma funktionalitet som Microsoft Excel för att lägga till arbetsbok och arbetsbladscoped namngivna områden. Vid skapande av ett arbetsbladscoped namngivet område bör arbetsbladsreferensen användas i det namngivna området för att specificera det som ett arbetsbladscoped namngivet område.

{{% /alert %}} 

## **Lägga till ett namngivet intervall med arbetsboksuppsikt**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges.go" >}}
## **Lägg till ett namngivet område med arbetsbladomfång**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges-1.go" >}}
## **Fortsatta ämnen**
- [Skapa åtkomst och kopiera namngivna områden](/cells/sv/cpp/create-access-and-copy-named-ranges/)
- [Formatera och modifiera namngivna områden](/cells/sv/cpp/format-and-modify-named-ranges/)
- [Hämta intervall med externa länkar](/cells/sv/cpp/get-range-with-external-links/)
- [Implementera icke-sekventiella områden](/cells/sv/cpp/implementing-non-sequential-ranges/)

