---
title: Gestione delle interruzioni di pagina
type: docs
weight: 30
url: /it/net/managing-page-breaks/
---
{{% alert color="primary" %}}

Secondo la definizione, un'interruzione di pagina è un punto in un flusso di testo in cui una pagina finisce e inizia la successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunta l'interruzione di pagina, la pagina viene terminata e il resto dei dati dopo l'interruzione di pagina viene stampato sulla pagina successiva durante la stampa. In parole semplici, le interruzioni di pagina dividono il foglio di lavoro in più pagine in base alle tue specifiche. Puoi anche aggiungere interruzioni di pagina ai tuoi fogli di lavoro in fase di esecuzione utilizzando Aspose.Cells. Aspose.Cells consente agli sviluppatori di aggiungere due tipi di interruzioni di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

Nel resto della discussione, descriveremo come aggiungere interruzioni di pagina orizzontali o verticali nei fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}}

## **Interruzioni di pagina**

Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)fornisce un'ampia gamma di proprietà e metodi utilizzati per gestire un foglio di lavoro.

 Per aggiungere le interruzioni di pagina, utilizzare il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**Interruzioni di pagina orizzontali**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) e[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)proprietà.

 Il[**Interruzioni di pagina orizzontali**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) e[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)le proprietà sono raccolte che possono contenere diverse interruzioni di pagina. Ogni raccolta contiene diversi metodi per la gestione delle interruzioni di pagina orizzontali e verticali.

### **Aggiunta di interruzioni di pagina**

 Per aggiungere un'interruzione di pagina in un foglio di lavoro, inserisci interruzioni di pagina verticali e orizzontali nella cella specificata chiamando il metodo[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) e[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) metodi. A testa**Aggiungere** Il metodo prende il nome della cella in cui deve essere aggiunta l'interruzione.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

Nelle modalità Anteprima interruzione di pagina o Anteprima di stampa, puoi vedere come funzionano queste interruzioni di pagina.

{{% /alert %}}

### **Cancellazione di tutte le interruzioni di pagina**

 Per cancellare tutte le interruzioni di pagina in un foglio di lavoro, chiama il metodo[**OrizzontalePageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) e[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) collezioni'[**Chiaro()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)metodi.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Rimozione di un'interruzione di pagina specifica**

 Per rimuovere un'interruzione di pagina specifica, chiama il file[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) e[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) metodi. A testa**RimuoviAt**Il metodo prende l'indice dell'interruzione di pagina che sta per essere rimossa.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Importante da sapere**

 Quando imposti**FitToPages** proprietà (es[**FitToPagesAlto**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) e[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) nelle impostazioni di impostazione della pagina, le impostazioni dell'interruzione di pagina sono interessate, quindi, se si stampa il foglio di lavoro, le impostazioni dell'interruzione di pagina non vengono considerate anche se sono ancora impostate.
