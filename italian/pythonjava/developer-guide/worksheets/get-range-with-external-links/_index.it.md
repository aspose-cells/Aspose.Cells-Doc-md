---
title: Ottieni intervallo con collegamenti esterni
type: docs
weight: 60
url: /it/python-java/get-range-with-external-links/
---
## **Ottieni intervallo con collegamenti esterni**
Esistono molti casi in cui i file Excel accedono ai dati da altri file Excel mediante l'uso di collegamenti esterni. Aspose.Cells for Python via Java offre la possibilità di recuperare questi collegamenti esterni utilizzando il[Nome.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) metodo. Il[Nome.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) restituisce un array di tipo[Area di riferimento](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). Il[Area di riferimento](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)la classe fornisce un[NomeFile Esterno](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)proprietà che restituisce il nome del file esterno.

Il seguente frammento di codice mostra come ottenere collegamenti esterni.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
