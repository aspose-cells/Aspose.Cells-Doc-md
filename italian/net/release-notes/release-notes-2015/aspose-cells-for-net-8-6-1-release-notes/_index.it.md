---
title: Aspose.Cells for .NET 8.6.1 Note di rilascio
type: docs
weight: 30
url: /it/net/aspose-cells-for-net-8-6-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.6.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.1/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-43905) - Supporto per modificare l'attributo di destinazione del collegamento ipertestuale HTML in "_blank"

 (CELLSNET-43885) - Possibilità di recuperare la ConnectionString di ExternalConnection di tipo WebQuery

 (CELLSNET-43935) - Ignora la colonna nascosta con ExportTableOptions.PlotVisibleColumns impostato su true

 (CELLSNET-43925) - Aggiunta di un riferimento alle macro VBA nella cartella di lavoro


## **Miglioramenti**


 (CELLSNET-43933) - Cell.Formula può accettare una formula non valida e API prova a correggerla

 (CELLSNET-43476) - API necessario per verificare se la licenza è caricata o meno

 (CELLSNET-43310) - Ridenominazione di nomi di fogli di lavoro duplicati durante la combinazione di cartelle di lavoro

 (CELLSNET-42518) - Possibilità di accedere a oggetti secondari tramite marcatori intelligenti


## **Insetti**


 (CELLSNET-43946) - Cell.HtmlString restituisce una stringa che esegue il rendering della stringa normale come pedice

(CELLSNET-43941) - Il grafico non viene generato correttamente

 (CELLSNET-43936) - Mostra le chiavi della legenda anche se Chart.ChartDataTable.ShowLegendKey è impostato su false

 (CELLSNET-43991) - La rimozione dei fogli di lavoro danneggia l'XLSX risultante

 (CELLSNET-43988) - La password da modificare viene persa quando XLSX viene nuovamente salvato con Aspose.Cells

 (CELLSNET-43984) - La password da modificare viene convertita in password da aprire quando XLSM viene nuovamente salvato

 (CELLSNET-43983) - La password da modificare viene convertita in password da aprire quando XLSX viene nuovamente salvato

 (CELLSNET-43982) - La password da modificare viene convertita in password da aprire quando XLTM viene nuovamente salvato

 (CELLSNET-43981) - La password da modificare viene persa quando XLTM viene nuovamente salvato

 (CELLSNET-43980) - La password da modificare viene convertita in password da aprire quando XLTX viene nuovamente salvato

 (CELLSNET-43979) - Carattere SetStyle non applicato per alcuni tipi di carattere

 (CELLSNET-43977) - La password da modificare viene persa quando XLTX viene nuovamente salvato con Aspose.Cells

 (CELLSNET-43976) - Tentativi multipli di aprire XLSX protetto da password

(CELLSNET-43973) - La password da modificare viene persa dopo il nuovo salvataggio di XLSM

 (CELLSNET-43968) - L'applicazione Excel consiglia di aprire l'XLSB risultante in sola lettura

 (CELLSNET-43967) - L'XLT protetto da password si danneggia dopo il nuovo salvataggio

 (CELLSNET-43966) - La formula ISNONTEXT restituisce il valore errato dopo CalculateFormula

 (CELLSNET-43965) - DetectFileFormat(FileStream) consuma molta memoria per il file zip

 (CELLSNET-43951) - La password da modificare viene persa nei file OOXML

 (CELLSNET-43950) - Problemi di identificazione della protezione in Aspose.Cells

 (CELLSNET-43944) - La dimensione dell'immagine non è corretta e cambia dopo il ripristino

 (CELLSNET-43943) - Impossibile leggere l'apice dal carattere della cella

 (CELLSNET-43940) - Cella errata selezionata all'apertura del report

 (CELLSNET-43931) - L'eliminazione di righe dall'intervallo denominato danneggia l'XLSX risultante

 (CELLSNET-43928) - Il valore DocumentProperty Author viene letto incompleto

(CELLSNET-43927) - #REF nella formula che fa riferimento all'oggetto elenco in un altro foglio di lavoro

 (CELLSNET-43891) - Problema delle operazioni Workbook.VBAProject.Modules

 (CELLSNET-43737) - FileFormatInfo.IsEncrypted ha un valore errato per i formati legacy

 (CELLSNET-42120) - Valore DisplayStringValue non corretto in alcuni scenari

 (CELLSNET-42110) - I bordi impostati per gli intervalli in XLSX non vengono visualizzati nel PDF


## **Eccezioni**


 (CELLSNET-43932) - Errore da forma a immagine! durante il rendering di un foglio di calcolo in PDF

 (CELLSNET-43964) - Il recupero dello stile di visualizzazione di tutte le celle genera un'eccezione IndexOutOfRangeException

 (CELLSNET-43926) - CellsException in Workbook.CalculateFormula

 (CELLSNET-43911) - CellsException in Workbook.Save

 (CELLSNET-43930) - Il metodo GetNamedRanges() genera l'eccezione Domain First Chance

 (CELLSNET-43918) - Eccezione all'apertura del file modello XLSX



\2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-44004) - Supporto per caricare e salvare file SpreasheetML(XML) - GridDesktop


## **Miglioramenti**


(CELLSNET-43873) - Vecchio codice in - Formattazione di un intervallo di Cells - l'articolo non funziona


## **Insetti**


 (CELLSNET-43997) - La cella attiva nel foglio non si trova nella posizione corretta durante il caricamento/salvataggio di un file XLSX - GridWeb

 (CELLSNET-43993) - Errore C2686 durante la compilazione di VS2008 C++ con griddesktop.dll

 (CELLSNET-43986) - WebWorksheet o GridWorkSheet non hanno il metodo SetReadonlyRange

 (CELLSNET-43970) - Problema di regressione durante l'aggiornamento da 8.4.2.0 a 8.6.0

 (CELLSNET-43952) - LoadValueList API manca nella classe Aspose.Cells.GridWeb.Validation

 (CELLSNET-43859) - Cell riempito con il colore giallo non viene esportato nel file XLSX


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge enum HtmlLinkTargetType e HtmlSaveOptions.LinkTargetType.

 Viene utilizzato per impostare il tipo di attributo di destinazione in HTML
