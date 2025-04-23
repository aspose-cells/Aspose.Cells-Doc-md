---
title: ワークシートとタブの表示と非表示
type: docs
weight: 10
url: /ja/python-net/show-and-hide-worksheets-and-tabs/
description: この記事は、Aspose.Cells for Python via .NET APIを使用してExcelワークシートの表示や非表示をプログラムで行うためのサンプルコードを提供します。さらに、Excelワークブックのタブの表示と非表示についても説明します。
keywords: Python Excelライブラリ、Pythonでワークシートの表示と非表示、Pythonでタブの表示と非表示、Pythonでタブバーの幅を制御する。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、ワークブックの要素（ワークシートやタブを含む）を表示・非表示にすることを可能にします。

{{% /alert %}}

## **ワークシートの表示と非表示**

Excelファイルには複数のワークシートを持つことができます。Excelファイルを作成するとき、作業用のワークシートを追加します。各ワークシートは独立しており、自分のデータや書式設定を持っています。時には、特定のワークシートを非表示にしたり表示したりしたい場合もあります。したがって、**Aspose.Cells for Python via .NET**は、開発者がExcelファイル内のワークシートの表示状態を制御できるようにします。

Aspose.Cells for Python via .NETは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。

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

Aspose.Cells for Python via .NETを使用して、開発者はExcelファイル内のシートタブやスクロールボタンの表示制御を行えます。

Aspose.Cells for Python via .NETは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスは、Excelファイルの管理に役立つさまざまなプロパティとメソッドを提供します。Excelファイルのタブの表示・非表示を制御するには、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)プロパティを使用します。[**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)は真理値のプロパティであり、trueまたはfalseの値だけを格納できます。

### **タブを表示する**

**true**に設定することで、タブを表示します。

### **タブを非表示にする**

 **false**に設定することで、Excelファイル内のタブを非表示にします。

以下は、Excelファイル（book1.xls）を開き、そのタブを非表示にして修正したファイルをoutput.xlsとして保存する完全な例です。コードの実行後、ワークブックのタブが非表示になっていることが確認できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **タブバーの幅を制御する**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
