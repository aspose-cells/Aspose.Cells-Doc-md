---
title: Döljning av visning av nollvärden i kalkylarket
type: docs
weight: 50
url: /sv/net/hiding-the-display-of-zero-values-in-the-worksheet/
description: Den här artikeln visar dig exempelkod som förklarar hur man programmässigt döljer nollvärden i ett Excel kalkylblad med hjälp av C# biblioteket eller .NET API.
keywords: dölj nollvärden av excel kalkylblad i C#
---

{{% alert color="primary" %}} 

Ibland måste du dölja nollvärden i ett kalkylblad. Det kan vara en personlig preferens eller en formateringsstandard.

{{% /alert %}} 

För att dölja nollvärden i ett arbetsblad i Microsoft Excel (till exempel Microsoft Excel 2003):

1. Från menyn ** Verktyg ** väljer du ** Alternativ ** och väljer sedan fliken ** Visa **.
1. Avmarkera alternativet ** Nollvärden **.
1. Klicka på **OK**.

Se följande exempelkod som visar hur man döljer nollor med Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HidingDisplayOfZeroValues-1.cs" >}}
