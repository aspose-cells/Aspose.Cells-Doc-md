---
title: Calcola il fattore di scala della pagina di impostazione
type: docs
weight: 300
url: /it/python-net/calculate-page-setup-scaling-factor/
description: Questo articolo fornisce un esempio di codice che spiega come utilizzare le API di Aspose.Cells per Python via .NET per calcolare il fattore di scala dell impostazione della pagina utilizzando l opzione adatta perņ in larghezza n pagine per m alte.
keywords: Libreria Excel Python, Python Adatta a n pagine di larghezza per m alte, calcola il fattore di scala delle impostazioni della pagina in Python.
---

{{% alert color="primary" %}}

Quando si imposta il fattore di scala dell'impostazione della pagina utilizzando l'opzione **Fit to n page(s) wide by m tall**, Microsoft Excel calcola il Fattore di scala dell'impostazione della pagina. È possibile calcolare la stessa cosa utilizzando la proprietà [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale). Questa proprietà restituisce un valore double che può essere convertito in valore percentuale. Ad esempio, se restituisce 0.5 significa che il fattore di scala è del 50%.

{{% /alert %}}

Il seguente codice di esempio illustra come calcolare il fattore di scala dell'impostazione della pagina utilizzando la proprietà [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
{{< app/cells/assistant language="python-net" >}}
