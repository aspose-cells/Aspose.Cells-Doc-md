---
title: Come specificare la posizione dei caratteri TrueType
type: docs
weight: 30
url: /it/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

Questo articolo descrive:

1. [Dove l'API Aspose.Cells cerca i caratteri TrueType](/cells/it/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Come specificare esplicitamente una cartella di caratteri TrueType per l'API di Aspose.Cells](/cells/it/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Come limitare l'API Aspose.Cells a utilizzare solo una posizione dei caratteri TrueType](/cells/it/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Lavorare con i Caratteri**

### **Dove Aspose.Cells Cerca i Caratteri TrueType su Windows**

Aspose.Cells cerca i caratteri nella cartella **Windows\Fonts**. Questa impostazione predefinita funziona nella maggior parte dei casi, specificare le proprie cartelle di caratteri solo se è davvero necessario.

### **Dove Aspose.Cells Cerca i Caratteri TrueType su Linux**

Per impostazione predefinita, l'API Aspose.Cells cerca i caratteri in tutte le seguenti posizioni, anche se le diverse distribuzioni Linux memorizzano i caratteri in cartelle diverse.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

Questo comportamento predefinito funzionerà per la maggior parte delle distribuzioni Linux, ma non è garantito che funzioni sempre. Potrebbe essere necessario specificare esplicitamente la posizione dei caratteri TrueType. 

{{% /alert %}}

### **Come Specificare Esplicitamente una Cartella dei Caratteri**

Le API di Aspose.Cells hanno esposto molti metodi factory per la classe FontConfigs per specificare i caratteri o le cartelle dei caratteri, come descritto di seguito.

1. Il metodo setFontFolder accetta il primo parametro di tipo String con la posizione della directory dei caratteri, mentre il secondo parametro di tipo Boolean serve per indicare alle API di Aspose.Cells di cercare ricorsivamente nelle cartelle i file dei caratteri.
1. Il metodo setFontFolders accetta un array di tipo String in modo da poter specificare molte directory dei caratteri utilizzando questo approccio. È anche possibile indicare alle API di Aspose.Cells di cercare ricorsivamente nelle cartelle specificando true come secondo parametro.
1. Il metodo setFontSources accetta un array di tipo FontSourceBase per specificare un elenco delle posizioni individuali dei caratteri.

{{% alert color="primary" %}}

Quando si specifica la cartella dei caratteri utilizzando uno qualsiasi dei metodi sopra menzionati, consigliamo di impostare la posizione del carattere all'avvio dell'applicazione, in caso contrario è possibile ricevere risultati mal formattati.

{{% /alert %}} {{% alert color="primary" %}}

Impostare la cartella dei caratteri utilizzando uno qualsiasi dei metodi sopra menzionati non garantisce che l'API di Aspose.Cells non cercherà i caratteri nelle posizioni predefinite come la cartella dei caratteri di sistema.

{{% /alert %}}

### **Come Limitare l'Utilizzo da Parte di Aspose.Cells a Soli una Cartella dei Caratteri**

A partire da Aspose.Cells for Java 8.1.0, impostare gli argomenti JVM come **-DAspose.Cells.FontDirExc=\"TuaCartellaDeiFont** garantirà che l'API Aspose.Cells utilizzerà solo la posizione dei font come specificata.

Impostare gli argomenti specificati utilizzando il metodo System.setProperty come mostrato di seguito.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Si prega di notare quanto segue:

- La dichiarazione sopra indicata dovrebbe essere all'inizio dell'applicazione.
- Utilizzare l'approccio sopra indicato non richiede di impostare la directory dei font utilizzando i metodi FontConfigs discussi in precedenza.
- La stringa "FontDirSet" dovrebbe essere il percorso completo alla cartella contenente i font richiesti.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
