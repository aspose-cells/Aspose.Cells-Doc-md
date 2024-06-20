---
title: Ottieni Avvertimenti durante il Caricamento del File Excel
type: docs
weight: 60
url: /it/java/get-warnings-while-loading-excel-file/
---

## **Possibili Scenari di Utilizzo**

A volte l'utente cerca di caricare il documento di lavoro che è in parte danneggiato ma caricabile. In tal caso, Aspose.Cells genera degli avvisi durante il caricamento del documento di lavoro. È possibile catturare questi avvisi implementando l'interfaccia [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) e impostando la proprietà [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback).

## **Ottieni avvisi durante il caricamento del file Excel**

Il seguente codice di esempio spiega come ottenere avvertimenti durante il caricamento del file excel. Il codice carica il [file excel di esempio](sampleDuplicateDefinedName.xlsx) che genera [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME) avviso al caricamento. Questo avviso viene quindi catturato dal metodo [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo)) che stampa i messaggi di avviso sulla console. Il codice quindi salva il documento di lavoro come [file excel di output](outputDuplicateDefinedName.xlsx). Se apri il file excel di esempio in Microsoft Excel, ti verrà anche visualizzato questo avviso come mostrato in questa schermata. Si prega di controllare anche l'output della console del codice riportato di seguito per una maggiore comprensione.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Output della console**

Questo è l'output della console del codice sopra quando eseguito con il [file excel di esempio fornito](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
