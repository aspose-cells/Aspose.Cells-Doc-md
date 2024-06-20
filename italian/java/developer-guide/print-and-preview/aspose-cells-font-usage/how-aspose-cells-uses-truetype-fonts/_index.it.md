---
title: Come Aspose.Cells utilizza i caratteri TrueType
type: docs
weight: 10
url: /it/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells richiede i caratteri TrueType durante la generazione di fogli di calcolo in formati come PDF, XPS e immagini.

Quando Aspose.Cells genera un foglio di calcolo, richiede l'accesso ai caratteri TrueType utilizzati nel foglio di calcolo. Questa è una prassi normale durante la generazione di PDF, XPS e immagini e garantisce che il documento o l'immagine convertiti appaiano identici per qualsiasi visualizzatore.

{{% /alert %}}

## **Informazioni su Font**

### **Disponibilità e sostituzione del font**

Un foglio di calcolo può essere formattato utilizzando vari caratteri come Arial, Times New Roman, Verdana e altri. Quando Aspose.Cells genera un foglio di calcolo, cerca di selezionare i caratteri utilizzati nel foglio di calcolo. Tuttavia, ci sono situazioni in cui il carattere esatto potrebbe non essere disponibile, quindi Aspose.Cells deve sostituire un carattere simile al suo posto.

Di seguito è illustrato il processo che Aspose.Cells segue dietro le quinte.

1. Aspose.Cells cerca i caratteri sul file system corrispondenti al nome esatto del carattere utilizzato nel foglio di calcolo.
1. Se Aspose.Cells non riesce a trovare caratteri con lo stesso nome esatto, cerca di utilizzare il carattere predefinito specificato nella proprietà DefaultStyle.Font del Workbook.
1. Se Aspose.Cells non riesce a individuare il carattere definito nella proprietà DefaultStyle.Font del workbook, cerca di selezionare i caratteri più adatti tra tutti i caratteri disponibili.
1. Infine, se Aspose.Cells non riesce a trovare alcun carattere sul file system, genera il foglio di calcolo utilizzando Arial.

### **Dove Aspose.Cells cerca i caratteri**

Aspose.Cells cerca automaticamente i caratteri TrueType sul file system. Nella maggior parte dei casi è possibile fare affidamento sul comportamento predefinito di Aspose.Cell per trovare i caratteri TrueType, ma talvolta potrebbe essere necessario specificare le cartelle che contengono i caratteri TrueType utilizzando il metodo factory FontConfigs.setFontFolder.

### **Problemi tipici relativi ai caratteri e relative soluzioni**

Questa tabella elenca alcuni dei problemi che potresti incontrare durante la generazione di fogli di calcolo in PDF utilizzando Aspose.Cells e le relative soluzioni.

{{% alert color="primary" %}}

Tieni presente che quando copi i caratteri la maggior parte di essi sono protetti da copyright. Localizza prima la licenza di un carattere e verifica che possano essere liberamente trasferiti su un'altra macchina. 

{{% /alert %}}

|**Problema** |**Motivo** |**Soluzione** |
| :- | :- | :- |
|Il layout e i caratteri nel documento generato sono diversi dall'originale. |Stai utilizzando Aspose.Cells su Linux o Mac OS dove i caratteri TureType non sono presenti per impostazione predefinita, quindi Aspose.Cells non può individuare i caratteri sul tuo computer. |Copia i file dei caratteri TrueType da una macchina Windows o installa un pacchetto di caratteri TrueType. Utilizza il metodo factory FontConfigs.setFontFolder per specificare la posizione dei file dei caratteri.|

{{% alert color="primary" %}}

Controlla gli articoli dettagliati su

- [Come posizionare i font TrueType su Linux](/cells/it/java/come-installare-i-font-truetype-su-linux/).
- [Come specificare la posizione dei font TrueType](/cells/it/java/come-specificare-la-posizione-dei-font-truetype/).
- [Come ottenere avvisi quando si verifica la sostituzione dei font](/cells/it/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
