---
title: Formattare e modificare intervalli con nome
type: docs
weight: 85
url: /it/net/format-and-modify-named-ranges/
---

## **Formattare intervalli**

### **Impostazione del colore di sfondo e degli attributi del carattere su un intervallo nominato**

Per applicare la formattazione, definire un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) per specificare le impostazioni dello stile e applicarlo all'oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

Nell'esempio seguente viene mostrato come impostare il colore di riempimento solido (colore ombreggiatura) con impostazioni del carattere a un intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Aggiunta di bordi a un intervallo nominato**

È possibile aggiungere i bordi a un intervallo di celle invece che a una singola cella. L'oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) fornisce un metodo [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- Tipo di bordo, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- Stile della linea, lo stile della linea, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- Colore, il colore della linea, selezionato dall'enumerazione Colore.

L'esempio seguente mostra come impostare un bordo di contorno a un intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

Il seguente esempio mostra come impostare i bordi intorno ad ogni cella nell'intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Rinomina un intervallo nominato**

Aspose.Cells ti consente di rinominare un intervallo con nome secondo le tue esigenze. Puoi ottenere l'intervallo con nome e rinominarlo usando l'attributo [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text). Nell'esempio seguente viene mostrato come rinominare un intervallo con nome.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Unione di intervalli**

Aspose.Cells fornisce il metodo [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) per unire gli intervalli, il metodo restituisce un oggetto [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8). Nell'esempio seguente viene mostrato come unire gli intervalli.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Intersezione di intervalli**

Aspose.Cells fornisce il metodo [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) per intersecare due intervalli. Il metodo restituisce un oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Per verificare se un intervallo interseca un altro intervallo, utilizzare il metodo [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) che restituisce un valore booleano. L'esempio seguente mostra come intersecare gli intervalli.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Unisci celle nell'intervallo nominato**

Aspose.Cells fornisce il metodo [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) per unergere le celle nell'intervallo. Nell'esempio seguente viene mostrato come unire le celle individuali di un intervallo nominato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Rimuovere un intervallo nominato**

Aspose.Cells fornisce il metodo [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) per cancellare il nome dell'intervallo. Per cancellare il contenuto dell'intervallo, utilizzare il metodo [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index). Nell'esempio seguente viene mostrato come rimuovere un intervallo nominato con il suo contenuto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
