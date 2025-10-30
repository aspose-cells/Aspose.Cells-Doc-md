---
title: Ordinamento dei dati
type: docs
weight: 130
url: /it/python-net/sort-data-of-excel/
description: Scopri come ordinare i dati utilizzando l API Aspose.Cells for for Python via .NET.
keywords: Libreria Python Excel, Ordina i dati in ordine ascendente o discendente, Ordina i dati in base al colore di sfondo con Python.
---

{{% alert color="primary" %}}

L'ordinamento dei dati è una delle molte utili funzionalità di Microsoft Excel. Consente agli utenti di ordinare i dati per renderne più semplice la scansione. Aspose.Cells for for Python via .NET consente agli sviluppatori di ordinare i dati del foglio di lavoro in ordine alfabetico o numerico, funzionando allo stesso modo di Microsoft Excel per ordinare i dati.

{{% /alert %}}

## **Ordinare i dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1. Seleziona **Dati** dal menu **Ordina**. Verrà visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco - definito come un gruppo contiguo di dati in cui i dati sono visualizzati in colonne.

## **Ordinamento dei dati con Aspose.Cells for Python Excel Library**

Aspose.Cells for for Python via .NET fornisce la classe [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) utilizzata per ordinare i dati in ordine ascendente o discendente. La classe ha alcuni membri importanti, ad esempio, proprietà come Key1 ... Key3 e Order1 ... Order3. Questi membri vengono utilizzati per definire le chiavi ordinate e specificare l'ordine di ordinamento delle chiavi.

È necessario definire le chiavi e impostare l'ordine di ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il metodo [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

Il metodo [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) accetta i seguenti parametri:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), le celle per il foglio di lavoro sottostante.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), l'intervallo di celle. Definire l'area delle celle prima di applicare l'ordinamento dei dati.

Questo esempio utilizza il file di modello "Book1.xls" creato in Microsoft Excel. Dopo l'esecuzione del codice seguente, i dati vengono ordinati in modo appropriato.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

Se si desidera ordinare *DaSinistraADestra*, utilizzare l'attributo [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/).

{{% /alert %}}

### **Ordinamento dei dati con colore di sfondo utilizzando Aspose.Cells for Python Excel Library**

Excel fornisce funzionalità per ordinare i dati in base al colore di sfondo. La stessa funzionalità è fornita utilizzando Aspose.Cells for for Python via .NET utilizzando DataSorter in cui [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). CellColor può essere utilizzato in [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono un determinato colore nella [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any), la funzione sono poste in alto o in basso in base all'impostazione dell'Ordine di ordinamento e l'ordine delle altre celle non viene affatto modificato.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Argomenti avanzati**
- [Ordina dati nella colonna con elenco di ordinamenti personalizzati](/cells/it/python-net/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
