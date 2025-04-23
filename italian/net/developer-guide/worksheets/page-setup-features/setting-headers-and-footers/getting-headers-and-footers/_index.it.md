---
title: Ottenere Intestazioni o Piè di Pagina
type: docs
weight: 30
url: /it/net/get-headers-or-footers/
description: Questo articolo spiega come ottenere programmatticamente intestazioni e piè di pagina da file Excel o OpenOffice utilizzando l API C# o la libreria .NET.
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina vengono visualizzati solo nella visualizzazione Layout di pagina, Anteprima di stampa e sulle pagine stampate. 

È inoltre possibile utilizzare la finestra di dialogo Imposta pagina se si desidera visualizzare le intestazioni o i piè di pagina per più di un foglio di lavoro alla volta. 

Per altri tipi di fogli, come fogli grafico o grafici, è possibile inserire solo intestazioni e piè di pagina utilizzando la finestra di dialogo Imposta pagina.

{{% /alert %}}

## **Ottenere Intestazioni e Piè di Pagina in MS Excel**
1. Fare clic sul foglio di lavoro dove si desidera visualizzare o modificare le intestazioni o i piè di pagina.
2. Sulla scheda Vista, nel gruppo Visualizzazione cartelle di lavoro, fare clic su Layout di pagina.
  Excel visualizza il foglio di lavoro in vista Layout di pagina.
3. Per visualizzare o modificare un'intestazione o un piè di pagina, fare clic sulla casella di testo intestazione o piè di pagina a sinistra, al centro o a destra nella parte superiore o inferiore della pagina del foglio di lavoro (sotto Intestazione o sopra Piè di pagina).


## **Ottenere Intestazioni e Piè di Pagina usando Aspose.Cells per .Net**
Con i metodi [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getheader/) e [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getfooter/), lo sviluppatore .Net può semplicemente ottenere intestazioni o piè di pagina dal file.

1. Costruire il Workbook per aprire il file.
2. Ottiene il foglio di lavoro in cui si desidera ottenere l'intestazione o il piè di pagina.
3. Ottiene l'intestazione o il piè di pagina con un ID di sezione specifico.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

## **Analizza Intestazioni e Piè di Pagina in elenco di comandi**
Il testo dell'intestazione o del piè di pagina può contenere comandi speciali, ad esempio un segnaposto per il numero di pagina, la data corrente o attributi di formattazione del testo.

I comandi speciali sono rappresentati da una singola lettera con un e commerciale iniziale ("&").

Le stringhe di intestazione e piè di pagina sono costruite utilizzando la grammatica ABNF. Non è facile da capire senza visualizzatore .

Aspose.Cells per .Net fornisce il metodo [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getcommands/) per analizzare intestazioni e piè di pagina come elenco di comandi.

I seguenti codici mostrano come analizzare l'intestazione o il piè di pagina come elenco di comandi e processarli:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
