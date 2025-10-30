---
title: Impostazioni di riempimento
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo. Supporta la impostazione delle impostazioni di riempimento delle celle, consentendo agli utenti di personalizzare lo sfondo e lo stile delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per Python via .NET per impostare le opzioni di riempimento delle celle.
keywords: Aspose.Cells per Python via .NET, Celle, Impostazioni di Riempimento, Sfondo, Stile
type: docs
weight: 50
url: /it/python-net/cells-fill-settings/
---

## **Colori e motivi di sfondo**

Microsoft Excel può impostare i colori del primo piano (contorno) e lo sfondo (riempimento) delle celle e i motivi di sfondo.

Aspose.Cells per Python via .NET supporta anche queste funzionalità in modo flessibile. In questo argomento, impareremo a usare queste funzionalità con Aspose.Cells.

### **Impostazione di colori e motivi di sfondo**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che permette di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Il [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) ha i metodi [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) e [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) utilizzati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fornisce proprietà per impostare i colori di primo piano e di sfondo delle celle. Aspose.Cells per Python via .NET fornisce un'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) che contiene un insieme di tipi predefiniti di motivi di sfondo.

|**Motivi di sfondo**|**Descrizione**|
| :- | :- |
|DIAGONAL_CROSSHATCH| Rappresenta un motivo incrociato diagonale |
|DIAGONAL_STRIPE| Rappresenta un motivo a strisce diagonali|
|GRAY6| Rappresenta un motivo grigio del 6,25%|
|GRAY12| Rappresenta un motivo grigio del 12,5%|
|GRAY25| Rappresenta un motivo grigio del 25%
|GRAY50| Rappresenta il motivo grigio al 50%|
|GRAY75| Rappresenta il motivo grigio al 75%|
|HORIZONTAL_STRIPE| Rappresenta il motivo a strisce orizzontali|
|NONE| Rappresenta nessuno sfondo|
|REVERSE_DIAGONAL_STRIPE| Rappresenta il motivo a strisce diagonali inverse|
|SOLID| Rappresenta un motivo solido|
|THICK_DIAGONAL_CROSSHATCH| Rappresenta il motivo a croce diagonale spesso|
|THIN_DIAGONAL_CROSSHATCH| Rappresenta il motivo a croce diagonale sottile|
|THIN_DIAGONAL_STRIPE| Rappresenta il motivo a strisce diagonali sottili|
|THIN_HORIZONTAL_CROSSHATCH| Rappresenta il motivo a croce orizzontale sottile|
|THIN_HORIZONTAL_STRIPE| Rappresenta il motivo a strisce orizzontali sottili|
|THIN_REVERSE_DIAGONAL_STRIPE| Rappresenta il motivo a strisce diagonali inverse sottili|
|THIN_VERTICAL_STRIPE| Rappresenta il motivo a strisce verticali sottili|
|VERTICAL_STRIPE| Rappresenta il motivo a strisce verticali|

Nell'esempio seguente, il colore dell'oggetto A1 è impostato ma A2 è configurato per avere sia colori di primo piano sia di sfondo con un modello di sfondo a strisce verticali.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **Importante sapere**

{{% alert color="primary" %}}

- Per impostare il colore di primo piano o di sfondo di una cella, utilizzare le proprietà [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) o [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Entrambe le proprietà avranno effetto solo se la proprietà [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) è configurata.
- La proprietà [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) imposta il colore si sfumatura della cella.
  La proprietà [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) specifica il tipo di motivo di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells per Python via .NET fornisce un'enumerazione, [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype). che contiene un insieme di tipi di motivi di sfondo predefiniti.
- Se si seleziona il valore *BackgroundType.None* dall'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), il colore del primo piano non viene applicato.
  Allo stesso modo, il colore di sfondo non viene applicato se si selezionano i valori *BackgroundType.None* o *BackgroundType.Solid*.
- Quando si recupera il colore di sfondo di una cella, se [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) è *BackgroundType.None*, [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) restituirà *Color.Empty*.

{{% /alert %}}

### **Applicazione degli effetti di riempimento a sfumatura**

Per applicare i vostri desiderati effetti di riempimento a sfumatura alla cella, utilizzate il metodo [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) di conseguenza.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **Colori e Palette**

Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells per Python via .NET è possibile non solo usare i colori esistenti della palette, ma anche colori personalizzati. Prima di usare un colore personalizzato, aggiungilo prima alla palette.

Questo argomento tratta come aggiungere colori personalizzati alla palette.

### **Aggiunta colori personalizzati alla palette**

Aspose.Cells per Python via .NET supporta la palette di 56 colori di Microsoft Excel. Per usare un colore personalizzato non definito nella palette, aggiungi il colore alla palette.

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) fornisce un metodo [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette) che accetta i seguenti parametri per aggiungere un colore personalizzato e modificare la palette:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella palette che il colore personalizzato sostituirà. Dovrebbe essere compreso tra 0 e 55.

Nell'esempio seguente viene aggiunto un colore personalizzato (Orchidea) alla palette prima di applicarlo a un carattere.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

La palette contiene solo 56 colori. Quando si aggiunge un colore personalizzato alla palette, la palette cambia e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando si modifica la palette, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato file XLS (Excel 97 - 2003) in quanto non vi è alcuna limitazione per i formati file XLSX o altri formati di file avanzati di MS Excel (2007/2010 o 2013).

{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}
