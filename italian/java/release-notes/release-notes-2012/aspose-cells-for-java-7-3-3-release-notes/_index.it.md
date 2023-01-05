---
title: Aspose.Cells for Java 7.3.3 Note di rilascio
type: docs
weight: 20
url: /it/java/aspose-cells-for-java-7-3-3-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 7.3.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.3/)

{{% /alert %}} 

Noi siamo
 felice di annunciare Aspose.Cells for Java v7.3.3!

 Nuove caratteristiche

- Aggiungere il metodo Row.getLastDataCell() per ottenere l'ultima cella con dati in una riga
- Aggiunte nuove API per ottenere lo stesso oggetto Style per le celle con le stesse impostazioni di stile

 Miglioramenti

- Aggiungi virgolette ai valori delle celle vuote quando esporti un CSV con

 opzione

 Eccezioni

- La formattazione condizionale con caratteri Unicode non riesce
- L'impostazione della formula prima di aggiungere aree per la formattazione condizionale e quindi la ridenominazione del foglio di lavoro ha causato un errore durante il salvataggio della cartella di lavoro
- Il nuovo salvataggio di un file modello XLS ha causato l'eccezione NegativeArraySizeException

 Insetti

- Il valore della data formattata era diverso da quello mostrato in MS Excel
- I nomi delle serie di grafici vengono persi se CellCollection viene cancellato
- La visualizzazione di spazi vuoti come spazi/zero non funziona per i file XLSX
- La formattazione delle etichette dati per i grafici non va bene
- La sottolineatura del carattere è scomparsa nel file PDF sottoposto a rendering
- L'impostazione degli stili dei caratteri non ha avuto effetto per XLSX in modalità LightCells
- Parte del piè di pagina è stata persa durante il salvataggio in PDF
