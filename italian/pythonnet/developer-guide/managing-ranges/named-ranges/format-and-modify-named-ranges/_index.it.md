---
title: Formattare e modificare intervalli con nome
type: docs
weight: 85
url: /it/python-net/format-and-modify-named-ranges/
description: Questo articolo mostra come formattare e modificare gli intervalli con nome tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Python Excel, Formattare e modificare gli intervalli con nome in Python, Impostare il colore di sfondo e gli attributi del carattere a un intervallo con nome in Python, Aggiungere i bordi a un intervallo con nome in Python, Rinominare un intervallo con nome in Python, Unione di intervalli in Python, Intersezione di intervalli in Python, Unire le celle nell intervallo con nome in Python.
---

## **Formattare intervalli**

### **Come impostare il colore di sfondo e gli attributi del carattere a un intervallo con nome**

Per applicare la formattazione, definire un oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) per specificare le impostazioni dello stile e applicarlo all'oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

Nell'esempio seguente viene mostrato come impostare il colore di riempimento solido (colore ombreggiatura) con impostazioni del carattere a un intervallo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **Come aggiungere i bordi a un intervallo con nome**

È possibile aggiungere i bordi a un intervallo di celle invece che a una singola cella. L'oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) fornisce un metodo [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor) che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- Tipo di bordo, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- Stile della linea, lo stile della linea, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- Colore, il colore della linea, selezionato dall'enumerazione Colore.

L'esempio seguente mostra come impostare un bordo di contorno a un intervallo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **Come rinominare un intervallo con nome**

Aspose.Cells ti consente di rinominare un intervallo con nome secondo le tue esigenze. Puoi ottenere l'intervallo con nome e rinominarlo usando l'attributo [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text). Nell'esempio seguente viene mostrato come rinominare un intervallo con nome.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **Come eseguire l'unione degli intervalli**

Aspose.Cells fornisce il metodo [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) per eseguire l'unione degli intervalli. L'esempio seguente mostra come eseguire l'unione degli intervalli.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **Come intersecare gli intervalli**

Aspose.Cells fornisce il metodo [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) per intersecare due intervalli. Il metodo restituisce un oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Per verificare se un intervallo interseca un altro intervallo, utilizzare il metodo [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) che restituisce un valore booleano. L'esempio seguente mostra come intersecare gli intervalli.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **Come unire le celle nell'intervallo con nome**

Aspose.Cells fornisce il metodo [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) per unergere le celle nell'intervallo. Nell'esempio seguente viene mostrato come unire le celle individuali di un intervallo nominato.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
