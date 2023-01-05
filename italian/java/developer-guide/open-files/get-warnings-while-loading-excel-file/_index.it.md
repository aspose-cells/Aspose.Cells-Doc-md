---
title: Ricevi avvisi durante il caricamento del file Excel
type: docs
weight: 60
url: /it/java/get-warnings-while-loading-excel-file/
---
## **Possibili scenari di utilizzo**

 volte l'utente tenta di caricare la cartella di lavoro che è in qualche modo danneggiata ma caricabile. In tal caso, Aspose.Cells genera avvisi durante il caricamento della cartella di lavoro. Puoi rilevare questi avvisi implementando il file**[IWarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)** interfaccia e impostazione**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)**proprietà.

## **Ricevi avvisi durante il caricamento del file Excel**

 Il codice di esempio seguente spiega come ricevere avvisi durante il caricamento del file excel. Il codice carica il file[file excel di esempio](sampleDuplicateDefinedName.xlsx) che lancia**[DuplicateDefinedName](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)** avviso al caricamento. Questo avviso viene quindi catturato da**[IWarningCallback.Warning()](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo))** metodo che stampa i messaggi di avviso sulla console. Il codice quindi salva la cartella di lavoro come[file excel di output](outputDuplicateDefinedName.xlsx)Se apri il file excel di esempio in Microsoft Excel, ti verrà visualizzato anche questo avviso come mostrato in questo screenshot. Si prega di controllare anche l'output della console del codice indicato di seguito per una maggiore comprensione.

![cose da fare:immagine_alt_testo](get-warnings-while-loading-excel-file_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Uscita console**

 Ecco l'output della console del codice precedente quando eseguito con il file fornito[file excel di esempio](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
