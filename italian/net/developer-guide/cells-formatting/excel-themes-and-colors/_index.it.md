---
title: Temi e colori di Excel
type: docs
weight: 100
url: /it/net/excel-themes-and-colors/
description: Codice C# per utilizzare lo schema colori Excel con Aspose.Cells for .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **Come applicare e creare una combinazione di colori in Excel**
 temi dei documenti semplificano il coordinamento dei colori, dei caratteri e degli effetti di formattazione grafica dei documenti Excel e li aggiornano rapidamente.
I temi forniscono un aspetto unificato con stili con nome, effetti grafici e altri oggetti utilizzati in una cartella di lavoro. Ad esempio, lo stile Accent1 ha un aspetto diverso nei temi Office e Apex. Spesso si applica un tema al documento e quindi lo si modifica nel modo desiderato.

###  **Come applicare una combinazione di colori in Excel**
1. Apri Excel e vai alla scheda "Layout di pagina" nella barra multifunzione di Excel.
1. Fare clic sul pulsante "Colori" nella sezione "Temi".
<br>
<img src="color.png" width=70% />
1. Scegli una tavolozza di colori che corrisponda alle tue esigenze o passa il mouse sopra uno schema per vedere un'anteprima dal vivo.

###  **Come creare una combinazione di colori personalizzata in Excel**
Puoi creare il tuo set di colori per conferire al tuo documento un aspetto fresco e unico o conformarti agli standard del marchio della tua organizzazione.

1. Apri Excel e vai alla scheda "Layout di pagina" nella barra multifunzione di Excel.
1. Fare clic sul pulsante "Colori" nella sezione "Temi".
1. Fare clic sul pulsante "Personalizza colori...".
<br>
<img src="color2.png" width=70% />

1. Nella finestra di dialogo "Crea nuovi colori tema", puoi selezionare i colori per ciascun elemento facendo clic sui menu a discesa dei colori accanto ad essi. Puoi scegliere i colori dalla tavolozza o definire colori personalizzati utilizzando l'opzione "Altri colori".
<br>
<img src="color3.png" width=70% />
1. Dopo aver selezionato tutti i colori desiderati, fornisci un nome per la tua combinazione di colori personalizzata nel campo "Nome".

1. Fare clic sul pulsante "Salva" per salvare la combinazione di colori personalizzata. La tua combinazione di colori personalizzata sarà ora disponibile nel menu a discesa "Colori" per un utilizzo futuro.

##  **Come creare e applicare la combinazione di colori in Aspose.Cells**
Aspose.Cells fornisce funzionalità per la personalizzazione di temi e colori.

###  **Come creare un tema colore personalizzato in Aspose.Cells**
Se nel file vengono utilizzati i colori del tema, non è necessario modificare ciascuna cella individualmente, è sufficiente modificare i colori nel tema.

L'esempio seguente mostra come applicare temi personalizzati con i colori desiderati. Utilizziamo un file modello di esempio creato manualmente in Microsoft Excel 2007.

L'esempio seguente carica un file modello XLSX, definisce i colori per diversi tipi di colore del tema, applica i colori personalizzati e salva il file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **Come applicare i colori del tema in Aspose.Cells**

L'esempio seguente applica i colori di primo piano e dei caratteri di una cella in base ai tipi di colore del tema predefinito (della cartella di lavoro). Salva anche il file Excel su disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **Come ottenere e impostare i colori del tema in Aspose.Cells**
 Di seguito sono riportati alcuni metodi e proprietà che implementano i colori del tema.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Utilizzato per impostare il colore di primo piano.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Utilizzato per impostare il colore dello sfondo.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Utilizzato per impostare il colore del carattere.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Utilizzato per ottenere un colore del tema.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Utilizzato per impostare un colore del tema.

L'esempio seguente mostra come ottenere e impostare i colori del tema.

L'esempio seguente utilizza un file modello XLSX, ottiene i colori per diversi tipi di colore del tema, modifica i colori e salva il file Excel Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **Argomenti avanzati**
- [Estrai i dati del tema dal file Excel](/cells/it/net/extract-theme-data-from-excel-file/)
