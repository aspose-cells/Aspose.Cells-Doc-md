---  
title: Impostazioni numero
linktitle: Impostazioni numero  
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo che supporta molte impostazioni numeriche diverse delle celle. Questo articolo introduce come usare la libreria Aspose.Cells per gestire le impostazioni numeriche delle celle per adattare i formati numerici nei fogli di calcolo.  
keywords: Aspose.Cells, libreria Node.js, foglio di calcolo elettronico, impostazioni numeriche delle celle, formattazione, gestione, Formati di Numeri e Date  
type: docs  
weight: 10  
url: /it/nodejs-cpp/cells-number-settings/  
---  

## **Come impostare i formati di visualizzazione dei numeri e delle date**  

Una funzione molto potente di Microsoft Excel è che permette agli utenti di impostare i formati di visualizzazione dei valori numerici e delle date. Sappiamo che i dati numerici possono essere usati per rappresentare valori diversi tra cui decimali, valute, percentuali, frazioni o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in formati diversi a seconda del tipo di informazione che rappresentano. Allo stesso modo, ci sono molti formati in cui una data o ora può essere visualizzata.  
Aspose.Cells supporta questa funzionalità e consente agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.  

### **Come impostare i formati di visualizzazione in Microsoft Excel**  

Per impostare i formati di visualizzazione in Microsoft Excel:  

1. Fai clic con il pulsante destro del mouse su qualsiasi cella.  
2. Selezionare **Formato celle**. Apparirà una finestra di dialogo che permette di impostare i formati di visualizzazione di qualsiasi tipo di valore.  

Sul lato sinistro della finestra di dialogo, ci sono molte categorie di valori come **Generale**, **Numero**, **Valuta**, **Contabile**, **Data**, **Ora**, **Percentuale**, ecc. Aspose.Cells supporta tutti questi formati di visualizzazione.  

Aspose.Cells fornisce un modulo, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Excel. Il modulo [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dal modulo [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Il modulo [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) rappresenta un oggetto del modulo [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells fornisce metodi [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) e [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) per il modulo [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Questi metodi vengono usati per ottenere e impostare la formattazione di una cella. Il modulo [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) fornisce alcune proprietà utili per gestire i formati di visualizzazione di numeri e date.  

### **Come utilizzare i formati numerici incorporati**  

Aspose.Cells offre alcuni formati numerici integrati per configurare i formati di visualizzazione di numeri e date. Questi formati numerici integrati possono essere applicati utilizzando il metodo [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Tutti i formati numerici integrati sono assegnati con valori numerici unici. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato al metodo [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) per applicare il formato di visualizzazione. Questo metodo è veloce. I formati numerici integrati supportati da Aspose.Cells sono elencati di seguito.  

|**Valore**|**Tipo**|**Stringa di formato**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **Come utilizzare i formati numerici personalizzati**  

Per definire una stringa di formato personalizzata, usa il metodo [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Questo metodo non è veloce come l'uso di formati preimpostati, ma è più flessibile.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

Se usi il metodo [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) per impostare il formato numerico, qualsiasi formato precedente impostato con il metodo [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) viene sovrascritto e viceversa.  

{{% /alert %}}  

## **Argomenti avanzati**  
- [Verificare il formato numerico personalizzato quando si imposta Style.Custom Property](/cells/it/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Elenco dei formati numerici supportati](/cells/it/nodejs-cpp/list-of-supported-number-formats/)  
- [Render Personalizzare data formato modello g e ge mm dd](/cells/it/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Specificare Personalizzare numerico Decimale e Gruppo Separatori per Cartella di lavoro](/cells/it/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Specifica di formattazione pattern personalizzato DBNum](/cells/it/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
{{< app/cells/assistant language="nodejs-cpp" >}}
