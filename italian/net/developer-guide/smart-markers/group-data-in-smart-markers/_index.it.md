---
title: Come Raggruppare Dati in Smart Markers
type: docs
weight: 30
url: /it/net/how-to-group-data-in-smart-markers/
---

## **Possibili Scenari di Utilizzo**
In alcuni report Excel potrebbe essere necessario suddividere i dati in gruppi per renderli più facili da leggere e analizzare. Uno dei principali scopi per suddividere i dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ciascun gruppo di record

I marcatore intelligenti di Aspose.Cells ti consentono di raggruppare i dati per campi e inserire righe di riepilogo tra i set di dati o gruppi di dati. Ad esempio, se si raggruppano i dati per Customers.CustomerID, è possibile aggiungere un record di riepilogo ogni volta che cambia il gruppo

## **Parametri di Raggruppamento Dati in Smart Markers**
Di seguito sono riportati alcuni dei parametri di smart marker utilizzati per raggruppare i dati.
### **group:normal/merge/repeat**
Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- **normale** - Il valore del campo di raggruppamento non viene ripetuto per i record corrispondenti nella colonna; invece vengono stampati una volta per gruppo di dati.
- **unire** - Lo stesso comportamento del parametro normale, eccetto che unisce le celle nel campo di raggruppamento per ciascun insieme di gruppi.
- **ripetere** - Il valore del campo di raggruppamento viene ripetuto per i record corrispondenti.

Ad esempio: &=Customers.CustomerID(gruppo:unire)
### **skip**
Salta un numero specificato di righe dopo ciascun gruppo.

Ad esempio, &=Employees.EmployeeID(gruppo:normale,saltare:1)
### **subtotalN**
Esegue un'operazione di riepilogo per un dato campo relativo a un campo di raggruppamento. La N rappresenta i numeri tra 1 e 11 che specificano la funzione utilizzata nel calcolo dei subtotali all'interno di un elenco di dati. (1=MEDIA, 2=CONTATORE, 3=CONT.VALORI, 4=MASSIMO, 5=MINIMO,...9=SOMMA ecc.) Consultare il riferimento Subtotali nell'aiuto di Microsoft Excel per ulteriori dettagli.

Il formato effettivo viene specificato come:
subtotalN:Rif dove Rif si riferisce alla colonna di raggruppamento.

Ad esempio,

- &=Products.Units(subtotal9:Products.ProductID) specifica la funzione di riepilogo sul campo **Units** rispetto al campo **ProductID** nella tabella **Products**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) specifica la funzione di riepilogo sul campo **Col3** raggruppato per **Col1** nella tabella **Tabx**.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specifica la funzione di riepilogo sul campo **ColumnD** raggruppato per **ColumnA** e **ColumnB** nella tabella **Table1**.

## **Come Raggruppare Dati in Smart Markers**

Questo esempio mostra alcuni dei parametri di raggruppamento in azione. Utilizza il database Microsoft Access Northwind.mdb ed estrae i dati dalla tabella chiamata "Dettagli ordine". Creiamo un file designer chiamato SmartMarker_Designer.xls in Microsoft Excel e inseriamo smart marker in varie celle nei fogli di lavoro. I marker vengono elaborati per riempire i fogli di lavoro. I dati sono collocati e organizzati da un campo di raggruppamento.

Il file designer ha due fogli di lavoro. Nel primo mettiamo smart marker con parametri di raggruppamento come mostrato nello screenshot qui sotto. Sono collocati tre smart marker (con parametri di raggruppamento):
&=[Order Details].OrderID(group:merge,skip:1),
&=[Dettagli Ordine].Quantità(subtotale9:Dettagli Ordine.IDOrdine), e
&=[Dettagli Ordine].PrezzoUnitario(subtotale9:Dettagli Ordine.IDOrdine) vanno in A5, B5 e C5 rispettivamente.

|**Il primo foglio di lavoro nel file SmartMarker_Designer.xls, completo di smart markers**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
Nel secondo foglio di lavoro del file del designer, inseriamo alcuni altri smart marker come mostrato nella figura sottostante. Collochiamo i seguenti smart marker:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), e
&=subtotale9:Dettagli Ordine.IDOrdine in A5, B5, C5, D5 e C6 rispettivamente.

|**Il secondo foglio di lavoro del file SmartMarker_Designer.xls, mostrando smart markers misti.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Qui è riportato il codice sorgente utilizzato nell'esempio.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Se hai bisogno di aggiungere le tue etichette personalizzate alle righe riepilogative o desideri concatenare il nome del campo con un'etichetta, ad esempio "Subtotale degli Ordini", Aspose.Cells fornisce gli attributi Label e LabelPosition, in modo da poter inserire le tue etichette personalizzate nei Smart Marker mentre concateni con le righe di subtotali nei dati di raggruppamento. Consulta il documento su come Aggiungere Etichette Personalizzate per Concatenare con le Righe di Subtotale nei Smart Markers per ulteriori riferimenti.

{{% /alert %}} 
