---
title: Crittografare file Excel
type: docs
weight: 90
url: /it/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ti consente di crittare e proteggere con password i tuoi fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è 'Office 97/2000 Compatible' o 'Crittografia debole (XOR)'. È importante scegliere la corretta lunghezza della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questo è considerato una crittografia debole. Per una crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono tipi di crittografia forte, ad esempio il 'Microsoft Strong Cryptographic Provider'. Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.

Aspose.Cells per Python via .NET consente di crittografare e proteggere con password i file Microsoft Excel con il tipo di crittografia desiderato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per impostare le impostazioni di crittografia del file in Microsoft Excel (qui Microsoft Excel 2003):

1. Dal menu **Strumenti**, seleziona **Opzioni**. Verrà visualizzata una finestra di dialogo.
1. Selezionare la scheda **Sicurezza**.
1. Immetti una password e clicca su **Avanzate**
1. Scegliere il tipo di crittografia e confermare la password.

## **Crittografia con Aspose.Cells**

Il seguente esempio mostra come criptografare e proteggere con password un file excel utilizzando l'API Aspose.Cells per Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Specificare la password per modificare l'opzione**

Il seguente esempio mostra come impostare l'opzione **Password per modificare** di Microsoft Excel per un file esistente usando l'API Aspose.Cells per Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Verifica la password del file crittografato**

Per verificare la password del file criptato, Aspose.Cells per Python via .NET offre il metodo [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Questi metodi accettano due parametri, il flusso del file e la password da verificare.
Il seguente frammento di codice dimostra l'uso del metodo [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) per verificare se la password fornita è valida o meno.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **Criptazione/decriptazione di file ODS**

Aspose.Cells per Python via .NET consente di criptare e decriptare file ODS. Il file ODS decriptato può essere aperto sia in Excel che in OpenOffice, tuttavia il file ODS criptato può essere aperto solo in OpenOffice dopo aver fornito la password. Excel non può aprire il file ODS criptato e potrebbe mostrare un messaggio di avviso. Le opzioni di crittografia non sono applicabili ai files ODS, a differenza di altri tipi di file. Per criptare un file ODS, carica il file e imposta il valore [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) sulla password effettiva prima di salvarlo. Il file ODS criptato risultante può essere aperto solo in OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

Per decifrare un file ODS, caricare il file fornendo una password in [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Una volta caricato il file, impostare la stringa [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) su null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

