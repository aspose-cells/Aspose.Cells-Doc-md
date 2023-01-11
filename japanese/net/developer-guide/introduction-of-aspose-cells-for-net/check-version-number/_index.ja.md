﻿---
title: バージョン番号の確認
type: docs
weight: 80
url: /ja/net/check-version-number/
---
{{% alert color="primary" %}}

Aspose.Cells のどのバージョンを使用しているのだろうか?新しい機能を導入し、問題を修正するために、Aspose.Cells の新しいバージョンを定期的に公開しています。バージョン番号は、メジャー バージョン番号、マイナー バージョン番号、および修正プログラム バージョン番号で構成されます。各数値は 0 以上の整数でなければなりません。形式は次のとおりです。

メジャー.マイナー.ホットフィックス

Aspose.Cells の新しいビルドをリリースすると、バージョン番号が更新されます。

この記事では、システムにインストールされている Aspose.Cells のバージョンを手動で確認する方法と、Aspose.Cells API を使用する方法について説明します。

{{% /alert %}}

## **バージョン番号を手動で確認する**

使用している Aspose.Cells のバージョンを手動で確認するには:

1.  Aspose.Cells.dll ファイルを右クリックして、**プロパティ**.
1. [バージョン] (または [詳細]) タブをクリックして、バージョン番号を確認します。

## **Aspose.Cells API を使用してバージョン番号を確認します**

API を使用して、使用している Aspose.Cells のバージョンを確認するには、[セルヘルパー](https://reference.aspose.com/cells/net/aspose.cells/cellshelper)クラス GetVersion 静的メソッドを使用して、Aspose.Cell のバージョン番号を取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}