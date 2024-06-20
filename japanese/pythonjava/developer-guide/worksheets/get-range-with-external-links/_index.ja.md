---
title: 外部リンクを含む範囲を取得
type: docs
weight: 60
url: /ja/python-java/get-range-with-external-links/
---

## **外部リンク付きの範囲を取得する**
Excel ファイルが他の Excel ファイルからデータにアクセスする場面は多々あります。Aspose.Cells for Python via Java では、[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) メソッドを使用してこれらの外部リンクを取得するオプションを提供します。[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) メソッドは、[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) タイプの配列を返します。[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) クラスは、[ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) プロパティを提供し、外部ファイルの名前を返します。

次のコードスニペットには、外部リンクの取得方法が示されています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
