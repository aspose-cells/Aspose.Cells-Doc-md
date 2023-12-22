---
title: Adatta automaticamente l'altezza della riga durante il caricamento del file
type: docs
weight: 120
url: /it/net/autofit-row-height/
description: Scopri come adattare le righe la cui altezza non è personalizzata.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **Possibili scenari di utilizzo**
 L'altezza della riga corrisponde automaticamente al carattere del contenuto, ma quando l'altezza della riga memorizzata nella cache non corrisponde all'altezza del contenuto nel file, MS Excel regolerà automaticamente l'altezza della riga durante il caricamento del file, mentre Aspose.Cells non lo farà regolarlo automaticamente per migliorare le prestazioni. Se è necessario utilizzare il programma Aspose.Cells per far corrispondere automaticamente le altezze delle righe durante il caricamento dei file, è possibile raggiungere l'obiettivo tramite il parametro[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Fare riferimento ai seguenti dati immagine. Possiamo osservare che l'altezza della riga della cache nella riga 11 è 15, ma Excel ha regolato automaticamente l'altezza della riga durante il caricamento del file.
<br>
<img src="1.png" width=70% />

##  **Regola l'altezza della riga utilizzando Aspose.Cells**
Se carichi direttamente il file e lo salvi in PDF, i dati non verranno visualizzati completamente in PDF perché l'altezza della riga della cache è solo 15.
<br>
<img src="2.png" width=70% />
<br>
 Se imposti il parametro[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) su true durante il caricamento del file, Aspose.Cells regolerà automaticamente l'altezza della riga. L'altezza della riga modificata può soddisfare efficacemente i requisiti di visualizzazione del testo.
<br>
<img src="3.png" width=70% />

##  **C# Codice Campione**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}