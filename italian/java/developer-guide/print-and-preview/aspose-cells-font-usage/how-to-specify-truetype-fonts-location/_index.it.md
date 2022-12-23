---
title: Come specificare la posizione dei caratteri TrueType
type: docs
weight: 30
url: /it/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

Questo articolo descrive:

1. [Dove Aspose.Cells API cerca i font TrueType](/cells/it/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Come specificare esplicitamente una cartella di font TrueType per Aspose.Cells API](/cells/it/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Come limitare Aspose.Cells API per utilizzare solo una posizione dei caratteri TrueType](/cells/it/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Lavorare con i caratteri**

### **Dove Aspose.Cells cerca i caratteri TrueType su Windows**

 Aspose.Cells cerca i caratteri nel file**Windows\Font** cartella. Questa impostazione predefinita funziona la maggior parte delle volte, quindi specifica le tue cartelle di caratteri solo se ne hai davvero bisogno.

### **Dove Aspose.Cells cerca i caratteri TrueType su Linux**

Per impostazione predefinita, Aspose.Cells API cerca i caratteri in tutte le seguenti posizioni, sebbene distribuzioni Linux diverse memorizzino i caratteri in cartelle diverse.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

 Questo comportamento predefinito funzionerà per la maggior parte delle distribuzioni Linux, ma non è garantito che funzioni sempre. Potrebbe essere necessario specificare esplicitamente la posizione dei caratteri TrueType.

{{% /alert %}}

### **Come specificare in modo esplicito una cartella dei caratteri**

Aspose.Cells Le API hanno esposto molti metodi factory per la classe FontConfigs per specificare i caratteri o le cartelle dei caratteri come descritto di seguito.

1. Il metodo setFontFolder accetta il primo parametro di tipo String con la posizione nella directory dei caratteri, mentre il secondo parametro di tipo Boolean indica alle API Aspose.Cells di cercare i file dei caratteri nelle cartelle in modo ricorsivo.
1. Il metodo setFontFolders accetta un array di tipo String quindi puoi specificare molte directory di font usando questo approccio. Puoi anche indirizzare le API Aspose.Cells a cercare le cartelle in modo ricorsivo specificando true come secondo parametro.
1. Il metodo setFontSources accetta un array di tipo FontSourceBase per specificare un elenco di posizioni dei singoli caratteri.

{{% alert color="primary" %}}

Quando specifichi la cartella dei caratteri utilizzando uno dei metodi sopra menzionati, ti consigliamo di impostare la posizione del carattere all'inizio dell'applicazione, altrimenti potresti ricevere risultati con una formattazione scadente.

{{% /alert %}} {{% alert color="primary" %}}

L'impostazione della cartella dei caratteri utilizzando uno dei metodi di cui sopra non garantisce che Aspose.Cells API non cercherà i caratteri nelle posizioni predefinite come la cartella dei caratteri del sistema.

{{% /alert %}}

### **Come limitare lo Aspose.Cells all'uso di una sola cartella di caratteri**

 A partire da Aspose.Cells for Java 8.1.0, impostando gli argomenti JVM come**-DAspose.Cells.FontDirExc="DirFont**assicurerà che Aspose.Cells API utilizzerà solo la posizione dei caratteri specificata.

Impostare gli argomenti specificati utilizzando il metodo System.setProperty come mostrato di seguito.

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Si prega di notare quanto segue:

- La dichiarazione di cui sopra dovrebbe essere all'inizio della domanda.
- L'utilizzo dell'approccio precedente non richiede l'impostazione della directory dei caratteri utilizzando uno dei metodi FontConfigs discussi in precedenza.
- La stringa "FontDirSet" dovrebbe essere il percorso completo della cartella contenente i caratteri richiesti.

{{% /alert %}}
