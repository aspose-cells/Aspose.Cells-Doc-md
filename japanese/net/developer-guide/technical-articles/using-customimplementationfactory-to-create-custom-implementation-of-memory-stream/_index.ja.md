---
title: CustomImplementationFactory を使用してメモリ ストリームのカスタム実装を作成する
type: docs
weight: 40
url: /ja/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **考えられる使用シナリオ**

Aspose.Cells は API という名前の[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)これにより、ユーザーは、デフォルトの MemoryStream の代わりに Recyclable メモリ実装を使用するなど、カスタム実装を提供できます。

## **CustomImplementationFactory を使用してメモリ ストリームのカスタム実装を作成する**

次のサンプル コードは、[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)あなたのプログラムで。システムに十分なメモリがあっても、メモリが連続していない場合があります。メモリ ストリーム オブジェクトは連続したメモリを使用しますが、連続していないメモリを代わりに使用するような方法でメモリ ストリームの実装を提供できます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
