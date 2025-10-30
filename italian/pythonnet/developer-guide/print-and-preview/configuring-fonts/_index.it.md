---
title: Configurazione dei Font per la Visualizzazione dei Fogli di Lavoro
type: docs
weight: 10
url: /it/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells per Python via .NET offrono la possibilità di rappresentare i fogli di calcolo in formati immagine e di convertirli in formati PDF & XPS. Per massimizzare l'accuratezza della conversione, è necessario che i caratteri usati nel foglio di calcolo siano disponibili nella directory dei font di default del sistema operativo. Se i font richiesti non sono presenti, le API di Aspose.Cells per Python via .NET cercheranno di sostituirli con quelli disponibili.

## **Selezione dei font**

Di seguito è descritto il processo seguito dalle API di Aspose.Cells per Python via .NET dietro le quinte.

1. L'API cerca di trovare i font nel file system corrispondenti al nome esatto del font utilizzato nel foglio di calcolo.
1. Se l'API non riesce a trovare i font con lo stesso nome esatto, tenta di utilizzare il font predefinito specificato nella proprietà [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) del foglio di lavoro.
1. Se l'API non riesce a individuare il font definito nella proprietà [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) del foglio di lavoro, tenta di utilizzare il font specificato nelle proprietà [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) o [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font).
1. Se l'API non riesce a individuare il font definito nelle proprietà [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) o [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font), tenta di utilizzare il font specificato nella proprietà [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name).
1. Se l'API non riesce a individuare il font definito nella proprietà [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name), tenta di selezionare i font più adatti tra tutti i font disponibili.
1. Infine, se l'API non riesce a trovare alcun font nel file system, renderizza il foglio di calcolo utilizzando Arial.

## **Impostazione delle cartelle dei font personalizzate**

Le API di Aspose.Cells per Python via .NET cercano i font necessari nella directory dei font predefinita del sistema operativo. Se i font richiesti non sono disponibili, le API cercano nelle directory personalizzate (definite dall'utente). La classe [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) ha diverse modalità per impostare directory di font personalizzate come descritto di seguito.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): Questo metodo è utile se c'è solo una cartella da impostare.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): Questo metodo è utile quando i font risiedono in più cartelle e l'utente desidera impostare tutte le cartelle separatamente anziché combinare tutti i font in una singola cartella.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): Questo meccanismo è utile quando l'utente desidera caricare i font da più cartelle o un singolo file font o dati font da un array di byte.

{{% alert color="primary" %}}

Entrambi i metodi [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) e [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) accettano un secondo parametro di tipo Boolean. Passare **true** come secondo parametro indirizza le API di Aspose.Cells per Python via .NET a cercare nei sottocartelle i file dei font.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Usa uno dei metodi sopra menzionati all’inizio dell’applicazione, prima di invocare altri oggetti di Aspose.Cells per Python via .NET.

{{% /alert %}} {{% alert color="primary" %}}

Se tutti i metodi sopra menzionati vengono utilizzati per impostare le origini dei font, solo le ultime impostazioni avranno effetto.

{{% /alert %}}

## **Meccanismo di sostituzione del font**

Le API di Aspose.Cells per Python via .NET offrono anche la possibilità di specificare un font sostitutivo per scopi di rendering. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina dove deve essere eseguita la conversione. Gli utenti possono fornire una lista di nomi di font come alternativa al font originale richiesto. Per ottenere questo, le API di Aspose.Cells per Python via .NET hanno esposto il metodo [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) che accetta due parametri. Il primo, di tipo **stringa**, è il nome del font da sostituire. Il secondo è un array di tipo **stringa**. Gli utenti possono fornire una lista di nomi di font come sostituzione del nome del font originale (specificato nel primo parametro).

Ecco uno scenario d'uso semplice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Raccolta informazioni**

Oltre ai metodi sopra citati, le API di Aspose.Cells per Python via .NET offrono anche strumenti per raccogliere informazioni sulle fonti e le sostituzioni impostate.

1. Il metodo [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) restituisce un array di tipo [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) contenente l'elenco delle fonti specificate. Nel caso in cui non siano state impostate fonti, il metodo [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) restituirà un array vuoto.
1. Il metodo [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) accetta un parametro di tipo **string** che consente di specificare il nome del carattere per il quale è stata impostata una sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del carattere specificato, il metodo [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) restituirà null.

## **Argomenti avanzati**
- [Imposta il carattere predefinito durante il rendering del foglio elettronico in immagini](/cells/it/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Imposta la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per dare priorità](/cells/it/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formati di carattere supportati](/cells/it/python-net/supported-font-formats/)
- [Foglio elettronico in immagine - Imposta il formato pixel per l'immagine renderizzata](/cells/it/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

{{< app/cells/assistant language="python-net" >}}
