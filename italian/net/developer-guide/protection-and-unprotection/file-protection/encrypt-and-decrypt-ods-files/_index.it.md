---
title: Crittografa e decritta i file ODS
type: docs
weight: 10
url: /it/net/encrypt-and-decrypt-ods-files/
description: proteggi con password e crittograi i file ODS utilizzando Aspose.Cells per .Net che è una libreria pura net.
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

## **Cifra il file ODS con Aspose.Cells per .Net**
Per cifrare un file ODS, caricare il file e impostare il valore [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) alla password effettiva prima di salvarlo. Il file ODS cifrato risultante può essere aperto solo con OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Decifra il file ODS con Aspose.Cells per .Net**

Per decifrare un file ODS, caricare il file fornendo una password in [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). Una volta caricato il file, impostare la stringa [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) su null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
