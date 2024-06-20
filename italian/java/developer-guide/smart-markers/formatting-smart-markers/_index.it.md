---
title: Formattazione dei marcatore intelligenti
type: docs
weight: 20
url: /it/java/formatting-smart-markers/
---

## **Copia dell'attributo di stile**
A volte, quando si utilizzano i marcatore intelligenti, si desidera copiare lo stile della cella che contiene i tag del marcatore intelligente. È possibile utilizzare l'attributo CopyStyle dei tag del marcatore intelligente a tale scopo.
### **Copia degli stili dalle celle con i marcatore intelligenti**
Questo esempio utilizza un semplice file di modello di Microsoft Excel con due marcatori nelle celle A2 e B2. Il marcatore incollato nella cella B2 utilizza l'attributo CopyStyle, mentre il marcatore nella cella A2 non lo fa. Applica formattazione semplice (ad esempio, imposta il colore del font su **rosso** e imposta il colore di riempimento della cella su **giallo**).

Questo esempio utilizza un [file di modello](template1.xlsx) con alcuni marcatori nelle celle. Quando si esegue il codice, Aspose.Cells copia la formattazione in tutti i record della colonna B ma non mantiene la formattazione nella colonna A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **Aggiunta di etichette personalizzate**
### **Introduzione**
Mentre si lavora con la funzionalità di raggruppamento dei dati degli Smart Markers, a volte è necessario aggiungere le proprie etichette personalizzate alla riga di riepilogo. Si desidera anche concatenare il nome della colonna con tale etichetta, ad esempio "Totale parziale degli ordini". Aspose.Cells fornisce attributi Label e LabelPosition, in modo da poter inserire le etichette personalizzate negli Smart Markers mentre concateni le righe di subtotalizzazione nei dati di raggruppamento.
### **Aggiunta di etichette personalizzate da concatenare con le righe di subtotalizzazione negli Smart Markers**
Questo esempio utilizza un [file di modello](template.xlsx) con alcuni markers nelle celle. Quando si esegue il codice, Aspose.Cells aggiunge alcune etichette personalizzate alle righe di riepilogo per i dati raggruppati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
