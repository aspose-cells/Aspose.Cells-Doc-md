---
title: Specificare i Separatori Decimali e di Gruppo Personalizzati per il Workbook
type: docs
weight: 100
url: /it/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Questo articolo mostra come cambiare il separatore decimale e di gruppo in MS Excel e con il codice Java utilizzando l API Aspose.Cells for Java.
keywords: specifica il separatore decimale personalizzato in excel, specifica il separatore decimale personalizzato in excel java, specifica il separatore di gruppo personalizzato in excel, specifica il separatore di gruppo personalizzato in excel java, specifica il separatore decimale e di gruppo personalizzato in excel, specifica il separatore decimale e di gruppo personalizzato in excel java, cambia il separatore decimale e di gruppo in excel java, cambia il separatore decimale e di gruppo in excel, cambia il separatore decimale in excel, cambia il separatore decimale in excel java, cambia il separatore di gruppo in excel, cambia il separatore di gruppo in excel java
---

{{% alert color="primary" %}}

In Microsoft Excel, è possibile specificare i separatori decimali e migliaia personalizzati invece di utilizzare i separatori di sistema dalle **Opzioni Avanzate di Excel** come mostrato nella schermata sottostante.

Aspose.Cells fornisce le proprietà [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) e [WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) per impostare i separatori personalizzati per formattare/interpretare i numeri.

{{% /alert %}}

## **Specificare i Separatori Personalizzati utilizzando Microsoft Excel**

1. Apri **Opzioni** nella scheda **File**.
1. Apri la scheda **Avanzate**.
1. Modifica le impostazioni nella sezione **Opzioni di Modifica**.

La seguente schermata mostra le **Opzioni Avanzate di Excel** e evidenzia la sezione per specificare i **Separatori Personalizzati**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specificare separatori personalizzati utilizzando Aspose.Cells**

Il seguente codice di esempio illustra come specificare i Separatori Personalizzati utilizzando l'API di Aspose.Cells. Specifica il Separatore Decimale e di Gruppo Personalizzati come punto e spazio rispettivamente. Quindi il numero **123,456.789** sarà visualizzato come **123 456.789** come mostrato nello screenshot che mostra il PDF generato dall'output del codice.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
