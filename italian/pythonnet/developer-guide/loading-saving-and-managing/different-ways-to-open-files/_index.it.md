---
title: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Con Aspose.Cells è semplice aprire file, ad esempio, per recuperare dati o utilizzare un modello di designer per accelerare il processo di sviluppo.

{{% /alert %}}

## **Apertura di un file tramite un percorso**

Gli sviluppatori possono aprire un file Microsoft Excel utilizzando il percorso del file sul computer locale specificandolo nel costruttore della classe **Workbook**. Basta passare il percorso nel costruttore come una *stringa*. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Apertura di un File tramite uno Stream**

È anche semplice aprire un file Excel come uno stream. Per farlo, utilizzare una versione sovraccaricata del costruttore che accetta l'oggetto *BufferStream* che contiene il file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Apertura di un File con solo Dati**

Per aprire un file solo con dati, utilizzare le classi **LoadOptions** e **LoadFilter** per impostare l'attributo e le opzioni correlate delle classi per il file di modello da caricare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file Excel non nativi o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) con Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Ci sono buone probabilità che il costruttore **Workbook** possa generare un *System.OutOfMemoryException* durante il caricamento di grandi fogli di calcolo. Questa eccezione suggerisce che la memoria disponibile è insufficiente per caricare completamente il foglio di calcolo in memoria e quindi il foglio di calcolo deve essere caricato abilitando le preferenze di memoria.

{{% /alert %}}
