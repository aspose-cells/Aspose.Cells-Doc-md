---
title: Ottieni Range con Collegamenti Esterni
type: docs
weight: 120
url: /it/net/get-range-with-external-links/
---

## **Ottieni Intervallo con Link Esterni**

Molte volte i file di Excel accedono ai dati da altri file di Excel utilizzando collegamenti esterni. Aspose.Cells fornisce l'opzione per recuperare questi collegamenti esterni utilizzando il metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas). Il metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) restituisce un array di tipo [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). La classe [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) fornisce una proprietà [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename) che restituisce il nome del file esterno. La classe [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) espone i seguenti membri.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): La colonna finale dell'area
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): La riga finale dell'area
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Ottieni il nome del file esterno se si tratta di un riferimento esterno
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indica se si tratta di un'area
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indica se si tratta di un collegamento esterno
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indica in quale foglio si trova questo riferimento
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): La colonna di inizio dell'area
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): La riga di inizio dell'area

Il codice di esempio riportato di seguito dimostra l'uso del metodo [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) per ottenere intervalli con collegamenti esterni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
