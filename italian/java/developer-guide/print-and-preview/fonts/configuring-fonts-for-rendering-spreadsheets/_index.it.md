---
title: Configurazione dei caratteri per il rendering di fogli di calcolo
type: docs
weight: 10
url: /it/java/configuring-fonts-for-rendering-spreadsheets/
---
## **Possibili scenari di utilizzo**

Aspose.Cells Le API forniscono la possibilità di eseguire il rendering dei fogli di calcolo in formati immagine e di convertirli in formati PDF e XPS. Per massimizzare la fedeltà della conversione, è necessario che i caratteri utilizzati nel foglio di calcolo siano disponibili nella directory dei caratteri predefinita del sistema operativo. Nel caso in cui i font richiesti non siano presenti allora le API Aspose.Cells cercheranno di sostituire i font richiesti con quelli disponibili.

## **Selezione dei caratteri**

Di seguito è riportato il processo che le API Aspose.Cells seguono dietro le quinte.

1. L'API tenta di trovare i caratteri nel file system corrispondenti al nome esatto del carattere utilizzato nel foglio di calcolo.
1.  Se l'API non riesce a trovare i caratteri con lo stesso identico nome, tenta di utilizzare il carattere predefinito specificato in Cartella di lavoro[**PredefinitoStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) proprietà.
1.  Se l'API non è in grado di individuare il carattere definito sotto la cartella di lavoro[**PredefinitoStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) proprietà, tenta di utilizzare il carattere specificato in[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) proprietà.
1. Se l'API non è in grado di individuare il carattere definito in[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) proprietà, tenta di utilizzare il carattere specificato in[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) proprietà.
1. Se l'API non è in grado di individuare il carattere definito in[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) proprietà, tenta di selezionare i caratteri più adatti tra tutti i caratteri disponibili.
1. Infine, se l'API non riesce a trovare alcun carattere nel file system, esegue il rendering del foglio di calcolo utilizzando Arial.

{{% alert color="primary" %}}

 Le API Aspose.Cells analizzano sempre la directory dei caratteri predefinita del sistema operativo con un'eccezione, ovvero; quando argomenti JVM**-DAspose.Cells.FontDirExc="DirFont"** sono impostati. In tal caso, le API Aspose.Cells salteranno la scansione della directory dei caratteri predefinita del sistema operativo e cercheranno solo il percorso come specificato negli argomenti JVM di cui sopra.

{{% /alert %}}

## **Imposta cartelle di caratteri personalizzati**

 Aspose.Cells Le API ricercano i caratteri richiesti nella directory dei caratteri predefinita del sistema operativo. Nel caso in cui i caratteri richiesti non siano disponibili nella directory dei caratteri del sistema, le API effettuano la ricerca nelle directory personalizzate (definite dall'utente). Il[**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)class ha esposto diversi modi per impostare directory di font personalizzate come descritto di seguito.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): questo metodo è utile se è presente una sola cartella da impostare.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): questo metodo è utile quando i font risiedono in più cartelle e l'utente desidera impostare tutte le cartelle separatamente anziché combinare tutti i font in un'unica cartella.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): questo meccanismo è utile quando l'utente desidera caricare font da più cartelle o un singolo file di font o dati di font da un array di byte.

{{% alert color="primary" %}}

 Tutti e due[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) ) accettano un secondo parametro di tipo booleano. Di passaggio**VERO**come secondo parametro indirizzerà le API Aspose.Cells a cercare nelle sottocartelle i file dei caratteri.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Si prega di utilizzare uno dei metodi sopra menzionati all'inizio dell'applicazione, ovvero; prima di richiamare qualsiasi altro oggetto delle API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Se si utilizza più di uno dei metodi sopra menzionati per impostare le fonti dei caratteri, avranno effetto solo le ultime impostazioni.

{{% /alert %}}

## **Meccanismo di sostituzione dei caratteri**

 Le API Aspose.Cells forniscono anche la possibilità di specificare il carattere sostitutivo per scopi di rendering. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina in cui deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di caratteri in alternativa al carattere originariamente richiesto. Per ottenere ciò, le API Aspose.Cells hanno esposto il metodo FontConfigs.setFontSubstitutes che accetta 2 parametri. Il primo parametro è di tipo**Corda** , che dovrebbe essere il nome del carattere che deve essere sostituito. Il secondo parametro è un array di tipo**Corda**. Gli utenti possono fornire un elenco di nomi di font in sostituzione del font originale (specificato nel primo parametro).

Ecco un semplice scenario di utilizzo.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Raccolta di informazioni**

Oltre ai metodi sopra menzionati, le API Aspose.Cells hanno anche fornito mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): questo metodo restituisce un array di tipo[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) contenente l'elenco delle fonti di font specificate. Nel caso in cui non siano state impostate fonti, il file[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) restituirà un array vuoto.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): questo metodo accetta un parametro di tipo**Corda** permettendo di specificare il nome del carattere per il quale è stata impostata la sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del carattere specificato, il file[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) restituirà null.
