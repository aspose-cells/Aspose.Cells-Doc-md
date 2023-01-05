---
title: Ottieni intervallo con collegamenti esterni
type: docs
weight: 140
url: /it/java/get-range-with-external-links/
---
## **Ottieni intervallo con collegamenti esterni**

Molte volte i file Excel accedono ai dati da altri file Excel utilizzando collegamenti esterni. Aspose.Cells offre la possibilità di recuperare questi collegamenti esterni utilizzando il[**Nome.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) metodo. Il[**Nome.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) restituisce un array di tipo[**Area di riferimento**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). Il[**Area di riferimento**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)la classe fornisce un[**NomeFile Esterno**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)proprietà che restituisce il nome del file esterno. Il[**Area di riferimento**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)class espone i seguenti membri.

- [**Fine colonna**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): la colonna finale dell'area
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): La riga finale dell'area
- [**NomeFile Esterno**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): ottiene il nome del file esterno se si tratta di un riferimento esterno
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Indica se si tratta di un'area
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Indica se si tratta di un collegamento esterno
- [**FoglioNome**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Indica in quale foglio si trova questo riferimento
- [**Inizio colonna**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): la colonna iniziale dell'area
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): La riga iniziale dell'area

Il codice di esempio fornito di seguito dimostra l'uso di[**Nome.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) per ottenere intervalli con collegamenti esterni.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
