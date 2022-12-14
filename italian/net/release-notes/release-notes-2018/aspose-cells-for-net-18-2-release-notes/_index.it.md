---
title: Aspose.Cells for .NET 18.2 Note di rilascio
type: docs
weight: 110
url: /it/net/aspose-cells-for-net-18-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.2](https://www.nuget.org/packages/Aspose.Cells/18.2.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-45889|Converti il contenuto della cella in collegamento ipertestuale - Opzione ImportTableOptions.IsFormulas|Nuova caratteristica|
|CELLSNET-45886|Imposta i margini del commento|Nuova caratteristica|
|CELLSNET-45855|Fornire WorkbookSetting.StreamProvider per controllare le risorse esterne|Nuova caratteristica|
|CELLSNET-45845|Foglio di stile esterno non supportato durante la conversione di andata e ritorno|Aumento|
|CELLSNET-45888|Il collegamento DDE non è presente all'interno di Worksheets.ExternalLinks|Aumento|
|CELLSNET-45893|Aspose.Cells.GridWeb non inserisce testo come Microsoft Excel quando il testo a capo è abilitato|Aumento|
|CELLSNET-45833|Le proprietà dell'immagine (titolo e oggetto) vengono perse nella conversione da forma a immagine|Insetto|
|CELLSNET-45822|Caratteri invertiti nelle etichette durante la conversione da Excel a PDF|Insetto|
|CELLSNET-45776|Alcuni dati delle colonne non vengono completamente espansi/visualizzati durante il salvataggio di un file MHtml nel formato di file Excel|Insetto|
|CELLSNET-44829|L'HTML di output non corrisponde a Microsoft Excel|Insetto|
|CELLSNET-44319|Il valore del filtro della tabella pivot non viene mantenuto all'aggiornamento|Insetto|
|CELLSNET-45887|#VALORE!' errore per il calcolo di ArrayFormula|Insetto|
|CELLSNET-45883|Grafico a torta 3D: non viene visualizzato correttamente nel PDF di output|Insetto|
|CELLSNET-45881|L'apertura e il salvataggio del file Excel di input provoca l'avviso di visualizzazione protetta rossa in MS Excel|Insetto|
|CELLSNET-45880|Parte delle etichette dell'asse x viene visualizzata nella seconda riga del grafico|Insetto|
|CELLSNET-45864|EMF convertito da Aspose.Cells non è esattamente accurato|Insetto|
|CELLSNET-45885|Il tipo (attributo) del collegamento esterno viene modificato dopo l'apertura/salvataggio|Insetto|
|CELLSNET-45872|Impossibile leggere la connessione dati di Excel quando il suo tipo è CSV|Insetto|
|CELLSNET-45868|Il valore della proprietà PrintTitleRows scompare dopo l'apertura e il salvataggio di Aspose.Cells|Insetto|
|CELLSNET-45865|I caratteri speciali utilizzati nel nome di una colonna non funzionano: problema relativo agli indicatori intelligenti|Insetto|
|CELLSNET-45858|La modifica dell'origine del collegamento influisce sui contenuti dei menu a discesa|Insetto|
|CELLSNET-45857|File danneggiato durante la copia di un foglio da una cartella di lavoro a un'altra|Insetto|
|CELLSNET-45901|Allineamento della casella di testo perso durante il rendering in PDF|Insetto|
|CELLSNET-45875|Il valore Cell viene perso e alcune parti delle etichette dell'asse x vengono visualizzate nella seconda riga|Insetto|
|CELLSNET-45873|Implementazione del controllo interattivo per gruppi di radio button in GridWeb|Insetto|
|CELLSNET-45902|Il foglio di lavoro diventa sovradimensionato e non risponde quando si naviga o si fa clic su di esso in Aspose.Cells.GridWeb|Insetto|
|CELLSNET-45849|L'immagine esce dalle dimensioni del foglio di lavoro della griglia|Insetto|
|CELLSNET-45824|Le immagini nel file Excel non vengono visualizzate in dimensioni normali durante l'importazione del file in Aspose.Cells.GridDesktop|Insetto|
|CELLSNET-45874|Eccezione "La stringa di input non era in un formato corretto" durante l'importazione del file Excel in Aspose.Cells.GridWeb|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge l'enumerazione LoadDataFilterOptions.DefinedNames**
Indica se caricare gli oggetti Name definiti durante il caricamento del file modello.
#### **Modifica il comportamento di LoadDataFilterOptions.Formula enum**
Nelle versioni precedenti carichiamo sempre gli oggetti Nome definiti durante il caricamento delle formule. Ora forniamo un enum separato per gli oggetti Name definiti in modo esplicito, quindi Formula enum indicherà solo che le formule devono essere caricate ora, indipendentemente dal fatto che gli oggetti Name definiti vengano caricati o meno. Tuttavia, una cosa dovrebbe essere notata, gli oggetti Nome comunemente definiti sono usati dalle formule, se l'utente carica solo le formule e non carica gli oggetti Nome definiti, la formula della cella che fa riferimento a quei Nomi verrà danneggiata e potrebbe causare un'eccezione. Quindi, generalmente se l'utente desidera caricare formule, devono essere caricati anche gli oggetti Nome definiti. Ma l'utente può caricare solo oggetti Nome definiti senza caricare formule.
#### **Aggiungere l'enumerazione SheetType.Dialog**
Rappresenta il foglio di dialogo.
#### **Aggiunge la proprietà WorkbookSettings.MaxRowsOfSharedFormula**
Ottiene e imposta il numero massimo di righe della formula condivisa. La formula condivisa verrà suddivisa in più formule condivise se le righe totali della formula condivisa sono maggiori di essa.
#### **Aggiunge la proprietà WorkbookSettings.StreamProvider**
Ottiene e imposta il provider di flussi per la risorsa esterna.
#### **Aggiunge la proprietà ShapeTextAlignment.IsAutoMargin**
Indica se il margine della cornice di testo è automatico.
#### **Aggiunge la proprietà ImportTableOptions.IsFormulas**
Rappresenta quale colonna nel datatable deve essere importata come formule.
