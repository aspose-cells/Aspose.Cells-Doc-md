---
title: Domande frequenti
type: docs
weight: 100
url: /it/net/faq/
---

## **Come risolvere System.StackOverFlowException su Workbook.CalculateFormula?**
A volte, gli utenti si trovano di fronte a System.StackOverFlowException sul metodo Workbook.CalculateFormula. Questa eccezione di solito si verifica perché la dimensione dello stack predefinita di IIS è troppo piccola (solo 265k). Puoi risolvere questo errore creando un altro thread con una dimensione dello stack aumentata e quindi spostando il tuo codice relativo a Workbook.CalculateFormula al suo interno.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problema con lo spessore delle linee durante il rendering di Excel in PDF**
A volte, quando il file Excel viene convertito in PDF, lo spessore delle linee è diverso nel PDF di output. Questo problema non è causato da Aspose.Cells. È causato da **Adobe Reader** quando le impostazioni **"Smooth line art"** e **"Enhance thin lines"** sono selezionate. Deselezionare queste opzioni visualizzerà correttamente il PDF.

Se selezionate **"Smooth line art"** e **"Enhance thin lines"**, lo spessore delle linee è diverso. Seguire i seguenti passaggi per farlo:

- Andare su **Modifica**
- Seleziona **Preferenze**
- Nella categoria **Visualizzazione pagina** seleziona **"Smooth line art"** e **"Enhance thin lines"**

Se deselezionate **"Smooth line art"** e **"Enhance thin lines"**, lo spessore delle linee è lo stesso. Per ottenere questo seguire i seguenti passaggi:

- Andare su **Modifica**
- Seleziona **Preferenze**
- Nella categoria **Visualizzazione pagina** deseleziona **"Smooth line art"** e **"Enhance thin lines"**
## **Come risolvere System.OutOfMemoryException durante il caricamento di grandi fogli di calcolo?**
C'è una buona probabilità che il costruttore di Workbook possa generare System.OutOfMemoryException durante il caricamento di grandi fogli di calcolo. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo in memoria, quindi il foglio di calcolo deve essere caricato abilitando le [Preferenze di memoria](/cells/it/net/ottimizzazione-utilizzo-memoria-lavorando-con-file-grandi-e-dati-ampie/).

Le API Aspose.Cells forniscono Preferenze di Memoria per ottimizzare il consumo di memoria durante il caricamento e l'elaborazione dei fogli di calcolo. Queste opzioni sono utili anche per caricare efficientemente grandi fogli di calcolo contenenti enormi set di dati nell'oggetto Workbook come dimostrato di seguito.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Determinare quale dimensione dello stack è necessaria per un determinato Workbook**
Anche se abbiamo migliorato il motore di calcolo delle formule di Aspose.Cells e nella maggior parte dei casi, dovresti essere in grado di ottenere tutte le formule calcolate con successo per un determinato file di modello senza specificare una dimensione dello stack più piccola. Ma ancora, a volte StackOverFlowException sul metodo Workbook.CalculateFormula potrebbe essere inevitabile. Forniamo nuove API per gli utenti per tracciare i calcoli delle formule. Abbiamo aggiunto una classe chiamata "AbstractCalculationMonitor" e fornito una proprietà, cioè, *CalculationOptions.CalculationMonitor* per far fronte a/tracciare il problema.

Gli utenti possono seguire la dimensione dello stack da soli utilizzando le API. Si noti che controllare lo stack per ogni cella sicuramente degraderà le prestazioni in misura maggiore. Vedere il segmento di codice di esempio per il riferimento:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

Non c'è un modo migliore per ottenere la dimensione dello stack utilizzata a tempo di esecuzione. Il codice soprastante che abbiamo fornito è solo a scopo di esempio. Le prestazioni saranno certamente degradate in modo significativo. Quindi, pensiamo che il codice possa essere ottimizzato dagli utenti (che desiderano davvero usarlo) in base ai loro diversi scenari e requisiti. Ad esempio, controllare lo stack quando il conteggio delle celle ricorsive raggiunge un certo numero, raccogliere il tasso medio di aumento dello stack per una cella ricorsiva e determinare la frequenza per controllare lo stack, ecc.

{{% /alert %}}

