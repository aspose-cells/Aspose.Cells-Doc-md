---
title: Aspose.Cells for Java 8.4.1 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-8-4-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.4.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.1/)

{{% /alert %}}

Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells

## Aspose.Cells

### **Caratteristiche principali**

Base di codice principale spostata in Java 6 (sono supportati anche Java 7 e 8). Supporto caduto for Java 5 e 1.4.

### **Altri miglioramenti e modifiche**

### **Nuove caratteristiche**

(CELLSJAVA-41235) - Supporto RenderToSize API per l'immagine del foglio di lavoro

(CELLSJAVA-41234) - Supporta i punti elenco durante l'utilizzo di SmartMarkers o il metodo Cell.setHtmlString

### **Insetti**

(CELLSJAVA-41229) - Aspose.Cells non genera singoli HTM e file CSS per i fogli nella conversione da Excel a HTML

(CELLSJAVA-41170) - SheetRender.toImage esegue il rendering dell'immagine con etichette "(vuote)" sull'asse x del grafico

(CELLSJAVA-41270) - Problema con Cells.insertRange() poiché l'area unita non viene spostata correttamente

(CELLSJAVA-41240) - Il testo in carattere Arial viene tagliato dall'alto durante il rendering del foglio di calcolo in PDF

(CELLSJAVA-41238) - CARTA_UN_2 non funziona come previsto quando si salva come PDF

(CELLSJAVA-41217) - Quando i dati della categoria della serie hanno una virgola, le legende del grafico a torta non vengono visualizzate correttamente

(CELLSJAVA-41194) - Sovrapposizione delle voci della legenda durante la conversione del grafico in immagine

(CELLSJAVA-41002) - La linea tratteggiata manca nel grafico 1

(CELLSJAVA-40993) - Linee griglia orizzontali mancanti nel grafico di crescita

(CELLSJAVA-41259) - L'impostazione di Name.setRefersTo e il ricalcolo delle formule generano un valore errato durante la conversione del foglio di calcolo in HTML

(CELLSJAVA-41258) - Il caricamento e il salvataggio di XLSX con Aspose.Cells danneggiano il foglio di calcolo risultante

(CELLSJAVA-41255) - Il pulsante personalizzato diventa immagine e la didascalia scompare nell'output XLSX

(CELLSJAVA-41254) - Microsoft Excel si arresta in modo anomalo quando viene aperto il file XLSX di output

(CELLSJAVA-41253) - Il menu a discesa scompare nel file XLSX di output

### **Eccezioni**

(CELLSJAVA-41266) - java.lang.NumberFormatException si è verificata all'apertura del file XLSX del modello

(CELLSJAVA-41248) - Eccezione puntatore nullo all'apertura del file XLSX di origine

(CELLSJAVA-41265) - Eccezione: "java.lang.NullPointerException" all'apertura di un file SpreadsheetML

(CELLSJAVA-41264) - Eccezione durante l'utilizzo di Cell.getStringValueWithoutFormat

(CELLSJAVA-41246) - Eccezione: formula dinamica non valida... che coinvolge la funzione Indice durante l'utilizzo delle formule dinamiche degli indicatori intelligenti

## Aspose.Cells Griglia Suite

### **Altri miglioramenti e modifiche**

### **Miglioramenti**

(CELLSJAVA-41213) - Gridweb: impostazione di confini diversi tramite operazioni web

### **Insetti**

(CELLSJAVA-41261) - I caratteri multibyte nell'elenco di convalida dei dati sono stati modificati in "??" quando lo si seleziona in FireFox

(CELLSJAVA-41260) - Impossibile scoprire, selezionare o aumentare l'altezza della riga nascosta in GridWeb

(CELLSJAVA-41257) - La navigazione è errata quando ci si sposta dalla cella C1 --> C3 utilizzando i tasti freccia

(CELLSJAVA-41256) - Alcune regole di formattazione condizionale non possono essere utilizzate o parzialmente utilizzate nel file modello quando vengono importate in GridWeb

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

Aggiunge la proprietà Workbook.IsLicensed.

Indica se la licenza è stata impostata.

Metodo Workbook.ValidateFormula obsoleto.

Utilizzare invece la proprietà Cell.Formula.

Aggiunge la proprietà ImageOrPrintOptions.SVGFitToViewPort.

Indica se l'immagine SVG generata è adatta alla porta di visualizzazione.

Aggiunge il metodo ImageOrPrintOptions.SetDesiredSize.

Imposta la larghezza e l'altezza desiderate dell'immagine.

Aggiunge il metodo Aspose.Cells.GridDesktop.WorksheetCollection.MoveTo

Sposta il foglio di lavoro dall'indice specificato a un altro indice.

**Nota**

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.4.1 sono inclusi anche in questo Aspose.Cells for Java v8.4.1.
