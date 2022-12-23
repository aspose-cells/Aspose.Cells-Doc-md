---
title: Aspose.Cells for Java 7.2.1 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-7-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 7.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.1/)

{{% /alert %}} 

Noi siamo
 felice di annunciare Aspose.Cells for Java v7.2.1!

 Nuove caratteristiche

- Formatta la tabella pivot con stili personalizzati per diverse categorie (modifica lo stile rapido della tabella pivot)

 Miglioramenti

- Cells.findString()/find() supporta la ricerca di RegExand in un intervallo specifico
- Supporto Picture.setTitle()/getTitle()
- Salva i grafici MS Excel nel file ODS
- Rendi il file Aspose.Cells creato XLS compatibile con il POI

 Eccezioni

- La lettura del file XLSX produce: "java.lang.ClassCastException:org.dom4j.Namespace"

 Insetti

- Il file XLSX salvato restituisce l'errore: "I dati potrebbero essere stati persi"
- Il numero formattato non era corretto nel PDF generato (sono stati persi migliaia di caratteri del gruppo)
- Il grafico a barre non veniva visualizzato nel PDF generato per la versione JDK6
- I riferimenti non vengono aggiornati quando si espande un intervallo
