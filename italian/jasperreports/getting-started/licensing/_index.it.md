---
title: Licenza
type: docs
weight: 40
url: /it/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells for JasperReports è disponibile come valutazione gratuita a tempo illimitato dal[pagina di download](https://downloads.aspose.com/cells/jasperreports). Le versioni di valutazione e con licenza del prodotto sono lo stesso download.

 Quando sei soddisfatto della versione di valutazione, puoi farlo[acquistare una licenza](https://purchase.aspose.com/). Assicurati di comprendere e accettare i termini della licenza.

La licenza è disponibile per il download dalla pagina dell'ordine quando l'ordine è stato pagato. La licenza è un file XML con testo in chiaro e firma digitale. La licenza contiene informazioni come il nome del cliente, il prodotto acquistato e il tipo di licenza. Non modificare il contenuto del file di licenza: ciò invalida la licenza.

Ci sono due modi per applicare una licenza:

- [Chiama setLicense](/cells/it/jasperreports/licensing/#call-setlicense)
- [Impostare un parametro dell'esportatore in applicationContext.xml](/cells/it/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Dopo aver installato la licenza,

- [Verifica che funzioni](/cells/it/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Chiama setLicense**

{{% alert color="primary" %}}

Questo metodo è applicabile per l'utilizzo con JasperReports.

{{% /alert %}}

Scarica la licenza sul tuo computer e copiala nella cartella appropriata (ad esempio la cartella della tua applicazione o**JasperReports\lib**).
Aggiungi il seguente codice al tuo progetto:

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Impostare il parametro LicenseFile Exporter in applicationContext.xml**

{{% alert color="primary" %}}

Questo metodo è applicabile per l'utilizzo con JasperServer.

{{% /alert %}}

1.  Scarica la licenza sul tuo computer e copiala sul file**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** cartella, dove**\<DirInstall>** sta per la directory di installazione di JasperServer.
1.  Individua il**\<DirInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file e aggiungere le seguenti righe:

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Verifica che la licenza funzioni**

Esporta qualsiasi rapporto in formato XLS e controlla se il rapporto contiene un messaggio di valutazione. Se non viene visualizzato alcun messaggio di valutazione, la licenza funziona correttamente.

**Aspose.Cells for JasperReports inserisce un foglio di lavoro di valutazione in modalità valutazione** 

![cose da fare:immagine_alt_testo](licensing_1.png)

**Quando una licenza valida non esiste un foglio di lavoro di valutazione** 

![cose da fare:immagine_alt_testo](licensing_2.png)
