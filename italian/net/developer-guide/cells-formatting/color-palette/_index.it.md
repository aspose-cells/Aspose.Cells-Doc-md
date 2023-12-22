---
title: Come utilizzare la tavolozza dei colori
type: docs
weight: 80
url: /it/net/excel-color-palette/
description: Codice C# per aggiungere colori personalizzati alla tavolozza e utilizzare la tavolozza dei colori Excel con Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **Colori e tavolozza**

Una tavolozza è il numero di colori disponibili da utilizzare nella creazione di un'immagine. L'utilizzo di una tavolozza standardizzata in una presentazione consente all'utente di creare un aspetto coerente. Ogni file Excel (97-2003) Microsoft dispone di una tavolozza di 56 colori che possono essere applicati a celle, caratteri, linee della griglia, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile non solo utilizzare i colori già esistenti nella tavolozza ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla tavolozza.

In questo argomento viene illustrato come aggiungere colori personalizzati alla tavolozza.

##  **Aggiungi colori personalizzati alla tavolozza**

Aspose.Cells supporta la tavolozza di 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella tavolozza, aggiungere il colore alla tavolozza.

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe fornisce a[**Cambia tavolozza**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) metodo che accetta i seguenti parametri per aggiungere un colore personalizzato per modificare la tavolozza:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella tavolozza che verrà sostituito dal colore personalizzato. Dovrebbe essere compreso tra 0 e 55.

L'esempio seguente aggiunge un colore personalizzato (Orchidea) alla tavolozza prima di applicarlo a un carattere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La tavolozza contiene solo 56 colori. Quando aggiungi un colore personalizzato alla tavolozza, la tavolozza viene modificata e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando cambi la tavolozza, fai molta attenzione. Inoltre, questa è la limitazione solo nel formato di file XLS (Excel 97 - 2003) poiché non esiste tale limitazione per XLSX o altri formati di file avanzati MS Excel (2007/2010 o 2013).

{{% /alert %}}