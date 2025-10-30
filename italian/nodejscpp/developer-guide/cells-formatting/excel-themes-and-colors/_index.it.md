---  
title: Temi e Colori di Excel
linktitle: Temi e Colori di Excel  
type: docs  
weight: 100  
url: /it/nodejs-cpp/excel-themes-and-colors/  
description: Impara come usare schemi di colori personalizzati con Aspose.Cells for Node.js via C++.  
keywords: Creazione e applicazione di Schemi di Colori in Node.js, Creare programmaticamente uno schema di colore personalizzato in Node.js, come applicare programmaticamente uno schema di colore personalizzato in Node.js, Come usare lo schema di colore in Excel con Node.js  
---  

## **Come Applicare e Creare uno Schema Colori in Excel**  
I temi del documento facilitano il coordinamento dei colori, dei caratteri e degli effetti di formattazione grafica dei documenti di Excel e consentono di aggiornarli rapidamente.  
I temi offrono un aspetto unificato con stili nominati, effetti grafici e altri oggetti utilizzati in un workbook. Ad esempio, lo stile Accent1 appare diverso nei temi Office e Apex. Spesso, si applica un tema al documento e poi lo si modifica secondo le preferenze.  

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

## **Come creare e applicare un set di colori in Aspose.Cells**  
Aspose.Cells offre funzionalità per personalizzare temi e colori.  

### **Come creare un tema di colori personalizzato in Aspose.Cells**  
Se nel file sono utilizzati i colori del tema, non è necessario modificare ogni cella singolarmente; basta modificare i colori nel tema.  

Nell'esempio seguente viene mostrato come applicare temi personalizzati con i colori desiderati. Utilizziamo un file modello creato manualmente in Microsoft Excel 2007.  

Il seguente esempio carica un file modello XLSX, definisce i colori per diversi tipi di colore del tema, applica i colori personalizzati e salva il file Excel.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **Come applicare colori tema in Aspose.Cells**  
Il seguente esempio applica i colori di primo piano e di carattere di una cella in base ai tipi di colore predefiniti del tema (del workbook). Salva anche il file Excel su disco.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **Come ottenere e impostare colori tema in Aspose.Cells**  
Di seguito sono riportati alcuni metodi e proprietà che implementano i colori tema.  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-): Usato per impostare il colore di primo piano.  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-): Usato per impostare il colore di sfondo.  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-): Usato per impostare il colore del font.  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-): Usato per ottenere un colore del tema.  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-): Usato per impostare un colore del tema.  

L'esempio seguente mostra come ottenere e impostare i colori del tema.  

Il seguente esempio utilizza un file modello XLSX, ottiene i colori per diversi tipi di colore del tema, modifica i colori e salva il file Microsoft Excel.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **Argomenti avanzati**  
- [Estrai dati tema dal file Excel](/cells/it/nodejs-cpp/extract-theme-data-from-excel-file/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
