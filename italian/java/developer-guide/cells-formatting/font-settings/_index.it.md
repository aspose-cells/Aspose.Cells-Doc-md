---
title: Gestione delle Impostazioni del Font
linktitle: Impostazioni del carattere
type: docs
weight: 20
url: /it/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

L'aspetto del testo può essere controllato modificando le impostazioni del carattere. Queste impostazioni del carattere possono includere il nome, lo stile, la dimensione, il colore e altri effetti dei font come mostrato di seguito nella figura:

Impostazioni del carattere in Microsoft Excel 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Proprio come Microsoft Excel, anche Aspose.Cells supporta la configurazione delle impostazioni del carattere delle celle.

{{% /alert %}} 
## **Configurazione delle Impostazioni del Carattere**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file di Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente di accedere a ciascun foglio di lavoro in un file di Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ogni elemento nella raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells fornisce il metodo [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) utilizzato per impostare la formattazione di una cella. Inoltre, l'oggetto della classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) fornisce proprietà per configurare le impostazioni del carattere.

Questo articolo mostra come:

- [Applicare un font specifico al testo.](/cells/it/java/dealing-with-font-settings/)
- [Impostare il testo in grassetto](/cells/it/java/dealing-with-font-settings/).
- [Impostare la dimensione del font](/cells/it/java/dealing-with-font-settings/).
- [Impostare il colore del font](/cells/it/java/dealing-with-font-settings/).
- [Sottolineare il testo](/cells/it/java/dealing-with-font-settings/).
- [Barrare il testo](/cells/it/java/dealing-with-font-settings/).
- [Impostare il testo come pedice](/cells/it/java/dealing-with-font-settings/).
- [Impostare il testo come apice](/cells/it/java/dealing-with-font-settings/).
### **Impostazione del nome del carattere**
Applicare un font specifico al testo nelle celle utilizzando la proprietà [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) dell'oggetto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Impostare lo stile del carattere su Grassetto**
Imposta il testo in grassetto impostando la proprietà [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) dell'oggetto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) a **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Impostazione della dimensione del carattere**
Imposta la dimensione del carattere utilizzando la proprietà [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) dell'oggetto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Impostazione del tipo sottolineato del carattere**
Sottolinea il testo utilizzando la proprietà [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) dell'oggetto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font). Aspose.Cells offre vari tipi predefiniti di sottolineatura del carattere nella enumerazione [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType).

|**Tipi di sottolineatura del carattere**|**Descrizione**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Nessun sottolineatura|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Un singolo sottolineatura|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Doppio sottolineatura|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Un singolo sottolineatura contabile|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Doppio sottolineatura contabile|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Sottolineatura tratteggiata|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Sottolineatura spessa a trattino-punto-punto|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Sottolineatura spessa a tratino-punto|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Sottolineatura spessa tratteggiata|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Sottolineatura lunga trattata|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Sottolineatura spessa lunga trattata|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Sottolineatura trattino-punto|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Trattino-Punto-Punto Sottolineato|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Sottolineato a Puntini|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Sottolineato Spesso a Puntini|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Sottolineatura spessa|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Ondulato sottolineatura|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Doppia ondulato sottolineatura|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Ondulato pesante sottolineatura|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Sottolinea solo caratteri non spazio|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Impostazione del colore del carattere**
Imposta il colore del font con la proprietà [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)'s [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color). Seleziona un colore qualsiasi dall'enumerazione [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) e assegna il colore selezionato alla proprietà [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)'s [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Impostazione dell'effetto barrato sul testo**
Barrare il testo con la proprietà [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)'s [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Impostazione del pedice**
Rendi il testo in apice utilizzando la proprietà [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)'s [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Impostazione del pedice**
Applica il pedice al testo con la proprietà [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)'s [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Argomenti avanzati**
- [Applica gli effetti esponente e pedice sulle font](/cells/it/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro](/cells/it/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
