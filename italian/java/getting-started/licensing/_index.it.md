---
title: Licenza
type: docs
weight: 50
url: /it/java/licensing/
description: Aspose.Cells for JAVA fornisce piani di acquisto diversi o offre una versione di prova gratuita e una licenza temporanea di 30 giorni per valutazione utilizzando le politiche di licenza e sottoscrizione in Java.
keywords: Applica la licenza da disco o flusso Java. Impostare la licenza da disco o flusso Java. Applicare la licenza in Aspose.Cells for Java.
---

## **Come applicare una licenza nel componente Aspose.Cells**

La licenza è un file XML in formato normale che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concessa la licenza, la data di scadenza della sottoscrizione e così via. Il file è firmato digitalmente, quindi non modificarlo; anche l'aggiunta involontaria di una riga vuota nel file lo renderà non valido.

È necessario impostare una licenza prima di utilizzare Aspose.Cells per evitare le limitazioni di valutazione. È necessario impostare una licenza solo una volta per applicazione o processo.

La licenza può essere caricata da uno stream o file nei seguenti percorsi:

1. Percorso esplicito.
1. La cartella che contiene Aspose.Cells.jar.

Usa il metodo [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense-java.io.InputStream-) per licenziare il componente. Spesso il modo più semplice per impostare una licenza è posizionare il file di licenza nella stessa cartella di Aspose.Cells.jar e specificare solo il nome del file senza percorso, come mostrato nel seguente esempio:

### **Come Applicare una Licenza da Disco**

In questo esempio **Aspose.Cells** cercherà di trovare il file della licenza nella cartella che contiene i JAR della tua applicazione.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Come Applicare una Licenza da Stream**

Inizializza una licenza da uno stream.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Come Applicare una Licenza in Aspose.Cells.GridWeb**

Si consiglia di mettere il codice di licenza in un punto della tua applicazione web dove dovrebbe essere elaborato per primo.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Come Applicare una Licenza Metered**

Aspose.Cells consente ai developer di applicare una chiave metered. Si tratta di un nuovo meccanismo di licenza. Il nuovo meccanismo di licenza sarà utilizzato insieme al metodo di licenza esistente. I clienti che desiderano essere fatturati in base all'uso delle funzionalità API possono utilizzare la licenza metered. Per ulteriori dettagli, consulta la sezione [FAQ sulla Licenza Metered](https://purchase.aspose.com/faqs/licensing/metered).

Una nuova classe [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) è stata introdotta per applicare la chiave metered. Di seguito è riportato il codice di esempio che mostra come impostare la chiave pubblica e privata metered.

{{< highlight java >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
