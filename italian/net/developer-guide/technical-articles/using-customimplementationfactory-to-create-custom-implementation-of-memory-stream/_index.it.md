---
title: Utilizzo di CustomImplementationFactory per creare un implementazione personalizzata di MemoryStream
type: docs
weight: 40
url: /it/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ha fornito un'API chiamata [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) che consente all'utente di fornire un'implementazione personalizzata come l'uso di un'implementazione della memoria riciclabile invece della MemoryStream predefinita.

## **Utilizzo di CustomImplementationFactory per creare un'implementazione personalizzata di MemoryStream**

Il codice di esempio seguente illustra come fare uso di [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) nel tuo programma. A volte, c'è abbastanza memoria nel tuo sistema ma la memoria non è contigua. Gli oggetti MemoryStream utilizzano memoria contigua ma puoi fornire l'implementazione di MemoryStream in modo che utilizzi invece la memoria non contigua

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
