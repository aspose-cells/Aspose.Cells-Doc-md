---
title: Formatta e modifica gli intervalli denominati
type: docs
weight: 85
url: /it/net/format-and-modify-named-ranges/
---
## **Intervalli di formati**

### **Impostazione del colore di sfondo e degli attributi dei caratteri su un intervallo denominato**

 Per applicare la formattazione, definire a[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto per specificare le impostazioni di stile e applicarlo al[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range)oggetto.

L'esempio seguente mostra come impostare il colore di riempimento a tinta unita (colore di ombreggiatura) con le impostazioni del carattere su un intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Aggiunta di bordi a un intervallo denominato**

 È possibile aggiungere bordi a un intervallo di celle invece che a una singola cella. Il[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range) oggetto fornisce a[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)metodo che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

-  Tipo di bordo, il tipo di bordo, selezionato da[**Tipo di bordo**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)enumerazione.
-  Stile della linea, lo stile della linea, selezionato da[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumerazione.
- Color, il colore della linea, selezionato dall'enumerazione Color.

L'esempio seguente mostra come impostare un bordo del contorno su un intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

L'esempio seguente mostra come impostare i bordi intorno a ogni cella dell'intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Rinominare un intervallo denominato**

 Aspose.Cells ti consente di rinominare un intervallo denominato per le tue necessità. È possibile ottenere l'intervallo denominato e rinominarlo utilizzando[**Nome.Testo**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)attributo. L'esempio seguente mostra come rinominare un intervallo denominato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Unione delle gamme**

 Aspose.Cells fornisce[**Intervallo.Unione**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)metodo per prendere l'unione per gli intervalli, il metodo restituisce un[*Lista di array*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)oggetto. L'esempio seguente mostra come prendere l'unione per gli intervalli.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Intersezione di gamme**

 Aspose.Cells fornisce il[**Intervallo.Intersezione**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) metodo per intersecare due intervalli. Il metodo restituisce a[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range) oggetto. Per verificare se un intervallo interseca un altro intervallo, utilizzare il[**Intervallo.Intersezione**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)metodo che restituisce un valore booleano. L'esempio seguente mostra come intersecare gli intervalli.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Unisci Cells nell'intervallo denominato**

 Aspose.Cells fornisce[**Intervallo.Unisci()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)metodo per unire le celle nell'intervallo. L'esempio seguente mostra come unire le singole celle di un intervallo denominato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Rimuovi un intervallo denominato**

 Aspose.Cells fornisce il[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) metodo per cancellare il nome dell'intervallo. Per cancellare il contenuto dell'intervallo, utilizzare[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)metodo. L'esempio seguente mostra come rimuovere un intervallo denominato con il relativo contenuto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
