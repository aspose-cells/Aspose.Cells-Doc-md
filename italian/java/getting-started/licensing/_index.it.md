---
title: Licensing
type: docs
weight: 50
url: /it/java/licensing/
description: Aspose.Cells per JAVA fornisce diversi piani di acquisto o offre una prova gratuita e una licenza temporanea di 30 giorni per la valutazione utilizzando lo Licensing e le politiche di abbonamento allo Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **Come applicare una licenza nel componente Aspose.Cells**

La licenza è un file XML di testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concessa la licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificare il file; anche l'aggiunta involontaria di un'interruzione di riga aggiuntiva nel file lo invaliderà.

È necessario impostare una licenza prima di utilizzare Aspose.Cells se si desidera evitare le sue limitazioni di valutazione. È necessario impostare una licenza solo una volta per applicazione o processo.

La licenza può essere caricata da un flusso o da un file nelle seguenti posizioni:

1. Percorso esplicito.
1. La cartella che contiene il file Aspose.Cells.jar.

 Usa il[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) metodo per ottenere la licenza del componente. Spesso il modo più semplice per impostare una licenza è inserire il file di licenza nella stessa cartella di Aspose.Cells.jar e specificare solo il nome del file senza percorso, come mostrato nell'esempio seguente:

###  **Come applicare una licenza da disco**

 In questo esempio**Aspose.Cells** tenterà di trovare il file di licenza nella cartella che contiene i JAR della tua applicazione.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **Come applicare una licenza da Stream**

Inizializza una licenza da un flusso.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **Come applicare una licenza in Aspose.Cells.GridWeb**

Si consiglia di inserire il codice di licenza in un punto dell'applicazione Web in cui deve essere elaborato per primo.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Come applicare la licenza a consumo**

Aspose.Cells consente agli sviluppatori di applicare la chiave a consumo. Si tratta di un nuovo meccanismo di concessione delle licenze. Il nuovo meccanismo di licenza verrà utilizzato insieme al metodo di licenza esistente. I clienti che desiderano ricevere una fattura in base all'utilizzo delle funzionalità API possono utilizzare la licenza a consumo. Per ulteriori dettagli, fare riferimento a[Con tassametro Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)sezione.

Una nuova classe[Misurato](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)è stato introdotto per applicare la chiave misurata. Di seguito è riportato il codice di esempio che mostra come impostare la chiave pubblica e privata misurata.

{{< highlight "java" >}}

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
