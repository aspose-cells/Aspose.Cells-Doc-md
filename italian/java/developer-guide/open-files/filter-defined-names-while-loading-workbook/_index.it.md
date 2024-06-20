---
title: Filtra i Nomi Definiti durante il caricamento del Workbook
type: docs
weight: 50
url: /it/java/filter-defined-names-while-loading-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di filtrare o rimuovere i nomi definiti presenti all'interno del workbook. Si prega di usare [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) per caricare i nomi definiti e usare ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) per rimuoverli durante il caricamento del workbook. Si noti che se verranno rimossi i nomi definiti, le formule all'interno del workbook potrebbero interrompersi.

## **Filtra i nomi definiti durante il caricamento del foglio di lavoro**

Il seguente codice di esempio carica il [file Excel di esempio](61767873.xlsx) che ha una formula nella cella C1 contenente i nomi definiti, cioè *=SUM(MyName1, MyName2)*. Poiché stiamo usando ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) per rimuovere i nomi definiti durante il caricamento del workbook, la formula nella cella C1 nel [file Excel di output](61767872.xlsx) si interrompe e si vede *#NAME?* al suo posto. Si prega di consultare la seguente schermata che mostra l'effetto del codice sul file Excel di esempio.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
