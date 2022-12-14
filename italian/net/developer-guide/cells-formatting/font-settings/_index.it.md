---
title: Impostazioni carattere
type: docs
weight: 30
url: /it/net/cells-font-settings/
---
{{% alert color="primary" %}}

L'aspetto di un testo può essere controllato modificando le impostazioni dei caratteri. Le impostazioni dei caratteri possono includere il nome, lo stile, la dimensione, il colore e altri effetti dei caratteri. Proprio come Microsoft Excel, Aspose.Cells supporta anche la configurazione delle impostazioni dei caratteri delle celle.

{{% /alert %}}

## **Configurazione delle impostazioni dei caratteri**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione rappresenta un oggetto della[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fornisce il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**Ottieni stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) e[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metodi utilizzati per ottenere e impostare lo stile di formattazione di una cella. Il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)class fornisce le proprietà per la configurazione delle impostazioni dei caratteri.

### **Impostazione del nome del carattere**

 Gli sviluppatori possono applicare qualsiasi tipo di carattere al testo all'interno di una cella utilizzando il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[Nome](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Impostazione dello stile del carattere su grassetto**

 Gli sviluppatori possono rendere il testo in grassetto impostando l'estensione[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[**È audace**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) proprietà a**VERO**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Impostazione della dimensione del carattere**

Imposta la dimensione del carattere con il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)dell'oggetto[**Dimensione**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Impostazione del colore del carattere**

Utilizzare il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[**Colore**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)proprietà per impostare il colore del carattere. Selezionare qualsiasi colore dall'enumerazione Color (parte del framework .NET) e assegnarlo al[**Colore**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Impostazione del tipo di sottolineatura del carattere**

Utilizzare il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)dell'oggetto[**Sottolineare**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)proprietà per sottolineare il testo. Aspose.Cells offre vari tipi di sottolineatura dei caratteri predefiniti nel file[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) enumerazione.

|**Tipi di caratteri sottolineati**|**Descrizione**|
|:- |:- |
|Contabilità|Un'unica sottolineatura contabile|
|Doppio|Doppia sottolineatura|
|Doppia Contabilità|Doppia sottolineatura contabile|
|Nessuno|Nessuna sottolineatura|
|Separare|Una sola sottolineatura|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Impostazione dell'effetto barrato**

Applicare barrato impostando il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) dell'oggetto[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)proprietà a**VERO**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Impostazione dell'effetto pedice**

Applicare pedice impostando il[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)dell'oggetto[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) proprietà a**VERO**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Impostazione dell'effetto apice sul carattere**

 Gli sviluppatori possono applicare l'effetto apice sul carattere impostando il[**IsApice**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) proprietà del[**Stile.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) opporsi a**VERO**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Argomenti avanzati**
- [Applicare effetti di apice e pedice sui caratteri](/cells/it/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di caratteri utilizzati in un foglio di calcolo o in una cartella di lavoro](/cells/it/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

