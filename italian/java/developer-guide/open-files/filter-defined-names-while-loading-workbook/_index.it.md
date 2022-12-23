---
title: Filtra i nomi definiti durante il caricamento della cartella di lavoro
type: docs
weight: 50
url: /it/java/filter-defined-names-while-loading-workbook/
---
## **Possibili scenari di utilizzo**

Aspose.Cells consente di filtrare o rimuovere i nomi definiti presenti all'interno della cartella di lavoro. Si prega di utilizzare[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)per caricare nomi definiti e utilizzare ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)per rimuoverli durante il caricamento della cartella di lavoro. Tieni presente che se rimuoverai i nomi definiti, le formule all'interno della cartella di lavoro potrebbero interrompersi.

## **Filtra i nomi definiti durante il caricamento della cartella di lavoro**

Il codice di esempio seguente carica il file[esempio di file Excel](61767873.xlsx)che ha una formula nella cella C1 contenente i nomi definiti, ad es*=SOMMA(MioNome1, MioNome2)*. Dal momento che stiamo usando ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)per rimuovere i nomi definiti durante il caricamento della cartella di lavoro, la formula nella cella C1 in[file Excel di output](61767872.xlsx)si rompe e vedi*#NAME?*invece. Si prega di vedere lo screenshot seguente che mostra l'effetto del codice sul file Excel di esempio.

![cose da fare:immagine_alt_testo](filter-defined-names-while-loading-workbook_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
