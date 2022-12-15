---
title: Crittografare e decrittografare i file Excel
type: docs
weight: 10
url: /it/net/encrypt-and-decrypt-excel-files/
description: Come crittografare e decrittografare i file Excel utilizzando C#. Blocca e sblocca i file Excel.
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) consente di crittografare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un provider di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è "Compatibile con Office 97/2000" o "Crittografia debole (XOR)". È importante scegliere la lunghezza corretta della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questa è considerata una crittografia debole. Per una crittografia avanzata, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono anche tipi di crittografia avanzata, ad esempio il "Microsoft Strong Cryptographic Provider". Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.

Aspose.Cells consente di crittografare e proteggere con password i file di Microsoft Excel con il tipo di crittografia desiderato.

{{% /alert %}}

## **Utilizzo di Microsoft Excel**

Per configurare le impostazioni di crittografia dei file in Microsoft Excel (qui Microsoft Excel 2003):

1.  Dal**Strumenti** menù, selezionare**Opzioni**Apparirà una finestra di dialogo.
1.  Seleziona il**Sicurezza** scheda.
1.  Immettere una password e fare clic**Avanzate**
1. Scegli il tipo di crittografia e conferma la password.

## **Crittografia file Excel con Aspose.Cells**

L'esempio seguente mostra come crittografare e proteggere con password un file Excel utilizzando l'API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Specificare la password per modificare l'opzione**

 L'esempio seguente mostra come impostare il**Password da modificare** Opzione di Microsoft Excel per un file esistente che utilizza l'API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Decrittografia file Excel con Aspose.Cells**
È molto utile aprire il file excel protetto da password e decrittografarlo utilizzando l'API Aspose.Cells come i seguenti codici:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Argomenti avanzati**
- [Crittografare e decrittografare i file ODS](/cells/it/net/encrypt-and-decrypt-ods-files/)
- [Impostazione del tipo di crittografia avanzata](/cells/it/net/setting-strong-encryption-type/)
- [Specifica l'autore durante la protezione dalla scrittura della cartella di lavoro](/cells/it/net/specify-author-while-write-protecting-workbook/)
- [Verifica la password dei file crittografati](/cells/it/net/verify-password-of-encrypted-excel-and-ods-files/)

