---
title: バージョン番号を確認
type: docs
weight: 80
url: /ja/python-java/check-version-number/
---

{{% alert color="primary" %}}

お使いのAspose.Cellsのバージョンを知りたいですか？ 当社は定期的に新しいAspose.Cellsのバージョンをリリースし、新機能を導入したり問題を修正したりしています。バージョン番号は、メジャー バージョン番号とマイナー バージョン番号、ホットフィックス バージョン番号で構成されます。各番号は0以上の整数である必要があります。書式は次のとおりです:

major.minor.hotfix

新しいAspose.Cellsのビルドをリリースすると、バージョン番号を更新します。

この記事では、システムにインストールされているAspose.Cellsのバージョンを手動で確認する方法とAspose.Cells APIを使用した方法について説明します。

{{% /alert %}}

## **バージョン番号を手動で確認する**

手動でAspose.Cellsのバージョンを確認するには:

1. Aspose.Cells.dllファイルを右クリックし、**プロパティ**を選択します。
1. バージョン（または詳細）タブをクリックしてバージョン番号を確認します。

## **Aspose.Cells APIを使用したバージョン番号の確認**

APIを介してAspose.Cellsの使用バージョンを確認するには、[CellsHelper](https://reference.aspose.com/cells/python-java/asposecells.api/cellshelper) クラスのGetVersion静的メソッドを使用して、Aspose.Cellsのバージョン番号を取得します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CheckVersionNumber.py" >}}
