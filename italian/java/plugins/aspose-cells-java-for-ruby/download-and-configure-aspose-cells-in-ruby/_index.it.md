---
title: Scarica e configura Aspose.Cells in Ruby
type: docs
weight: 10
url: /it/java/download-and-configure-aspose-cells-in-ruby/
---
## **Scarica le librerie richieste**
Scarica le librerie richieste menzionate di seguito. Questi sono i requisiti per l'esecuzione di Aspose.Cells Java per gli esempi di Ruby.

- [Aspose.Cell for Java Componente](https://downloads.aspose.com/cells/java/)
## **Scarica esempi dai siti di codifica sociale**
Le seguenti versioni di esempi in esecuzione sono disponibili per il download sui siti di social coding sotto indicati:

**Git Hub**

- [Aspose.Cells Java per Rubino](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installazione**
È molto semplice e facile da installare Aspose.cells Java per Ruby gem, segui questi semplici passaggi:

1.  Aggiungi questa riga al Gemfile della tua applicazione.

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1.  E poi eseguire

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**O**

1.  Esegui il seguente comando.

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Usando**
Includere i file richiesti per lavorare con l'esempio helloworld.

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Comprendiamo il codice sopra.

1. La prima riga si assicura che le celle aspose siano caricate e disponibili.
1. Includere i file necessari per accedere alle celle aspose.
1. Inizializzare le librerie. Le classi JAVA aspose vengono caricate dal percorso fornito nel file aspose.yml/
