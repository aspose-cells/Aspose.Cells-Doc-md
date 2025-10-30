---
title: Crittografa e decritta i file ODS
type: docs
weight: 10
url: /it/python-net/encrypt-and-decrypt-ods-files/
description: proteggi con password e crittografa file ODS con Aspose.Cells per Python via .NET che è una libreria pura .net.
---

{{% alert color="primary" %}}
OpenOffice.org è un pacchetto per ufficio completo che supporta la protezione con password e la crittografia dei file. Tuttavia, i file ODS crittografati possono essere aperti solo da OpenOffice dopo aver fornito la password. Excel non può aprire il file ODS crittografato e potrebbe mostrare un messaggio di avviso. Le opzioni di crittografia non sono applicabili per i file ODS a differenza di altri tipi di file. 
Aspose.Cells per Python via .NET consente di crittografare e decrittografare il file ODS. Il file ODS decrittografato può essere aperto sia in Excel che in OpenOffice, 
{{% /alert %}}

## **Crittografa con OpenOffice Calc**
1. Seleziona **Salva con nome** e seleziona la casella **Salva con password**.
1. Fai clic sul pulsante **Salva**.
1. Digita la password desiderata nei campi **Inserisci password per aprire** e **Conferma password** nella finestra Imposta password che si apre. 
1. Fare clic sul pulsante **OK** per salvare il file.

## **Crittografa il file ODS con Aspose.Cells per Python via .NET**
Per cifrare un file ODS, caricare il file e impostare il valore [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) alla password effettiva prima di salvarlo. Il file ODS cifrato risultante può essere aperto solo con OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Decrittografa il file ODS con Aspose.Cells per Python via .NET**

Per decifrare un file ODS, caricare il file fornendo una password in [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Una volta caricato il file, impostare la stringa [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) su null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
