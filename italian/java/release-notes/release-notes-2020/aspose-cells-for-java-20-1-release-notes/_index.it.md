---
title: Aspose.Cells for Java 20.1 Note di rilascio
type: docs
weight: 60
url: /it/java/aspose-cells-for-java-20-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.1/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41325|Il metodo Cell.getValidation restituisce null per ODS|Nuova caratteristica|
|CELLSJAVA-43074|Da XLSX a PDF, differenza nell'output PDF quando si utilizza Oracle JDK rispetto a Open JDK|Aumento|
|CELLSJAVA-43083|L'opacità non viene applicata agli istogrammi|Insetto|
|CELLSJAVA-41879|%of, %of Row, %of ParentRowTotal, %ParentTotal, ecc. non funzionano nell'output di pivot excel|Insetto|
|CELLSJAVA-43062|Il colore di sfondo predefinito di Cell è errato nell'output HTML|Insetto|
|CELLSJAVA-43063|L'output di SheetRender.toImage() non è corretto|Insetto|
|CELLSJAVA-43070|calcolaFormula() non calcola il valore|Insetto|
|CELLSJAVA-43086|Lo stile di formato percentuale viene applicato in modo non corretto nelle impostazioni internazionali norvegesi|Insetto|
|CELLSJAVA-43082|Carattere più piccolo reso in ogni prima riga della tabella|Insetto|
|CELLSJAVA-41360|Cells con le formule vengono visualizzate all'interno del PDF mentre non vengono visualizzate all'interno dell'ODS|Insetto|
|CELLSJAVA-42786|Da ODS a XLSX: il grafico a linee perde le righe e le voci delle legende|Insetto|
|CELLSJAVA-42788|Da ODS a XLSX: il cerchio diventa quadrato|Insetto|
|CELLSJAVA-43073|Informazioni DataMashup non accessibili nella cartella di lavoro|Insetto|
|CELLSJAVA-43092|Impossibile elaborare il file Excel|Insetto|

## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà ReplaceOptions.RegexKey.**
 Indica se la chiave cercata è regex. Se**VERO**quindi la chiave cercata (da sostituire parte) verrà presa come regex specificata dall'utente.
### **Elimina il metodo ValidationCollection.Add(Aspose.Cells.Validation) obsoleto.**
Usare invece il metodo ValidationCollection.Add(CellArea).
### **Aggiunge la proprietà PowerQueryFormula.FormulaDefinition.**
Ottiene la definizione della formula della query avanzata.
### **Aggiunge la proprietà DBConnection.PowerQueryFormula.**
Ottiene la definizione della formula di query di alimentazione.
### **Aggiunge la proprietà HtmlSaveOptions.ExportHeadings.**
Indica se esportare le intestazioni durante il salvataggio del file in HTML. Il valore predefinito è falso. Se desideri importare il file HTML in Excel, mantieni il valore predefinito.
### **Aggiunge la classe XAdESTType**
Tipo di firma elettronica avanzata XML (XAdES).
### **Aggiunge la proprietà DigitalSignature.XAdESTType**
Ottiene e imposta il tipo di firma elettronica avanzata XML (XAdES). Il valore predefinito è Nessuno (XAdES è disattivato).
