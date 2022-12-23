---
title: Aspose.Cells for .NET 20.1 Note di rilascio
type: docs
weight: 70
url: /it/net/aspose-cells-for-net-20-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.1](https://www.nuget.org/packages/Aspose.Cells/20.1.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47026|Supporta l'opzione del formato di visualizzazione "Rank dal più piccolo al più grande" e "Rank dal più grande al più piccolo".|Nuova caratteristica|
|CELLSNET-47030|Visualizza le intestazioni durante il salvataggio in HTML|Nuova caratteristica|
|CELLSNET-47089|Supporta tutti i formati di visualizzazione dei dati di DataField|Nuova caratteristica|
|CELLSNET-47062|Supporto per DEV.ST.P e DEV.ST.S|Nuova caratteristica|
|CELLSNET-47070|Supporto per Regex nella funzione Sostituisci simile a Find() utilizzando le opzioni|Nuova caratteristica|
|CELLSNET-46998|Supporto per le firme XAdES|Nuova caratteristica|
|CELLSNET-40174|Inserimento di CheckBox nel foglio del tipo di grafico|Nuova caratteristica|
|CELLSNET-43089|Supporto per la formattazione condizionale durante la conversione da ODS a XLSX|Nuova caratteristica|
|CELLSNET-43090|Supporto per la convalida dei dati durante la conversione del formato ODS nel formato XLSX|Nuova caratteristica|
|CELLSNET-47064|Supporta le forme nel grafico per il file .xlsx.|Aumento|
|CELLSNET-47065|Ottieni PowerQuery da DataConnections|Aumento|
|CELLSNET-47066|Recupera PowerQuery MCode formattato simile a MS Excel|Aumento|
|CELLSNET-47008|Problema durante il rendering di un'immagine di un grafico con un'angolazione specifica|Insetto|
|CELLSNET-47063|Problema di rendering di Excel su stampante quando i caratteri non sono installati|Insetto|
|CELLSNET-44237|Ordinamento discendente del DataField della tabella pivot|Insetto|
|CELLSNET-47002|Il valore calcolato viene visualizzato come "#REF!" nel risultante PDF|Insetto|
|CELLSNET-47050|Alcuni campi nella prima pagina non compaiono nell'output PDF|Insetto|
|CELLSNET-40733|File Open Office .ods: la formattazione condizionale non rimane|Insetto|
|CELLSNET-47039|I grafici a dispersione XY nel file ODS non vengono visualizzati correttamente|Insetto|
|CELLSNET-47040|I grafici netti nel file ODS non vengono visualizzati correttamente|Insetto|
|CELLSNET-47060|Supporta XY personalizzato del titolo nel file ods|Insetto|
|CELLSNET-47072|La differenza nel percorso del collegamento recuperato da Aspose.Cells rispetto a Excel|Insetto|
|CELLSNET-47087|Si è verificato un problema durante la stampa del file excel salvato da Aspose.Cells for .NET|Insetto|
|CELLSNET-47082|Il calcolo della formula si blocca|Insetto|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà ReplaceOptions.RegexKey.**
 Indica se la chiave cercata è regex. Se**VERO**quindi la chiave cercata (da sostituire parte) verrà presa come regex specificata dall'utente.
#### **Aggiunge il metodo CustomImplementationFactory.CreateCultureInfo.**
Alcune impostazioni cultura potrebbero non essere supportate dall'ambiente dell'utente. Per evitare l'eccezione per tali situazioni, l'utente può eseguire l'override di questo metodo per fornire invece un'istanza CultureInfo valida.
#### **Elimina il metodo ValidationCollection.Add(Aspose.Cells.Validation) obsoleto.**
Usare invece il metodo ValidationCollection.Add(CellArea).
#### **Aggiunge la proprietà PowerQueryFormula.FormulaDefinition.**
Ottiene la definizione della formula della query avanzata.
#### **Aggiunge la proprietà DBConnection.PowerQueryFormula.**
Ottiene la definizione della formula di query di alimentazione.
#### **Aggiunge la proprietà HtmlSaveOptions.ExportHeadings.**
 Indica se esportare le intestazioni durante il salvataggio del file in HTML. Il valore predefinito è**falso**. Se desideri importare il file HTML in Excel, mantieni il valore predefinito.
#### **Aggiunge la classe XAdESTType**
Tipo di firma elettronica avanzata XML (XAdES).
#### **Aggiunge la proprietà DigitalSignature.XAdESTType**
Ottiene e imposta il tipo di firma elettronica avanzata XML (XAdES). Il valore predefinito è Nessuno (XAdES è disattivato).
