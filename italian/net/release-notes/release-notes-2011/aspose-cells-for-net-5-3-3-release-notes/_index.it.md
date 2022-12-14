---
title: Aspose.Cells for .NET 5.3.3 Note di rilascio
type: docs
weight: 70
url: /it/net/aspose-cells-for-net-5-3-3-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 5.3.3](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-5.3.3/)

{{% /alert %}} 
### **Siamo felici di annunciare Aspose.Cells for .NET v5.3.3!**
### **1) Aspose.Cells**
### **Miglioramenti**
 25032 Impostare l'attributo Destinazione collegamento ipertestuale durante la conversione di file Excel in formato Html

 25960 Renderizza le caselle di controllo nel file Html

 26082 Supporto dell'allineamento giustificato nel rendering del formato PDF

 26341 Miglioramento da Excel a Pdf per Mono

 26342 I collegamenti web esterni hanno alcuni strani caratteri allegati

 25332 Miglioramento di varie proprietà personalizzate nei documenti XLS, XLSX/XLSM

 26472 Supporto funzione/formula DEV.ST.S
### **Prestazione**
 25774 Conversione da Excel a PDF
### **Eccezioni**
 27076 Gestire FormatException durante l'apertura di un file ODS

 27063 Indice colonna non valido - Aspose.Cells.CellsException dal metodo SheetRender.ToImage()

 26571 Aspose.Cells non può aprire il file XLS

 26309 L'array di origine non era abbastanza lungo: eccezione all'apertura del file Excel

25972 Il metodo SheetRender.ToImage() non riesce a eseguire il rendering di alcuni fogli di lavoro
### **Insetti**
 26141 Rendering di un'immagine quasi vuota (dal metodo Chart.ToImage()), le linee tratteggiate non vengono visualizzate correttamente

 26570 Il titolo nel grafico L'immagine non viene visualizzata sul lato destro dell'area del grafico

 26601 Le etichette dei dati non sono visibili correttamente utilizzando la funzione Grafico su immagine

 26686 Nessun valore nell'immagine del grafico generato utilizzando la funzione Grafico a immagine

 18878 Riduce la dimensione del carattere durante il salvataggio in un file Pdf

 19318 Testo errato nell'esportazione PDF

 24011 Salva in Pdf (bug)

 26727 Diversi problemi durante il salvataggio del file Excel generato come PDF

 25920 Le tabelle pivot vengono danneggiate

 26100 L'impostazione RefreshDataOnOpeningFile non sembra funzionare

 26758 Tavolo girevole danneggiato con Aspose.Cells

 24961 Problema di danneggiamento dei file

 26198 Ottenere il valore massimo di ValueAxis in un grafico Excel

 26198 Un problema con i metodi PutValue e ClearContents

 26544 Problema con la copia di righe e la formattazione condizionale

26711 La cella calcolata ha "#VALORE!" dopo aver utilizzato il metodo Workbook.CalculateFormula()

 26728 Ottieni "#Valore!" nelle celle calcolate

 26984 Problema con il calcolo delle formule nei fogli di lavoro

 26308 La formula XLSB restituisce un valore diverso dalla formula XLSX

 25783 Il file Excel si apre con un avviso dopo l'utilizzo di Range.CopyValue per l'intestazione della tabella

 25797 ListObjectCollection.Add danneggia la formattazione nelle celle di intestazione

 25879 2007 Il file Excel posiziona una forma con zOrderPosition pari a 0 in cima

 25970 Rendering di testo alternativo nel file XLSX di MS Excel 2010

 26013 Casella di testo collegata Cell restituisce null

 26049 Inserire una nuova colonna in una tabella

 26313 Documento danneggiato dopo l'elaborazione con Aspose.Cells
### **2) Aspose.Cells.GridWeb**
### **Nuove caratteristiche**
26410 Espandi/Comprimi le righe raggruppate sui lati server e client
### **Eccezioni**
 26227 Gestire l'eccezione generata durante l'ottenimento del colore del numero con formattazione personalizzata
### **3) Aspose.Cells.GridDesktop**
### **Nuove caratteristiche**
 26545 Personalizza i caratteri utilizzati per visualizzare i nomi dei fogli di lavoro

 21788 Contrassegna alcuni passaggi di annullamento continui ed esegui operazioni di annullamento/ripristino in una volta sola

 27138 Copia formule da modelli Excel
### **Regressione**
 27139 Le catene di formule non vengono calcolate di conseguenza quando si modifica il valore di una cella
