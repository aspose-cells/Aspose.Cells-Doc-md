---
title: Scarica e Configura Aspose.Cells in Ruby
type: docs
weight: 10
url: /it/java/download-and-configure-aspose-cells-in-ruby/
---

## **Scarica le librerie necessarie**
Scarica le librerie necessarie indicate di seguito. Queste sono necessarie per eseguire gli esempi di Aspose.Cells Java per Ruby.

- [Componente Aspose.Cell for Java](https://downloads.aspose.com/cells/java/)
## **Scarica esempi dai siti di codice sociale**
Le versioni in esecuzione degli esempi disponibili per il download sono disponibili sui siti di codici sociali di seguito menzionati:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installazione**
È molto semplice e facile installare Aspose.cells Java per il gemma Ruby, segui questi semplici passaggi:

1. Aggiungi questa riga al Gemfile della tua applicazione. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. E quindi esegui 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**OPPURE**

1. Esegui il seguente comando. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Utilizzo**
Includi i file richiesti per lavorare con l'esempio helloworld.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Capisci il codice sopra.

1. La prima riga assicura che aspose cells sia caricato e disponibile.
1. Includi i file necessari per accedere alle celle di aspose.
1. Inizializza le librerie. Le classi aspose JAVA vengono caricate dal percorso fornito nel file aspose.yml/
