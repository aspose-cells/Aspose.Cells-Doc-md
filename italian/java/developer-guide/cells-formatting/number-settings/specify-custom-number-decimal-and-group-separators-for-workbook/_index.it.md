---
title: Specifica numeri decimali personalizzati e separatori di gruppo per la cartella di lavoro
type: docs
weight: 100
url: /it/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Questo articolo mostra come modificare il numero decimale e il separatore di gruppo in MS Excel e con il codice Java utilizzando il codice Aspose.Cells for Java API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 In Microsoft Excel, è possibile specificare i separatori decimali e delle migliaia personalizzati invece di utilizzare i separatori di sistema dal**Opzioni avanzate di Excel** come mostrato nello screenshot qui sotto.

 Aspose.Cells fornisce il[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) e[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) properties per impostare i separatori personalizzati per la formattazione/l'analisi dei numeri.

{{% /alert %}}

## **Specifica di separatori personalizzati utilizzando Microsoft Excel**

1.  Aprire**Opzioni** nel**File** scheda.
1. Apri il**Avanzate** scheda.
1.  Modificare le impostazioni nel**Opzioni di modifica** sezione.

 Lo screenshot seguente mostra il**Opzioni avanzate di Excel** ed evidenzia la sezione per specificare il file**Separatori personalizzati**.

![cose da fare:immagine_alt_testo](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specifica di separatori personalizzati utilizzando Aspose.Cells**

 Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando Aspose.Cells API. Specifica i separatori numerici personalizzati e di gruppo rispettivamente come punto e spazio. Quindi il numero**123,456.789** verrà visualizzato come**123 456.789** come mostrato nello screenshot che mostra il PDF di output generato dal codice.

![cose da fare:immagine_alt_testo](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
