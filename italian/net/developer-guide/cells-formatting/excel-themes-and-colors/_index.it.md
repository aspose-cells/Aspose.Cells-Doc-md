---
title: Temi e colori di Excel
type: docs
weight: 100
url: /it/net/excel-themes-and-colors/
---
## **Temi e colori di Excel**

temi forniscono un aspetto unificato con stili con nome, effetti grafici e altri oggetti utilizzati in una cartella di lavoro. Ad esempio, lo stile Accent1, ad esempio, ha un aspetto diverso nei temi Office e Apex. Spesso si applica un tema del documento e poi lo si modifica nel modo desiderato.

Aspose.Cells fornisce funzionalità per la personalizzazione di temi e colori.

### **Ottenere e impostare i colori del tema**

Di seguito sono riportati alcuni metodi e proprietà che implementano i colori del tema.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Utilizzato per impostare il colore di primo piano.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Utilizzato per impostare il colore di sfondo.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Utilizzato per impostare il colore del carattere.
- [**Cartella di lavoro.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Utilizzato per ottenere un colore del tema.
- [**Cartella di lavoro.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Utilizzato per impostare un colore del tema.

L'esempio seguente mostra come ottenere e impostare i colori del tema.

L'esempio seguente utilizza un file modello XLSX, ottiene i colori per diversi tipi di colore del tema, modifica i colori e salva il file Excel Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **Personalizza i temi**

L'esempio seguente mostra come applicare temi personalizzati con i colori desiderati. Utilizziamo un file modello di esempio creato manualmente in Microsoft Excel 2007.

L'esempio seguente carica un file modello XLSX, definisce i colori per i diversi tipi di colore del tema, applica i colori personalizzati e salva il file excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **Usa i colori del tema**

L'esempio seguente applica i colori di primo piano e dei caratteri di una cella in base ai tipi di colore del tema predefinito (della cartella di lavoro). Salva anche il file excel su disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

## **Argomenti avanzati**
- [Estrai i dati del tema dal file Excel](/cells/it/net/extract-theme-data-from-excel-file/)
