---
title: Uso de CustomImplementationFactory para crear implementación personalizada de Memory Stream
type: docs
weight: 40
url: /es/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Escenarios de uso posibles**

Aspose.Cells ha proporcionado una API llamada [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) que permite al usuario proporcionar una implementación personalizada, como usar una implementación de memoria reciclable en lugar de MemoryStream predeterminado.

## **Uso de CustomImplementationFactory para crear implementación personalizada de Memory Stream**

El siguiente código de ejemplo ilustra cómo hacer uso de [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) en su programa. A veces, hay suficiente memoria en su sistema pero la memoria no es contigua. Los objetos de Memory Stream utilizan memoria contigua, pero puede proporcionar la implementación de Memory Stream de tal manera que use la memoria no contigua en su lugar.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
