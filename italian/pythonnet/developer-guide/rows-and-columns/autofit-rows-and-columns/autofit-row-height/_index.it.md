---
title: Adattamento automatico dell altezza della riga in modo automatico durante il caricamento del file
type: docs
weight: 120
url: /it/python-net/autofit-row-height/
description: Scopri come adattare le righe che non hanno altezza personalizzata tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Adegua automaticamente l altezza della riga quando si carica un file di Python, Regola automaticamente l altezza della riga quando si apre un file di Excel. 
---

## **Possibili Scenari di Utilizzo**
L'altezza della riga corrisponde automaticamente al carattere del contenuto, ma quando l'altezza della riga memorizzata non corrisponde all'altezza del contenuto nel file, MS Excel regolerà automaticamente l'altezza della riga durante il caricamento del file, mentre Aspose.Cells per Python via .NET non lo regolerà automaticamente per migliorare le prestazioni. Se è necessario utilizzare il programma Aspose.Cells per Python via .NET per corrispondere automaticamente le altezze delle righe durante il caricamento dei file, è possibile raggiungere l'obiettivo tramite il parametro [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/).

Si prega di fare riferimento ai seguenti dati dell'immagine. Possiamo osservare che l'altezza della riga memorizzata nella riga 11 è 15, ma Excel ha regolato automaticamente l'altezza della riga durante il caricamento del file.
<br>
<img src="1.png" width=70% />

## **Regolare l'altezza della riga utilizzando la libreria Excel Aspose.Cells per Python**
Se carichi direttamente il file e lo salvi in PDF, i dati non verranno completamente visualizzati in PDF perché l'altezza della riga della cache è solo 15.
<br>
<img src="2.png" width=70% />
<br>
Se imposti il parametro [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) su true durante il caricamento del file, allora Aspose.Cells per Python via .NET regolerà automaticamente l'altezza della riga. L'altezza della riga regolata può soddisfare efficacemente i requisiti di visualizzazione del testo.
<br>
<img src="3.png" width=70% />

## **Codice di esempio Python**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
