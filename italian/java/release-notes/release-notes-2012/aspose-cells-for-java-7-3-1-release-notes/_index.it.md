---
title: Aspose.Cells for Java 7.3.1 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-7-3-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 7.3.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.1/)

{{% /alert %}} 

Noi siamo
 felice di annunciare Aspose.Cells for Java v7.3.1 per gli utenti!

 Nuove caratteristiche

 -Analizzare gli script nelle intestazioni/piè di pagina di Page Setup

- Formattazione condizionale: include i campi mancanti del tipo DataBar
- Formattazione condizionale: include i valori mancanti del tipo IconSet
- Formattazione condizionale - Supporto
- Leggi le regole di formattazione condizionale con le formule tra fogli
- Supporta le proprietà Cells.MinDataColumn e Cells.MinDataRow
- Supporta i colori di sfondo Cell con formattazione condizionale (MS Excel 2010)
- Sono supportati i filtri dati della tabella pivot
- È supportata la convalida avanzata dei dati di MS Excel 2010

 (Nota:

Tutti i biglietti di cui sopra
sono originariamente aggiunti per conto degli utenti .NET. Dalla nostra versione Java di
il prodotto è ugualmente abbinato (per quanto riguarda caratteristiche e miglioramenti) con .NET
ora, quindi abbiamo incorporato queste nuove funzionalità/miglioramenti nella versione Java
 anche del prodotto.
) 

 Miglioramenti

 -I file di font temporanei vengono creati più di una volta durante il salvataggio in PDF

 -La data nell'intestazione/piè di pagina non è stata formattata in base alle impostazioni locali della cartella di lavoro

- Supporto nuova opzione: Aspose.Cells.Disable=SunFontManager invece di java.awt.headless per il crash JVM di Open JDK

 -Esporta forme automatiche per il file HTML

 Eccezioni

- Eccezione: "Errore da forma a immagine" durante il salvataggio in PDF

 -Problema da forma a immagine durante il salvataggio in PDF

- "NullPointerException" per il metodo Chart.calculate()

 -Il salvataggio di XLS come PDF ha causato un'eccezione

 -Il salvataggio di XLS come PDF ha causato un'eccezione II

 Insetti

 -Testo sovrapposto e linee della griglia mancanti per il salvataggio di PDF

-I bordi extra sono stati mostrati durante il nuovo salvataggio

 file modello come file XLS

 -La lettura del nome con riferimento "!$A$1" ha causato un'eccezione

 -PDF generazione non riuscita con i dati del grafico specifico

 -Le formule non sono corrette dopo aver inserito l'intervallo

 -Il PDF generato dalla cartella di lavoro di Excel aveva un numero maggiore di pagine

 -Le etichette dei grafici sono diventate disallineate e sovrapposte durante la copia del foglio di lavoro
