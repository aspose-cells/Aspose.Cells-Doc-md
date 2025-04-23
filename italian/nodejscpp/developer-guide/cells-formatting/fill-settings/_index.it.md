---  
title: Impostazioni di riempimento
linktitle: Impostazioni di riempimento  
description: Scopri come personalizzare le impostazioni di riempimento, sfondo e stile delle celle usando la libreria Aspose.Cells per Node.js tramite C++.  
keywords: Aspose.Cells, Celle, Impostazioni di Riempimento, Sfondo, Stile, Node.js via C++  
type: docs  
weight: 50  
url: /it/nodejs-cpp/cells-fill-settings/  
---  

## **Colori e motivi di sfondo**  

Microsoft Excel può impostare i colori del primo piano (contorno) e lo sfondo (riempimento) delle celle e i motivi di sfondo.  

Aspose.Cells supporta anche queste funzionalità in modo flessibile. In questo argomento, impariamo ad utilizzare queste funzionalità utilizzando Aspose.Cells.  

### **Impostazione di colori e motivi di sfondo**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Ogni elemento nella raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

La classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) ha i metodi [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) e [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) che vengono usati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) fornisce proprietà per impostare i colori di primo piano e di sfondo delle celle. Aspose.Cells offre un'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) che contiene una serie di pattern di sfondo predefiniti, come descritto di seguito.  

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **Importante sapere**  

{{% alert color="primary" %}}  

- Per impostare il colore di primo piano o di sfondo di una cella, usa i metodi [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).[**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) o [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).[**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-). Entrambi i metodi avranno effetto solo se la proprietà [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).[**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) è configurata.  
- Il metodo [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) imposta il colore dell'ombra della cella.  
  Il metodo [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) specifica il tipo di pattern di sfondo usato per il colore di primo piano o di sfondo. Aspose.Cells fornisce un'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) che contiene una serie di pattern di sfondo predefiniti.  
- Se si seleziona il valore *BackgroundType.None* dall'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype), il colore di primo piano non viene applicato.  
  Allo stesso modo, il colore di sfondo non viene applicato se si selezionano i valori *BackgroundType.None* o *BackgroundType.Solid*.  
- Quando si recupera il colore di sfondo di una cella, se [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) è *BackgroundType.None*, [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) restituirà *Color.Empty*.  

{{% /alert %}}  

### **Applicazione degli effetti di riempimento a sfumatura**  

Per applicare uniformemente gli effetti di riempimento sfumato desiderati alla cella, usa il metodo [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).[**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-) di conseguenza.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **Colori e Palette**  

Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.  

Con Aspose.Cells è possibile utilizzare non solo i colori esistenti nella palette ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla palette.  

Questo argomento tratta come aggiungere colori personalizzati alla palette.  

### **Aggiunta colori personalizzati alla palette**  

Aspose.Cells supporta la palette a 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella palette, aggiungi il colore alla palette.  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) fornisce un metodo [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) che accetta i seguenti parametri per aggiungere un colore personalizzato e modificare la palette:  

- Colore personalizzato, il colore personalizzato da aggiungere.  
- Indice, l'indice del colore nella palette che il colore personalizzato sostituirà. Dovrebbe essere compreso tra 0 e 55.  

Nell'esempio seguente viene aggiunto un colore personalizzato (Orchidea) alla palette prima di applicarlo a un carattere.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

La palette contiene solo 56 colori. Quando si aggiunge un colore personalizzato alla palette, la palette cambia e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando si modifica la palette, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato file XLS (Excel 97 - 2003) in quanto non vi è alcuna limitazione per i formati file XLSX o altri formati di file avanzati di MS Excel (2007/2010 o 2013).  

{{% /alert %}}  

