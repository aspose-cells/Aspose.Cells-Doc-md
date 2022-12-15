---
title: Aspose.Cells for Java 7.2.2 Note di rilascio
type: docs
weight: 60
url: /it/java/aspose-cells-for-java-7-2-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 7.2.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.2/)

{{% /alert %}} 

Noi siamo
 felice di annunciare Aspose.Cells for Java v7.2.2!

 Nuove caratteristiche

- Testo RegEx Cerca il metodo Cells.Find()

 Miglioramenti

- Rendi Aspose.Cells compatibile con la versione precedente dei barattoli Woodstox
- I file OOXML incorporati OLE in XLS escono come file pacchettizzati OLE anziché file decompressi
- Supporta ExportObjectListener per il salvataggio di file HTML
- Copia la formattazione condizionale durante la copia delle righe

 Eccezioni

- Picture.isPrintable() per Picture inPageSetup causa NullPointerException
- Il salvataggio della cartella di lavoro crittografata con la tabella pivot provoca java.lang.NegativeArraySizeException

 Insetti

- Cells.importCustomObjects() con il formato DateTime specificato non funziona
- ChartType errato del grafico a dispersione
- Il valore doppio perde precisione durante la lettura dal file modello CSV
- La serie di grafici è capovolta durante la conversione in un'immagine
- Il file XLSX risalvato causa l'errore "Excelfound contenuto illeggibile…".
- La tabella pivot salvata ha causato "ProtectionView" quando è stata aperta in MS Excel
- Utilizzo della convalida dell'elenco tramite Aspose.Cellscreates un file XLS che non funziona dopo aver modificato il separatore di elenco del sistema
