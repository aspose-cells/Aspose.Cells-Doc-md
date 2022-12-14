---
title: Diversi modi per aprire i file
type: docs
weight: 10
url: /it/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Con Aspose.Cells è semplice aprire file, ad esempio, per recuperare dati o utilizzare un modello di designer per velocizzare il processo di sviluppo.

{{% /alert %}}

## **Apertura di un file tramite un percorso**

 Gli sviluppatori possono aprire un file Excel Microsoft utilizzando il percorso del file sul computer locale specificandolo nel**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**costruttore di classe. Basta passare il percorso nel costruttore come a*corda*. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Apertura di un file tramite un flusso**

È anche semplice aprire un file Excel come flusso. Per fare ciò, usa una versione sovraccaricata del costruttore che accetta il*Flusso*oggetto che contiene il file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Apertura di un file con solo dati**

 Per aprire un file con solo dati, utilizzare l'estensione**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** e**[Carica filtro](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**classes per impostare l'attributo correlato e le opzioni delle classi per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Caricamento solo fogli visibili**

 Durante il caricamento di a**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**a volte potresti aver bisogno solo di dati in fogli di lavoro visibili in una cartella di lavoro. Aspose.Cells consente di saltare i dati in fogli di lavoro invisibili durante il caricamento di una cartella di lavoro. Per fare ciò, crea una funzione personalizzata che erediti il file**[Carica filtro](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**class e passa la sua istanza a**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Ecco l'implementazione del*CustomnLoad*class a cui si fa riferimento nel frammento precedente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file Excel non nativi o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) entro il numero Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Ci sono buone possibilità che il**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** il costruttore può lanciare*System.OutOfMemoryException* durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo nella memoria, pertanto il foglio di calcolo deve essere caricato abilitando le Preferenze memoria.

{{% /alert %}}
