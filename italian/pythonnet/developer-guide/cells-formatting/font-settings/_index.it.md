---
title: Impostazioni del carattere
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo. Supporta la impostazione delle impostazioni del carattere delle celle, consentendo agli utenti di personalizzare lo stile e le proprietà delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per Python via .NET per impostare le impostazioni del carattere delle celle.
keywords: Aspose.Cells per Python via .NET, Celle, Impostazioni del caratte, Stili, Proprietà
type: docs
weight: 30
url: /it/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

L'aspetto e la sensazione di un testo possono essere controllati modificando le impostazioni del carattere. Le impostazioni del carattere possono includere il nome, lo stile, la dimensione, il colore e altri effetti dei font. Proprio come Microsoft Excel, Aspose.Cells per Python via .NET supporta anche la configurazione delle impostazioni del carattere delle celle.

{{% /alert %}}

## **Configurazione delle Impostazioni del Carattere**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente di accedere a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Ogni elemento nella raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells fornisce i metodi [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) e [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) utilizzati per ottenere e impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fornisce proprietà per configurare le impostazioni del carattere.

### **Impostazione del nome del carattere**

Gli sviluppatori possono applicare qualsiasi font al testo all’interno di una cella usando la proprietà [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) dell’oggetto [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **Impostare lo stile del carattere su Grassetto**

Gli sviluppatori possono rendere il testo in grassetto impostando la proprietà [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) dell'oggetto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) su **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **Impostazione della dimensione del carattere**

Imposta la dimensione del carattere con la proprietà [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size) dell'oggetto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **Impostazione del colore del carattere**

Utilizzare la proprietà [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) dell'oggetto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) per impostare il colore del carattere. Selezionare qualsiasi colore dall'enumerazione Color (parte del framework .NET) e assegnarlo alla proprietà [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **Impostazione del tipo sottolineato del carattere**

Usa la proprietà [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) dell’oggetto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) per sottolineare il testo. Aspose.Cells per Python via .NET offre vari tipi di sottolineatura predefiniti nella enumerazione [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype).

|**Tipi di sottolineatura del carattere**|**Descrizione**|
| :- | :- |
|ACCOUNTING| Sottolineatura contabile singola|
|DOUBLE| Doppia sottolineatura|
|DOUBLE_ACCOUNTING| Sottolineatura contabile doppia|
|NONE| Nessuna sottolineatura|
|SINGLE| Sottolineatura singola|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **Impostazione dell'effetto barrato**

Applicare il barrato impostando la proprietà [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) dell'oggetto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) su **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **Impostazione dell'effetto pedice**

Applica il pedice impostando la proprietà [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) dell'oggetto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) su **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **Impostazione dell'effetto esponente sulla font**

I programmatori possono applicare l'effetto esponente sulla font impostando la proprietà [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) dell'oggetto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) su **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **Argomenti avanzati**
- [Applica gli effetti esponente e pedice sulle font](/cells/it/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro](/cells/it/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


