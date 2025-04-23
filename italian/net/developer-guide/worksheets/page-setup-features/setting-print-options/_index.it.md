---
title: Impostazione delle opzioni di stampa
type: docs
weight: 40
url: /it/net/setting-print-options/
description: Questo articolo dimostra come impostare programmaticamente le Opzioni di Stampa della funzionalità di Impostazioni Pagina del Foglio di Calcolo di Excel utilizzando l API C# e la Libreria .NET. È possibile impostare l Area di Stampa, i Titoli di Stampa e l Ordine delle Pagine.
keywords: impostare area di stampa excel c#, impostare titoli di stampa excel c#, impostare ordine pagine excel c#
---

{{% alert color="primary" %}}

Le impostazioni di pagina di Microsoft Excel forniscono diverse opzioni di stampa (anche chiamate opzioni di foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro.

{{% /alert %}}

## **Opzioni di stampa**

Queste opzioni di stampa consentono agli utenti di:

- Selezionare un'area di stampa specifica su un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare gli intitoli di riga/colonna.
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

Aspose.Cells supporta tutte le opzioni di stampa offerte da Microsoft Excel e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro utilizzando le proprietà offerte dalla classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Come vengono utilizzate queste proprietà è discusso più dettagliatamente di seguito.

### **Impostare l'area di stampa**

Per impostazione predefinita, l'area di stampa incorpora tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

Per selezionare un'area di stampa specifica, utilizzare la proprietà [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) della classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Assegnare un intervallo di celle che definisce l'area di stampa a questa proprietà.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Impostare i titoli di stampa**

Aspose.Cells consente di designare intitoli di riga e colonna da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, utilizzare le proprietà [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) e [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) della classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup).

Le righe o le colonne che verranno ripetute sono definite passando il loro numero di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Impostare altre opzioni di stampa**

La classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) fornisce anche diverse altre proprietà per impostare opzioni di stampa generali come segue:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): una proprietà booleana che definisce se stampare o meno le griglie.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): una proprietà booleana che definisce se stampare o meno gli intitoli di riga e colonna.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): una proprietà booleana che definisce se stampare o meno il foglio di lavoro in modalità bianco e nero.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): una proprietà booleana che definisce se stampare il foglio senza grafica.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): definisce se stampare gli errori delle celle come visualizzati, vuoto, trattino o N/D.

Per impostare le proprietà [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) e [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors), Aspose.Cells fornisce anche due enumerazioni, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) e [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) che contengono valori predefiniti da assegnare rispettivamente alle proprietà [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) e [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors).

I valori predefiniti nell'enumerazione [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) sono elencati di seguito con le loro descrizioni.

|**Tipi di Commenti di Stampa**|**Descrizione**|
| :- | :- |
|PrintInPlace|Specifica di stampare i commenti come visualizzati sul foglio di lavoro.|
|PrintNoComments|Specifica di non stampare i commenti.|
|PrintSheetEnd| Specifica di stampare i commenti alla fine del foglio di lavoro.

I valori predefiniti dell'enumerazione [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) sono elencati di seguito con le loro descrizioni.



|**Tipi di Errori di Stampa**|**Descrizione**|
| :- | :- |
|PrintErrorsBlank| Specifica di non stampare gli errori.
|PrintErrorsDash| Specifica di stampare gli errori come "--".
|PrintErrorsDisplayed| Specifica di stampare gli errori come visualizzato.
|PrintErrorsNA| Specifica di stampare gli errori come "#N/A".

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Imposta l'Ordine delle Pagine**

La classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) fornisce la proprietà [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) che viene utilizzata per ordinare la stampa di più pagine del foglio di lavoro. Ci sono due possibilità per ordinare le pagine come segue.

- **In basso poi a destra:** stampa tutte le pagine in basso prima di stampare eventuali pagine a destra.
- **A destra poi in basso:** stampa le pagine da sinistra a destra prima di stampare le pagine sottostanti.

Aspose.Cells fornisce un'enumerazione, [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype), che contiene tutti i tipi di ordinamento predefiniti.

I valori predefiniti dell'enumerazione [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) sono elencati di seguito.

|**Tipi di Ordine di Stampa**|**Descrizione**|
| :- | :- |
|DownThenOver|Rappresenta l'ordine di stampa come in basso e poi sopra.|
|OverThenDown|Rappresenta l'ordine di stampa come sopra e poi in basso.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
