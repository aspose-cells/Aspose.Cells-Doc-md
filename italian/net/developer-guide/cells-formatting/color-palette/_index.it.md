---
title: Come Usare la Palette di Colori
type: docs
weight: 80
url: /it/net/excel-color-palette/
description: Codice C# per aggiungere colori personalizzati alla palette e utilizzare la palette di colori di Excel con l API Aspose.Cells for .NET
keywords: c# aggiungere colori personalizzati alla palette, c# palette di colori di Excel in modo programmato, in modo programmato come usare la palette di colori nel workbook, c# come utilizzare la palette di colori in Excel
---

## **Colori e Palette**

Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile utilizzare non solo i colori esistenti nella palette ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla palette.

Questo argomento tratta come aggiungere colori personalizzati alla palette.

## **Aggiungi Colori Personalizzati alla Palette**

Aspose.Cells supporta la palette a 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella palette, aggiungi il colore alla palette.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fornisce un metodo [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) che richiede i seguenti parametri per aggiungere un colore personalizzato alla modifica della palette:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella palette che il colore personalizzato sostituirà. Dovrebbe essere compreso tra 0 e 55.

Nell'esempio seguente viene aggiunto un colore personalizzato (Orchidea) alla palette prima di applicarlo a un carattere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La palette contiene solo 56 colori. Quando si aggiunge un colore personalizzato alla palette, la palette cambia e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando si modifica la palette, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato file XLS (Excel 97 - 2003) in quanto non vi è alcuna limitazione per i formati file XLSX o altri formati di file avanzati di MS Excel (2007/2010 o 2013).

{{% /alert %}}
