---
title: Crittografare e decrittografare i file ODS
type: docs
weight: 10
url: /it/net/encrypt-and-decrypt-ods-files/
description: proteggere con password e crittografare i file ODS utilizzando Aspose.Cells per .Net che è una libreria di rete pura.
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

## **Crittografare il file ODS con Aspose.Cells per .Net**
 Per crittografare un file ODS, caricare il file e impostare l'estensione[**Impostazioni cartella di lavoro.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) valore alla password effettiva prima di salvarla. Il file ODS crittografato di output può essere aperto solo in OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Decrittografare il file ODS con Aspose.Cells per .Net**

 Per decrittografare un file ODS, caricare il file fornendo una password nel file[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Una volta caricato il file, imposta il file[**Impostazioni cartella di lavoro.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) stringa a null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
