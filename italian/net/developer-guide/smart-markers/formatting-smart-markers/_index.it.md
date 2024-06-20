---
title: Formattazione dei marcatore intelligenti
type: docs
weight: 20
url: /it/net/formatting-smart-markers/
---

## **Copia dell'attributo di stile**
A volte, quando si utilizzano i marcatore intelligenti, si desidera copiare lo stile della cella che contiene i tag del marcatore intelligente. È possibile utilizzare l'attributo CopyStyle dei tag del marcatore intelligente a tale scopo.
### **Copia degli stili dalle celle con i marcatore intelligenti**
Questo esempio utilizza un semplice file di modello di Microsoft Excel con due marcatori nelle celle A2 e B2. Il marcatore incollato nella cella B2 utilizza l'attributo CopyStyle, mentre il marcatore nella cella A2 non lo fa. Applica formattazione semplice (ad esempio, imposta il colore del font su **rosso** e imposta il colore di riempimento della cella su **giallo**).

Durante l'esecuzione del codice, Aspose.Cells copia la formattazione in tutti i record della colonna B ma non mantiene la formattazione nella colonna A.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Aggiunta di etichette personalizzate**
### **Introduzione**
Mentre si lavora con la funzionalità di raggruppamento dei dati degli Smart Markers, a volte è necessario aggiungere le proprie etichette personalizzate alla riga di riepilogo. Si desidera anche concatenare il nome della colonna con tale etichetta, ad esempio "Totale parziale degli ordini". Aspose.Cells fornisce attributi Label e LabelPosition, in modo da poter inserire le etichette personalizzate negli Smart Markers mentre concateni le righe di subtotalizzazione nei dati di raggruppamento.
### **Aggiunta di etichette personalizzate da concatenare con le righe di subtotalizzazione negli Smart Markers**
Questo esempio utilizza un [file di dati](96927971.xlsx) e un [file di modello](96927972.xlsx) con alcuni marker nelle celle. Durante l'esecuzione del codice, Aspose.Cells aggiunge alcune etichette personalizzate alle righe di riepilogo per i dati raggruppati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
