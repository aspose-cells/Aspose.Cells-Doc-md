---
title: Использование CustomImplementationFactory для создания пользовательской реализации потока памяти
type: docs
weight: 40
url: /ru/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет API с названием [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory), которое позволяет пользователю предоставить пользовательскую реализацию, такую как использование реализации памяти Recyclable вместо стандартного MemoryStream.

## **Использование CustomImplementationFactory для создания пользовательской реализации потока памяти**

Нижеприведенный образец кода иллюстрирует, как использовать [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) в вашей программе. Иногда в вашей системе достаточно памяти, но память не является непрерывной. Объекты Memory Stream используют непрерывную память, но вы можете предоставить реализацию Memory Stream таким образом, что он будет использовать непрерывную память.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
