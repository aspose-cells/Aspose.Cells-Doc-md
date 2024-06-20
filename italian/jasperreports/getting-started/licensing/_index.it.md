---
title: Licenza
type: docs
weight: 40
url: /it/jasperreports/licensing/
---

{{% alert color="primary" %}}

La versione Aspose.Cells for JasperReports è disponibile come valutazione gratuita e illimitata nel tempo dalla [pagina di download](https://downloads.aspose.com/cells/jasperreports). Le versioni di valutazione e con licenza del prodotto sono lo stesso download.

Quando sei soddisfatto della versione di valutazione, puoi [acquistare una licenza](https://purchase.aspose.com/). Assicurati di comprendere e accettare i termini della licenza.

La licenza è disponibile per il download dalla pagina dell'ordine una volta che l'ordine è stato pagato. La licenza è un file XML in chiaro firmato digitalmente. La licenza contiene informazioni come il nome del cliente, il prodotto acquistato e il tipo di licenza. Non modificare il contenuto del file di licenza: questo invalida la licenza.

Ci sono due modi per applicare una licenza:

- [Chiamata a setLicense](/cells/it/jasperreports/licensing/#call-setlicense)
- [Imposta un parametro dell'esportatore in applicationContext.xml](/cells/it/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Dopo aver installato la licenza,

- [Verifica che funzioni](/cells/it/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Chiamata a setLicense**

{{% alert color="primary" %}}

Questo metodo è applicabile all'uso con JasperReports.

{{% /alert %}}

Scarica la licenza sul tuo computer e copiala nella cartella appropriata (ad esempio, nella cartella dell'applicazione o **JasperReports\lib**).
Aggiungi il seguente codice al tuo progetto:

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Imposta il parametro del file di licenza nell'applicationContext.xml**

{{% alert color="primary" %}}

Questo metodo è applicabile all'uso con JasperServer.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Verifica che la licenza funzioni**

Esporta qualsiasi report in formato XLS e controlla se il report contiene un messaggio di valutazione. Se non c'è nessun messaggio di valutazione, allora la licenza funziona correttamente.

**Aspose.Cells for JasperReports inietta un foglio di lavoro di valutazione in modalità di valutazione** 

![todo:image_alt_text](licensing_1.png)

**Quando c'è una licenza valida non c'è un foglio di lavoro di valutazione** 

![todo:image_alt_text](licensing_2.png)
