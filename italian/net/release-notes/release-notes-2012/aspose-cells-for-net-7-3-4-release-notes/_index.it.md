---
title: Aspose.Cells for .NET 7.3.4 Note di rilascio
type: docs
weight: 10
url: /it/net/aspose-cells-for-net-7-3-4-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 7.3.4](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.3.4/)

{{% /alert %}} 

 Siamo felici di annunciare Aspose.Cells for .NET v7.3.4!



\1) Aspose.Cells 



 Nuove caratteristiche

- Supporta grafici Open Office 3D
- Calcola la media ponderata sulla riga Subtotale tra due colonne (SmartMarkers)
- Rileva l'origine dati verticale o orizzontale di un grafico



 Miglioramenti

- Trova e sostituisci testi interni



 Prestazione

- Il metodo CalculateFormula della cartella di lavoro richiede più di 30 secondi
- Degrado delle prestazioni per Office 2007 rispetto al 2003

 -CalculateFormula impiega circa 3 minuti su una macchina 8 Core

- Aspose Cell sostituendo Excel Wrapper
- Il salvataggio di un documento Excel richiede più di un minuto



 Eccezioni

- Eccezione "formula non valida" all'apertura di un file XLSX
- Aspose.Cells genera l'eccezione "ArgumentNullException" all'apertura di un file modello
- Salvare un file MHtml, leggere in Aspose.Cells è un problema



 Insetti

- La formula non è calcolata correttamente
- I controlli ActiveX danneggiano una cartella di lavoro
- 4 I fogli di calcolo non possono essere riscritti
- I grafici di Excel sono bloccati dopo il salvataggio
- Errore durante la copia dei fogli di lavoro

 -Immagine del grafico radar riempita resa con segni di spunta dell'asse nascosti tramite il metodo Chart.ToImage

 -Problema di formattazione delle etichette dei dati

- Problema con il calcolo del grafico di Excel
- Problema con un istogramma con entrambi gli assi
- Più campi pivot calcolati generano un file illeggibile.
- Problema con le parti XML personalizzate
- Questo file è danneggiato dopo essere stato salvato

 -La conversione di XLS in XLSX e viceversa crea un file XLS non valido

 -La conversione di XLS in XLSX crea un documento non valido

- Il rendering di un file MS Excel in un documento PDF presenta un problema relativo ai contenuti



 \2) ReteWeb



 Insetti

40838 - GridWeb - Formattazione non salvata correttamente

 41140 - Problema durante l'utilizzo dell'opzione "Aggiungi riga".

 41152 - Quando si modifica Aspose.Cells.GridWeb, la cella salta quando viene selezionata

 41154 - Problema di rendering sul controllo GridWeb

 41149 - Evidenzia il problema con il controllo GridWeb

41183 - 

 41126 - GridWeb Cell'sstyle BorderWidth problema



 \3) GridDesktop



 Insetti

 40709 - Problema di rendering di GridDesktop

41098 - Cell Problema di protezione/blocco con GridDesktop
