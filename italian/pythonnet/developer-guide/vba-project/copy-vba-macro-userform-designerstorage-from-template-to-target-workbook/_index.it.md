---
title: Copia il designer dello UserForm del macro VBA dal modello al workbook di destinazione
type: docs
weight: 130
url: /it/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells per Python via .NET ti permette di copiare un progetto VBA da un file Excel a un altro. Il progetto VBA consiste in vari tipi di moduli, ad esempio Documento, Procedurale, Designer, ecc. Tutti i moduli possono essere copiati con codice semplice, ma per il modulo Designer, ci sono alcuni dati aggiuntivi chiamati Designer Storage che devono essere accessibili o copiati. I seguenti due metodi si occupano di Designer Storage.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione**

Si prega di vedere il codice di esempio seguente. Copia il progetto VBA dal [file Excel modello](50528345.xlsm) in un workbook vuoto e lo salva come il [file Excel di output](50528346.xlsm). Se apri il progetto VBA all'interno del file Excel modello, vedrai un User Form come mostrato di seguito. Il User Form è composto da Designer Storage, quindi verrà copiato utilizzando i metodi [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) e [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La seguente schermata mostra il file Excel di output e i suoi contenuti che sono stati copiati dal file Excel modello. Quando fai clic sul Pulsante 1, si apre il VBA User Form che ha a sua volta un pulsante di comando che mostra una finestra di messaggio cliccando.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

