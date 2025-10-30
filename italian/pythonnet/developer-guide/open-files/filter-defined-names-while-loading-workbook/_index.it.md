---
title: Filtra i Nomi Definiti durante il caricamento del Workbook
type: docs
weight: 50
url: /it/python-net/filter-defined-names-while-loading-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells for Python via .NET consente di filtrare o rimuovere i nomi definiti presenti all’interno del workbook. Usa [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) per caricare i nomi definiti e ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) per rimuoverli durante il caricamento del workbook. Nota che, se rimuovi i nomi definiti, le formule all’interno del workbook potrebbero non funzionare più.

## **Filtra i nomi definiti durante il caricamento del foglio di lavoro**

Il codice di esempio seguente carica il [file Excel di esempio](61767860.xlsx) che ha una formula nella cella **C1** contenente i nomi definiti cioè *=SUM(MyName1, MyName2)*. Poiché stiamo usando ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) per rimuovere i nomi definiti durante il caricamento della cartella di lavoro, la formula nella cella C1 nel [file Excel di output](61767861.xlsx) si interrompe e si visualizza *#NAME?* invece. Si prega di consultare lo screenshot seguente che mostra l'effetto del codice sul file Excel di esempio.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
