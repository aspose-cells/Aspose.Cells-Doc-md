---
title: Temi e Colori di Excel
type: docs
weight: 130
url: /it/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

I temi forniscono un aspetto unificato con stili nominati, effetti grafici e altri oggetti utilizzati in un foglio di calcolo. Ad esempio, lo stile Accent1 appare diverso nei temi Office e Apex. Spesso si applica un tema del documento e quindi lo si modifica secondo le proprie esigenze.

**Applicazione dei temi in Microsoft Excel**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Ottieni e Imposta i Colori del Tema**

Le API di Aspose.Cells forniscono funzionalità per personalizzare temi e colori. Di seguito sono riportati alcuni metodi e proprietà che implementano i colori del tema.

- La proprietà Style.ForegroundThemeColor può essere utilizzata per impostare il colore primo piano.
- La proprietà Style.BackgroundThemeColor può essere utilizzata per impostare il colore di sfondo.
- La proprietà Font.ThemeColor può essere utilizzata per impostare il colore del font.
- Il metodo Workbook.getThemeColor può essere utilizzato per ottenere un colore del tema.
- Il metodo Workbook.setThemeColor può essere utilizzato per impostare un colore del tema.

L'esempio seguente mostra come ottenere e impostare i colori del tema.

L'esempio seguente utilizza un file XLSX di modello, ottiene i colori per diversi tipi di colori del tema, cambia i colori e salva il file Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Personalizzazione dei Temi**

L'esempio seguente mostra come applicare temi personalizzati con i colori desiderati. L'esempio utilizza un file di modello di esempio creato manualmente in Microsoft Excel 2007.

**Il file di modello CustomThemeColor.xlsx**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

Nell'esempio seguente viene caricato un file XLSX modello, vengono definiti colori per diversi tipi di colori tema, vengono applicati i colori personalizzati e viene salvato il file excel.

**Il file generato con i colori del tema personalizzati**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Utilizzo dei Colori del Tema**

Nell'esempio seguente vengono applicati i colori di primo piano e del testo di una cella in base ai tipi di colore tema predefiniti (del foglio di lavoro). Viene inoltre salvato il file excel su disco.

L'output seguente viene generato durante l'esecuzione del codice.

**I colori del tema applicati alla cella D3 del foglio di lavoro** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Argomenti avanzati**
- [Estrai dati tema dal file Excel](/cells/it/java/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="java" >}}
