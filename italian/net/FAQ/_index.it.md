---
title: FAQ
type: docs
weight: 100
url: /it/net/faq/
---
## **Come risolvere System.StackOverFlowException su Workbook.CalculateFormula?**
A volte, gli utenti affrontano System.StackOverFlowException sul metodo Workbook.CalculateFormula. Questa eccezione si verifica in genere perché la dimensione predefinita dello stack di IIS è troppo piccola (solo 265 kB). Puoi correggere questo errore creando un altro thread con una dimensione dello stack maggiore e quindi spostando il codice correlato Workbook.CalculateFormula al suo interno.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problema di spessore delle linee durante il rendering di Excel a PDF**
 volte, quando il file Excel viene convertito in PDF, lo spessore delle linee è diverso nell'output PDF. Questo problema non è causato da Aspose.Cells. È causato da**Adobe Reader** quando le sue impostazioni**"Linea liscia arte"** e**"Migliora le linee sottili"** sono controllati. Deselezionando queste opzioni verrà visualizzato PDF bene.

 Se controlla**"Linea liscia arte"** e**"Migliora le linee sottili"**, lo spessore delle linee è diverso. Guarda i seguenti passaggi come è fatto:

-  Vai a**Modificare**
-  Selezionare**Preferenze**
-  Nel**Visualizzazione della pagina** Categoria Controlla il**"Linea liscia arte"** e**"Migliora le linee sottili"**

 Se deseleziona**"Linea liscia arte"** e**"Migliora le linee sottili"**, lo spessore delle linee è lo stesso. Per raggiungere questo obiettivo basta seguire i passaggi seguenti:

-  Vai a**Modificare**
-  Selezionare**Preferenze**
-  Nel**Visualizzazione della pagina** Categoria Deseleziona il**"Linea liscia arte"** e**"Migliora le linee sottili"**
## **Come risolvere System.OutOfMemoryException durante il caricamento di fogli di calcolo di grandi dimensioni?**
Ci sono buone possibilità che il costruttore di Workbook possa generare System.OutOfMemoryException durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo nella memoria, pertanto il foglio di calcolo deve essere caricato abilitando il[Preferenze di memoria](/cells/it/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells Le API forniscono le preferenze di memoria per ottimizzare il consumo di memoria durante il caricamento e l'elaborazione dei fogli di calcolo. Queste opzioni sono utili anche per caricare in modo efficiente i fogli di calcolo di grandi dimensioni contenenti enormi set di dati nell'oggetto cartella di lavoro, come illustrato di seguito.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Determina quale dimensione dello stack è necessaria per una determinata cartella di lavoro**
Tuttavia, abbiamo migliorato il motore di calcolo delle formule Aspose.Cells e, nella maggior parte dei casi, dovresti essere in grado di ottenere tutte le formule calcolate correttamente per un determinato file modello senza specificare dimensioni dello stack inferiori. Tuttavia, a volte StackOverFlowException sul metodo Workbook.CalculateFormula potrebbe essere inevitabile. Forniamo nuove API per consentire agli utenti di tenere traccia dei calcoli delle formule. Abbiamo aggiunto una classe denominata "AbstractCalculationMonitor" e fornito una proprietà, ad es.*CalculationOptions.CalculationMonitor*affrontare/rintracciare il problema.

Gli utenti possono tracciare la dimensione dello stack da soli utilizzando le API. Tieni presente che il controllo dello stack per ogni cella ridurrà sicuramente le prestazioni in misura maggiore. Vedere il segmento di codice di esempio per riferimento:

`     `public class MyCalculationMonitor : AbstractCalculationMonitor
`     `{  ` `public override void BeforeCalculate(int sheetIndex, int rowIndex, int colIndex)  ` `{  ` `if(new StackTrace(false).FrameCount > 2000)  ` `{  ` `throw new Exception(" Interrompi il calcolo della formula a causa del rischio di StackOverflowException");  ` `}  ` `}  ` `} 



{{% alert color="primary" %}} 

Non esiste un modo migliore per ottenere la dimensione dello stack utilizzata in fase di esecuzione. Il codice sopra che abbiamo fornito è solo per esempio. Le prestazioni saranno sicuramente degradate in modo significativo. Quindi, pensiamo che il codice possa essere ottimizzato dagli utenti (che vogliono davvero usarlo) in base ai loro diversi scenari e requisiti. Ad esempio, controllando lo stack quando il conteggio delle celle ricorsive raggiunge un certo numero, raccogliendo il tasso medio di aumento dello stack per una cella ricorsiva e determinando la frequenza per controllare lo stack, ecc.

{{% /alert %}}

