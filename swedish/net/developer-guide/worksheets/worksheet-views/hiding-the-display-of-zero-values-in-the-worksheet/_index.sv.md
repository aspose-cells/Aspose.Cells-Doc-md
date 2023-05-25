---
title: Döljer visningen av nollvärden i arbetsbladet
type: docs
weight: 50
url: /sv/net/hiding-the-display-of-zero-values-in-the-worksheet/
description: Den här artikeln visar exempelkod som förklarar hur du programmässigt döljer nollvärdena i ett Excel-kalkylblad med hjälp av C#-biblioteket eller .NET API.
keywords: hide zero values of excel worksheet in c#
---
{{% alert color="primary" %}} 

Ibland måste du dölja nollvärden i ett kalkylblad. Det kan vara en personlig preferens eller en formateringsstandard.

{{% /alert %}} 

Så här döljer du nollvärden i ett kalkylblad i Microsoft Excel (till exempel Microsoft Excel 2003):

1.  Från**Verktyg** menyn, välj**Alternativ** och välj sedan **Visa** flik.
1.  Avmarkera**Noll värden** alternativ.
1. Klicka på *OK**.

Se följande exempelkod som visar att gömmer nollor med Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HidingDisplayOfZeroValues-1.cs" >}}
