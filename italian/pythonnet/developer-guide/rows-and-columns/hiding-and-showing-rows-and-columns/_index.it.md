---
title: Nascondere e mostrare righe e colonne
type: docs
weight: 60
url: /it/python-net/hiding-and-showing-rows-and-columns/
description: Questo articolo mostra come nascondere e mostrare righe e colonne tramite Aspose.Cells per Python via .NET API.
keywords: Libreria Excel Python, Nascondi e mostra righe Python di Aspose.Cells, Nascondi e mostra colonne Python, Nascondi righe e colonne Python, Mostra righe e colonne Python.
---

{{% alert color="primary" %}}

A volte ha senso nascondere alcune righe o colonne in un foglio di lavoro e mostrarle successivamente. Microsoft Excel offre questa funzionalità, così come Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Controllo della visibilità di righe e colonne**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) che consente ai developer di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) che rappresenta tutte le celle nel foglio di lavoro. La collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi vengono discussi di seguito.

## **Come nascondere righe e colonne**

Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) e [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Entrambi i metodi prendono l'indice della riga e della colonna come parametro per nascondere la riga o colonna specifica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

È anche possibile nascondere una riga o colonna impostando rispettivamente l'altezza della riga e la larghezza della colonna a 0.

{{% /alert %}}

## **Come mostrare righe e colonne**

Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) e [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Entrambi i metodi prendono due parametri:

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o colonna dopo l'annullamento della visualizzazione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Mentre si rende visibile una colonna nascosta, se è necessario ripristinarla alla larghezza assegnata in precedenza o alla larghezza originale, si prega di mostrare la colonna con larghezza negativa. Ad esempio: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **Come nascondere righe e colonne multiple**

Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando rispettivamente i metodi [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) e [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Entrambi i metodi prendono l'indice di partenza della riga o colonna e il numero di righe o colonne che devono essere nascoste come parametri.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

È anche possibile utilizzare i metodi [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/) e [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) della classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) per rendere visibili più righe e colonne.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
