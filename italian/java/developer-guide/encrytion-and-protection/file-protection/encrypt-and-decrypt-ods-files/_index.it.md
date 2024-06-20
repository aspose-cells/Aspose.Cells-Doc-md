---
title: Crittografa e decritta i file ODS
type: docs
weight: 10
url: /it/java/encrypt-and-decrypt-ods-files/
description: Proteggere con password e crittografare i file ODS utilizzando Aspose.Cells for Java che è una libreria puramente Java.
---

{{% alert color="primary" %}}
OpenOffice.org è un pacchetto per ufficio completo che supporta la protezione con password e la crittografia dei file. Tuttavia, i file ODS crittografati possono essere aperti solo da OpenOffice dopo aver fornito la password. Excel non può aprire il file ODS crittografato e potrebbe mostrare un messaggio di avviso. Le opzioni di crittografia non sono applicabili per i file ODS a differenza di altri tipi di file. 
Aspose.Cells consente di crittografare e decrittografare i file ODS. Il file ODS decrittografato può essere aperto sia in Excel che in OpenOffice. 
{{% /alert %}}

## **Crittografa con OpenOffice Calc**
1. Seleziona **Salva con nome** e seleziona la casella **Salva con password**.
1. Fai clic sul pulsante **Salva**.
1. Digita la password desiderata nei campi **Inserisci password per aprire** e **Conferma password** nella finestra Imposta password che si apre. 
1. Fare clic sul pulsante **OK** per salvare il file.

## **Crittografia/Decrittografia del file ODS:**

Per crittografare un file ODS, caricare il file e passare la password effettiva a [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) prima di salvarlo. Il file ODS crittografato in output può essere aperto solo in OpenOffice. Per decrittografare un file ODS, caricare il file fornendo la password a [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password). Una volta caricato il file, chiamare la funzione [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String)) con la password effettiva come argomento e infine passare null a [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Codice di Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
