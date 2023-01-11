﻿---
title: Converti foglio di lavoro in CSV
type: docs
weight: 30
url: /it/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Converti foglio di lavoro in CSV**
Se gli sviluppatori devono salvare i propri file in una posizione di archiviazione, possono semplicemente specificare il nome del file (con il relativo percorso di archiviazione completo) e il formato del file desiderato (utilizzando il**FileFormatType**enumerazione) mentre si chiama il**Salva**metodo di**Cartella di lavoro**oggetto.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF e XSSF - Converti foglio di lavoro in CSV**
Il codice seguente mostra come il foglio di lavoro può essere convertito in CSV utilizzando Apache POI HSSF e XSSF API rispetto a Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Un rudimentale processore XLSX -> CSV modellato sul

\* Programma di esempio POI XLS2CSVmra di Nick Burch dal

\* pacchetto org.apache.poi.hssf.eventusermodel.examples.

\* A differenza della versione HSSF, questa la ignora completamente

\* righe mancanti.

\* <p/>

\* Le schede tecniche vengono lette utilizzando un parser SAX per conservare i file

\* footprint di memoria relativamente piccolo, quindi dovrebbe essere così

\* in grado di leggere enormi cartelle di lavoro. La tabella degli stili e

\* la tabella delle stringhe condivise deve essere tenuta in memoria. Il

\* Viene utilizzata la classe della tabella degli stili POI standard, ma viene utilizzata una classe personalizzata

La classe \* (sola lettura) viene utilizzata per la tabella delle stringhe condivise

\* perché lo standard POI SharedStringsTable cresce molto

\* rapidamente con il numero di stringhe univoche.

\* <p/>

\* Grazie a Eric Smith per una patch che risolve un problema

\* attivato da celle con più elementi "t", ovvero

\* come Excel rappresenta diversi formati (ad esempio, una parola

\* semplice e una parola in grassetto).

\*

\* @autore Chris Lott

*/

public class ApacheXLSX2CSV {