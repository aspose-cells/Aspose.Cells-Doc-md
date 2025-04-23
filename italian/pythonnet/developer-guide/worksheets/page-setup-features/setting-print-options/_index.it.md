---
title: Impostazione delle opzioni di stampa
type: docs
weight: 40
url: /it/python-net/setting-print-options/
description: Questo articolo mostra come impostare programmaticamente le Opzioni di stampa della funzionalità di configurazione della pagina di Excel utilizzando l API Aspose.Cells per Python via .NET. Puoi impostare l Area di stampa, i Titoli di stampa e l Ordine della pagina.
keywords: Libreria Python per Excel, imposta area di stampa Excel in Python, imposta titoli di stampa Excel in Python, come impostare l ordine della pagina in Excel con Python, impostare le Opzioni di stampa in Python, impostare l Area di stampa in Python, impostare i Titoli di stampa in Python. 
---

{{% alert color="primary" %}}

Le impostazioni di pagina di Microsoft Excel forniscono diverse opzioni di stampa (anche chiamate opzioni di foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro.

{{% /alert %}}

## **Come impostare le Opzioni di stampa**

Queste opzioni di stampa consentono agli utenti di:

- Selezionare un'area di stampa specifica su un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare gli intitoli di riga/colonna.
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

Aspose.Cells per Python via .NET supporta tutte le opzioni di stampa offerte da Microsoft Excel e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro utilizzando le proprietà offerte dalla classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Come vengono usate queste proprietà è descritto più dettagliatamente di seguito.

## **Come impostare l'Area di stampa**

Per impostazione predefinita, l'area di stampa incorpora tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

Per selezionare un'area di stampa specifica, utilizzare la proprietà [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) della classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Assegnare un intervallo di celle che definisce l'area di stampa a questa proprietà.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Come impostare i Titoli di stampa**

Aspose.Cells per Python via .NET ti permette di designare le intestazioni di riga e colonna per ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, usa le proprietà [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) e [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) della classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup).

Le righe o le colonne che verranno ripetute sono definite passando il loro numero di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Come impostare altre opzioni di stampa**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fornisce anche diverse altre proprietà per impostare opzioni di stampa generali come segue:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): una proprietà booleana che definisce se stampare o meno le griglie.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): una proprietà booleana che definisce se stampare o meno gli intitoli di riga e colonna.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): una proprietà booleana che definisce se stampare o meno il foglio di lavoro in modalità bianco e nero.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): una proprietà booleana che definisce se stampare il foglio senza grafica.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): definisce se stampare gli errori delle celle come visualizzati, vuoto, trattino o N/D.

Per impostare le proprietà [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) e [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors), Aspose.Cells fornisce anche due enumerazioni, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) e [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) che contengono valori predefiniti da assegnare rispettivamente alle proprietà [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) e [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors).

I valori predefiniti nell'enumerazione [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) sono elencati di seguito con le loro descrizioni.

|**Tipi di Commenti di Stampa**|**Descrizione**|
| :- | :- |
|PRINT_IN_PLACE| Specifica la stampa dei commenti come visualizzati sul foglio di lavoro.|
|PRINT_NO_COMMENTS| Specifica di non stampare commenti.|
|PRINT_SHEET_END| Specifica di stampare i commenti alla fine del foglio di lavoro.|

I valori predefiniti dell'enumerazione [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) sono elencati di seguito con le loro descrizioni.



|**Tipi di Errori di Stampa**|**Descrizione**|
| :- | :- |
|PRINT_ERRORS_BLANK| Specifica di non stampare errori.|
|PRINT_ERRORS_DASH| Specifica di stampare errori come "--".|
|PRINT_ERRORS_DISPLAYED| Specifica di stampare gli errori come visualizzati.|
|PRINT_ERRORS_NA| Specifica di stampare gli errori come "#N/A".|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Come impostare l'ordine di stampa**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fornisce la proprietà [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) che viene utilizzata per ordinare la stampa di più pagine del foglio di lavoro. Ci sono due possibilità per ordinare le pagine come segue.

- **In basso poi a destra:** stampa tutte le pagine in basso prima di stampare eventuali pagine a destra.
- **A destra poi in basso:** stampa le pagine da sinistra a destra prima di stampare le pagine sottostanti.

Aspose.Cells fornisce un'enumerazione, [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype), che contiene tutti i tipi di ordinamento predefiniti.

I valori predefiniti dell'enumerazione [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) sono elencati di seguito.

|**Tipi di Ordine di Stampa**|**Descrizione**|
| :- | :- |
|DOWN_THEN_OVER| Rappresenta l'ordine di stampa come giù poi a destra.|
|OVER_THEN_DOWN| Rappresenta l'ordine di stampa come a destra poi giù.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
