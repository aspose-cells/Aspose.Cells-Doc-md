---
title: Come Prevenire agli Utenti di Stampare un File Excel
type: docs
weight: 600
url: /it/net/how-to-prevent-printing-excel/
description: Scopri come impedire agli utenti di stampare Excel tramite l API Aspose.Cells for .NET.
keywords: stampa excel, impedire la stampa di excel, come impedire agli utenti di stampare excel, excel impedire la stampa, impedire la stampa del workbook, impedire agli utenti di stampare l intero workbook con VBA. 
---

## **Possibili Scenari di Utilizzo**
Nel nostro lavoro quotidiano, potrebbero esserci alcune informazioni importanti nel file Excel, al fine di proteggere i dati interni dalla divulgazione, l'azienda non ci permetterà di stamparli. Questo documento ti dirà come impedire agli altri di stampare i file Excel.

## **Come impedire agli utenti di stampare file in MS-Excel**
È possibile applicare il seguente codice VBA per proteggere il file specifico dalla stampa.
1. Apri il tuo documento di lavoro che non consenti agli altri di stampare.
1. Seleziona la scheda 'Sviluppatore' nel nastro di Excel e fai clic sul pulsante 'Visualizza codice' nella sezione 'Controlli'. In alternativa, puoi premere contemporaneamente i tasti ALT + F11 per aprire la finestra di Microsoft Visual Basic for Applications.
<br>
<img src="1.png" width=70% />
1. Quindi, nel riquadro a sinistra dell'Esplora progetti, fai doppio clic su ThisWorkbook per aprire il modulo e aggiungi alcuni codici VBA.
<br>
<img src="2.png" width=70% />
1. Salva e chiudi questo codice, torna al documento di lavoro e, ora quando stampi il file di esempio, non sarà consentito e otterrai il seguente avviso:
<br>
<img src="3.png" width=70% />

## **Come impedire agli utenti di stampare file Excel utilizzando Aspose.Cells for .NET**

Il seguente codice di esempio illustra come impedire agli utenti di stampare un file excel:

1. Caricare il [file di esempio](sample.xlsx).
1. Ottieni l'oggetto VbaModuleCollection dalla proprietà VbaProject del documento di lavoro.
1. Ottieni l'oggetto VbaModule tramite il nome 'ThisWorkbook'.
1. Imposta la proprietà dei codici di VbaModule.
1. Salva il file di esempio nel formato [xlsm](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
