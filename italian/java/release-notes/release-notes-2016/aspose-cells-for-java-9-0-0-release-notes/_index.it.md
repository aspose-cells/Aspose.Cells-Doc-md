---
title: Aspose.Cells for Java 9.0.0 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-9-0-0-release-notes/
---
## **1) Aspose.Cells**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41947 | Capacità di rilevare se un DataPoint è in torta o barra| Nuova caratteristica|
|CELLSJAVA-41827 | Il foglio di calcolo impiega più di 3 minuti per calcolare le formule quando si utilizza il metodo Workbook.calculateFormula()| Aumento|
|CELLSJAVA-41969 | Manca l'ombreggiatura Cell durante la conversione del formato di file HTML in XLSX| Insetto|
|CELLSJAVA-41955 | La cartella di lavoro in HTML mostra '#' nelle celle| Insetto|
|CELLSJAVA-41942 |Bordi mancanti, ombreggiatura delle celle e immagini: rendering da HTML a Excel| Insetto|
|CELLSJAVA-41967 | Cells mancante nel PDF quando sono definite più aree di stampa in un singolo foglio| Insetto|
|CELLSJAVA-41958 | La legenda del lato destro viene troncata nell'immagine del grafico| Insetto|
|CELLSJAVA-41953 | Testo fuori posto nel diagramma dopo la conversione in formato HTML| Insetto|
|CELLSJAVA-41948 | Il grafico viene modificato durante la conversione del foglio di calcolo in HTML| Insetto|
|CELLSJAVA-41981 | Posizione errata della linea verticale nel PDF del grafico| Insetto|
|CELLSJAVA-41964 | L'adattamento automatico non considera il livello di rientro| Insetto|
|CELLSJAVA-40260 | Modifica del testo di una WordArt esistente in un file Excel| Insetto|
|CELLSJAVA-41971 | Cell.getValiationValue() genera NullPointerException per il tipo di convalida personalizzato| Eccezione|
|CELLSJAVA-41963 | Si verifica un'eccezione di dimensione della chiave illegale durante l'apertura della sorgente a5.xlsx| Eccezione|
|CELLSJAVA-41962 | L'eccezione ArrayIndexOutOfBoundsException si verifica durante l'apertura dell'origine a4.xls| Eccezione|
|CELLSJAVA-41961 | Stringa non valida nell'eccezione del file si verifica durante l'apertura del sorgente a3.xls| Eccezione|
|CELLSJAVA-41960 | L'eccezione NegativeArraySizeException si verifica durante l'apertura dell'origine a2.xls| Eccezione|
|CELLSJAVA-41959 | L'eccezione NullPointerException si verifica durante l'apertura dell'origine a1.xlsx| Eccezione|
## **2) Aspose.Cells Griglia Suite**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41965 |Ottieni la versione come CELLSNET-44565 e CELLSNET-44676 necessaria anche per GridWeb (Java)| Aumento|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà Shape.TextOptions**
Rappresenta le opzioni di testo della forma.
### **Metodo Worksheet.SetBackground obsoleto**
Utilizzare invece la proprietà Worksheet.BackgroundImage.
### **LineShape.BeginArrowheadStyle e ArcShape.BeginArrowheadStyle obsoleti**
Utilizzare invece la proprietà Shape.Line.BeginArrowheadStyle.
### **LineShape.BeginArrowheadWidth e ArcShape.BeginArrowheadWidth obsoleti**
Utilizzare invece la proprietà Shape.Line.BeginArrowheadWidth.
### **LineShape.BeginArrowheadLength e ArcShape.BeginArrowheadLength obsoleti**
Utilizzare invece la proprietà Shape.Line.BeginArrowheadLength.
### **LineShape.EndArrowheadStyle e ArcShape.EndArrowheadStyle obsoleti**
Utilizzare invece la proprietà Shape.Line.EndArrowheadStyle.
### **LineShape.EndArrowheadWidth e ArcShape.EndArrowheadWidth obsoleti**
Utilizzare invece la proprietà Shape.Line.EndArrowheadWidth.
### **LineShape.EndArrowheadLength e ArcShape.EndArrowheadLength obsoleti**
Utilizzare invece la proprietà Shape.Line.EndArrowheadLength.
### **Elimina il metodo Worksheet.CopyConditionalFormatting() obsoleto**
### **Elimina il metodo Workbook.CheckWriteProtectedPassword() obsoleto**
Utilizzare invece il metodo WorkbookSettings.WriteProtection.ValidatePassword.
### **Rinomina Workbook.RemoveDigitallySign come metodo Workbook.RemoveDigitalSignature**
Il metodo Workbook.RemoveDigitallySign è stato rinominato in Workbook.RemoveDigitalSignature.
### **Aggiunge la proprietà ChartSplitType.Auto**
Rappresenta i punti dati che devono essere divisi utilizzando il meccanismo predefinito per questo tipo di grafico.
### **Aggiunge la proprietà ChartPoint.IsInSecondaryPlot**
Ottiene o imposta un valore che indica se questi punti dati si trovano nella seconda torta o barra di un grafico a torta o a barre del grafico a torta.
### **Aggiunge la proprietà OleObject.ClassIdentifier**
Ottiene o imposta l'identificatore di classe dell'oggetto incorporato.
