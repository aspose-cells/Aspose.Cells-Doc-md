---
title: Ottieni Range con Collegamenti Esterni
type: docs
weight: 60
url: /it/python-java/get-range-with-external-links/
---

## **Ottieni Intervallo con Link Esterni**
Ci sono molte istanze in cui i file di Excel accedono ai dati da altri file di Excel tramite l'uso di collegamenti esterni. Aspose.Cells for Python via Java offre l'opzione di recuperare questi collegamenti esterni utilizzando il metodo [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)). Il metodo [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) restituisce un array di tipo [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). La classe [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) fornisce una proprietà [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) che restituisce il nome del file esterno.

Il seguente frammento di codice mostra come ottenere i collegamenti esterni.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
