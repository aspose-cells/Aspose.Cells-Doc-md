---
title: Ottieni intervallo con collegamenti esterni con Golang tramite C++
linktitle: Ottieni Range con Collegamenti Esterni
type: docs
weight: 120
url: /it/go-cpp/get-range-with-external-links/
description: Impara come recuperare intervalli con collegamenti esterni nei file di Excel usando Aspose.Cells con Golang tramite C++.
---

## **Ottieni Intervallo con Link Esterni**

Molte volte i file Excel accedono ai dati da altri file Excel utilizzando link esterni. Aspose.Cells offre l'opzione di recuperare questi link esterni utilizzando il metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/). Il metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) restituisce un array di tipo [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). La classe [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) fornisce una proprietà [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) che restituisce il nome del file esterno. La classe [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) espone i seguenti membri.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): La colonna finale dell'area
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): La riga finale dell'area
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): Ottieni il nome del file esterno se questo è un riferimento esterno
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): Indica se questa è un'area
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): Indica se questa è una connessione esterna
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): Indica in quale foglio si trova questo riferimento
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): La colonna di inizio dell'area
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): La riga di inizio dell'area

Il codice di esempio riportato di seguito mostra l'uso del metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) per ottenere intervalli con collegamenti esterni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
