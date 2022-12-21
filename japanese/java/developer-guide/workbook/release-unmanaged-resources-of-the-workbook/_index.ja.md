---
title: ワークブックの管理されていないリソースを解放する
type: docs
weight: 290
url: /ja/java/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}} 

Aspose.Cells提供[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\) ) メソッドのアンマネージ リソースを解放する[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)物体。 Dispose パターンは、ファイルおよびパイプ ハンドル、レジストリ ハンドル、待機ハンドル、またはアンマネージ メモリのブロックへのポインターなど、アンマネージ リソースにアクセスするオブジェクトに対してのみ使用されます。これは、ガベージ コレクターが未使用の管理対象オブジェクトを効率的に再利用できるが、管理されていないオブジェクトを再利用できないためです。

{{% /alert %}} 
## **ワークブックの管理されていないリソースを解放する**
次のサンプル コードは、[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
