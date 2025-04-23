---
title: カスタム実装のMemory Streamを作成するためのCustomImplementationFactoryを使用する
type: docs
weight: 40
url: /ja/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **可能な使用シナリオ**

Aspose.Cellsは、デフォルトのMemoryStreamの代わりにRecyclable memory実装などのカスタム実装を提供する [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) というAPIを提供しています。

## **CustomImplementationFactoryを使用してMemory Streamのカスタム実装を作成する**

次のサンプルコードは、プログラムで[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)を使用する方法を示しています。システムに十分なメモリがある場合でも、そのメモリが連続していないことがあります。Memory Streamオブジェクトは連続したメモリを使用しますが、非連続のメモリを使用するようにMemory Streamの実装を提供することも可能です。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
{{< app/cells/assistant language="csharp" >}}
