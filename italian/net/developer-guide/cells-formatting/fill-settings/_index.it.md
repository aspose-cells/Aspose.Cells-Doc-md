---
title: Impostazioni di riempimento
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Supporta l impostazione delle impostazioni di riempimento delle celle, consentendo agli utenti di personalizzare lo sfondo e lo stile delle celle. Questo articolo presenterà come utilizzare la libreria Aspose.Cells per impostare le impostazioni di riempimento delle celle.
keywords: Aspose.Cells, Celle, Impostazioni di riempimento, Sfondo, Stile
type: docs
weight: 50
url: /it/net/cells-fill-settings/
---

## **Colori e motivi di sfondo**

Microsoft Excel può impostare i colori del primo piano (contorno) e lo sfondo (riempimento) delle celle e i motivi di sfondo.

Aspose.Cells supporta anche queste funzionalità in modo flessibile. In questo argomento, impariamo ad utilizzare queste funzionalità utilizzando Aspose.Cells.

### **Impostazione di colori e motivi di sfondo**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Ciascun elemento della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Il [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) ha i metodi [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) e [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) che vengono utilizzati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fornisce proprietà per impostare i colori del primo piano e dello sfondo delle celle. Aspose.Cells fornisce un'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) che contiene un insieme di tipi predefiniti di motivi di sfondo che sono di seguito elencati.

|**Motivi di sfondo**|**Descrizione**|
| :- | :- |
|DiagonalCrosshatch|Rappresenta un motivo a croce diagonale|
|DiagonalStripe|Rappresenta un motivo a strisce diagonali|
|Gray6|Rappresenta un motivo grigio al 6.25%|
|Gray12|Rappresenta un motivo grigio al 12.5%|
|Gray25|Rappresenta un motivo grigio al 25%|
|Gray50|Rappresenta 50% modello grigio|
|Gray75|Rappresenta 75% modello grigio|
|HorizontalStripe|Rappresenta modello a strisce orizzontali|
|None|Rappresenta nessuno sfondo|
|ReverseDiagonalStripe|Rappresenta modello a strisce diagonali invertite|
|Solid|Rappresenta modello solido|
|ThickDiagonalCrosshatch|Rappresenta modello spesso di incroci diagonali|
|ThinDiagonalCrosshatch|Rappresenta modello sottile di incroci diagonali|
|ThinDiagonalStripe|Rappresenta modello sottile a strisce diagonali|
|ThinHorizontalCrosshatch|Rappresenta modello sottile di incroci orizzontali|
|ThinHorizontalStripe|Rappresenta modello sottile a strisce orizzontali|
|ThinReverseDiagonalStripe|Rappresenta modello sottile a strisce diagonali invertite|
|ThinVerticalStripe|Rappresenta modello sottile a strisce verticali|
|VerticalStripe|Rappresenta modello a strisce verticali|

Nell'esempio seguente, il colore dell'oggetto A1 è impostato ma A2 è configurato per avere sia colori di primo piano sia di sfondo con un modello di sfondo a strisce verticali.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Importante sapere**

{{% alert color="primary" %}}

- Per impostare il colore di primo piano o di sfondo di una cella, utilizzare le proprietà [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) o [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Entrambe le proprietà avranno effetto solo se la proprietà [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) è configurata.
- La proprietà [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) imposta il colore si sfumatura della cella.
  La proprietà [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) specifica il tipo di modello di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells fornisce un'enumerazione, [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), che contiene un insieme di tipi di modelli di sfondo predefiniti.
- Se si seleziona il valore *BackgroundType.None* dall'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), il colore del primo piano non viene applicato.
  Allo stesso modo, il colore di sfondo non viene applicato se si selezionano i valori *BackgroundType.None* o *BackgroundType.Solid*.
- Quando si recupera il colore di sfondo di una cella, se [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) è *BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) restituirà *Color.Empty*.

{{% /alert %}}

### **Applicazione degli effetti di riempimento a sfumatura**

Per applicare i vostri desiderati effetti di riempimento a sfumatura alla cella, utilizzate il metodo [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) di conseguenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Colori e Palette**

Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile utilizzare non solo i colori esistenti nella palette ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla palette.

Questo argomento tratta come aggiungere colori personalizzati alla palette.

### **Aggiunta colori personalizzati alla palette**

Aspose.Cells supporta la palette a 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella palette, aggiungi il colore alla palette.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fornisce un metodo [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) che richiede i seguenti parametri per aggiungere un colore personalizzato alla modifica della palette:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella palette che il colore personalizzato sostituirà. Dovrebbe essere compreso tra 0 e 55.

Nell'esempio seguente viene aggiunto un colore personalizzato (Orchidea) alla palette prima di applicarlo a un carattere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La palette contiene solo 56 colori. Quando si aggiunge un colore personalizzato alla palette, la palette cambia e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando si modifica la palette, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato file XLS (Excel 97 - 2003) in quanto non vi è alcuna limitazione per i formati file XLSX o altri formati di file avanzati di MS Excel (2007/2010 o 2013).

{{% /alert %}}
