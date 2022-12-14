---
title: Crittografia di file Excel
type: docs
weight: 90
url: /it/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) consente di crittografare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un provider di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è "Compatibile con Office 97/2000" o "Crittografia debole (XOR)". È importante scegliere la lunghezza corretta della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questa è considerata una crittografia debole. Per una crittografia avanzata, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono anche tipi di crittografia avanzata, ad esempio "Microsoft Strong Cryptographic Provider". Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.

Aspose.Cells consente di crittografare e proteggere con password i file Excel Microsoft con il tipo di crittografia desiderato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per configurare le impostazioni di crittografia dei file in Microsoft Excel (qui Microsoft Excel 2003):

1.  Dal**Strumenti** menù, selezionare**Opzioni**Apparirà una finestra di dialogo.
1.  Seleziona il**Sicurezza** scheda.
1.  Immettere una password e fare clic**Avanzate**
1. Scegli il tipo di crittografia e conferma la password.

## **Crittografia con Aspose.Cells**

L'esempio seguente mostra come crittografare e proteggere con password un file excel utilizzando Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Specificare la password per modificare l'opzione**

 L'esempio seguente mostra come impostare il**Password da modificare** Microsoft Opzione di Excel per un file esistente utilizzando Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Verificare la password del file crittografato**

 Per verificare la password del file cifrato, Aspose.Cells for .NET fornisce il[**Verifica la password**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) metodo. Questi metodi accettano due parametri, il flusso di file e la password che deve essere verificata.
Il seguente frammento di codice illustra l'uso di[**Verifica la password**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) metodo per verificare se la password fornita è valida o meno.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Crittografia/decrittografia del file ODS con Aspose.Cells**

Aspose.Cells consente di crittografare e decrittografare il file ODS. Il file ODS decrittografato può essere aperto sia in Excel che in OpenOffice, tuttavia il file ODS crittografato può essere aperto solo da OpenOffice dopo aver fornito la password. Excel non è in grado di aprire il file ODS crittografato e potrebbe generare un messaggio di avviso. Le opzioni di crittografia non sono applicabili per il file ODS a differenza di altri tipi di file. Per crittografare un file ODS, caricare il file e impostare l'estensione[**Impostazioni cartella di lavoro.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) valore alla password effettiva prima di salvarla. Il file ODS crittografato di output può essere aperto solo in OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 Per decrittografare un file ODS, caricare il file fornendo una password nel file[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Una volta caricato il file, imposta il file[**Impostazioni cartella di lavoro.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) stringa a null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
