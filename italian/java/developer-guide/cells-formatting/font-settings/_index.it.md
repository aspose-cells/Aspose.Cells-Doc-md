---
title: Gestione delle impostazioni dei caratteri
linktitle: Impostazioni carattere
type: docs
weight: 20
url: /it/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

L'aspetto del testo può essere controllato modificando le impostazioni del carattere. Queste impostazioni dei caratteri possono includere il nome, lo stile, la dimensione, il colore e altri effetti dei caratteri come mostrato di seguito nella figura:

**Impostazioni dei caratteri in Microsoft Excel** 

![cose da fare:immagine_alt_testo](dealing-with-font-settings_1.png)

Proprio come Microsoft Excel, Aspose.Cells supporta anche la configurazione delle impostazioni dei caratteri delle celle.

{{% /alert %}} 
## **Configurazione delle impostazioni dei caratteri**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. Ogni elemento del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 Aspose.Cells fornisce il[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ), utilizzato per impostare la formattazione di una cella. Inoltre, l'oggetto del[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class fornisce le proprietà per la configurazione delle impostazioni dei caratteri.

Questo articolo mostra come:

- [Applicare un carattere specifico al testo.](/cells/it/java/dealing-with-font-settings/)
- [Imposta il testo in grassetto](/cells/it/java/dealing-with-font-settings/).
- [Imposta la dimensione del carattere](/cells/it/java/dealing-with-font-settings/).
- [Imposta il colore del carattere](/cells/it/java/dealing-with-font-settings/).
- [Sottolineare il testo](/cells/it/java/dealing-with-font-settings/).
- [Testo barrato](/cells/it/java/dealing-with-font-settings/).
- [Imposta il testo in pedice](/cells/it/java/dealing-with-font-settings/).
- [Imposta il testo in apice](/cells/it/java/dealing-with-font-settings/).
### **Impostazione del nome del carattere**
 Applicare un carattere specifico al testo nelle celle utilizzando il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[imposta nome](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Impostazione dello stile del carattere su grassetto**
 Impostare il testo in grassetto impostando il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) proprietà a**VERO**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Impostazione della dimensione del carattere**
 Impostare la dimensione del carattere utilizzando il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Impostazione del tipo di sottolineatura del carattere**
 Sottolineare il testo con il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setSottolineato](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) proprietà. Aspose.Cells offre vari tipi di sottolineatura dei caratteri predefiniti nel file[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)enumerazione.

|**Tipi di caratteri sottolineati**|**Descrizione**|
|:- |:- |
|[NESSUNO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Nessuna sottolineatura|
|[SEPARARE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Una sola sottolineatura|
|[DOPPIO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Doppia sottolineatura|
|[CONTABILITÀ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Un'unica sottolineatura contabile|
|[DOPPIO_CONTO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Doppia sottolineatura contabile|
|[TRATTINO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Sottolineatura tratteggiata|
|[TRATTINO_PUNTO_PUNTO_PESANTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Sottolineatura tratteggiata-punto-punto spessa|
|[TRATTINO_PUNTO_PESANTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Spessa sottolineatura tratteggiata|
|[TRATTEGGIATO_PESANTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Sottolineatura tratteggiata spessa|
|[DASH_LUNGO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Sottolineatura tratteggiata lunga|
|[TRATTINO_LUNGO_PESANTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Spessa sottolineatura tratteggiata lunga|
|[PUNTO_LINEA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Tratto-punto sottolineato|
|[PUNTO_PUNTO_TRATTINO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Trattino-punto-punto sottolineato|
|[PUNTEGGIATO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Sottolineatura punteggiata|
|[PUNTEGGIATO_PESANTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Sottolineatura punteggiata spessa|
|[PESANTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Sottolineatura spessa|
|[ONDA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Onda sottolineata|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Sottolineatura a doppia onda|
|[ONDULATO_PESANTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Sottolineatura dell'onda pesante|
|` `[PAROLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Sottolinea solo caratteri diversi dallo spazio|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Impostazione del colore del carattere**
 Imposta il colore del carattere con il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) proprietà. Seleziona qualsiasi colore da[Colore](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enumerazione e assegnare il colore selezionato al file[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Impostazione dell'effetto barrato sul testo**
 Barrare il testo con il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setSbarramento](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Impostazione pedice**
 Rendi il testo in apice usando il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Impostazione apice**
 Applica l'apice al testo con il[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) dell'oggetto[setApice](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Argomenti avanzati**
- [Applicare effetti di apice e pedice sui caratteri](/cells/it/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di caratteri utilizzati in un foglio di calcolo o in una cartella di lavoro](/cells/it/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
