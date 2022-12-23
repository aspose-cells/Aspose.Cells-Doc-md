---
title: Ottieni intervallo con collegamenti esterni
type: docs
weight: 120
url: /it/net/get-range-with-external-links/
---
## **Ottieni intervallo con collegamenti esterni**

Molte volte i file Excel accedono ai dati da altri file Excel utilizzando collegamenti esterni. Aspose.Cells offre la possibilità di recuperare questi collegamenti esterni utilizzando il[**Nome.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)metodo. Il[**Nome.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)Il metodo restituisce un array di tipo[**Area di riferimento**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). Il[**Area di riferimento**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) la classe fornisce un[**NomeFile Esterno**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)proprietà che restituisce il nome del file esterno. Il[**Area di riferimento**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)class espone i seguenti membri.

- [**Fine colonna**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): la colonna finale dell'area
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): La riga finale dell'area
- [**NomeFile Esterno**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): ottiene il nome del file esterno se si tratta di un riferimento esterno
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indica se si tratta di un'area
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indica se si tratta di un collegamento esterno
- [**FoglioNome**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indica in quale foglio si trova questo riferimento
- [**Inizio colonna**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): la colonna iniziale dell'area
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): La riga iniziale dell'area

 Il codice di esempio fornito di seguito dimostra l'uso di[**Nome.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)metodo per ottenere intervalli con collegamenti esterni.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
