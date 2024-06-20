---
title: Impostazioni del carattere
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Supporta l impostazione delle impostazioni del carattere delle celle, consentendo agli utenti di personalizzare lo stile e le proprietà del carattere delle celle. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per impostare le impostazioni del carattere delle celle.
keywords: Aspose.Cells, Celle, Impostazioni del Carattere, Stili, Proprietà
type: docs
weight: 30
url: /it/net/cells-font-settings/
---

{{% alert color="primary" %}}

L'aspetto di un testo può essere controllato modificando le impostazioni del carattere. Le impostazioni del carattere possono includere il nome, lo stile, le dimensioni, il colore e altri effetti dei font. Proprio come Microsoft Excel, Aspose.Cells supporta anche la configurazione delle impostazioni del carattere delle celle.

{{% /alert %}}

## **Configurazione delle Impostazioni del Carattere**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ciascun elemento nella collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) e [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) utilizzati per ottenere e impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fornisce proprietà per configurare le impostazioni del carattere.

### **Impostazione del nome del carattere**

Gli sviluppatori possono applicare qualsiasi carattere al testo all'interno di una cella utilizzando la proprietà [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Impostare lo stile del carattere su Grassetto**

Gli sviluppatori possono rendere il testo in grassetto impostando la proprietà [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) su **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Impostazione della dimensione del carattere**

Imposta la dimensione del carattere con la proprietà [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Impostazione del colore del carattere**

Utilizzare la proprietà [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) per impostare il colore del carattere. Selezionare qualsiasi colore dall'enumerazione Color (parte del framework .NET) e assegnarlo alla proprietà [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Impostazione del tipo sottolineato del carattere**

Utilizzare la proprietà [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) per sottolineare il testo. Aspose.Cells offre vari tipi predefiniti di sottolineatura nel'enumerazione [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype).

|**Tipi di sottolineatura del carattere**|**Descrizione**|
| :- | :- |
|Accounting|Un solo sottolineatura contabile|
|Double|Doppia sottolineatura|
|DoubleAccounting|Doppia sottolineatura contabile|
|None|Nessuna sottolineatura|
|Single|Una singola sottolineatura|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Impostazione dell'effetto barrato**

Applicare il barrato impostando la proprietà [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) su **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Impostazione dell'effetto pedice**

Applica il pedice impostando la proprietà [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) su **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Impostazione dell'effetto esponente sulla font**

I programmatori possono applicare l'effetto esponente sulla font impostando la proprietà [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) dell'oggetto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) su **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Argomenti avanzati**
- [Applica gli effetti esponente e pedice sulle font](/cells/it/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro](/cells/it/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

