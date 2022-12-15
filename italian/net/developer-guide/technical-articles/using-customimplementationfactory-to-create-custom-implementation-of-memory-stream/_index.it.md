---
title: Utilizzo di CustomImplementationFactory per creare un'implementazione personalizzata di Memory Stream
type: docs
weight: 40
url: /it/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **Possibili scenari di utilizzo**

 Aspose.Cells ha fornito un'API denominata[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)che consente all'utente di fornire un'implementazione personalizzata come l'utilizzo dell'implementazione della memoria riciclabile invece del MemoryStream predefinito.

## **Utilizzo di CustomImplementationFactory per creare un'implementazione personalizzata di Memory Stream**

Il seguente codice di esempio illustra come utilizzare[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)nel tuo programma. A volte, c'è abbastanza memoria nel tuo sistema ma la memoria non è contigua. Gli oggetti Memory Stream utilizzano la memoria contigua ma puoi fornire l'implementazione di Memory Stream in modo tale che utilizzi invece la memoria non contigua,

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
