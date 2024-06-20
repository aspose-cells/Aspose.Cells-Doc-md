---
title: ページ設定スケーリングファクターを計算します
type: docs
weight: 300
url: /ja/net/calculate-page-setup-scaling-factor/
description: この記事では、Excel ワークシートのページ設定のスケーリングファクターをプログラムで計算するために、C# API または .NET ライブラリを使用する方法についてのサンプルコードを提供します。
keywords: Excel のページの幅 n ページ、高さ m ページに合わせる c#、ページ設定スケーリングファクターの計算 c#
---

{{% alert color="primary" %}}

**ページの幅 n ページ、高さ m ページに合わせる** オプションを使用してページ設定のスケーリングを設定すると、Microsoft Excel はページ設定のスケーリングファクターを計算します。同様の計算は [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) プロパティを使用して行うことができます。このプロパティは、パーセンテージ値に変換可能な double 値を返します。たとえば、0.5 を返すと、スケーリングファクターが 50％であることを意味します。

{{% /alert %}}

次のサンプルコードは、[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) プロパティを使用してページ設定のスケーリングファクターを計算する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
