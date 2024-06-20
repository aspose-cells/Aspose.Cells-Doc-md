---
title: Filtra i Nomi Definiti durante il caricamento del Workbook
type: docs
weight: 50
url: /it/net/filter-defined-names-while-loading-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di filtrare o rimuovere i nomi definiti presenti all'interno del workbook. Si prega di usare [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) per caricare i nomi definiti e usare ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) per rimuoverli durante il caricamento del workbook. Si noti che se verranno rimossi i nomi definiti, le formule all'interno del workbook potrebbero interrompersi.

## **Filtra i nomi definiti durante il caricamento del foglio di lavoro**

Il codice di esempio seguente carica il [file Excel di esempio](61767860.xlsx) che ha una formula nella cella **C1** contenente i nomi definiti cioè *=SUM(MyName1, MyName2)*. Poiché stiamo usando ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) per rimuovere i nomi definiti durante il caricamento della cartella di lavoro, la formula nella cella C1 nel [file Excel di output](61767861.xlsx) si interrompe e si visualizza *#NAME?* invece. Si prega di consultare lo screenshot seguente che mostra l'effetto del codice sul file Excel di esempio.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
