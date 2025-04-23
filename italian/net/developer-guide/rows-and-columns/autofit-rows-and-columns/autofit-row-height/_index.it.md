---
title: Adattamento automatico dell altezza della riga in modo automatico durante il caricamento del file
type: docs
weight: 120
url: /it/net/autofit-row-height/
description: Scopri come adattare le righe la cui altezza non è personalizzata.
keywords: Adattamento automatico dell altezza della riga durante il caricamento del file, regola automaticamente l altezza della riga all apertura del file di Excel. 
---

## **Possibili Scenari di Utilizzo**
L'altezza della riga corrisponde automaticamente al carattere del contenuto, ma quando l'altezza della riga memorizzata non corrisponde all'altezza del contenuto nel file, MS Excel regolerà automaticamente l'altezza della riga durante il caricamento del file, mentre Aspose.Cells non la regolerà automaticamente per migliorare le prestazioni. Se è necessario utilizzare il programma Aspose.Cells per corrispondere automaticamente le altezze delle linee durante il caricamento dei file, è possibile raggiungere l'obiettivo attraverso il parametro [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Si prega di fare riferimento ai seguenti dati dell'immagine. Possiamo osservare che l'altezza della riga memorizzata nella riga 11 è 15, ma Excel ha regolato automaticamente l'altezza della riga durante il caricamento del file.
<br>
<img src="1.png" width=70% />

## **Regolare l'altezza della riga utilizzando Aspose.Cells**
Se carichi direttamente il file e lo salvi in PDF, i dati non verranno completamente visualizzati in PDF perché l'altezza della riga della cache è solo 15.
<br>
<img src="2.png" width=70% />
<br>
Se imposti il parametro [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) su true quando carichi il file, allora Aspose.Cells regolerà automaticamente l'altezza della riga. L'altezza della riga regolata può soddisfare efficacemente i requisiti di visualizzazione del testo.
<br>
<img src="3.png" width=70% />

## **Codice di esempio C#**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
