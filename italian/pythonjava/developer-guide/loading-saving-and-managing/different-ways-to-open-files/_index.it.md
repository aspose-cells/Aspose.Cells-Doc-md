---
title: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Con Aspose.Cells è semplice aprire file, ad esempio, per recuperare dati o utilizzare un modello di designer per accelerare il processo di sviluppo.

{{% /alert %}}

## **Apertura di un file tramite un percorso**

I programmatori possono aprire un file Microsoft Excel utilizzando il percorso del file sul computer locale specificandolo nel costruttore della classe [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Basta passare il percorso nel costruttore come *stringa*. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Apertura di un File tramite uno Stream**

È anche semplice aprire un file Excel come uno stream. Per farlo, utilizzare una versione sovraccaricata del costruttore che accetta l'oggetto *BufferStream* che contiene il file.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Apertura di un File con solo Dati**

Per aprire un file solo con i dati, utilizza le classi [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) e [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter) per impostare l'attributo correlato e le opzioni delle classi per il file modello da caricare.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file Excel non nativi o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) con Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

È probabile che il costruttore [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) possa generare *System.OutOfMemoryException* durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo in memoria quindi il foglio di calcolo deve essere caricato abilitando le Preferenze di memoria.

{{% /alert %}}
