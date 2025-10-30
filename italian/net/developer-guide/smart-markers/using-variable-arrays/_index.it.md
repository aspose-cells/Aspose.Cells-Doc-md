---
title: Importazione intelligente di array variabili in Excel con Smart Markers
type: docs
weight: 30
url: /it/net/how-to-import-variable-arrays-with-smart-markers/
---

## **Perché usare array variabili per Smart Markers**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. Ripetizione dinamica senza hardcoded: i marker statici falliscono per dati di lunghezza variabile (ad esempio, articoli dell'ordine, permessi utente). Gli array vengono iterati dinamicamente. 
2. Aggregazione semplificata: calcola somme, medie o filtri direttamente. Evita la logica manuale JavaScript/C# nei modelli.
3. Rappresentazione di dati tabulari/lista: adattamento naturale: tabelle, griglie e liste mappano intrinsecamente agli array.
4. Efficienza della memoria: gli array riducono la complessità dei modelli e il sovraccarico del data-binding.
5. Integrazione con API/Sorgenti dati: si allinea con dati JSON/centro array (ad esempio, API REST).

## **Come importare array variabili con Smart Markers**
Il seguente esempio di codice mostra come utilizzare array variabili nei marcatore intelligenti. Inseriamo un marcatore di array variabili nella cella A1 del primo foglio di lavoro del file Excel in modo dinamico che contiene una stringa di valori che impostiamo per il marcatore, elaboriamo i marcatori per riempire i dati nelle celle contro il marcatore. Infine, salviamo il file Excel


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **Come importare proprietà HTML con Smart Markers**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
