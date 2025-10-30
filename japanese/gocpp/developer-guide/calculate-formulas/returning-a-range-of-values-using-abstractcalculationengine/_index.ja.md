---
title: GolangをC++経由でAbstractCalculationEngineを使用して値の範囲を返す
linktitle: AbstractCalculationEngineを使用して値の範囲を返す
description: この記事では、GolangをC++経由でAspose.Cellsライブラリを使用してMicrosoft Excelで値の範囲を返す抽象計算エンジンを紹介します。既存のExcelファイルを読み込むか、新規のExcelファイルを作成し、提供されるメソッドを使用して値の範囲を取得し、結果を返します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、値の範囲を返す抽象計算エンジン
type: docs
weight: 55
url: /ja/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excelの組み込み関数としてサポートされていないユーザー定義またはカスタム関数を実装するために使用される[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)クラスを提供します。

この記事では、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)から値の範囲を返す方法について説明します。

{{% /alert %}}

以下のコードは、[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)クラスの使用例を示し、そのメソッドを通じて値の範囲を返します。

`CalculateCustomFunction`という関数を持つクラスを作成します。このクラスは[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)を実装しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
次に、プログラムで上記の関数を使用します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
