---
title: Formattazione dei marcatori intelligenti
type: docs
weight: 20
url: /it/net/formatting-smart-markers/
---
## **Copia attributo stile**
A volte, quando si utilizzano i marcatori intelligenti, si desidera copiare lo stile della cella che contiene i tag dei marcatori intelligenti. È possibile utilizzare l'attributo CopyStyle dei tag del marcatore intelligente per questo scopo.
### **Copia di stili da Cells con Smart Marker**
 Questo esempio utilizza un semplice file Excel modello Microsoft con due marcatori nelle celle A2 e B2. Il marcatore incollato nella cella B2 utilizza l'attributo CopyStyle, mentre il marcatore nella cella A2 no. Applicare una formattazione semplice (ad esempio, impostare il colore del carattere su**rosso** e imposta il colore di riempimento della cella su**giallo**).

Durante l'esecuzione del codice, Aspose.Cells copia la formattazione in tutti i record nella colonna B ma non mantiene la formattazione nella colonna A.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Aggiunta di etichette personalizzate**
### **introduzione**
Mentre si lavora con la funzione di raggruppamento dei dati di Smart Markers, a volte è necessario aggiungere le proprie etichette personalizzate alla riga di riepilogo. Vuoi anche concatenare il nome della colonna con quell'etichetta, ad esempio "Sub Total of Orders". Aspose.Cells ti fornisce gli attributi Label e LabelPosition, quindi puoi inserire le tue etichette personalizzate negli Smart Marker mentre concateni con le righe Subtotale nel raggruppamento dei dati.
### **Aggiunta di etichette personalizzate da concatenare con le righe del totale parziale negli indicatori intelligenti**
Questo esempio usa a[file di dati](96927971.xlsx) e un[file modello](96927972.xlsx) con pochi marcatori nelle cellule. Durante l'esecuzione del codice, Aspose.Cells aggiunge alcune etichette personalizzate alle righe di riepilogo per i dati raggruppati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
