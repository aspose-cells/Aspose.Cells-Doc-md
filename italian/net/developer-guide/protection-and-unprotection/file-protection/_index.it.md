---
title: Crittografa e Decrittografa file Excel
type: docs
weight: 10
url: /it/net/encrypt-and-decrypt-excel-files/
description: Come crittografare e decrittografare i file Excel utilizzando C#. Bloccare e sbloccare i file Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ti consente di crittare e proteggere con password i tuoi fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è 'Office 97/2000 Compatible' o 'Crittografia debole (XOR)'. È importante scegliere la corretta lunghezza della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questo è considerato una crittografia debole. Per una crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono tipi di crittografia forte, ad esempio il 'Microsoft Strong Cryptographic Provider'. Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.

Aspose.Cells consente di crittografare e proteggere con password file Microsoft Excel con il tipo di crittografia desiderato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per impostare le impostazioni di crittografia del file in Microsoft Excel (qui Microsoft Excel 2003):

1. Dal menu **Strumenti**, seleziona **Opzioni**. Verrà visualizzata una finestra di dialogo.
1. Selezionare la scheda **Sicurezza**.
1. Immetti una password e clicca su **Avanzate**
1. Scegliere il tipo di crittografia e confermare la password.

## **Crittare file Excel con Aspose.Cells**

L'esempio seguente mostra come crittare e proteggere con password un file excel utilizzando l'API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Specificare la password per modificare l'opzione**

L'esempio seguente mostra come impostare l'opzione **Password per modificare** per un file esistente utilizzando l'API Aspose.Cells di Microsoft Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Decrittografare un file Excel con Aspose.Cells**
È molto semplice aprire un file Excel protetto da password e decifrarlo usando l'API Aspose.Cells come segue:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Argomenti avanzati**
- [Crittografa e Decrittografa file ODS](/cells/it/net/encrypt-and-decrypt-ods-files/)
- [Impostazione del tipo di crittografia forte](/cells/it/net/setting-strong-encryption-type/)
- [Specificare l'autore durante la protezione in scrittura del workbook](/cells/it/net/specify-author-while-write-protecting-workbook/)
- [Verifica password dei file crittografati](/cells/it/net/verify-password-of-encrypted-excel-and-ods-files/)

{{< app/cells/assistant language="csharp" >}}
