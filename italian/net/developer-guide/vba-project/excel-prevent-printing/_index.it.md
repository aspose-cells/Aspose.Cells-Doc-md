---
title: Come impedire agli utenti di stampare file Excel
type: docs
weight: 600
url: /it/net/how-to-prevent-printing-excel/
description: Scopri come impedire agli utenti di stampare Excel tramite Aspose.Cells for .NET API.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **Possibili scenari di utilizzo**
Nel nostro lavoro quotidiano potrebbero esserci alcune informazioni importanti nel file Excel, al fine di proteggere la diffusione dei dati interni, l'azienda non ci consentirà di stamparli. Questo documento ti spiegherà come impedire ad altri di stampare file Excel.

##  **Come impedire agli utenti di stampare file in MS-Excel**
È possibile applicare il seguente codice VBA per proteggere il file specifico da stampare.
1. Apri la cartella di lavoro che non consenti ad altri di stampare.
1. Seleziona la scheda "Sviluppatore" nella barra multifunzione di Excel e fai clic sul pulsante "Visualizza codice" nella sezione "Controlli". In alternativa, puoi tenere premuti i tasti ALT + F11 per aprire la finestra Microsoft Visual Basic for Applications.
<br>
<img src="1.png" width=70% />
1. Quindi, in Project Explorer a sinistra, fai doppio clic su ThisWorkbook per aprire il modulo e aggiungi alcuni codici vba.
<br>
<img src="2.png" width=70% />
1. Quindi salva e chiudi questo codice e vai al backup della cartella di lavoro e ora, quando stampi il file di esempio, non sarà consentita la stampa e riceverai la seguente casella di avviso:
<br>
<img src="3.png" width=70% />

##  **Come impedire agli utenti di stampare file Excel utilizzando Aspose.Cells for .NET**

Il seguente codice di esempio illustra come impedire agli utenti di stampare file Excel:

1.  Carica il[file di esempio](sample.xlsx).
1. Ottieni l'oggetto VbaModuleCollection dalla proprietà VbaProject di Workbook.
1. Ottieni l'oggetto VbaModule tramite il nome "ThisWorkbook".
1. Imposta la proprietà codes di VbaModule.
1.  Salvare il file di esempio in[formato xlsm](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}