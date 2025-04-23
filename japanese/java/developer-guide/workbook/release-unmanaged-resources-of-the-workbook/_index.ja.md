---
title: ブックのアンマネージリソースを解放する
type: docs
weight: 290
url: /ja/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cellsは [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) メソッドを提供しており、これを使用して [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) オブジェクトの管理外リソースを解放します。この dispose パターンは、ファイルやパイプハンドル、レジストリハンドル、待機ハンドル、または未管理メモリのブロックへのポインタなど、管理外リソースにアクセスするオブジェクトのみに適用されます。ガベージコレクターは未使用の管理されたオブジェクトの回収に非常に効率的ですが、未管理オブジェクトの回収はできません。

{{% /alert %}} 
## **ブックのアンマネージリソースを解放する**
このサンプルコードは [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) メソッドの使い方を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
