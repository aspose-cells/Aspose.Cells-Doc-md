---
title: Copia VBA Macro UserForm DesignerStorage dal modello alla cartella di lavoro di destinazione
type: docs
weight: 60
url: /it/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Possibili scenari di utilizzo**

Aspose.Cells consente di copiare il progetto VBA da un file Excel in un altro file Excel. Il progetto VBA è costituito da vari tipi di moduli, ad esempio Documento, Procedurale, Designer, ecc. Tutti i moduli possono essere copiati con un codice semplice, ma per il modulo Designer sono presenti alcuni dati aggiuntivi chiamati Designer Storage a cui è necessario accedere o copiare. I due metodi seguenti si occupano di Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **Copia VBA Macro UserForm DesignerStorage dal modello alla cartella di lavoro di destinazione**

Vedere il seguente codice di esempio. Copia il progetto VBA dal file[modello di file Excel](50528367.xlsm)in una cartella di lavoro vuota e la salva come file[file Excel di output](50528366.xlsm). Se apri il progetto VBA all'interno del file Excel modello, vedrai un modulo utente come mostrato di seguito. Il modulo utente è costituito da Designer Storage, quindi verrà copiato utilizzando[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) e[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])) metodi.

![cose da fare:immagine_alt_testo](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

Lo screenshot seguente mostra il file Excel di output e il suo contenuto che sono stati copiati dal file Excel modello. Quando fai clic sul pulsante 1, si apre il modulo utente VBA che a sua volta ha un pulsante di comando che mostra una finestra di messaggio al clic.

![cose da fare:immagine_alt_testo](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
