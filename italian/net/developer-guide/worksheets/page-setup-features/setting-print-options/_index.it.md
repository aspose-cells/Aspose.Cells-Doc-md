---
title: Impostazione delle opzioni di stampa
type: docs
weight: 40
url: /it/net/setting-print-options/
---
{{% alert color="primary" %}}

Microsoft Le impostazioni di impostazione della pagina di Excel forniscono diverse opzioni di stampa (dette anche opzioni del foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro.

{{% /alert %}}

## **Impostazione delle opzioni di stampa**

Queste opzioni di stampa consentono agli utenti di:

- Selezionare un'area di stampa specifica su un foglio di lavoro.
- Stampa titoli.
- Stampa griglia.
- Stampa le intestazioni di riga/colonna.
- Ottieni una bozza di qualità.
- Stampa commenti.
- Stampa gli errori della cella.
- Definire l'ordine delle pagine.

 Aspose.Cells supporta tutte le opzioni di stampa offerte da Microsoft Excel e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro utilizzando le proprietà offerte dal[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)classe. Il modo in cui queste proprietà vengono utilizzate è discusso di seguito in modo più dettagliato.

### **Imposta area di stampa**

Per impostazione predefinita, l'area di stampa incorpora tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

 Per selezionare un'area di stampa specifica, utilizzare il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe'[**Area di stampa**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)proprietà. Assegnare a questa proprietà un'area di celle che definisce l'area di stampa.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Imposta i titoli di stampa**

 Aspose.Cells consente di designare le intestazioni di riga e colonna da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, usa il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe'[**PrintTitleColonne**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) e[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)proprietà.

Le righe o le colonne che verranno ripetute vengono definite passando i loro numeri di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Imposta altre opzioni di stampa**

 Il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class fornisce anche diverse altre proprietà per impostare le opzioni di stampa generali come segue:

- [**StampaLinee griglia**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)una proprietà booleana che definisce se stampare o meno le linee della griglia.
- [**StampaIntestazioni**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): una proprietà booleana che definisce se stampare o meno le intestazioni di righe e colonne.
- [**Bianco e nero**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): una proprietà booleana che definisce se stampare o meno il foglio di lavoro in modalità bianco e nero.
- [**StampaCommenti**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro.
- [**Stampabozza**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): una proprietà booleana che definisce se stampare il foglio senza grafica..
- [**Errori di stampa**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): definisce se stampare gli errori della cella come visualizzato, vuoto, trattino o N/D.

 Per impostare il[**StampaCommenti**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) e[**Errori di stampa**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) properties, Aspose.Cells fornisce anche due enumerazioni,[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , e[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) che contengono valori predefiniti da assegnare al file[**StampaCommenti**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) e[**Errori di stampa**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)proprietà rispettivamente.

 I valori predefiniti in[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)enumerazione sono elencate di seguito con le relative descrizioni.

|**Stampa tipi di commenti**|**Descrizione**|
|:- |:- |
|Stampa sul posto|Specifica di stampare i commenti come visualizzati nel foglio di lavoro.|
|StampaNessun commento|Specifica di non stampare i commenti.|
|StampaFoglioFine|Specifica di stampare i commenti alla fine del foglio di lavoro.|

 I valori predefiniti di[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)enumerazione sono elencate di seguito con le relative descrizioni.



|**Tipi di errori di stampa**|**Descrizione**|
|:- |:- |
|PrintErrorsBlank|Specifica di non stampare gli errori.|
|PrintErrorsDash|Specifica di stampare gli errori come "--".|
|PrintErrorsVisualizzato|Specifica di stampare gli errori come visualizzati.|
|PrintErrorsNA|Specifica di stampare gli errori come "#N/D".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Imposta l'ordine delle pagine**

 Il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)la classe fornisce il[**Ordine**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)proprietà utilizzata per ordinare la stampa di più pagine del foglio di lavoro. Ci sono due possibilità per ordinare le pagine come segue.

- **Giù poi sopra:** stampa tutte le pagine in basso prima di stampare quelle a destra.
- **Sopra e poi giù:** stampa le pagine da sinistra a destra prima di stampare le pagine sottostanti.

 Aspose.Cells fornisce un'enumerazione,[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)che contiene tutti i tipi di ordine predefiniti.

 I valori predefiniti di[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)enumerazione sono elencati di seguito.

|**Tipi di ordini di stampa**|**Descrizione**|
|:- |:- |
|DownThenOver|Rappresenta l'ordine di stampa come down then over.|
|OverThenDown|Rappresenta l'ordine di stampa come over then down.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
