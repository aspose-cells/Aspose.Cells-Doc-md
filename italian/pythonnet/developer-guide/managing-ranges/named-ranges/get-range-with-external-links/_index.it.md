---
title: Ottieni Range con Collegamenti Esterni
type: docs
weight: 120
url: /it/python-net/get-range-with-external-links/
description: Questo articolo mostra come ottenere un intervallo con link esterni tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Ottenere Intervallo con Link Esterni in Python.
---

## **Ottieni Intervallo con Link Esterni**

Molte volte i file Excel accedono ai dati da altri file Excel tramite link esterni. Aspose.Cells for Python via .NET fornisce l'opzione per recuperare questi link esterni utilizzando il metodo [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool). Il metodo [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) restituisce un array di tipo [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea). La classe [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) fornisce una proprietà [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/) che restituisce il nome del file esterno. La classe [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) espone i seguenti membri.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): La colonna finale dell'area
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): La riga finale dell'area
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Ottieni il nome del file esterno se si tratta di un riferimento esterno
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Indica se si tratta di un'area
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Indica se si tratta di un collegamento esterno
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Indica in quale foglio si trova questo riferimento
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): La colonna di inizio dell'area
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): La riga di inizio dell'area

Il codice di esempio riportato di seguito dimostra l'uso del metodo [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) per ottenere intervalli con collegamenti esterni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
