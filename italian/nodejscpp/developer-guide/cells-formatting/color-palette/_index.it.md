---  
title: Come Usare la Palette di Colori
linktitle: Come Usare la Palette di Colori  
type: docs  
weight: 80  
url: /it/nodejs-cpp/excel-color-palette/  
description: Codice Node.js per aggiungere colori personalizzati alla palette e usare la palette dei colori di Excel con Aspose.Cells for Node.js via C++.  
keywords: node.js aggiungi colori personalizzati alla palette, palette di colori Excel programmaticamente con node.js, come usare programmaticamente la palette dei colori nel libro di lavoro, come usare la palette dei colori in Excel con node.js  
---  

## **Colori e Palette**  

Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.  

Con Aspose.Cells for Node.js via C++, è possibile non solo usare i colori esistenti della palette, ma anche colori personalizzati. Prima di usare un colore personalizzato, aggiungilo alla palette.  

Questo argomento tratta come aggiungere colori personalizzati alla palette.  

## **Aggiungi Colori Personalizzati alla Palette**  

Aspose.Cells supporta la palette a 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella palette, aggiungi il colore alla palette.  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) fornisce un metodo [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) che accetta i seguenti parametri per aggiungere un colore personalizzato e modificare la palette:  

- Colore personalizzato, il colore personalizzato da aggiungere.  
- Indice, l'indice del colore nella palette che il colore personalizzato sostituirà. Dovrebbe essere compreso tra 0 e 55.  

Nell'esempio seguente viene aggiunto un colore personalizzato (Orchidea) alla palette prima di applicarlo a un carattere.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

La palette contiene solo 56 colori. Quando si aggiunge un colore personalizzato alla palette, la palette cambia e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando si modifica la palette, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato file XLS (Excel 97 - 2003) in quanto non vi è alcuna limitazione per i formati file XLSX o altri formati di file avanzati di MS Excel (2007/2010 o 2013).  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
