---
title: Aspose.Cells for Java 7.3.4 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-7-3-4-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 7.3.4](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.4/)

{{% /alert %}} 

Noi siamo
felice di annunciare Aspose.Cells for Java v7.3.4!

 Nuove caratteristiche

- Supporto per il formato TIFF nella funzione Sheet-to-Image

 Miglioramenti

- Il piè di pagina destro non è sopra il piè di pagina centrale come in MS Excel

 Eccezioni

- Eccezione di memoria esaurita durante la conversione di Excel in PDF
- L'impostazione di "+100" come formula condizionale ha causato un'eccezione
- Eccezione: "StackOverflowError" durante il calcolo delle formule
- "IllegalArgumentException" viene generata quando viene chiamato Workbook.copy()

 Insetti

- Il testo arabo è diventato caratteri spazzatura nel file CSV salvato con UTF-8
- Errore "I dati potrebbero essere stati persi" per il file XLS risalvato da Aspose.Cells
- "Excel ha trovato contenuto illeggibile….."errore per Aspose.Cells' rapporto generato
- Cell.getFormula() non ha distinto diversi intervalli con lo stesso nome ma ambito diverso
- Titolo automatico per l'emissione del grafico a torta
- Cell.getR1C1Formula() non ha distinto intervalli denominati diversi con lo stesso nome ma ambito diverso
