---
title: Aspose.Cells for .NET Note sulla versione 22.11
type: docs
weight: 2
url: /it/net/aspose-cells-for-net-22-11-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.11](https://www.nuget.org/packages/Aspose.Cells/22.11.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-52026|Supporta la copia della sequenza temporale|
|CELLSNET-52022|Distinguere o distinguere tra la formula di matrice legacy CSE e la normale formula di matrice|
|CELLSNET-52156|Disabilita le celle di tabella unite durante il salvataggio di XLSX in HTML|
|CELLSNET-52159|Supporto per analizzare la proprietà compressa durante la conversione di HTML in Excel|
|CELLSNET-51939|Da XLSX a PDF: disallineamento dei contenuti|
|CELLSNET-51940|Da XLS a PDF: disallineamento del contenuto nelle celle|
|CELLSNET-52068|Da XLSX a PDF: forme mancanti/compressione del layout|
|CELLSNET-52092|La stampa e la spaziatura dei caratteri nelle figure di Excel è tagliata|
|CELLSNET-52186|Le forme/caselle sono vuote durante la conversione di documenti XLSX in PDF|
|CELLSNET-52225|Caratteri da XLSX a PDF nelle caselle di testo invertiti|
|CELLSNET-52086|Connessioni esterne danneggiate nel file generato|
|CELLSNET-52133|Le formule di Excel sono racchiuse tra parentesi graffe nel file xlsb risalvato|
|CELLSNET-52158|Rilevamento errato del riferimento circolare|
|CELLSNET-52174|Cell.IsArrayFormula è false per la formula di matrice dopo essere stata letta dal file modello xlsb|
|CELLSNET-52217|Le funzioni di ricerca sono state calcolate in modo errato per alcuni numeri grandi|
|CELLSNET-52221|La formula di matrice dinamica non è stata distribuita correttamente per CERCA.X|
|CELLSNET-52232|Le virgolette singole vengono rimosse dal nome del foglio del collegamento esterno|
|CELLSNET-52198|Problema di sovrapposizione durante la conversione dei grafici come file immagine|
|CELLSNET-52043|Problema durante il calcolo di "PageSetup.Zoom" con HorizontalPageBreaks|
|CELLSNET-52157|Il bordo della pagina si sovrappone al testo durante la conversione in pdf|
|CELLSNET-52118|Risultato incoerente tra diversi formati quando html è impostato su cella in OpenOffice e LibreCalc|
|CELLSNET-52125|Indice non compreso nell'intervallo per range.copy con immagine|
|CELLSNET-52143| Il tipo di relazione del collegamento viene modificato durante la conversione di un file XLS in XLSM|
|CELLSNET-52144|Conversione da XLS a XLSM che modifica il tipo di relazione di collegamento|
|CELLSNET-52151|Il salvataggio di xlsb ha sostituito tutti i commenti con l'ultimo commento|
|CELLSNET-52152|Il valore dell'altezza della riga non è corretto quando l'operazione di adattamento automatico della riga viene applicata tramite Aspose.Cells|
|CELLSNET-52155|Formattazione condizionale persa dopo la copia dell'intervallo|
|CELLSNET-52181|Da XLSX a HTML: l'intervallo Cells non viene esportato correttamente|
|CELLSNET-52214|Il contenuto dell'ultima riga viene troncato nel file Excel di output|
|CELLSNET-52236| Il marcatore intelligente (gruppo: unisci) non funziona per le celle unite|
|CELLSNET-52241|Le caselle (forme) nel documento non vengono visualizzate nel PDF di output|
|CELLSNET-52243|La modifica del progetto VBA genererà un errore quando la cartella di lavoro viene salvata|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà Cell.IsDynamicArrayFormula**

Indica se la formula della cella è una formula di matrice dinamica (vero) o una formula di matrice legacy (falso).

### **Rende obsoleta la proprietà SparklineGroup.SparklineCollection e aggiunge la proprietà SparklineGroup.Sparklines**

Usare invece la proprietà SparklineGroup.Sparklines.

### **Rende obsoleta la proprietà Worksheet.SparklineGroupCollection e aggiunge la proprietà Worksheet.SparklineGroups**

Usare invece la proprietà Worksheet.SparklineGroups.
