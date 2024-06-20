---
title: Crittografare file Excel
type: docs
weight: 90
url: /it/net/encrypting-excel-files/
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

## **Crittografia con Aspose.Cells**

L'esempio seguente mostra come crittare e proteggere con password un file excel utilizzando l'API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Specificare la password per modificare l'opzione**

L'esempio seguente mostra come impostare l'opzione **Password per modificare** per un file esistente utilizzando l'API Aspose.Cells di Microsoft Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Verifica la password del file crittografato**

Per verificare la password del file crittografato, Aspose.Cells for .NET fornisce il metodo [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Questi metodi accettano due parametri: lo stream del file e la password da verificare.
Il seguente frammento di codice dimostra l'uso del metodo [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) per verificare se la password fornita è valida o meno.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Crittografia/Decrittografia del file ODS con Aspose.Cells**

Aspose.Cells consente di crittografare e decrittografare il file ODS. Il file ODS decrittografato può essere aperto sia in Excel che in OpenOffice, tuttavia il file ODS crittografato può essere aperto solo da OpenOffice dopo aver fornito la password. Excel non può aprire il file ODS crittografato e potrebbe generare un messaggio di avviso. Le opzioni di crittografia non sono applicabili per i file ODS a differenza di altri tipi di file. Per crittografare un file ODS, carica il file e imposta il valore [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) alla password effettiva prima di salvarlo. Il file ODS crittografato in uscita può essere aperto solo in OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

Per decifrare un file ODS, caricare il file fornendo una password in [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). Una volta caricato il file, impostare la stringa [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) su null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
