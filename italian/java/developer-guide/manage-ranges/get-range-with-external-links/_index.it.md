---
title: Ottieni Range con Collegamenti Esterni
type: docs
weight: 140
url: /it/java/get-range-with-external-links/
---

## **Ottieni Intervallo con Link Esterni**

Molte volte, i file di Excel accedono ai dati da altri file di Excel utilizzando collegamenti esterni. Aspose.Cells fornisce l'opzione per recuperare questi collegamenti esterni utilizzando il metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)). Il metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) restituisce un array di tipo [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). La classe [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) fornisce una proprietà [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName) che restituisce il nome del file esterno. La classe [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) espone i seguenti membri.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): La colonna finale dell'area
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): La riga finale dell'area
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Ottieni il nome del file esterno se si tratta di un riferimento esterno
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Indica se si tratta di un'area
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Indica se si tratta di un collegamento esterno
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Indica in quale foglio si trova questo riferimento
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): La colonna di inizio dell'area
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): La riga di inizio dell'area

Il codice di esempio fornito di seguito dimostra l'uso del metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) per ottenere Range con collegamenti esterni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
