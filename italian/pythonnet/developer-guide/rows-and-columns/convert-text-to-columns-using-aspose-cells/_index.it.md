---
title: Convertire il testo in colonne usando Aspose.Cells
type: docs
weight: 30
url: /it/python-net/convert-text-to-columns-using-aspose-cells/
description: Questo articolo mostra come convertire il testo in colonne tramite l API Aspose.Cells for Python via .NET.
keywords: Libreria Excel Python, Convertire il testo in colonne in Python, Convertire il testo in colonne in Python.
---

## **Possibili Scenari di Utilizzo**

È possibile convertire il testo in colonne utilizzando Microsoft Excel. Questa funzionalità è disponibile da *Data Tools* sotto la scheda *Data*. Per suddividere il contenuto di una colonna in più colonne, i dati devono contenere un delimitatore specifico come una virgola (o qualsiasi altro carattere) in base al quale Microsoft Excel suddivide il contenuto di una cella in più celle. Aspose.Cells for Python via .NET fornisce anche questa funzionalità tramite il metodo [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/).

## **Convertire il testo in colonne utilizzando Aspose.Cells per la libreria Python di Excel**

Il codice di esempio seguente spiega l'uso del metodo [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/). Il codice prima aggiunge alcune persone nel nome della colonna A del primo foglio di lavoro. Il nome e cognome sono separati dal carattere spazio. Quindi applica il metodo [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) sulla colonna A e lo salva come file di output excel. Se apri il [file di output excel](25395213.xlsx), vedrai che i nomi sono nella colonna A mentre i cognomi sono nella colonna B come mostrato in questa schermata.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
