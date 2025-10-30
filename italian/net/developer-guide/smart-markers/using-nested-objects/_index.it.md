---
title: Importazione intelligente di oggetti annidati in Excel con Smart Markers
type: docs
weight: 30
url: /it/net/how-to-import-nested-objects-with-smart-markers/
---

## **Perché usare oggetti annidati per Smart Markers**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. Rappresentazione dei dati gerarchici: i dati del mondo reale sono intrinsecamente annidati (ad esempio, un Ordine contiene un Cliente, che ha un Indirizzo). Gli oggetti annidati rispecchiano questa struttura, evitando campi appiattiti/artificiali come customer_city.
2. Evitare collisioni di nomi: le strutture piatte rischiano di causare conflitti (ad esempio, product_name vs. supplier_name). La nidificazione delimita i nomi in modo naturale:
<<product.name>> vs. <<supplier.name>>.
3. Modularità & Riutilizzabilità: riutilizzo di sub-oggetti in diversi contesti, l’oggetto Indirizzo può essere incorporato in marcatori Cliente, Fornitore o Dipendente. Le modifiche a Indirizzo si propagano ovunque.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. Supporto Framework/Strumenti: motori moderni (ad esempio Handlebars, React, FoxPro) risolvono nativamente percorsi annidati. Si allinea con JSON/APIs dove i dati annidati sono standard.

## **Come importare tipi anonimi o oggetti personalizzati con Smart Markers**
Aspose.Cells supporta anche tipi anonimi o oggetti personalizzati in smart markers. L'esempio seguente mostra come funziona. Per l'importazione di dati da oggetti dinamici utilizzando Smart Markers, visita il seguente articolo:

[Importare da oggetto dinamico come origine dati](/cells/it/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **Come importare oggetti annidati con Smart Markers**
Aspose.Cells supporta oggetti annidati in smart markers, gli oggetti annidati devono essere semplici. Utilizziamo un file di modello semplice. Vedi il foglio di calcolo del designer che contiene alcuni smart markers annidati.

|**Il primo foglio di calcolo del file SM_NestedObjects.xlsx mostra smart markers annidati.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
L'esempio seguente mostra come funziona.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Come importare una lista generica come oggetto annidato con Smart Markers**
Aspose.Cells ora supporta anche l'utilizzo di una lista generica come oggetto annidato. Si prega di controllare lo screenshot del file Excel di output generato con il codice sottostante. Come si può vedere nello screenshot, un oggetto Teacher contiene più oggetti Student annidati.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **Come importare oggetti annidati non riga per riga con Smart Markers**
Il metodo di elaborazione predefinito attuale prevede di elaborare gli smart marker linea per linea. Ma a volte gli smart marker della stessa tabella dati devono essere elaborati insieme, indipendentemente dal fatto che siano nella stessa riga o meno, quindi è necessario specificare un intervallo con nome "_CellsSmartMarkers" e specificare WorkbookDesigner.LineByLine come falso prima di chiamare l'elaborazione. 
se sono nella stessa riga o meno, allora devi specificare un intervallo denominato "_CellsSmartMarkers" e specificare WorkbookDesigner.LineByLine come falso prima di chiamare l'elaborazione.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
