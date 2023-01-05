---
title: Uso de CustomImplementationFactory para crear una implementación personalizada de Memory Stream
type: docs
weight: 40
url: /es/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **Posibles escenarios de uso**

 Aspose.Cells ha proporcionado un API llamado[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)lo que permite al usuario proporcionar una implementación personalizada, como el uso de la implementación de memoria reciclable en lugar del MemoryStream predeterminado.

## **Uso de CustomImplementationFactory para crear una implementación personalizada de Memory Stream**

El siguiente código de ejemplo ilustra cómo hacer uso de[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)en tu programa A veces, hay suficiente memoria en su sistema pero la memoria no es contigua. Los objetos de Memory Stream usan memoria contigua, pero puede proporcionar la implementación de Memory Stream de tal manera que use la memoria no contigua en su lugar,

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
