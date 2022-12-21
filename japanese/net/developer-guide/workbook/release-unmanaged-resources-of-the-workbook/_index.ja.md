---
title: ワークブックの管理されていないリソースを解放する
type: docs
weight: 310
url: /ja/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

Aspose.Cells提供[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose)のアンマネージ リソースを解放するメソッド[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)物体。 Dispose パターンは、ファイルおよびパイプ ハンドル、レジストリ ハンドル、待機ハンドル、またはアンマネージ メモリのブロックへのポインターなど、アンマネージ リソースにアクセスするオブジェクトに対してのみ使用されます。これは、ガベージ コレクターが未使用の管理対象オブジェクトを効率的に再利用できるが、管理されていないオブジェクトを再利用できないためです。

{{% /alert %}}

[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)オブジェクトが実装するようになりました*System.IDisposable*単一のメソッドを持つインターフェース[**廃棄（）**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) .直接呼び出すこともできます[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose)メソッドまたはあなたが使用することができます*使用する*このメソッドを自動的に呼び出すステートメント。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
