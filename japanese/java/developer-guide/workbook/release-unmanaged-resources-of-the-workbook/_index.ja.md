---
title: ブックのアンマネージリソースを解放する
type: docs
weight: 290
url: /ja/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\))メソッドを提供しており、[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)オブジェクトのアンマネージリソースを解放します。 disposeパターンは、ファイルやパイプハンドル、レジストリハンドル、ウェイトハンドル、アンマネージメモリブロックへのポインタなど、アンマネージリソースにアクセスするオブジェクトにのみ使用されます。これは、ガベージコレクタが未使用の管理オブジェクトを効率的に回収できるが、アンマネージオブジェクトを回収できないためです。

{{% /alert %}} 
## **ブックのアンマネージリソースを解放する**
以下のサンプルコードは、[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\))メソッドの使用方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
