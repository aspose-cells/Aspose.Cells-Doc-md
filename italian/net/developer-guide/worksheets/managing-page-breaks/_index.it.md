---
title: Gestione dei salti di pagina
type: docs
weight: 30
url: /it/net/managing-page-breaks/
description: Questo articolo fornisce un codice di esempio e spiega come aggiungere interruzioni di pagina, cancellare interruzioni di pagina o eliminare interruzioni di pagina specifiche nei fogli di lavoro di Excel in modo programmato utilizzando l API C# o la libreria .NET.
keywords: interruzioni di pagina c#, interruzioni di pagina excel c#, cancella interruzione di pagina c#, elimina interruzione di pagina specifica c#
---

{{% alert color="primary" %}}

Secondo la definizione, un'interruzione di pagina è un punto in un flusso di testo in cui termina una pagina e inizia la successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunta l'interruzione di pagina, la pagina termina e il resto dei dati dopo l'interruzione di pagina viene stampato sulla pagina successiva durante la stampa. In parole semplici, le interruzioni di pagina dividono il foglio di lavoro in più pagine in base alle specifiche. È inoltre possibile aggiungere interruzioni di pagina ai fogli di lavoro durante l'esecuzione utilizzando Aspose.Cells. Aspose.Cells consente agli sviluppatori di aggiungere due tipi di interruzioni di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

Nel resto della discussione, descriveremo come è possibile aggiungere interruzioni di pagina orizzontali o verticali ai fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}}

## **Interruzioni di pagina**

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione di [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi utilizzati per gestire un foglio di lavoro.

Per aggiungere le interruzioni di pagina, utilizzare le proprietà [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) e [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) della classe [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks).

Le proprietà [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) e [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) sono collezioni che possono contenere diverse interruzioni di pagina. Ogni collezione contiene diversi metodi per gestire interruzioni di pagina orizzontali e verticali.

### **Aggiunta dei salti di pagina**

Per aggiungere un'interruzione di pagina in un foglio di lavoro, inserisci interruzioni di pagina verticale e orizzontale nella cella specificata chiamando i metodi [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) e [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index). Ogni metodo **Aggiungi** prende il nome della cella in cui la rottura dovrebbe essere aggiunta.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

In modalità anteprima interruzione di pagina o anteprima di stampa, è possibile vedere come funzionano queste interruzioni di pagina.

{{% /alert %}}

### **Cancellazione di tutte le interruzioni di pagina**

Per cancellare tutte le interruzioni di pagina in un foglio di lavoro, chiamare i metodi delle raccolte [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) e [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) di [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Rimozione di specifiche interruzioni di pagina**

Per rimuovere una specifica interruzione di pagina, chiamare i metodi [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) e [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat). Ciascun metodo **RemoveAt** prende l'indice dell'interruzione di pagina da rimuovere.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Importante sapere**

Quando si impostano le proprietà **FitToPages** (cioè [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) e [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) nelle impostazioni di impaginazione, le impostazioni delle interruzioni di pagina vengono influenzate, quindi, se si stampa il foglio di lavoro, le impostazioni delle interruzioni di pagina non vengono considerate anche se sono ancora impostate.
{{< app/cells/assistant language="csharp" >}}
