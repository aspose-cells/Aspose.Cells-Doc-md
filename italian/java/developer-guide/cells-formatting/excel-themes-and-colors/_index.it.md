---
title: Temi e colori di Excel
type: docs
weight: 130
url: /it/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

I temi forniscono un aspetto unificato con stili con nome, effetti grafici e altri oggetti utilizzati in una cartella di lavoro. Ad esempio, lo stile Accent1 ha un aspetto diverso nei temi Office e Apex. Spesso applichi un tema del documento e poi lo modifichi in base alle tue esigenze.

**Applicazione di temi in Microsoft Excel**

![cose da fare:immagine_alt_testo](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Ottenere e impostare i colori del tema**

Le API Aspose.Cells forniscono funzionalità per la personalizzazione di temi e colori. Di seguito sono riportati alcuni metodi e proprietà che implementano i colori del tema.

- La proprietà Style.ForegroundThemeColor può essere utilizzata per impostare il colore di primo piano.
- La proprietà Style.BackgroundThemeColor può essere utilizzata per impostare il colore di sfondo.
- La proprietà Font.ThemeColor può essere utilizzata per impostare il colore del carattere.
- Il metodo Workbook.getThemeColor può essere utilizzato per ottenere un colore del tema.
- Il metodo Workbook.setThemeColor può essere utilizzato per impostare un colore del tema.

L'esempio seguente mostra come ottenere e impostare i colori del tema.

L'esempio seguente utilizza un file XLSX modello, ottiene i colori per i diversi tipi di colore del tema, modifica i colori e salva il file Excel Microsoft.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Personalizzazione dei temi**

L'esempio seguente mostra come applicare temi personalizzati con i colori desiderati. L'esempio utilizza un file modello di esempio creato manualmente in Microsoft Excel 2007.

**Il file CustomThemeColor.xlsx del modello**

![cose da fare:immagine_alt_testo](excel-2007-themes-and-colors_2.png)

L'esempio seguente carica un file XLSX modello, definisce i colori per i diversi tipi di colore del tema, applica i colori personalizzati e salva il file excel.

**Il file generato con i colori del tema personalizzati**

![cose da fare:immagine_alt_testo](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Utilizzo dei colori del tema**

L'esempio seguente applica i colori di primo piano e dei caratteri di una cella in base ai tipi di colore del tema predefinito (della cartella di lavoro). Salva anche il file excel su disco.

Il seguente output viene generato durante l'esecuzione del codice.

**I colori del tema applicati alla cella D3 del foglio di lavoro** 

![cose da fare:immagine_alt_testo](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Argomenti avanzati**
- [Estrai i dati del tema dal file Excel](/cells/it/java/extract-theme-data-from-excel-file/)
