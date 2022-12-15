---
title: Come Aspose.Cells utilizza i caratteri TrueType
type: docs
weight: 10
url: /it/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells richiede i caratteri TrueType durante il rendering di fogli di calcolo in formati come PDF, XPS e immagini.

Quando Aspose.Cells esegue il rendering di un foglio di calcolo, richiede l'accesso ai caratteri TrueType utilizzati nel foglio di calcolo. Questa è una pratica normale durante la generazione di PDF, XPS e immagini e garantisce che il documento o l'immagine convertiti appaia identico per qualsiasi visualizzatore.

{{% /alert %}}

## **Informazioni sui caratteri**

### **Disponibilità e sostituzione dei caratteri**

Un foglio di calcolo può essere formattato utilizzando vari caratteri come Arial, Times New Roman, Verdana e altri. Quando Aspose.Cells esegue il rendering di un foglio di calcolo, tenta di selezionare i caratteri utilizzati nel foglio di calcolo. Tuttavia ci sono situazioni in cui il carattere esatto potrebbe non essere disponibile, quindi Aspose.Cells deve sostituirlo con un carattere simile.

Di seguito il processo che Aspose.Cells segue dietro le quinte.

1. Aspose.Cells tenta di trovare i caratteri nel file system corrispondenti al nome esatto del carattere utilizzato nel foglio di calcolo.
1. Se Aspose.Cells non è in grado di trovare caratteri con lo stesso identico nome, tenta di utilizzare il carattere predefinito specificato nella proprietà DefaultStyle.Font della cartella di lavoro.
1. Se Aspose.Cells non è in grado di individuare il tipo di carattere definito nella proprietà DefaultStyle.Font della cartella di lavoro, tenta di selezionare i tipi di carattere più adatti tra tutti i tipi di carattere disponibili.
1. Infine, se Aspose.Cells non riesce a trovare alcun carattere nel file system, esegue il rendering del foglio di calcolo utilizzando Arial.

### **Dove Aspose.Cells cerca i caratteri**

Aspose.Cells tenta di trovare automaticamente i font TrueType nel file system. La maggior parte delle volte puoi fare affidamento sul comportamento predefinito di Aspose.Cell per trovare i caratteri TrueType, ma a volte potresti dover specificare le cartelle che contengono i caratteri TrueType utilizzando il metodo di fabbrica FontConfigs.setFontFolder.

### **Tipici problemi e soluzioni relativi ai caratteri**

Questa tabella elenca alcuni dei problemi che potresti riscontrare durante il rendering di fogli di calcolo in PDF utilizzando Aspose.Cells e le relative soluzioni.

{{% alert color="primary" %}}

 Tieni presente quando copi qualsiasi carattere che la maggior parte dei caratteri è protetta da copyright. Individua prima la licenza di un font e verifica che possa essere trasferito liberamente su un'altra macchina.

{{% /alert %}}

|**Problema** |**Motivo** |**Soluzione** |
|:- |:- |:- |
| Il layout e i caratteri nel documento renderizzato sono diversi dall'originale.| Stai utilizzando Aspose.Cells su Linux o Mac OS dove i font TureType non sono presenti per impostazione predefinita, quindi Aspose.Cells non può individuare i font sul tuo computer.|Copia i file di font TrueType da un computer Windows o installa un pacchetto di font TrueType. Utilizzare il metodo factory FontConfigs.setFontFolder per specificare la posizione dei file dei font.|

{{% alert color="primary" %}}

Controlla gli articoli dettagliati su

- [Come posizionare i font TrueType su Linux](/cells/it/java/how-to-install-truetype-fonts-on-linux/).
- [Come specificare la posizione dei caratteri TrueType](/cells/it/java/how-to-specify-truetype-fonts-location/).
- [Come ricevere avvisi quando si verifica la sostituzione dei caratteri](/cells/it/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
