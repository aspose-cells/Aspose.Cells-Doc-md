---
title: 既存のスタイルを修正する
description: Aspose.Cellsは、既存のセルスタイルを変更可能なPythonライブラリです。この記事では、Aspose.Cells for Python via .NETライブラリを使って既存のセルスタイルを変更し、外観をカスタマイズする方法を紹介します。
keywords: 既存のスタイルを変更し、アプリケーションの外観と使いやすさをカスタマイズする、ガイド、チュートリアル、ヘルプドキュメント、開発ドキュメント、APIリファレンス、サンプルコード、ダウンロード、サポート。
type: docs
weight: 90
url: /ja/python-net/modify-an-existing-style/
---

{{% alert color="primary" %}}

セルに同じフォーマットオプションを適用するには、新しいフォーマットスタイルオブジェクトを作成します。フォーマットスタイルオブジェクトは、フォント、フォントサイズ、インデント、数値、罫線、パターンなどのフォーマット特性を組み合わせたものであり、名前が付けられ、セットとして保存されます。適用されると、そのスタイルのすべてのフォーマットが適用されます。

既存のスタイルを使用して、同じ属性で情報にフォーマットを適用することもできます。

セルが明示的にフォーマットされていない場合、**通常**スタイル(ワークブックのデフォルトスタイル)が適用されます。Microsoft Excelでは、通常スタイルに加えてComma、Currency、Percentなどのスタイルがいくつか事前に定義されています。

Aspose.Cells for Python via .NETは、これらのスタイルや他の定義済みのスタイルを任意の属性で変更可能です。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel 97-2003でスタイルを更新するには:

1. **書式**メニューで **スタイル** をクリックします。
1. **スタイル名** リストから変更したいスタイルを選択します。
1. **変更** をクリックします。
1. 「セルの書式設定」ダイアログのタブを使用して、望むスタイルオプションを選択します。
1. **OK** をクリックします。
1. **スタイルに含まれるもの** で、希望するスタイルの機能を指定します。
1. **OK** をクリックしてスタイルを保存し、選択した範囲に適用します。

## **Aspose.Cells for Python via .NETを使用して**

次の例は、[**Style.update**](https://reference.aspose.com/cells/python-net/aspose.cells/style/update) メソッドの使用方法を示しています。

### **スタイルの作成と変更**

この例では、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトを作成し、セルの範囲に適用し、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトを変更します。変更は、スタイルが適用されたセルと範囲に自動的に適用されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ModifyThroughStyleObject-1.py" >}}

### **既存のスタイルの変更**

この例では、範囲にすでに適用されているPercentという名前のスタイルが含まれる単純なテンプレートExcelファイルを使用します。具体的な手順は以下の通りです:

1. スタイルを取得します。
1. スタイルオブジェクトを作成します。
1. スタイルフォーマットを変更します。

変更は自動的に適用された範囲に適用されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ModifyThroughSampleExcelFile-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
