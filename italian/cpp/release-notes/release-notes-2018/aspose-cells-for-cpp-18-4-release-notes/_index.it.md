---
title: Aspose.Cells per le note di rilascio di CPP 18.4
type: docs
weight: 30
url: /it/cpp/aspose-cells-for-cpp-18-4-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells per CPP 18.4.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSCPP-53|Supporta funzioni/moduli di disegno|Nuova caratteristica|
|CELLSCPP-57|Implementare la libreria System.Drawing|Nuova caratteristica|
|CELLSCPP-68|Modulo Debug System.Drawing|Nuova caratteristica|
|CELLSCPP-69|Risolvere problemi nei casi di test C++|Nuova caratteristica|
|CELLSCPP-70|Risolvi la perdita di memoria nelle classi del modulo System.Drawing|Nuova caratteristica|
|CELLSCPP-73|Scrivere un metodo nella pubblicazione di file .h|Nuova caratteristica|
|CELLSCPP-75|Implementa la funzione C++: Draw Image from Stream|Nuova caratteristica|
|CELLSCPP-76|Implementa le classi C++: ComIStreamWrapper, Metafile|Nuova caratteristica|
|CELLSCPP-77|Test case di debug C++: copie|Nuova caratteristica|
|CELLSCPP-78|Risolvi i problemi nei casi di test C++: DigitalSignature, EnumTypes, Finds, Formulas, Hyperlinks module|Nuova caratteristica|
|CELLSCPP-79|Risolvi il problema del collegamento della versione di rilascio di C++|Nuova caratteristica|
|CELLSCPP-81|Risolto il problema FillPath nel modulo grafico|Nuova caratteristica|
|CELLSCPP-82|Risolto il problema del modulo System.Drawing per test case|Nuova caratteristica|
|CELLSCPP-83|Risolto il problema con gppoint FillPath nel modulo grafico|Nuova caratteristica|
|CELLSCPP-89|Traduci ed esegui il debug del test case nella directory Charts/EnumTypes|Nuova caratteristica|
|CELLSCPP-91|Traduci test case in Finds|Nuova caratteristica|
|CELLSCPP-96|Traduci ed esegui il debug del test case nella directory Formule/Hyperlink/ImpHtml/ImportExports/Inserts|Nuova caratteristica|
|CELLSCPP-97|Eseguire il debug e risolvere i problemi relativi al rendering da XLSX/XLS a PDF|Nuova caratteristica|
|CELLSCPP-98|Tradurre ed eseguire il debug del test case nella directory LightCells|Nuova caratteristica|
|CELLSCPP-100|Tradurre ed eseguire il debug del caso di test nella directory Merges/OpenSaves/PageSetups/PDF|Nuova caratteristica|
|CELLSCPP-101|Traduci ed esegui il debug del test case nella directory delle tabelle pivot|Nuova caratteristica|
|CELLSCPP-102|grafici non vengono analizzati (conservati) quando si apre/salva un formato di file XLSX|Nuova caratteristica|
|CELLSCPP-103|Traduci ed esegui il debug del test case nella directory Shapes|Nuova caratteristica|
|CELLSCPP-105|Traduci ed esegui il debug del test case nella directory XlsxTest|Nuova caratteristica|
|CELLSCPP-108|Apri i file e controlla i problemi relativi ai grafici|Nuova caratteristica|
|CELLSCPP-106|Problema di perdita di memoria|Insetto|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for C++. il forum di supporto Aspose.Cells.
#### **Rinomina tutti i metodi come 'SetIs*' in metodi 'Set*'**
Rinomina i metodi, ad esempio SetIsOutlineShown in SetIsOutlineShown, SetIsSelected in SetSelected in IWorksheet e così via. Per maggiori dettagli, consulta la guida di riferimento API.
#### **Cambia Colore in Sistema::Disegno::Colore**
Ad esempio, cambia Color::GetBlue() in System::Drawing::Color::GetBlue(). Poiché Color è un simbolo ambiguo qui, potrebbe essere Aspose::Cells::System::Drawing::Color o Gdiplus::Color. Per usare Color in Aspose Cells, devi aggiungere lo spazio dei nomi System::Drawing.
#### **Rinomina ICells::AddRange in AddIRange**
Aggiunge un riferimento all'oggetto intervallo alle celle.
#### **Rinomina ICells::ApplyColumnStyle in ApplyColumnIStyle**
Applica la formattazione a un'intera colonna.
#### **Rinomina ICells::ApplyRowStyle in ApplyRowIStyle**
Applica la formattazione a un'intera riga.
#### **Rinomina ICells::ApplyStyle in ApplyIStyle**
Applica la formattazione a un intero foglio di lavoro.
#### **Rinomina ICells::CopyColumn in CopyIColumn**
Copia i dati e la formattazione di un'intera colonna.
#### **Rinomina ICells::CopyColumns in CopyIColumns**
Copia i dati e la formattazione delle colonne specificate.
#### **Rinomina ICells::CopyColumns in CopyIColumns**
Copia i dati e la formattazione delle colonne specificate.
#### **Rinomina ICells::CopyRow in CopyIRow**
Copia i dati e la formattazione di un'intera riga.
#### **Rinomina ICells::CopyRows in CopyIRows**
Copia i dati e la formattazione delle righe specificate.
#### **Rinomina ICells::MoveRange in MoveIRange**
Sposta l'intervallo nella posizione di destinazione.
#### **Rinomina ICells::InsertRange in InsertIRange**
Inserisce un intervallo di celle e sposta le celle in base all'opzione di spostamento.
#### **Rinomina IColumn::ApplyStyle in ApplyIStyle**
Applica la formattazione a un'intera colonna.
#### **Rinomina IErrorCheckOption::AddRange in AddIRange**
Aggiunge un intervallo influenzato da questa impostazione.
#### **Rinomina IRange::ApplyStyle in ApplyIStyle**
Applica la formattazione a un intero intervallo.
#### **Rinomina IRow::ApplyStyle in ApplyIStyle**
Applica la formattazione a un'intera riga.
#### **Rinomina IPivotField::GetNumberFormat in Get_NumberFormat**
Rappresenta il formato di visualizzazione personalizzato di numeri e date. Poiché il nome del metodo GetNumberFormat è in conflitto con la funzione di sistema di Windows, dobbiamo rinominarlo.
#### **Rinomina IStyleFlag::GetNumberFormat in Get_NumberFormat**
Poiché il nome del metodo GetNumberFormat è in conflitto con la funzione di sistema di Windows, dobbiamo rinominarlo che rappresenta per ottenere l'impostazione del formato numerico.
#### **Rinomina IWorkbook::CopyTheme in CopyITheme**
Copia il tema da un'altra cartella di lavoro.
#### **Rinomina IWorksheet::SetBackground in SetBackgroundImage**
Imposta l'immagine di sfondo del foglio di lavoro.
