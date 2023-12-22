---
title: Ottenere intestazioni o piè di pagina
type: docs
weight: 30
url: /it/net/get-headers-or-footers/
description: Questo articolo spiega come ottenere intestazioni e piè di pagina a livello di codice da file Excel o OpenOffice utilizzando la libreria C# API o .NET.
---
{{% alert color="primary" %}}

 Intestazioni e piè di pagina vengono visualizzati solo nella visualizzazione Layout di pagina, Anteprima di stampa e sulle pagine stampate.

 Puoi anche utilizzare la finestra di dialogo Imposta pagina se desideri visualizzare intestazioni o piè di pagina per più fogli di lavoro alla volta.

Per altri tipi di fogli, ad esempio fogli grafici o grafici, è possibile inserire intestazioni e piè di pagina solo utilizzando la finestra di dialogo Imposta pagina.

{{% /alert %}}

##  **Ottenere intestazioni e piè di pagina in MS Excel**
1. Fai clic sul foglio di lavoro in cui desideri visualizzare o modificare intestazioni o piè di pagina.
2. Nella scheda Visualizza, nel gruppo Visualizzazioni cartella di lavoro, fare clic su Layout di pagina.
Excel visualizza il foglio di lavoro nella visualizzazione Layout di pagina.
3. Per visualizzare o modificare un'intestazione o un piè di pagina, fare clic sulla casella di testo dell'intestazione o del piè di pagina sinistra, centrale o destra nella parte superiore o inferiore della pagina del foglio di lavoro (sotto Intestazione o sopra Piè di pagina).


##  **Ottenere intestazioni e piè di pagina utilizzando Aspose.Cells per .Net**
 Con[**Foglio di lavoro.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) E[**Foglio di lavoro.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) metodi, lo sviluppatore .Net può semplicemente ottenere intestazioni o piè di pagina dal file.

1. Costruisci cartella di lavoro per aprire il file.
2. Ottiene il foglio di lavoro in cui desideri inserire intestazioni o piè di pagina.
3. Ottiene l'intestazione o il piè di pagina con l'ID di sezione specifico.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **Analizza intestazioni e piè di pagina nell'elenco dei comandi**
Il testo dell'intestazione o del piè di pagina può contenere comandi speciali, ad esempio un segnaposto per il numero di pagina, la data corrente o gli attributi di formattazione del testo.

I comandi speciali sono rappresentati da una singola lettera preceduta da una e commerciale ("&").

Le stringhe di intestazione e piè di pagina sono costruite utilizzando la grammatica ABNF. Non è facile da capire senza spettatore.

 Aspose.Cells per .Net fornisce[**Foglio di lavoro.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)metodo per analizzare intestazioni e piè di pagina come elenco di comandi.

I seguenti codici su come analizzare l'intestazione o il piè di pagina come elenco di comandi ed elaborare i comandi:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
