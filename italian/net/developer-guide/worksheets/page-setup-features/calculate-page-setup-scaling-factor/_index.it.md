---
title: Calcola il fattore di scala dell'impostazione della pagina
type: docs
weight: 300
url: /it/net/calculate-page-setup-scaling-factor/
description: In questo articolo viene fornito un codice di esempio che spiega come usare la libreria C# API o .NET per calcolare il fattore di scala Imposta pagina usando l'opzione Adatta a n pagine di larghezza per m di altezza del foglio di lavoro di Excel a livello di codice.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

 Quando si imposta il ridimensionamento dell'impostazione di pagina utilizzando**Adatta a n pagine di larghezza per m di altezza** option, Microsoft Excel calcola il fattore di scala dell'impostazione di pagina. Puoi calcolare la stessa cosa usando[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)proprietà. Questa proprietà restituisce un valore double che può essere convertito in valore percentuale. Ad esempio, se restituisce 0,5, significa che il fattore di scala è del 50%.

{{% /alert %}}

 Il seguente codice di esempio illustra come calcolare il fattore di ridimensionamento dell'impostazione della pagina utilizzando[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
