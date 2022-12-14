---
title: Aspose.Cells for Java 8.7.2 Note di rilascio
type: docs
weight: 120
url: /it/java/aspose-cells-for-java-8-7-2-release-notes/
---
## **Altri miglioramenti e modifiche**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41334 | Formula/funzione COLLEGAMENTO IPERTESTUALE: estende la raccolta Collegamento ipertestuale del foglio di lavoro per ottenere l'oggetto| Nuova caratteristica|
|CELLSJAVA-41788 | La proprietà Start' di un elenco ordinato non funziona correttamente| Insetto|
|CELLSJAVA-41763 | Aspose Cells API non è in grado di convertire ogni contenuto del file HTML in file Excel| Insetto|
|CELLSJAVA-41759 |Il layout è diverso durante il salvataggio del foglio di calcolo in HTML| Insetto|
|CELLSJAVA-41677 | Il collegamento ipertestuale che punta a nomi definiti risulta in un collegamento interrotto quando il foglio di calcolo viene convertito in HTML| Insetto|
|CELLSJAVA-41774 | Calcolo errato sull'analisi what-if| Insetto|
|CELLSJAVA-41748 | Il nome del mese russo viene visualizzato in modo diverso in PDF rispetto a Excel| Insetto|
|CELLSJAVA-41735 | Cell con formato valuta in BMD viene rilevato come DateTime| Insetto|
|CELLSJAVA-41648 | Il formato della data dipendente dalle impostazioni locali cambia in un formato personalizzato fisso durante la conversione di SpreadsheetML in XLSX| Insetto|
|CELLSJAVA-41777 | Problema con il file XLSB di output - Conversione da XLS a XLSB| Insetto|
|CELLSJAVA-41749 | L'impostazione dell'immagine nell'intestazione (per creare filigrana) ripristina le impostazioni del formato immagine| Insetto|
|CELLSJAVA-41787 | La conversione di Excel in PDF richiede un'eternità| Insetto|
|CELLSJAVA-41762 | Sovrapposizione dell'etichetta dell'asse durante la conversione del foglio di calcolo in PDF| Insetto|
|CELLSJAVA-41752 | Le etichette dati si sovrappongono al grafico a torta durante il rendering in PDF| Insetto|
|CELLSJAVA-41751 | Il testo del titolo dell'asse orizzontale/verticale maiuscolo appare in maiuscolo nel formato PDF del grafico| Insetto|
|CELLSJAVA-41736 | Problema di allineamento del grafico durante il rendering del foglio di lavoro nell'immagine| Insetto|
|CELLSJAVA-41755 | Regola verticale mancante nel formato PDF del grafico| Insetto|
|CELLSJAVA-41756 |Lo spessore dei filetti orizzontali è maggiore dello spessore nel grafico effettivo durante il rendering in PDF| Insetto|
|CELLSJAVA-41754 | SmartArt non viene copiato durante la copia della cartella di lavoro| Insetto|
|CELLSJAVA-41717 | L'allineamento verticale della legenda del grafico è cambiato durante la conversione di ODS in XLSX| Insetto|
|CELLSJAVA-41716 | Grafico mancante durante la conversione di ODS in XLSX| Insetto|
|CELLSJAVA-41636 | Cell problema di formato - il valore visualizzato non è corretto in GridWeb (JAVA)| Insetto|
|CELLSJAVA-41746 | java.lang.OutOfMemoryError: limite di overhead GC superato, durante il salvataggio del foglio di calcolo in PDF| Eccezione|
|CELLSJAVA-41768 | com.aspose.cells.Name non può essere trasmesso a java.lang.Integer durante la copia dei fogli di lavoro| Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà TextBoxCollection[string].**
Ottiene la casella di testo in base al nome.
### **Aggiunge la classe AbstractCalculationEngine e CalculationData.**
Nuovo API per consentire all'utente di implementare il proprio motore di calcolo per estendere il motore di calcolo predefinito di Aspose.Cells.
### **Aggiunge la proprietà CalculationOptions.CustomEngine.**
Consenti all'utente di utilizzare il nuovo motore di calcolo personalizzato per calcolare le formule.

{{% alert color="primary" %}} 

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.7.2 sono inclusi anche in questo Aspose.Cells for Java v8.7.2.

{{% /alert %}}
