---
title: Aspose.Cells for Java Note sulla versione 22.11
type: docs
weight: 2
url: /it/java/aspose-cells-for-java-22-11-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 22.11](https://releases.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.11/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44888|"+" e "-" sono scomparsi dopo la conversione: rendering da Excel a HTML|
|CELLSJAVA-44775|Etichette del grafico sovrapposte nel rendering del grafico all'immagine|
|CELLSJAVA-44882|Rendering dal grafico all'immagine: una delle etichette si trova all'interno del grafico ad anello|
|CELLSJAVA-44943|Da XLSX a PDF: le etichette dei grafici non sono visualizzate correttamente|
|CELLSJAVA-44928|Da XLS a PDF: dati insufficienti per un'immagine|
|CELLSJAVA-44910|Converti Excel in HTML produce migliaia di piccole immagini simili|
|CELLSJAVA-44944|Il ridimensionamento delle tabelle modifica la formattazione delle celle|
|CELLSJAVA-44948| Le immagini non possono essere visualizzate nel foglio durante la conversione da HTML a Excel|
|CELLSJAVA-44908|Eccezione "java.lang.OutOfMemoryError: Java heap space" durante il caricamento di file XLSB di grandi dimensioni|
|CELLSJAVA-44929|Regressione: "java.lang.NullPointerException" su Workbook.calculateFormula()|
|CELLSJAVA-44927|Eccezione "java.lang.IndexOutOfBoundsException: Index: 5, Size: 5" durante la conversione di file Excel in HTML|
|CELLSJAVA-44939|Errore "java.lang.StringIndexOutOfBoundsException: Indice stringa fuori intervallo: 0" durante il tentativo di leggere un file Excel|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà Cell.IsDynamicArrayFormula**

Indica se la formula della cella è una formula di matrice dinamica (vero) o una formula di matrice legacy (falso).

### **Rende obsoleta la proprietà SparklineGroup.SparklineCollection e aggiunge la proprietà SparklineGroup.Sparklines**

Usare invece la proprietà SparklineGroup.Sparklines.

### **Rende obsoleta la proprietà Worksheet.SparklineGroupCollection e aggiunge la proprietà Worksheet.SparklineGroups**

Usare invece la proprietà Worksheet.SparklineGroups.