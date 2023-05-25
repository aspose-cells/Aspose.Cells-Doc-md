---
title: ページ設定の倍率を計算する
type: docs
weight: 300
url: /ja/net/calculate-page-setup-scaling-factor/
description: この記事では、C# API または .NET ライブラリを使用して、Excel ワークシートの幅 n ページ×高さ m に合わせるオプションを使用してページ設定の倍率をプログラム的に計算する方法を説明するサンプル コードを紹介します。
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

を使用してページ設定の倍率を設定すると、**幅 n ページ、高さ m に合わせる**オプション、Microsoft Excel はページ設定倍率を計算します。次を使用して同じことを計算できます[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)財産。このプロパティは、パーセント値に変換できる double 値を返します。たとえば、0.5 が返された場合、スケーリング係数が 50% であることを意味します。

{{% /alert %}}

次のサンプル コードは、次を使用してページ設定の倍率を計算する方法を示しています。[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
