---
title: ワークシートとタブの表示と非表示
type: docs
weight: 10
url: /ja/net/show-and-hide-worksheets-and-tabs/
description: この記事では、C# APIまたは.NETライブラリを使用してExcelワークシートをプログラムで表示および非表示にするサンプルコードを提供します。また、Excelワークブックのタブを表示および非表示にする方法についても説明します。
---

{{% alert color="primary" %}}

Aspose.Cellsはユーザーに、ワークブック内のワークシートやタブなどの要素を表示または非表示にする機能を提供します。

{{% /alert %}}

## **ワークシートの表示と非表示**

Excelファイルには1つ以上のワークシートが含まれることがあります。Excelファイルを作成するときには、作業するExcelファイルにワークシートを追加します。Excelファイル内の各ワークシートは、独自のデータや書式設定などを持つため、他のワークシートから独立しています。開発者は時々、Excelファイル内で特定のワークシートを非表示にし、他のワークシートを表示したい場合があります。そのため、Aspose.Cellsは開発者がExcelファイル内のワークシートの表示を制御することを可能にします。

Aspose.CellsはExcelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれており、Excelファイル内の各ワークシートにアクセスできます。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスにはワークシートを管理するための多くのプロパティやメソッドが提供されています。ワークシートの表示を制御するには、[**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)クラスの[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)プロパティを使用します。[**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible)はBooleanプロパティであり、**true**または**false**の値のみを格納できます。

### **ワークシートを表示する**

ワークシートを**true**に設定することで、ワークシートを表示します。

### **ワークシートを非表示にする**

ワークシートを**false**に設定することで、ワークシートを非表示にします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **タブの表示と非表示**

Microsoft Excelの下部をよく見ると、いくつかのコントロールが表示されます。これには次のものが含まれます:

- シートタブ。
- タブのスクロールボタン。

シートタブはExcelファイル内のワークシートを表します。任意のタブをクリックするとそのワークシートに切り替えることができます。ワークブック内にワークシートが多いほど、シートタブも多く表示されます。Excelファイルに多くのワークシートが含まれている場合は、それらをナビゲートするためのボタンが必要になります。そのため、Microsoft Excelはシートタブのスクロールボタンを提供しています。

Aspose.Cellsを使用すると、開発者はExcelファイル内のシートタブとタブのスクロールボタンの表示を制御できます。

Aspose.CellsはExcelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイルを管理するための多くのプロパティやメソッドが提供されています。Excelファイル内のタブの表示を制御するために、開発者は[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)プロパティを使用できます。[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)はBooleanプロパティであり、**true**または**false**の値のみを格納できます。

### **タブを表示する**

**true**に設定することで、タブを表示します。

### **タブを非表示にする**

 **false**に設定することで、Excelファイル内のタブを非表示にします。

以下は、Excelファイル（book1.xls）を開き、そのタブを非表示にして修正したファイルをoutput.xlsとして保存する完全な例です。コードの実行後、ワークブックのタブが非表示になっていることが確認できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **タブバーの幅を制御する**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
