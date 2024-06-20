---
title: ページ設定スケーリングファクターを計算します
type: docs
weight: 260
url: /ja/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

**n個のページ幅x m個のページの高さに合わせる**オプションを使用してページ設定スケーリングを設定すると、Microsoft Excelはページ設定スケーリングファクターを計算します。 これを[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)プロパティを使用して同じ値を計算できます。 このプロパティは、パーセンテージ値に変換できるdouble値を返します。 たとえば、0.5079621076を返すと、スケーリングファクターは51％であることを意味します。

{{% /alert %}} 
## **ページ設定スケーリングファクターを計算します**
次のサンプルコードは、[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) プロパティを使用してページ設定のスケーリングファクターを計算する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
