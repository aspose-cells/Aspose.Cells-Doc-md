---
title: Impostazioni di riempimento
type: docs
weight: 50
url: /it/net/cells-fill-settings/
---
## **Colori e motivi di sfondo**

Microsoft Excel può impostare i colori di primo piano (contorno) e di sfondo (riempimento) delle celle e dei motivi di sfondo.

Aspose.Cells supporta anche queste funzionalità in modo flessibile. In questo argomento, impariamo a utilizzare queste funzionalità utilizzando Aspose.Cells.

### **Impostazione di colori e motivi di sfondo**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Ogni elemento del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione rappresenta un oggetto della[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) ha il[**Ottieni stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) e[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) metodi utilizzati per ottenere e impostare la formattazione di una cella. Il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)class fornisce le proprietà per impostare i colori di primo piano e di sfondo delle celle. Aspose.Cells fornisce a[**Tipo di sfondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumerazione che contiene una serie di tipi predefiniti di motivi di sfondo che sono riportati di seguito.

|**Modelli di sfondo**|**Descrizione**|
|:- |:- |
|Diagonale Crosshatch|Rappresenta il modello di tratteggio incrociato diagonale|
|Striscia diagonale|Rappresenta il motivo a strisce diagonali|
|Grigio6|Rappresenta il motivo grigio al 6,25%.|
|Grigio12|Rappresenta il motivo grigio al 12,5%.|
|Grigio25|Rappresenta il motivo grigio al 25%.|
|Grigio50|Rappresenta il motivo grigio al 50%.|
|Grigio75|Rappresenta il motivo grigio al 75%.|
|Striscia orizzontale|Rappresenta il motivo a strisce orizzontali|
|Nessuno|Non rappresenta alcuno sfondo|
|Striscia diagonale inversa|Rappresenta il motivo a strisce diagonali inverse|
|Solido|Rappresenta un modello solido|
|ThickDiagonalCrosshatch|Rappresenta un motivo a tratteggio incrociato diagonale spesso|
|ThinDiagonalCrosshatch|Rappresenta un motivo a tratteggio diagonale sottile|
|ThinDiagonalStripe|Rappresenta il motivo a strisce diagonali sottili|
|ThinHorizontalCrosshatch|Rappresenta un motivo a tratteggio incrociato orizzontale sottile|
|Sottile striscia orizzontale|Rappresenta un motivo a strisce orizzontali sottili|
|Thin ReverseDiagonalStripe|Rappresenta un sottile motivo a strisce diagonali inverse|
|Sottile striscia verticale|Rappresenta un motivo a strisce verticali sottili|
|Striscia verticale|Rappresenta il motivo a strisce verticali|

Nell'esempio seguente, il colore di primo piano della cella A1 è impostato ma A2 è configurato per avere sia i colori di primo piano che di sfondo con un motivo di sfondo a strisce verticali.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Importante da sapere**

{{% alert color="primary" %}}

-  Per impostare il colore di primo piano o di sfondo di una cella, utilizzare il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Colore di primo piano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) o[**Colore di sfondo**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) proprietà. Entrambe le proprietà avranno effetto solo se il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Modello**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)proprietà è configurata.
-  Il[**Colore di primo piano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)La proprietà imposta il colore dell'ombreggiatura della cella.
 Il[**Modello**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)La proprietà specifica il tipo di motivo di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells fornisce un'enumerazione,[**Tipo di sfondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)che contiene una serie di tipi predefiniti di motivi di sfondo.
-  Se selezioni*BackgroundType.None* valore dal[**Tipo di sfondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumerazione, il colore di primo piano non viene applicato.
 Allo stesso modo, il colore di sfondo non viene applicato se si seleziona il file*BackgroundType.None* o*BackgroundType.Solid* i valori.
-  Quando si recupera il colore di ombreggiatura/riempimento della cella, if[**Stile.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) è*BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) tornerà*Colore.Vuoto*.

{{% /alert %}}

### **Applicazione di effetti di riempimento sfumato**

 Per applicare gli effetti di riempimento sfumato desiderati alla cella, utilizzare il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**ImpostaGradienteDueColori**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)metodo di conseguenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Colori e tavolozza**

Una tavolozza è il numero di colori disponibili per l'uso nella creazione di un'immagine. L'uso di una tavolozza standardizzata in una presentazione consente all'utente di creare un aspetto coerente. Ogni file Excel Microsoft (97-2003) ha una tavolozza di 56 colori che possono essere applicati a celle, caratteri, griglie, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile non solo utilizzare i colori esistenti della tavolozza ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla tavolozza.

Questo argomento illustra come aggiungere colori personalizzati alla tavolozza.

### **Aggiunta di colori personalizzati alla tavolozza**

Aspose.Cells supporta la tavolozza dei 56 colori di Microsoft di Excel. Per utilizzare un colore personalizzato non definito nella tavolozza, aggiungi il colore alla tavolozza.

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe fornisce a[**Cambia tavolozza**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) metodo che accetta i seguenti parametri per aggiungere un colore personalizzato per modificare la tavolozza:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella tavolozza che verrà sostituito dal colore personalizzato. Dovrebbe essere compreso tra 0 e 55.

L'esempio seguente aggiunge un colore personalizzato (Orchidea) alla tavolozza prima di applicarlo a un font.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La tavolozza contiene solo 56 colori. Quando aggiungi un colore personalizzato alla tavolozza, la tavolozza viene modificata e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando cambi la tavolozza, fai molta attenzione. Inoltre, questa è la limitazione solo nel formato di file XLS (Excel 97 - 2003) poiché non esiste tale limitazione per XLSX o altri formati di file MS Excel avanzati (2007/2010 o 2013).

{{% /alert %}}
