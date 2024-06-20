---
title: Calcola il fattore di scala della pagina di impostazione
type: docs
weight: 300
url: /it/net/calculate-page-setup-scaling-factor/
description: Questo articolo fornisce del codice di esempio che spiega come utilizzare l API C# o la libreria .NET per calcolare il fattore di scala dell impostazione della pagina utilizzando l opzione Fit to n page(s) wide by m tall del foglio di calcolo di Excel in modo programmatico.
keywords: Fit to n page wide by m tall excel c#, calcolare fattore di scala dell impostazione della pagina c#
---

{{% alert color="primary" %}}

Quando si imposta il fattore di scala dell'impostazione della pagina utilizzando l'opzione **Fit to n page(s) wide by m tall**, Microsoft Excel calcola il Fattore di scala dell'impostazione della pagina. È possibile calcolare la stessa cosa utilizzando la proprietà [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale). Questa proprietà restituisce un valore double che può essere convertito in valore percentuale. Ad esempio, se restituisce 0.5 significa che il fattore di scala è del 50%.

{{% /alert %}}

Il seguente codice di esempio illustra come calcolare il fattore di scala dell'impostazione della pagina utilizzando la proprietà [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
