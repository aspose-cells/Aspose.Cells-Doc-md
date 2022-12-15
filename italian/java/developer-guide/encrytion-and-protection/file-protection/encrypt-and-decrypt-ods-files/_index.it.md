---
title: Crittografare e decrittografare i file ODS
type: docs
weight: 10
url: /it/java/encrypt-and-decrypt-ods-files/
description: proteggere con password e crittografare i file ODS utilizzando Aspose.Cells for Java che è una libreria Java pura.
---
{{% alert color="primary" %}}
 OpenOffice.org è una suite per ufficio completa che supporta la protezione tramite password e la crittografia dei file. Tuttavia, il file ODS crittografato può essere aperto solo da OpenOffice dopo aver fornito la password. Excel non è in grado di aprire il file ODS crittografato e potrebbe generare un messaggio di avviso. Le opzioni di crittografia non sono applicabili per il file ODS a differenza di altri tipi di file.
 Aspose.Cells consente di crittografare e decrittografare il file ODS. Il file ODS decrittografato può essere aperto sia in Excel che in OpenOffice,
{{% /alert %}}

## **Crittografare con OpenOffice Calc**
1.  Selezionare**Salva come** e fare clic su**Salva con password** scatola.
1.  Clicca il**Salva** pulsante.
1.  Digita la password desiderata in entrambi i file**Inserisci la password per aprire** e**Conferma password** campi nella finestra Imposta password che si apre.
1.  Clicca il**OK** pulsante per salvare il file.

## **Crittografia/decrittografia file ODS:**

 Per crittografare un file ODS, caricare il file e passare la password effettiva a[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) prima di salvarlo. Il file ODS crittografato di output può essere aperto solo in OpenOffice. Per decrittografare un file ODS, caricare il file fornendo la password nel file[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . Una volta caricato il file, chiama function[**Cartella di lavoro.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) con la password effettiva come argomento e infine passare null a[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Codice di esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
