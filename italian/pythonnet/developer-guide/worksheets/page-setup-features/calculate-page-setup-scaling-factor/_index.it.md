---
title: Calcola il fattore di scala della pagina di impostazione
type: docs
weight: 300
url: /it/python-net/calculate-page-setup-scaling-factor/
description: Questo articolo fornisce un codice di esempio che spiega come utilizzare le API di Aspose.Cells per Python via .NET per calcolare il fattore di ridimensionamento dell impostazione di pagina utilizzando l opzione Regola in larghezza a n pagine per altezza m del foglio di calcolo in modo programmato.
keywords: Libreria Excel di Python, Larghezza della pagina di adattamento a n pagine in alto per m pagine in larghezza di Excel, calcola il fattore di ridimensionamento dell impostazione di pagina in Python.
---

{{% alert color="primary" %}}

Quando si imposta il fattore di scala dell'impostazione della pagina utilizzando l'opzione **Fit to n page(s) wide by m tall**, Microsoft Excel calcola il Fattore di scala dell'impostazione della pagina. È possibile calcolare la stessa cosa utilizzando la proprietà [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale). Questa proprietà restituisce un valore double che può essere convertito in valore percentuale. Ad esempio, se restituisce 0.5 significa che il fattore di scala è del 50%.

{{% /alert %}}

Il seguente codice di esempio illustra come calcolare il fattore di scala dell'impostazione della pagina utilizzando la proprietà [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
