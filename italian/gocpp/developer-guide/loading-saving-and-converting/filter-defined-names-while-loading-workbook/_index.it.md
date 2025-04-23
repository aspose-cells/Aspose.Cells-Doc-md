---
title: Filtra i Nomi Definiti durante il caricamento del Workbook
type: docs
weight: 50
url: /it/go-cpp/filter-defined-names-while-loading-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells permette di filtrare o rimuovere i nomi definiti presenti nel workbook. Utilizzare [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) per caricare i nomi definiti durante il caricamento del workbook. Si noti che, se si rimuovono i nomi definiti, le formule nel workbook potrebbero rompersi.

## **Filtra i nomi definiti durante il caricamento del foglio di lavoro**

Il seguente esempio di codice carica il [file Excel di esempio](61767860.xlsx), che contiene una formula nella cella **C1** con i nomi definiti, ad esempio *=SUM(MyName1, MyName2)*. Poiché utilizziamo ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) per rimuovere i nomi definiti durante il caricamento del workbook, la formula nella cella C1 nel [file Excel di output](61767861.xlsx) si interrompe e mostra *#NAME?*. Vedere lo screenshot seguente che mostra l'effetto del codice sul file Excel di esempio.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
