---
title: Configurazione dei Font per la Visualizzazione dei Fogli di Lavoro
type: docs
weight: 10
url: /it/net/configuring-fonts-for-rendering-spreadsheets/
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells forniscono la possibilità di rendere i fogli di calcolo in formati di immagine e di convertirli in formati PDF e XPS. Per massimizzare la fedeltà della conversione, è necessario che i font utilizzati nel foglio di calcolo siano disponibili nella directory predefinita dei font del sistema operativo. Nel caso in cui i font richiesti non siano presenti, le API di Aspose.Cells cercheranno di sostituire i font richiesti con quelli disponibili.

## **Selezione dei font**

Di seguito il processo che le API di Aspose.Cells seguono dietro le quinte.

1. L'API cerca di trovare i font nel file system corrispondenti al nome esatto del font utilizzato nel foglio di calcolo.
1. Se l'API non riesce a trovare i font con lo stesso nome esatto, tenta di utilizzare il font predefinito specificato nella proprietà [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) del foglio di lavoro.
1. Se l'API non riesce a individuare il font definito nella proprietà [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) del foglio di lavoro, tenta di utilizzare il font specificato nelle proprietà [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont).
1. Se l'API non riesce a individuare il font definito nelle proprietà [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont), tenta di utilizzare il font specificato nella proprietà [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname).
1. Se l'API non riesce a individuare il font definito nella proprietà [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname), tenta di selezionare i font più adatti tra tutti i font disponibili.
1. Infine, se l'API non riesce a trovare alcun font nel file system, renderizza il foglio di calcolo utilizzando Arial.

{{% alert color="primary" %}}

In generale, le API di Aspose.Cells esaminano le directory di caratteri predefinite del sistema operativo su Windows, Linux, MacOS per impostazione predefinita. A partire da [Aspose.Cells for .NET 24.7](https://releases.aspose.com/cells/net/release-notes/2024/aspose-cells-for-net-24-7-release-notes/), le API esaminano inoltre le directory di caratteri cache di Office nel cloud per impostazione predefinita.

{{% /alert %}}

## **Impostazione delle cartelle dei font personalizzate**

Le API di Aspose.Cells cercano nella directory predefinita dei font del sistema operativo i font richiesti. Nel caso in cui i font richiesti non siano disponibili nella directory dei font del sistema, le API cercano attraverso le directory personalizzate (definite dall'utente). La classe [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) ha esposto una serie di modi per impostare le directory dei font personalizzate come dettagliato di seguito.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): Questo metodo è utile se c'è solo una cartella da impostare.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): Questo metodo è utile quando i font risiedono in più cartelle e l'utente desidera impostare tutte le cartelle separatamente anziché combinare tutti i font in una singola cartella.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): Questo meccanismo è utile quando l'utente desidera caricare i font da più cartelle o un singolo file font o dati font da un array di byte.

{{% alert color="primary" %}}

Sia i metodi [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) che [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) accettano un secondo parametro di tipo Boolean. Passare **true** come secondo parametro indirizzerà le API di Aspose.Cells a cercare i file dei font nelle sottocartelle.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Si prega di utilizzare uno qualsiasi dei metodi sopra menzionati all'inizio dell'applicazione, cioè; prima di invocare altri oggetti delle API di Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Se tutti i metodi sopra menzionati vengono utilizzati per impostare le origini dei font, solo le ultime impostazioni avranno effetto.

{{% /alert %}}

## **Meccanismo di sostituzione del font**

Le API di Aspose.Cells forniscono anche la possibilità di specificare il font sostitutivo per scopi di rendering. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina dove deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di font come alternativa al font originariamente richiesto. Per ottenere questo, le API di Aspose.Cells hanno esposto il metodo [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes) che accetta 2 parametri. Il primo parametro è di tipo **string**, che dovrebbe essere il nome del font da sostituire. Il secondo parametro è un array di tipo **string**. Gli utenti possono fornire un elenco di nomi di font come sostituzione al nome del font originale (specificato nel primo parametro).

Ecco uno scenario d'uso semplice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Raccolta informazioni**

Oltre ai metodi sopra menzionati, le API Aspose.Cells forniscono anche mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. Il metodo [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) restituisce un array di tipo [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) contenente l'elenco delle fonti specificate. Nel caso in cui non siano state impostate fonti, il metodo [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) restituirà un array vuoto.
1. Il metodo [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) accetta un parametro di tipo **string** che consente di specificare il nome del carattere per il quale è stata impostata una sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del carattere specificato, il metodo [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) restituirà null.

## **Argomenti avanzati**
- [Imposta il carattere predefinito durante il rendering del foglio elettronico in immagini](/cells/it/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Imposta la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per dare priorità](/cells/it/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formati di carattere supportati](/cells/it/net/supported-font-formats/)
- [Foglio elettronico in immagine - Imposta il formato pixel per l'immagine renderizzata](/cells/it/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="csharp" >}}
