---
title: Использование CustomImplementationFactory для создания пользовательской реализации Memory Stream
type: docs
weight: 40
url: /ru/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **Возможные сценарии использования**

 Aspose.Cells предоставил имя API[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)который позволяет пользователю предоставить пользовательскую реализацию, такую как использование реализации Recyclable memory вместо MemoryStream по умолчанию.

## **Использование CustomImplementationFactory для создания пользовательской реализации Memory Stream**

В следующем примере кода показано, как использовать[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)в вашей программе. Иногда в вашей системе достаточно памяти, но память не является непрерывной. Объекты Memory Stream используют непрерывную память, но вы можете реализовать реализацию Memory Stream таким образом, чтобы вместо этого он использовал несмежную память.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
