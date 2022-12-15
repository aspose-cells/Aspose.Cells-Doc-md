---
title: Applicare l'ombreggiatura a righe e colonne alternative con la formattazione condizionale
type: docs
weight: 30
url: /it/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells Le API forniscono i mezzi per aggiungere e manipolare le regole di formattazione condizionale per il file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)oggetto. Queste regole possono essere adattate in diversi modi per ottenere la formattazione desiderata in base a condizioni o regole. Questo articolo dimostrerà l'uso delle API Aspose.Cells for .NET per applicare l'ombreggiatura a righe e colonne alternate con l'aiuto delle regole di formattazione condizionale e delle funzioni integrate di Excel.

{{% /alert %}}

Questo articolo utilizza le funzioni integrate di Excel come RIGA, COLONNA e MOD. Ecco alcuni dettagli di queste funzioni per una migliore comprensione del frammento di codice fornito in precedenza.

- **RIGA()** La funzione restituisce il numero di riga di un riferimento di cella. Se il parametro di riferimento viene omesso, si presuppone che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione RIGA.
- **COLONNA()** La funzione restituisce il numero di colonna di un riferimento di cella. Se il parametro di riferimento viene omesso, si presuppone che il riferimento sia l'indirizzo della cella in cui è stata inserita la funzione COLONNA.
- **MOD()** La funzione restituisce il resto dopo che un numero è stato diviso per un divisore, dove il primo parametro della funzione è il valore numerico di cui si desidera trovare il resto e il secondo parametro è il numero utilizzato per dividere nel parametro numero. Se il divisore è 0, restituirà #DIV/0! errore.

Iniziamo a scrivere del codice per raggiungere questo obiettivo con l'aiuto dell'API Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

L'istantanea seguente mostra il foglio di calcolo risultante caricato nell'applicazione Excel.

|![cose da fare:immagine_alt_testo](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
|:- |

 Per applicare l'ombreggiatura a colonne alternative, tutto ciò che devi fare è cambiare la formula**=MOD(RIGA(),2)=0** come**=MOD(COLONNA(),2)=0** , questo è; invece di ottenere l'indice di riga, modificare la formula per recuperare l'indice di colonna.
Il foglio di calcolo risultante, in questo caso, avrà il seguente aspetto.

|![cose da fare:immagine_alt_testo](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
|:- |
