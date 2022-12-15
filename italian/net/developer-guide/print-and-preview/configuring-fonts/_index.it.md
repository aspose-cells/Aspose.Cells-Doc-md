---
title: Configurazione dei caratteri per il rendering di fogli di calcolo
type: docs
weight: 10
url: /it/net/configuring-fonts-for-rendering-spreadsheets/
---
## **Possibili scenari di utilizzo**

Aspose.Cells Le API forniscono la possibilità di eseguire il rendering dei fogli di calcolo in formati immagine e di convertirli in formati PDF e XPS. Per massimizzare la fedeltà della conversione, è necessario che i caratteri utilizzati nel foglio di calcolo siano disponibili nella directory dei caratteri predefinita del sistema operativo. Nel caso in cui i font richiesti non siano presenti allora le API Aspose.Cells cercheranno di sostituire i font richiesti con quelli disponibili.

## **Selezione dei caratteri**

Di seguito è riportato il processo che le API Aspose.Cells seguono dietro le quinte.

1. L'API tenta di trovare i caratteri nel file system corrispondenti al nome esatto del carattere utilizzato nel foglio di calcolo.
1.  Se l'API non riesce a trovare i caratteri con lo stesso identico nome, tenta di utilizzare il carattere predefinito specificato in Cartella di lavoro**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** proprietà.
1.  Se l'API non è in grado di individuare il carattere definito sotto la cartella di lavoro**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** proprietà, tenta di utilizzare il carattere specificato in**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** o**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** proprietà.
1. Se l'API non è in grado di individuare il carattere definito in**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** o**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** proprietà, tenta di utilizzare il carattere specificato in**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** proprietà.
1. Se l'API non è in grado di individuare il carattere definito in**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** proprietà, tenta di selezionare i caratteri più adatti tra tutti i caratteri disponibili.
1. Infine, se l'API non riesce a trovare alcun carattere nel file system, esegue il rendering del foglio di calcolo utilizzando Arial.

## **Imposta cartelle di caratteri personalizzati**

 Aspose.Cells Le API ricercano i caratteri richiesti nella directory dei caratteri predefinita del sistema operativo. Nel caso in cui i caratteri richiesti non siano disponibili nella directory dei caratteri del sistema, le API effettuano la ricerca nelle directory personalizzate (definite dall'utente). Il**[FontConfigs](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**class ha esposto diversi modi per impostare directory di font personalizzate come descritto di seguito.

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: Questo metodo è utile se c'è solo una cartella da impostare.
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: Questo metodo è utile quando i font risiedono in più cartelle e l'utente desidera impostare tutte le cartelle separatamente piuttosto che combinare tutti i font in un'unica cartella.
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: Questo meccanismo è utile quando l'utente desidera caricare font da più cartelle o un singolo file di font o dati di font da un array di byte.

{{% alert color="primary" %}}

 Tutti e due**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** i metodi accettano un secondo parametro di tipo booleano. Di passaggio**VERO** poiché il secondo parametro indirizzerà le API Aspose.Cells a cercare nelle sottocartelle i file dei caratteri.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Si prega di utilizzare uno dei metodi sopra menzionati all'inizio dell'applicazione, ovvero; prima di richiamare qualsiasi altro oggetto delle API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Se vengono utilizzati tutti i metodi sopra menzionati per impostare le origini dei caratteri, avranno effetto solo le ultime impostazioni.

{{% /alert %}}

## **Meccanismo di sostituzione dei caratteri**

 Le API Aspose.Cells forniscono anche la possibilità di specificare il carattere sostitutivo per scopi di rendering. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina in cui deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di caratteri in alternativa al carattere originariamente richiesto. Per raggiungere questo obiettivo, le API Aspose.Cells hanno esposto il file**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** metodo che accetta 2 parametri. Il primo parametro è di tipo**corda** , che dovrebbe essere il nome del carattere che deve essere sostituito. Il secondo parametro è un array di tipo**corda**Gli utenti possono fornire un elenco di nomi di font in sostituzione del nome del font originale (specificato nel primo parametro).

Ecco un semplice scenario di utilizzo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Raccolta di informazioni**

Oltre ai metodi sopra menzionati, le API Aspose.Cells hanno anche fornito mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** Il metodo restituisce un array di tipo**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)** contenente l'elenco delle fonti di font specificate. Nel caso in cui non siano state impostate fonti, il file**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**metodo restituirà un array vuoto.
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** Il metodo accetta un parametro di tipo**corda** permettendo di specificare il nome del carattere per il quale è stata impostata la sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del carattere specificato, il file**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**il metodo restituirà null.

## **Argomenti avanzati**
- [Imposta il carattere predefinito durante il rendering del foglio di calcolo sulle immagini](/cells/it/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions in modo che abbia la priorità](/cells/it/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formati di carattere supportati](/cells/it/net/supported-font-formats/)
- [Da foglio di lavoro a immagine: imposta il formato pixel per l'immagine di rendering](/cells/it/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
