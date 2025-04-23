---
title: Ordinamento dei dati
type: docs
weight: 130
url: /it/net/sort-data-of-excel/
description: Scopri come ordinare i dati utilizzando l API Aspose.Cells for .NET.
keywords: Ordina i dati in ordine ascendente o discendente, ordina i dati in base al colore di sfondo.
---

{{% alert color="primary" %}}

Il sorting dei dati è una delle molte utili funzionalità di Microsoft Excel. Consente agli utenti di ordinare i dati per renderli più facili da esaminare. Aspose.Cells consente ai programmatori di ordinare i dati del foglio di lavoro in ordine alfabetico o numerico, funzionante allo stesso modo di Microsoft Excel per ordinare i dati.

{{% /alert %}}

## **Ordinare i dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1. Seleziona **Dati** dal menu **Ordina**. Verrà visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco - definito come un gruppo contiguo di dati in cui i dati sono visualizzati in colonne.

## **Ordinare i dati con Aspose.Cells**

Aspose.Cells fornisce la classe [**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter) utilizzata per ordinare i dati in ordine ascendente o discendente. La classe ha alcuni membri importanti, ad esempio, proprietà come Key1 ... Key3 e Order1 ... Order3. Questi membri vengono utilizzati per definire le chiavi ordinate e specificare l'ordine di ordinamento della chiave.

È necessario definire le chiavi e impostare l'ordine di ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il metodo [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index) utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

Il metodo [**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1) accetta i seguenti parametri:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), le celle per il foglio di lavoro sottostante.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), l'intervallo di celle. Definire l'area delle celle prima di applicare l'ordinamento dei dati.

Questo esempio utilizza il file di modello "Book1.xls" creato in Microsoft Excel. Dopo l'esecuzione del codice seguente, i dati vengono ordinati in modo appropriato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

Se si desidera ordinare *DaSinistraADestra*, utilizzare l'attributo [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright).

{{% /alert %}}

### **Ordinamento dati con il colore di sfondo**

Excel fornisce funzionalità per ordinare i dati in base al colore di sfondo. La stessa funzionalità viene fornita utilizzando Aspose.Cells utilizzando DataSorter dove [**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor può essere utilizzato in [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono il colore specificato nella [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), sono posizionate in cima o in fondo in base all'impostazione di SortOrder e l'ordine delle altre celle non viene affatto cambiato.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Argomenti avanzati**
- [Ordina dati nella colonna con elenco di ordinamenti personalizzati](/cells/it/net/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="csharp" >}}
