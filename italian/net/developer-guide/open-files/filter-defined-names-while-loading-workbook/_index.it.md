---
title: Filtra i nomi definiti durante il caricamento della cartella di lavoro
type: docs
weight: 50
url: /it/net/filter-defined-names-while-loading-workbook/
---
## **Possibili scenari di utilizzo**

Aspose.Cells consente di filtrare o rimuovere i nomi definiti presenti all'interno della cartella di lavoro. Si prega di utilizzare[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)per caricare nomi definiti e utilizzare ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)per rimuoverli durante il caricamento della cartella di lavoro. Tieni presente che se rimuoverai i nomi definiti, le formule all'interno della cartella di lavoro potrebbero interrompersi.

## **Filtra i nomi definiti durante il caricamento della cartella di lavoro**

 Il codice di esempio seguente carica il file[esempio di file Excel](61767860.xlsx) che ha una formula nella cella**C1** contenente i nomi definiti, ad es*=SOMMA(MioNome1, MioNome2)*. Dal momento che stiamo usando ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) per rimuovere i nomi definiti durante il caricamento della cartella di lavoro, la formula nella cella C1 in[file Excel di output](61767861.xlsx) si rompe e vedi*#NAME?*invece. Si prega di vedere lo screenshot seguente che mostra l'effetto del codice sul file Excel di esempio.

![cose da fare:immagine_alt_testo](filter-defined-names-while-loading-workbook_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
