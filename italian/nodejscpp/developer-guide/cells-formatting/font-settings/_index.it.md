---  
title: Impostazioni del font con Node.js tramite C++  
linktitle: Impostazioni del carattere  
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo. Supporta la configurazione delle impostazioni dei font delle celle, consentendo agli utenti di personalizzare lo stile e le proprietà del font delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per impostare le impostazioni del font delle celle.  
keywords: Aspose.Cells, Celle, Impostazioni Font, Stili, Proprietà, Node.js tramite C++  
type: docs  
weight: 30  
url: /it/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
L'aspetto di un testo può essere controllato modificando le impostazioni del carattere. Le impostazioni del carattere possono includere il nome, lo stile, le dimensioni, il colore e altri effetti dei font. Proprio come Microsoft Excel, Aspose.Cells supporta anche la configurazione delle impostazioni del carattere delle celle.  
{{% /alert %}}  

## **Configurazione delle Impostazioni del Carattere**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ogni elemento nella raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells fornisce i metodi [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).[**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) e [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).[**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) che vengono usati per ottenere e impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) fornisce proprietà per la configurazione delle impostazioni di font.  

### **Impostazione del nome del carattere**  

Gli sviluppatori possono applicare qualsiasi font al testo all’interno di una cella usando il metodo [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Impostare lo stile del carattere su Grassetto**  

Gli sviluppatori possono rendere il testo in grassetto impostando il metodo [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) su **true**.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Impostazione della dimensione del carattere**  

Imposta la dimensione del font con il metodo [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Impostazione del colore del carattere**  

Usa il metodo [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) per impostare il colore del font. Seleziona un colore dall’enumerazione Color (parte di Node.js) e assegnalo al metodo [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Impostazione del tipo sottolineato del carattere**  

Usa il metodo [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) per sottolineare il testo. Aspose.Cells offre vari tipi di sottolineatura predefiniti nella enumerazione [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype).  

|**Tipi di sottolineatura del carattere**|**Descrizione**|  
| :- | :- |  
|Accounting|Un solo sottolineatura contabile|  
|Double|Doppia sottolineatura|  
|DoubleAccounting|Doppia sottolineatura contabile|  
|None|Nessuna sottolineatura|  
|Single|Una singola sottolineatura|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Impostazione dell'effetto barrato**  

Applicare il sbarrato impostando il metodo [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) su **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Impostazione dell'effetto pedice**  

Applicare il pedice impostando il metodo [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) su **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Impostazione dell'effetto esponente sulla font**  

Gli sviluppatori possono applicare l'effetto apice impostando il metodo [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) su **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Argomenti avanzati**  
- [Applica gli effetti esponente e pedice sulle font](/cells/it/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro](/cells/it/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


