---
title: Impostazioni dei caratteri
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Supporta l'impostazione delle impostazioni del carattere delle celle, consentendo agli utenti di personalizzare lo stile del carattere e le proprietà delle celle. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per configurare le impostazioni dei caratteri della cella.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /it/net/cells-font-settings/
---
{{% alert color="primary" %}}

L'aspetto di un testo può essere controllato modificando le impostazioni del carattere. Le impostazioni dei caratteri possono includere nome, stile, dimensione, colore e altri effetti dei caratteri. Proprio come Microsoft Excel, anche Aspose.Cells supporta la configurazione delle impostazioni dei caratteri delle celle.

{{% /alert %}}

##  **Configurazione delle impostazioni dei caratteri**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fornisce il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe'[**Ottieni Stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) E[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metodi utilizzati per ottenere e impostare lo stile di formattazione di una cella. IL[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fornisce proprietà per la configurazione delle impostazioni dei caratteri.

###  **Impostazione del nome del carattere**

 Gli sviluppatori possono applicare qualsiasi carattere al testo all'interno di una cella utilizzando il file[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[Nome](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **Impostazione dello stile del carattere su Grassetto**

 Gli sviluppatori possono rendere il testo in grassetto impostando il file[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[**È grassetto**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)proprietà su *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **Impostazione della dimensione del carattere**

Imposta la dimensione del carattere con[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)dell'oggetto[**Misurare**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **Impostazione del colore del carattere**

Usa il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[**Colore**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)proprietà per impostare il colore del carattere. Seleziona un colore qualsiasi dall'enumerazione Color (parte del framework .NET) e assegnalo a[**Colore**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **Impostazione del tipo di sottolineatura del carattere**

Usa il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)dell'oggetto[**Sottolineare**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)proprietà per sottolineare il testo. Aspose.Cells offre vari tipi di sottolineatura di caratteri predefiniti nel file[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) enumerazione.

|**Tipi di sottolineatura dei caratteri**|**Descrizione**|
| :- | :- |
|Contabilità|Un'unica sottolineatura contabile|
|Doppio|Doppia sottolineatura|
|Doppia contabilità|Doppia sottolineatura contabile|
|Nessuno|Nessuna sottolineatura|
|Separare|Una sola sottolineatura|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **Impostazione dell'effetto barrato**

Applicare la barratura impostando il file[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[**È Strikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)proprietà su *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **Impostazione dell'effetto dell'indice**

Applicare l'indice impostando il file[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)dell'oggetto[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)proprietà su *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **Impostazione dell'effetto apice sul carattere**

 Gli sviluppatori possono applicare l'effetto apice sul carattere impostando il file[**È apice**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) proprietà del[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)obiettare a *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **Argomenti avanzati**
- [Applica effetti di apice e pedice sui caratteri](/cells/it/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di caratteri utilizzati in un foglio di calcolo o in una cartella di lavoro](/cells/it/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

