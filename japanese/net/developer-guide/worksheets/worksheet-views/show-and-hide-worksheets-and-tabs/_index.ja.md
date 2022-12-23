---
title: ワークシートとタブの表示と非表示
type: docs
weight: 10
url: /ja/net/show-and-hide-worksheets-and-tabs/
description: この記事では、C# API または .NET ライブラリを使用して Excel ワークシートをプログラムで表示および非表示にするためのサンプル コードを提供します。さらに、Excel ワークブックのタブを表示および非表示にする方法。
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ユーザーはワークシートやタブを含むワークブックの要素を表示および非表示にできます。

{{% /alert %}}

## **ワークシートの表示と非表示**

Excel ファイルには、1 つまたは複数のワークシートを含めることができます。 Excel ファイルを作成するときはいつでも、作業している Excel ファイルにワークシートを追加します。 Excel ファイル内の各ワークシートは、独自のデータや書式設定などを持つことにより、他のワークシートから独立しています。開発者は、自分の興味のために Excel ファイルでいくつかのワークシートを非表示にし、他のワークシートを表示する必要がある場合があります。それで、**Aspose.Cells**開発者は、Excel ファイル内のワークシートの表示を制御できます。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。ワークシートの可視性を制御するには、[**可視**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)のプロパティ[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。[**可視**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)ブール型のプロパティです。つまり、格納できるのは**真実**また**間違い**価値。

### **ワークシートを表示する**

を設定して、ワークシートを表示します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**可視**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)プロパティへ**真実**

### **ワークシートを非表示にする**

を設定してワークシートを非表示にします。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**可視**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)プロパティへ**間違い**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **タブの表示と非表示**

Microsoft Excel ファイルの下部をよく見ると、多数のコントロールが表示されます。これらには以下が含まれます：

- シート タブ。
- タブスクロールボタン。

シート タブは、Excel ファイル内のワークシートを表します。任意のタブをクリックして、そのワークシートに切り替えます。ワークブック内のワークシートが多いほど、シート タブが多くなります。 Excel ファイルに十分な数のワークシートがある場合は、それらをナビゲートするためのボタンが必要です。そのため、Microsoft Excel には、シート タブをスクロールするためのタブ スクロール ボタンが用意されています。

Aspose.Cells を使用すると、開発者は Excel ファイルのシート タブとタブ スクロール ボタンの表示を制御できます。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。 Excel ファイルのタブの表示を制御するために、開発者は[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)財産。[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)ブール型のプロパティです。つまり、格納できるのは**真実**また**間違い**価値。

### **タブを表示する**

タブを表示するには[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)プロパティへ**真実**.

### **タブを非表示にする**

を設定して、Excel ファイルのタブを非表示にします。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)プロパティを false にします。

以下は、Excel ファイル (book1.xls) を開き、そのタブを非表示にして、変更したファイルを output.xls として保存する完全な例です。コードの実行後、ワークブックのタブが非表示になっていることがわかります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **タブバーの幅の制御**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
