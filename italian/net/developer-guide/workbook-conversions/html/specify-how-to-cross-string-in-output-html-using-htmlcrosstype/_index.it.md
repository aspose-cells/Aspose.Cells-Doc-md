---
title: Specificare come attraversare la stringa nell output HTML usando HtmlCrossType
type: docs
weight: 140
url: /it/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Possibili Scenari di Utilizzo**

Quando la cella contiene testo o una stringa ma è più grande della larghezza della cella, quindi la stringa va oltre se la prossima cella nella colonna successiva è vuota o null. Quando si salva il file di Excel in HTML, è possibile controllare questo overflow specificando il tipo di attraversamento utilizzando l'enumerazione [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Ha i seguenti valori

- **HtmlCrossType.Default**: Visualizza come MS Excel, dipende dalla prossima cella. Se la prossima cella è nulla, la stringa verrà attraversata o verrà troncata.

- **HtmlCrossType.MSExport**: Visualizza la stringa come esportazione HTML di MS Excel.

- **HtmlCrossType.Cross**: Visualizza una stringa attraversata HTML, le prestazioni per la creazione di file HTML di grandi dimensioni saranno più di dieci volte più veloci rispetto all'impostazione del valore su Default o FitToCell.

- **HtmlCrossType.FitToCell**: Visualizza solo la stringa all'interno della larghezza della cella.

## **Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType**

Il codice di esempio seguente carica il [file di Excel di esempio](51740732.xlsx) e lo salva nel formato HTML specificando diversi [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Si prega di scaricare gli [HTML di output](51740734.zip) generati con questo codice. Il file di Excel di esempio contiene l'immagine bordata con il colore rosso come mostrato in questa schermata che mostra l'effetto dei valori di [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) sull'HTML di output.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
