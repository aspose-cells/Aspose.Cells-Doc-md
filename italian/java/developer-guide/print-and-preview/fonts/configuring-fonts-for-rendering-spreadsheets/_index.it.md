---
title: Configurazione dei Font per la Visualizzazione dei Fogli di Lavoro
type: docs
weight: 10
url: /it/java/configuring-fonts-for-rendering-spreadsheets/
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells forniscono la possibilità di rendere i fogli di calcolo in formati di immagine e di convertirli in formati PDF e XPS. Per massimizzare la fedeltà della conversione, è necessario che i font utilizzati nel foglio di calcolo siano disponibili nella directory predefinita dei font del sistema operativo. Nel caso in cui i font richiesti non siano presenti, le API di Aspose.Cells cercheranno di sostituire i font richiesti con quelli disponibili.

## **Selezione dei font**

Di seguito il processo che le API di Aspose.Cells seguono dietro le quinte.

1. L'API cerca di trovare i font nel file system corrispondenti al nome esatto del font utilizzato nel foglio di calcolo.
1. Se l'API non riesce a trovare i font con lo stesso nome esatto, tenta di utilizzare il font predefinito specificato nella proprietà [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) del foglio di lavoro.
1. Se l'API non riesce a individuare il font definito nella proprietà [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) del foglio di lavoro, tenta di utilizzare il font specificato nelle proprietà [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont).
1. Se l'API non riesce a individuare il font definito nelle proprietà [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont), tenta di utilizzare il font specificato nella proprietà [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName).
1. Se l'API non riesce a individuare il font definito nella proprietà [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName), tenta di selezionare i font più adatti tra tutti i font disponibili.
1. Infine, se l'API non riesce a trovare alcun font nel file system, renderizza il foglio di calcolo utilizzando Arial.

{{% alert color="primary" %}}

In generale, le API di Aspose.Cells scansionano le directory dei font predefinite del sistema operativo su Windows, Linux, MacOS per impostazione predefinita. A partire da [Aspose.Cells for Java 24.7](https://releases.aspose.com/cells/java/release-notes/2024/aspose-cells-for-java-24-7-release-notes/), le API scansionano inoltre le directory dei font cache di Office nel cloud per impostazione predefinita.

{{% /alert %}}

{{% alert color="primary" %}}

Le API di Aspose.Cells scansionano sempre la directory dei font predefinita del sistema operativo con un'eccezione, cioè; quando vengono impostati gli argomenti JVM **-DAspose.Cells.FontDirExc="YourFontDir"**. In tal caso, le API di Aspose.Cells salteranno la scansione della directory dei font predefinita del sistema operativo e cercheranno solo nel percorso specificato negli argomenti JVM menzionati.

{{% /alert %}}

## **Impostazione delle cartelle dei font personalizzate**

Le API di Aspose.Cells cercano la directory predefinita dei font del sistema operativo per i font richiesti. Nel caso in cui i font richiesti non siano disponibili nella directory dei font del sistema, le API cercano attraverso le directory personalizzate (definite dall'utente). La classe [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) ha esposto un certo numero di modi per impostare le directory dei font personalizzate come dettagliato di seguito.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-): Questo metodo è utile se c'è solo una cartella da impostare.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-): Questo metodo è utile quando i font risiedono in più cartelle e l'utente desidera impostare tutte le cartelle separatamente anziché combinare tutti i font in una singola cartella.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources-com.aspose.cells.FontSourceBase[]-): Questo meccanismo è utile quando l'utente desidera caricare i font da più cartelle o un singolo file font o dati font da un array di byte.

{{% alert color="primary" %}}

Entrambi i metodi [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-) e [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-) accettano un secondo parametro di tipo Boolean. Passare **true** come secondo parametro indirizzerà le API di Aspose.Cells a cercare i file dei font nelle sottocartelle.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Si prega di utilizzare uno qualsiasi dei metodi sopra menzionati all'inizio dell'applicazione, cioè prima di invocare qualsiasi altro oggetto delle API di Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Se vengono utilizzati più di uno dei metodi sopra menzionati per impostare le origini dei font, solo le ultime impostazioni avranno effetto.

{{% /alert %}}

## **Meccanismo di sostituzione del font**

Le API di Aspose.Cells forniscono anche la capacità di specificare il font sostitutivo per scopi di visualizzazione. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina dove deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di font come alternativa al font richiesto originariamente. Per ottenere questo, le API di Aspose.Cells hanno esposto il metodo FontConfigs.setFontSubstitutes che accetta 2 parametri. Il primo parametro è di tipo **String**, che dovrebbe essere il nome del font che deve essere sostituito. Il secondo parametro è un array di tipo **String**. Gli utenti possono fornire un elenco di nomi di font come sostituti al font originale (specificato nel primo parametro).

Ecco uno scenario d'uso semplice.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Raccolta informazioni**

Oltre ai metodi sopra menzionati, le API Aspose.Cells forniscono anche mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): Questo metodo restituisce un array di tipo [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) contenente l'elenco delle origini dei font specificate. Nel caso in cui non siano state impostate delle origini, il metodo [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) restituirà un array vuoto.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-): Questo metodo accetta un parametro di tipo **String** permettendo di specificare il nome del font per il quale è stata impostata la sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del font specificato, il metodo [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-) restituirà null.
{{< app/cells/assistant language="java" >}}
