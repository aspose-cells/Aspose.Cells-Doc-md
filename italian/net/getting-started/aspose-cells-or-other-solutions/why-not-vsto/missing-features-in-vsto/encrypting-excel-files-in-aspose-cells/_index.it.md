---
title: Crittografare i File Excel in Aspose.Cells
type: docs
weight: 90
url: /it/net/encrypting-excel-files-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) consente di crittografare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi crittografici, o CSP, un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è 'Compatibile con Office 97/2000' o 'Crittografia debole (XOR)'. È importante scegliere la giusta lunghezza della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questo è considerato una crittografia debole. Per una crittografia forte, è richiesta una lunghezza della chiave minima di 128 bit. Microsoft Windows contiene CSP che offrono anche tipi di crittografia forte, ad esempio il 'Fornitore crittografico forte Microsoft'. A titolo informativo, la crittografia a 128 bit è quella che le banche utilizzano per crittografare la connessione con i loro sistemi di Internet Banking.

Aspose.Cells consente di crittografare e proteggere con password file Microsoft Excel con il tipo di crittografia desiderato.

{{% /alert %}} 
## **Utilizzando Microsoft Excel**
Per impostare le impostazioni di crittografia del file in Microsoft Excel (qui Microsoft Excel 2003):

1. Dal menu **Strumenti**, selezionare **Opzioni**.
   Compare una finestra di dialogo.
1. Selezionare la scheda **Sicurezza**.
1. Immetti una password e clicca su **Avanzate** 
   Finestra di dialogo **Opzioni** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_1.png)




1. Scegliere il tipo di crittografia e confermare la password. 

   Finestra di dialogo **Tipo di crittografia** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_2.png)



## **Crittografia con Aspose.Cells**
L'esempio seguente mostra come crittare e proteggere con password un file excel utilizzando l'API Aspose.Cells.

**C#**

{{< highlight csharp >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
