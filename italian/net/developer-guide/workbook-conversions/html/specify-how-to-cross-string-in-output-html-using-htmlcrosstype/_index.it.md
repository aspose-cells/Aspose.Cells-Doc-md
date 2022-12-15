---
title: Specificare come incrociare la stringa nell'HTML di output utilizzando HtmlCrossType
type: docs
weight: 140
url: /it/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Possibili scenari di utilizzo**

Quando la cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa va in overflow se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in HTML, puoi controllare questo overflow specificando il tipo incrociato usando il[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) enumerazione. Ha i seguenti valori

- **HtmlCrossType.Default**: Visualizza come MS Excel, dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocia o viene troncata.

- **HtmlCrossType.MSExport**: Visualizza la stringa come MS Excel che esporta HTML.

- **HtmlCrossType.Cross**: Visualizza HTML cross string, le prestazioni per la creazione di file HTML di grandi dimensioni saranno più di dieci volte più veloci rispetto all'impostazione del valore su Default o FitToCell.

- **HtmlCrossType.FitToCell**: Visualizza solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nell'HTML di output utilizzando HtmlCrossType**

 Il codice di esempio seguente carica il file[esempio di file Excel](51740732.xlsx) e lo salva in formato HTML specificando diverso[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) Si prega di scaricare il[HTML di output](51740734.zip) generato con questo codice. Il file Excel di esempio contiene l'immagine bordata di colore rosso come mostrato in questo screenshot che mostra l'effetto del[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) valori sull'output HTML.

![cose da fare:immagine_alt_testo](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
