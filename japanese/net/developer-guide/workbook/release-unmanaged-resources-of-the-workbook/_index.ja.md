---
title: ブックのアンマネージリソースを解放する
type: docs
weight: 310
url: /ja/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cellsは、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) オブジェクトのアンマネージリソースを解放するための [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) メソッドを提供しています。Disposeパターンは、ファイルやパイプハンドル、レジストリハンドル、待機ハンドル、またはアンマネージメモリブロックへのポインタなど、アンマネージリソースにアクセスするオブジェクトにだけ使用されます。これは、ガベージコレクタが未使用の管理オブジェクトを効率的に回収することができる一方で、アンマネージオブジェクトを回収することができないためです。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) オブジェクトは現在、*System.IDisposable* インターフェイスを実装しており、単一のメソッド [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) を持っています。[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) メソッドを直接呼び出すか、*Using* ステートメントを使用してこのメソッドを自動的に呼び出すことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
