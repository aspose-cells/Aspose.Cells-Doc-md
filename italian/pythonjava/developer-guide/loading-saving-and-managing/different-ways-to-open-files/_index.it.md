---
title: Diversi modi per aprire i file
type: docs
weight: 10
url: /it/python-java/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Con Aspose.Cells è semplice aprire file, ad esempio, per recuperare dati o utilizzare un modello di designer per velocizzare il processo di sviluppo.

{{% /alert %}}

## **Apertura di un file tramite un percorso**

 Gli sviluppatori possono aprire un file Excel Microsoft utilizzando il percorso del file sul computer locale specificandolo nel**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**costruttore di classe. Basta passare il percorso nel costruttore come a*corda*. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Apertura di un file tramite un flusso**

È anche semplice aprire un file Excel come flusso. Per fare ciò, usa una versione sovraccaricata del costruttore che accetta il*BufferStream*oggetto che contiene il file.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Apertura di un file con solo dati**

 Per aprire un file con solo dati, utilizzare l'estensione**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** e**[Filtro di caricamento](https://reference.aspose.com/cells/python-java/asposecells.api/Filtro di caricamento)**classes per impostare l'attributo correlato e le opzioni delle classi per il file modello da caricare.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file Excel non nativi o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) entro il numero Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Ci sono buone possibilità che il**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** il costruttore può lanciare*System.OutOfMemoryException* durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo nella memoria, pertanto il foglio di calcolo deve essere caricato abilitando le Preferenze memoria.

{{% /alert %}}
