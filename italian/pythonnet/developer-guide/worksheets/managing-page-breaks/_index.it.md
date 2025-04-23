---
title: Gestione dei salti di pagina
type: docs
weight: 30
url: /it/python-net/managing-page-breaks/
description: Questo articolo fornisce codice di esempio e spiega come aggiungere interruzioni di pagina, cancellare interruzioni di pagina o eliminare specifiche interruzioni di pagina in fogli di lavoro Excel programmaticamente usando le API di Aspose.Cells per Python via .NET.
keywords: Libreria Python per Excel, interruzioni di pagina Python, interruzioni di pagina in Excel in Python, cancellare interruzioni di pagina in Python.
---

{{% alert color="primary" %}}

Secondo la definizione, un'interruzione di pagina è un punto in un flusso di testo in cui termina una pagina e inizia la successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunta l'interruzione di pagina, il cui fine della pagina e il resto dei dati dopo l'interruzione di pagina viene stampato sulla pagina successiva durante la stampa. In parole semplici, le interruzioni di pagina dividono il foglio di lavoro in più pagine secondo le tue specifiche. Puoi anche aggiungere interruzioni di pagina ai tuoi fogli di lavoro a runtime usando Aspose.Cells per Python via .NET. Aspose.Cells per Python via .NET consente agli sviluppatori di aggiungere due tipi di interruzioni di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

 Nel resto della discussione, descriveremo come puoi aggiungere interruzioni di pagina orizzontali o verticali ai tuoi fogli di lavoro usando Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Interruzioni di pagina**

Aspose.Cells per Python via .NET fornisce una classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente di accedere a ogni foglio di lavoro del file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi utilizzati per gestire un foglio di lavoro.

Per aggiungere le interruzioni di pagina, utilizzare le proprietà [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) e [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) della classe [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks).

Le proprietà [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) e [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) sono collezioni che possono contenere diverse interruzioni di pagina. Ogni collezione contiene diversi metodi per gestire interruzioni di pagina orizzontali e verticali.

## **Come aggiungere interruzioni di pagina**

Per aggiungere un'interruzione di pagina in un foglio di lavoro, inserisci interruzioni di pagina verticali e orizzontali alla cella specificata chiamando i metodi [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) e [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str). Ogni metodo **add** prende il nome della cella in cui deve essere aggiunta l'interruzione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

In modalità anteprima interruzione di pagina o anteprima di stampa, è possibile vedere come funzionano queste interruzioni di pagina.

{{% /alert %}}


## **Importante sapere**

Quando si impostano le proprietà **FitToPages** (cioè [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) e [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) nelle impostazioni di impaginazione, le impostazioni delle interruzioni di pagina vengono influenzate, quindi, se si stampa il foglio di lavoro, le impostazioni delle interruzioni di pagina non vengono considerate anche se sono ancora impostate.
