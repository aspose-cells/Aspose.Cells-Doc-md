---
title: Impostazioni di riempimento
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Supporta l'impostazione delle impostazioni di riempimento delle celle, consentendo agli utenti di personalizzare lo sfondo e lo stile delle celle. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per configurare le impostazioni di riempimento delle celle.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /it/net/cells-fill-settings/
---
##  **Colori e motivi di sfondo**

Microsoft Excel può impostare i colori di primo piano (contorno) e di sfondo (riempimento) delle celle e dei motivi di sfondo.

Aspose.Cells supporta anche queste funzionalità in modo flessibile. In questo argomento impariamo a utilizzare queste funzionalità utilizzando Aspose.Cells.

###  **Impostazione dei colori e dei motivi di sfondo**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 IL[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) ha il[**Ottieni Stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) E[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) metodi utilizzati per ottenere e impostare la formattazione di una cella. IL[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fornisce proprietà per impostare i colori di primo piano e di sfondo delle celle. Aspose.Cells fornisce a[**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumerazione che contiene una serie di tipi predefiniti di pattern di sfondo forniti di seguito.

|**Modelli di sfondo**|**Descrizione**|
| :- | :- |
|Tratteggio incrociato diagonale|Rappresenta il modello di tratteggio incrociato diagonale|
|Striscia diagonale|Rappresenta il motivo a strisce diagonali|
|Grigio6|Rappresenta il 6,25% di motivo grigio|
|Grigio12|Rappresenta il 12,5% di motivo grigio|
|Grigio25|Rappresenta il 25% di motivo grigio|
|Grigio50|Rappresenta il 50% di motivo grigio|
|Grigio75|Rappresenta il 75% di motivo grigio|
|Striscia orizzontale|Rappresenta il motivo a strisce orizzontali|
|Nessuno|Non rappresenta lo sfondo|
|Striscia diagonale inversa|Rappresenta il motivo a strisce diagonali inverse|
|Solido|Rappresenta un modello solido|
|Tratteggio incrociato diagonale spesso|Rappresenta un motivo a tratteggio incrociato diagonale spesso|
|Tratteggio incrociato diagonale sottile|Rappresenta un motivo a tratteggio incrociato diagonale sottile|
|Striscia diagonale sottile|Rappresenta un motivo a strisce diagonali sottili|
|Tratteggio incrociato orizzontale sottile|Rappresenta un modello di tratteggio incrociato orizzontale sottile|
|Striscia orizzontale sottile|Rappresenta un motivo a strisce orizzontali sottili|
|Striscia diagonale inversa sottile|Rappresenta un sottile motivo a strisce diagonali inverse|
|Striscia verticale sottile|Rappresenta un motivo a strisce verticali sottili|
|Striscia verticale|Rappresenta il motivo a strisce verticali|

Nell'esempio seguente, il colore di primo piano della cella A1 è impostato ma A2 è configurata per avere sia i colori di primo piano che quelli di sfondo con un motivo di sfondo a strisce verticali.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **Importante da sapere**

{{% alert color="primary" %}}

-  Per impostare il colore di primo piano o di sfondo di una cella, utilizzare il comando[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Colore di primo piano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) O[**Colore di sfondo**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) proprietà. Entrambe le proprietà avranno effetto solo se il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Modello**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)la proprietà è configurata.
-  IL[**Colore di primo piano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)La proprietà imposta il colore dell'ombreggiatura della cella.
 IL[**Modello**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)La proprietà specifica il tipo di motivo di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells fornisce un'enumerazione,[**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). che contiene una serie di tipi predefiniti di motivi di sfondo.
-  Se selezioni*BackgroundType.None* valore da[**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumerazione, il colore di primo piano non viene applicato.
 Allo stesso modo, il colore di sfondo non viene applicato se si seleziona*BackgroundType.None* O*BackgroundType.Solid* valori.
-  Quando si recupera il colore di ombreggiatura/riempimento della cella, if[**Stile.Modello**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) è *BackgroundType.None*,[**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) restituirà *Color.Empty*.

{{% /alert %}}

###  **Applicazione degli effetti di riempimento sfumato**

 Per applicare gli effetti di riempimento sfumato desiderati alla cella, utilizzare il comando[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Imposta due gradienti di colore**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)metodo di conseguenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **Colori e tavolozza**

Una tavolozza è il numero di colori disponibili da utilizzare nella creazione di un'immagine. L'utilizzo di una tavolozza standardizzata in una presentazione consente all'utente di creare un aspetto coerente. Ogni file Excel (97-2003) Microsoft dispone di una tavolozza di 56 colori che possono essere applicati a celle, caratteri, linee della griglia, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile non solo utilizzare i colori già esistenti nella tavolozza ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla tavolozza.

In questo argomento viene illustrato come aggiungere colori personalizzati alla tavolozza.

###  **Aggiunta di colori personalizzati alla tavolozza**

Aspose.Cells supporta la tavolozza di 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella tavolozza, aggiungere il colore alla tavolozza.

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe fornisce a[**Cambia tavolozza**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) metodo che accetta i seguenti parametri per aggiungere un colore personalizzato per modificare la tavolozza:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella tavolozza che verrà sostituito dal colore personalizzato. Dovrebbe essere compreso tra 0 e 55.

L'esempio seguente aggiunge un colore personalizzato (Orchidea) alla tavolozza prima di applicarlo a un carattere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La tavolozza contiene solo 56 colori. Quando aggiungi un colore personalizzato alla tavolozza, la tavolozza viene modificata e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando cambi la tavolozza, fai molta attenzione. Inoltre, questa è la limitazione solo nel formato di file XLS (Excel 97 - 2003) poiché non esiste tale limitazione per XLSX o altri formati di file avanzati MS Excel (2007/2010 o 2013).

{{% /alert %}}
