---
title: Visa formler istället för värden i ett kalkylblad
type: docs
weight: 20
url: /sv/net/show-formulas-instead-of-values-in-a-worksheet/
description: Den här artikeln innehåller exempelkod för att använda C# API eller .NET Library för att programmatiskt visa formler istället för värden i ett Excel kalkylblad eller kalkylblad.
---

{{% alert color="primary" %}}

Det är möjligt att visa formler istället för beräknade värden i Microsoft Excel med hjälp av alternativet **Visa formler** från **Formler**-fliken. När formler visas visar Microsoft Excel formler i kalkylbladet. Du kan uppnå samma sak med hjälp av Aspose.Cells.

{{% /alert %}}

Aspose.Cells tillhandahåller en [**Worksheet.ShowFormulas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/showformulas)-egenskap. Ange detta till **true** för att ställa in Microsoft Excel att visa formler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ShowFormulasInsteadOfValues-1.cs" >}}
