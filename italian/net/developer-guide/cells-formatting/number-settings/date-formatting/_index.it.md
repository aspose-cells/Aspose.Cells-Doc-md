---
title: Come formattare un numero come data
type: docs
weight: 10
url: /it/net/format-number-to-date/
description: Questo articolo introdurrà come formattare il numero in data usando l API Aspose.Cells for .NET.
keywords: formatta il numero come data, impostazioni del numero della cella, formatta il numero come data, impostazioni della data, formato della data.
---

## **Possibili Scenari di Utilizzo**
Formattare numeri come date in Excel (o qualsiasi software di fogli di calcolo) è importante per vari motivi, soprattutto quando si lavora con dati che includono informazioni di tempo o pianificazione. Ecco perché è vantaggioso formattare i numeri come date:

1. Interpretazione corretta dei valori di data: in Excel, le date sono memorizzate come numeri seriali (ad esempio, 1 rappresenta il 1° gennaio 1900, e 44210 rappresenta il 6 settembre 2021). Se questi numeri non sono formattati come date, gli utenti potrebbero vedere numeri senza senso invece di date riconoscibili. La formattazione corretta permette a Excel di visualizzarle come date effettive (ad esempio, 06/09/2021 invece di 44210).
1. Semplifica i calcoli relativi al tempo: Excel può eseguire molti calcoli utilizzando le date, come calcolare il numero di giorni tra due date, aggiungere o sottrarre giorni, o determinare il giorno della settimana. Se i numeri non sono formattati come date, Excel non potrà eseguire efficacemente queste operazioni. Ad esempio, se vuoi conoscere il numero di giorni tra 01/09/2023 e 01/10/2023, Excel può calcolarlo facilmente se i numeri sono in formato data.
1. Garantisce coerenza: quando tutti i valori relativi alle date sono formattati correttamente, si garantisce che tutte le date appaiano in uno stile uniforme e leggibile. Questa coerenza è importante nei rapporti aziendali, nei programmi di progetto e nei database dove la coerenza delle date è cruciale.
Diverse regioni usano formati di data diversi (ad esempio MM/GG/AAAA negli USA contro GG/MM/AAAA in molti altri paesi), quindi la formattazione aiuta a garantire un'interpretazione corretta delle date.
1. Migliora la leggibilità: le date presentate in un formato standard (ad esempio, 01/01/2024) sono più facili da leggere rispetto a numeri seriali grezzi come 45000. Una corretta formattazione delle date rende il foglio di calcolo più user-friendly e previene confusioni. Questo è particolarmente importante in scenari di pianificazione, scadenze, gestione eventi o dati storici.
1. Aiuta nell'ordinamento e nel filtraggio: quando le date sono formattate correttamente, Excel le riconosce come date effettive, facilitando l'ordinamento o il filtraggio dei dati cronologicamente. Ad esempio, puoi ordinare una lista di eventi per data o filtrare un intervallo di dati per mostrare solo record tra due date specifiche. Senza una corretta formattazione delle date, l'ordinamento potrebbe basarsi sui numeri grezzi invece di date effettive.
1. Consente l'uso delle funzioni di data: Excel fornisce un'ampia gamma di potenti funzioni di data, come: OGGI(), DATEDIF(), WORKDAY(), ANNO(), MESE(), GIORNO(). Queste funzioni richiedono che le date siano formattate correttamente per calcoli precisi.
1. Supporta la visualizzazione (grafici / linee temporali): le date formattate correttamente possono essere utilizzate per creare grafici e diagrammi nei quali il tempo è un asse chiave. Ad esempio, in un grafico a linee temporali, Excel ha bisogno di date in un formato riconosciuto per tracciare gli eventi in modo accurato nel tempo. Numeri malformati o non formattati potrebbero causare grafici che non hanno senso o riflettono informazioni incorrette.
1. Previene fraintendimenti: i numeri grezzi possono essere facilmente fraintesi. Ad esempio, 44210 potrebbe essere letto come un valore numerico generale, ma quando formattato come data, è chiaro che rappresenta il 6 settembre 2021. Le date correttamente formattate aiutano ad evitare fraintendimenti sui dati.
1. Facilita l'inserimento dei dati: quando le celle sono formattate come date, gli utenti vengono invitati a inserire dati in un formato di data valido, il che previene errori di inserimento e garantisce che i valori di data siano catturati correttamente.
1. Critico per la pianificazione e il monitoraggio: in qualsiasi situazione che coinvolga pianificazione, monitoraggio o scadenze (come gestione progetti, previsioni finanziarie o rapporti sensibili al tempo), la formattazione dei numeri come date è cruciale per accuratezza e comprensione. Permette una migliore pianificazione e esecuzione.


## **Come formattare un numero come data in Excel**
Per formattare un numero come data in Excel, segui questi passaggi:

### **Utilizzando la barra multifunzione (scheda Home)**
1. Seleziona le celle contenenti i numeri che desideri formattare come date.
1. Vai alla scheda Home nella barra multifunzione.
1. Nel gruppo Numero, clicca sulla freccia a discesa nella casella Formato Numero (che potrebbe mostrare "Generale" o "Numero" per impostazione predefinita).
1. Scegli Data breve o Data lunga dal menu a discesa. Data breve: mostra la data in un formato conciso, ad esempio, MM/GG/AAAA (formato USA) o GG/MM/AAAA (formato internazionale). Data lunga: mostra la data in un formato più descrittivo, ad esempio, lunedì, 1 gennaio 2024.
<br>
<img src="1.png" width=60% />

### **Utilizzo della finestra di dialogo Formato celle**
1. Seleziona le celle che desideri formattare.
1. Fai clic con il tasto destro sulle celle selezionate e scegli Formato celle, o premi Ctrl + 1 (Windows) o Cmd + 1 (Mac).
1. Nella finestra di dialogo Formato celle, vai alla scheda Numero.
1. Dalla lista a sinistra, seleziona Data.
1. Scegli il formato data desiderato dall'elenco a destra (ad esempio, GG/MM/AAAA, MM/GG/AAAA, o formati personalizzati).
<br>
<img src="2.png" width=60% />
1. Fai clic su OK per applicare il formato data.

## **Come formattare un numero come data in Aspose.Cells**

Per formattare i numeri come data nel library Aspose.Cells for .NET per lavorare con file Excel, puoi applicare la formattazione della data alle celle programmaticamente. Ecco come farlo usando C# con Aspose.Cells:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Numbers-format-date.cs" >}}
{{< app/cells/assistant language="csharp" >}}
