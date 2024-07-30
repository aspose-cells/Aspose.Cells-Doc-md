---
title: ワークシートとタブの表示と非表示
type: docs
weight: 10
url: /ja/python-net/show-and-hide-worksheets-and-tabs/
description: この記事は、Aspose.Cells for Python via .NET API を使用して Excel ワークシートの表示および非表示をプログラムで行う方法、さらに Excel ワークブックのタブの表示および非表示方法を示しています。
keywords: Python Excel ライブラリ、Python でワークシートの表示と非表示、Python でのタブの表示と非表示、Python でタブバーの幅を制御する方法。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET は、ワークブックの要素、ワークシートおよびタブを表示または非表示にする機能を提供します。

{{% /alert %}}

## **ワークシートの表示と非表示**

Excel ファイルには 1 つ以上のワークシートが含まれる場合があります。Excel ファイルを作成するときには、作業する Excel ファイルにワークシートを追加します。Excel ファイルの各ワークシートは、独自のデータや書式設定などを持つ他のワークシートと独立しています。開発者は、Excel ファイル内で特定のワークシートを非表示にして他のワークシートを表示する必要がある場合があります。したがって、**Aspose.Cells for Python via .NET** を使用すると、Excel ファイル内のワークシートの可視性を制御することができます。

Aspose.Cells for Python via .NET は、Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスには、Excel ファイル内の各ワークシートにアクセスできる [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスにはワークシートを管理するための多くのプロパティやメソッドが提供されています。ワークシートの表示を制御するには、[**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible)クラスの[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)プロパティを使用します。[**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible)はBooleanプロパティであり、**true**または**false**の値のみを格納できます。

### **ワークシートを表示する**

ワークシートを**true**に設定することで、ワークシートを表示します。

### **ワークシートを非表示にする**

ワークシートを**false**に設定することで、ワークシートを非表示にします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **タブの表示と非表示**

Microsoft Excelの下部をよく見ると、いくつかのコントロールが表示されます。これには次のものが含まれます:

- シートタブ。
- タブのスクロールボタン。

シートタブはExcelファイル内のワークシートを表します。任意のタブをクリックするとそのワークシートに切り替えることができます。ワークブック内にワークシートが多いほど、シートタブも多く表示されます。Excelファイルに多くのワークシートが含まれている場合は、それらをナビゲートするためのボタンが必要になります。そのため、Microsoft Excelはシートタブのスクロールボタンを提供しています。

Aspose.Cells for Python via .NETを使用すると、開発者はExcelファイルでシートタブの表示とタブのスクロールボタンを制御できます。

Aspose.Cells for Python via .NETは、Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスは、Excelファイルを管理するための幅広いプロパティとメソッドを提供します。Excelファイルでタブの表示を制御するには、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)プロパティを使用できます。[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)はブール値のプロパティであり、**true**または**false**の値のいずれかを保存できます。

### **タブを表示する**

**true**に設定することで、タブを表示します。

### **タブを非表示にする**

 **false**に設定することで、Excelファイル内のタブを非表示にします。

以下は、Excelファイル（book1.xls）を開き、そのタブを非表示にして修正したファイルをoutput.xlsとして保存する完全な例です。コードの実行後、ワークブックのタブが非表示になっていることが確認できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **タブバーの幅を制御する**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
