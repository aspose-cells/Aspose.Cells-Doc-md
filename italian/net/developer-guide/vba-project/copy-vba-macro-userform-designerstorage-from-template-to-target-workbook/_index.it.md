---
title: Copia VBA Macro UserForm DesignerStorage dal modello alla cartella di lavoro di destinazione
type: docs
weight: 130
url: /it/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Possibili scenari di utilizzo**

Aspose.Cells consente di copiare un progetto VBA da un file Excel in un altro file Excel. Il progetto VBA è costituito da vari tipi di moduli, ad esempio Documento, Procedurale, Designer, ecc. Tutti i moduli possono essere copiati con un semplice codice, ma per il modulo Designer sono presenti alcuni dati aggiuntivi chiamati Designer Storage a cui è necessario accedere o copiare. I due metodi seguenti si occupano di Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Copia VBA Macro UserForm DesignerStorage dal modello alla cartella di lavoro di destinazione**

Vedere il seguente codice di esempio. Copia il progetto VBA dal file[modello di file Excel](50528345.xlsm) in una cartella di lavoro vuota e la salva come file[file Excel di output](50528346.xlsm). Se apri il progetto VBA all'interno del file Excel modello, vedrai un modulo utente come mostrato di seguito. Il modulo utente è costituito da Designer Storage, quindi verrà copiato utilizzando[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)e[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)metodi.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Lo screenshot seguente mostra il file Excel di output e il suo contenuto che sono stati copiati dal file Excel modello. Quando fai clic sul pulsante 1, si apre il modulo utente VBA che a sua volta ha un pulsante di comando che mostra una finestra di messaggio al clic.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
