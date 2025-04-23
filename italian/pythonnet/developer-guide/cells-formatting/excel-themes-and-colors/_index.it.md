---
title: Temi e Colori di Excel
type: docs
weight: 100
url: /it/python-net/excel-themes-and-colors/
description: Codice C# per usare la Scheda Colori di Excel con l’API Aspose.Cells per Python via .NET
keywords: C# per Creare e Applicare Schemi Colori, c# Creare un Schema Colori Personalizzato tramite programmazione, procedura dettagliata su come Applicare un Schema Colori Personalizzato, c# come Utilizzare uno Schema Colori in excel
---

## **Come Applicare e Creare uno Schema Colori in Excel**
I temi del documento facilitano il coordinamento dei colori, dei caratteri e degli effetti di formattazione grafica dei documenti di Excel e consentono di aggiornarli rapidamente. 
I temi forniscono un aspetto unificato con stili denominati, effetti grafici e altri oggetti utilizzati in un documento di lavoro. Ad esempio, lo stile Accent1, ad esempio, appare diverso nei temi Office e Apex. Spesso si applica un tema del documento e quindi lo si modifica a proprio piacimento.

### **Come Applicare uno Schema Colori in Excel**
1. Apri Excel e vai alla scheda "Layout di pagina" nel nastro di Excel.
1. Fai clic sul pulsante "Colori" nella sezione "Temi".
<br>
<img src="color.png" width=70% />
1. Scegli una combinazione di colori che corrisponda alle tue esigenze o passa il mouse su uno schema per vedere un'anteprima in tempo reale.

### **Come creare un set di colori personalizzato in Excel**
Puoi creare il tuo set di colori per dare al tuo documento un aspetto fresco e unico o per conformarti agli standard del marchio della tua organizzazione.

1. Apri Excel e vai alla scheda "Layout di pagina" nel nastro di Excel.
1. Fai clic sul pulsante "Colori" nella sezione "Temi".
1. Fai clic sul pulsante "Personalizza colori...".
<br>
<img src="color2.png" width=70% />

1. Nella finestra di dialogo "Crea nuovi colori tema", puoi selezionare i colori per ciascun elemento facendo clic sul menù a discesa accanto ad essi. Puoi scegliere i colori dalla palette o definire colori personalizzati utilizzando l'opzione "Altri colori".
<br>
<img src="color3.png" width=70% />
1. Dopo aver selezionato tutti i colori desiderati, fornisci un nome per il tuo set di colori personalizzato nel campo "Nome".

1. Fai clic sul pulsante "Salva" per salvare il tuo set di colori personalizzato. Il tuo set di colori personalizzato sarà ora disponibile nel menù a discesa "Colori" per un uso futuro.

## **Come creare e applicare uno schema di colori in Aspose.Cells per Python via .NET**
Aspose.Cells per Python via .NET offre funzionalità per personalizzare temi e colori.

### **Come creare un tema di colore personalizzato in Aspose.Cells per Python via .NET**
Se vengono utilizzati colori del tema nel file, non è necessario modificare ogni cella singolarmente, è sufficiente modificare i colori nel tema.

Nell'esempio seguente viene mostrato come applicare temi personalizzati con i colori desiderati. Utilizziamo un file modello creato manualmente in Microsoft Excel 2007.

Nell'esempio seguente viene caricato un file XLSX modello, vengono definiti colori per diversi tipi di colori tema, vengono applicati i colori personalizzati e viene salvato il file excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomizeThemes-1.py" >}}

### **Come applicare i colori dei temi in Aspose.Cells per Python via .NET**

Nell'esempio seguente vengono applicati i colori di primo piano e del testo di una cella in base ai tipi di colore tema predefiniti (del foglio di lavoro). Viene inoltre salvato il file excel su disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UtilizeThemeColors-1.py" >}}

### **Come ottenere e impostare i colori del tema in Aspose.Cells per Python via .NET**
 Di seguito sono riportati alcuni metodi e proprietà che implementano i colori tema.

- [**Style.foreground_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_theme_color): Utilizzato per impostare il colore del primo piano.
- [**Style.background_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_theme_color): Utilizzato per impostare il colore di sfondo.
- [**Font.theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/theme_color): Utilizzato per impostare il colore del testo.
- [**Workbook.get_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_theme_color): Utilizzato per ottenere un colore del tema.
- [**Workbook.set_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/set_theme_color): Utilizzato per impostare un colore del tema.

L'esempio seguente mostra come ottenere e impostare i colori del tema.

L'esempio seguente utilizza un file XLSX di modello, ottiene i colori per diversi tipi di colori del tema, cambia i colori e salva il file Microsoft Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetSetThemeColors-1.py" >}}

## **Argomenti avanzati**
- [Estrai dati tema dal file Excel](/cells/it/python-net/extract-theme-data-from-excel-file/)

