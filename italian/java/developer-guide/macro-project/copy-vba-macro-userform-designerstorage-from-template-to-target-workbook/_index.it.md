---
title: Copia il designer dello UserForm del macro VBA dal modello al workbook di destinazione
type: docs
weight: 60
url: /it/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di copiare il progetto VBA da un file Excel all'altro file Excel. Il progetto VBA consiste in vari tipi di moduli, cioè Documento, Procedurale, Designer, ecc. Tutti i moduli possono essere copiati con un semplice codice ma per il modulo Designer, c'è alcuni dati aggiuntivi chiamati Storage del Designer che devono essere accessibili o copiati. I seguenti due metodi si occupano di Storage del Designer.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione**

Si prega di consultare il seguente codice di esempio. Copia il progetto VBA dal [file di Excel modello](50528367.xlsm) in un workbook vuoto e salvalo come file di [output Excel](50528366.xlsm). Se apri il progetto VBA all'interno del file di Excel modello, vedrai un User Form come mostrato di seguito. Il User Form è composto da Storage del Designer, quindi verrà copiato utilizzando i metodi [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) e [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-).

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

La seguente schermata mostra il file Excel di output e i suoi contenuti che sono stati copiati dal file di Excel modello. Quando fai clic sul Pulsante 1, si apre il VBA User Form che ha a sua volta un pulsante di comando che mostra una finestra di messaggio cliccando su di esso.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
