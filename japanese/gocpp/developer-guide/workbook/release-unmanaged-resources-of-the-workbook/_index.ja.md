---
title: GolangとC++を使ってワークブックの未管理リソースを解放する
linktitle: ブックのアンマネージリソースを解放する
type: docs
weight: 310
url: /ja/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Aspose.Cellsを使用してGolangとC++経由でWorkbookの未管理リソースを解放する方法を学ぶ。
---

{{% alert color="primary" %}}

Aspose.Cellsは、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) オブジェクトのアンマネージリソースを解放するための [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) メソッドを提供しています。Disposeパターンは、ファイルやパイプハンドル、レジストリハンドル、待機ハンドル、またはアンマネージメモリブロックへのポインタなど、アンマネージリソースにアクセスするオブジェクトにだけ使用されます。これは、ガベージコレクタが未使用の管理オブジェクトを効率的に回収することができる一方で、アンマネージオブジェクトを回収することができないためです。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)オブジェクトは、単一のメソッド[**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/)を持つ*IDisposable*インターフェースを実装しています。[**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/)メソッドを直接呼び出すか、*Using*ステートメントを使用して自動的にこのメソッドを呼び出すことができます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
