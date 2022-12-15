---
title: Aspose.Cells for Java 2.1.2 Note di rilascio
type: docs
weight: 90
url: /it/java/aspose-cells-for-java-2-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 2.1.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.1.2/)

{{% /alert %}} 

 Siamo felici di annunciare Aspose.Cells per Jav!

 Cosa è cambiato:

- Fornisce funzionalità da grafico a immagine.
 Importa RichText dal file modello SpreadSheetML.
Supporta l'esportazione dell'oggetto Nome con riferimenti esterni per il file SpreadSheetML.
 Esporta le immagini in PageSetup per i file di Excel 2007.
 Importa controlli TextBox da file Excel 2007.
 Fornisce supporto per impostare il limite di record durante l'importazione di dati da ResultSet per marcatori intelligenti.
 Imposta la posizione di una forma al centro dell'intervallo specificato.
 Supporta l'aggiunta di campi calcolati per una tabella pivot.
 Supporta per ottenere/impostare la proprietà VeryHidden per un foglio di lavoro.
 Aggiunge una nuova formula all'elenco delle formule supportate: FREQUENZA
 Riconosce automaticamente il formato del file per l'API LightCells.
 Migliora il modello di stile per la considerazione delle prestazioni.
 Migliora l'API relativa ai commenti per considerazioni sulle prestazioni.
 Migliora le prestazioni di lettura di file Excel 2007 di grandi dimensioni.
 Aumenta le prestazioni dell'API LightCells per file Excel 2007 di grandi dimensioni.
 L'operazione di lettura per le proprietà di un documento è migliorata.
L'operazione di importazione dei file CSV è migliorata.
 67 correzioni e miglioramenti.

 Problemi risolti in Aspose.Cells for Java 2.1.2



|**ID problema** |**Componente** |**Riepilogo** |
|:- |:- |:- |
|6245 | xls| Raccogli gli stili|
|6362 | xls| Stile di copia durante l'inserimento di righe/colonne|
|11871 | xls| Copia l'intervallo di celle|
|11890 | html| Leggi Formattazione condizionale|
|11891 | grafico| Proprietà LogarithmicBase di ValueAxis|
|11911 | Foglio di calcoloML| Salva lo stile|
|11928 | xls| Leggi il file modello|
|11943 | Foglio di calcoloML| Leggi il file speciale generato da OWC|
|11973 | Foglio di calcoloML| Leggi il file speciale generato da OWC|
|12006 | CSV| Leggi il file csv|
|12032 | FormulaMotore| Formula CONTA.SE|
|12034 | xls| Colonne di adattamento automatico|
|12056 | FormulaMotore| SE formula|
|12080 | grafico| Valore formattato di ChartFrame|
|12105 | xls| Leggere l'altezza della riga|
|12128 | grafico| Ottieni un pennarello|
|12138 | grafico| Leggi marcatore|
|12184 | xls| Copia formule|
|12229 | Foglio di calcoloML| Leggi il testo ricco|
|12238 | xlsx| Prestazioni di lettura del file modello|
|12238 | xlsx| Prestazioni di lettura del file modello|
|12243 | grafico| Tipo di ASeries|
|12253 | xls| Tipo di collegamento del collegamento ipertestuale|
|12271 | grafico| Etichette dati|
|12275 | xls| Celle luminose|
|12317 | grafico| Testo del titolo|
|12324 | Grafico2Immagine| Opzione immagine|
|12347 | Foglio di calcoloML| Collegamento ipertestuale|
|12434 | grafico| GradientFill|
|12477 | xlsx| Celle luminose|
|12493 | xlsx| Leggi Formattazione condizionale|
|12498 | grafico| Collezione ChartPoints e LegendEntries|
|12575 | grafico| La dimensione di PlotArea|
|12576 | grafico|ErrorBar|
|12622 | xlsx| Leggi la formula condivisa|
|12625 | xlsx| Leggi il grafico|
|12667 | xls| Valore data/ora|
|12684 | CSV| Leggi il numero|
|12717 | xls| Immagine con Mac OS|
|12727 | xls| Leggi le proprietà del documento|
|12750 | xls| Ottieni il collegamento ipertestuale della forma|
|12870 | xlsx| Leggi l'oggetto di disegno|
|12880 | Grafico2Immagine| Disegna grafico|
|12894 | Tabella pivot| metodo addCalculateField()|
|12915 | xlsx| Salva valore stringa|
|12957 | Foglio di calcoloML| Salva le proprietà del documento|
|12971 | xls| Proprietà VeryHidden del foglio di lavoro|
|13012 | Grafico2Immagine| Carattere non supportato in un ambiente speciale|
|13101 | xlsx| Leggere PageSetup e stile|
|13270 | xls| Forma della posizione|
|13385 | xls| Copia filtro automatico|
|13386 | xlsx| Salva il file xlsx|
|13403 | xls| Salva lo stile|
|13418 | xls| Leggi filtro automatico|
|13448 | Marcatore intelligente| Limite di record per l'origine dati ResultSet|
|13614 | xlsx| Immagine in PageSetup|
|13639 | xls| Crea casella di testo|
|13679 | xlsx| Leggi il file xlsx con lo strumento zip di Apache|
|13725 | grafico| Copia asse|
|13735 | xls| Formule di FormatConditions/Validazioni|
|13736 | xls| Formato data|
|13821 | xls| Prestazioni di creazione Commento|
|14056 | grafico| Riempimento sfumato|
|14108 | xls| Copia interruzioni di pagina|
|14116 | xls| Elimina dati|
|14146 | Grafico2Immagine| Grafico2Immagine|
|14246 | xls| Copia PageSetup|


 Cambiamenti notevoli per gli utenti:



Nelle versioni precedenti, i metodi Cell.getStyle()/Row.getStyle()/Column.getStyle() potrebbero far sì che Cell/Row/Column mantengano il proprio oggetto Style. La successiva modifica dell'oggetto Style restituito per getStyle() cambierà direttamente lo stile di Cell/Row/Column.

 Da questa versione, tutti gli oggetti Style impostati su Cell/Row/Column verranno raccolti per considerazioni sulle prestazioni e Cell/Row/Column manterranno solo un riferimento di stile. La successiva modifica dell'oggetto Style restituito per getStyle() non cambierà lo stile di Cell/Row/Column. Per rendere effettiva la modifica, gli utenti devono chiamare setStyle() per Cell/Row/Column dopo che lo stile è stato modificato.

Questa regola è richiesta anche per i metodi Style.getFont()/getColor()/getPatternColor()/getBorderColor(). Nelle vecchie versioni, la modifica dell'oggetto Font/Color restituito poteva causare direttamente il cambio di stile. Nella nuova versione, dopo aver apportato modifiche all'oggetto Font/Color, gli utenti devono chiamare Style.setFont()/setColor()/setPatternColor()/setBorderColor() per rendere effettiva la modifica.
