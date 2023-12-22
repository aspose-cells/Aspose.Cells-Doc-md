---
title: 既存のスタイルを変更する
description: Aspose.Cells は、ユーザーが既存のセル スタイルを変更できるようにするスプレッドシート ファイルを操作するための .NET ライブラリです。この記事では、ユーザーが必要に応じてセルの外観を変更できるように、Aspose.Cells ライブラリを使用して既存のセル スタイルを変更する方法を紹介します。
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /ja/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

同じ書式設定オプションをセルに適用するには、新しい書式設定スタイル オブジェクトを作成します。書式設定スタイル オブジェクトは、フォント、フォント サイズ、インデント、数値、境界線、パターンなどの書式設定特性の組み合わせであり、名前が付けられ、セットとして保存されます。適用すると、そのスタイルのすべての書式設定が適用されます。

既存のスタイルを使用してワークブックとともに保存し、同じ属性を持つ情報の書式設定に使用することもできます。

セルが明示的に書式設定されていない場合、**普通**スタイル (ワークブックのデフォルト スタイル) が適用されます。 Microsoft Excel では、通常のスタイルに加えて、カンマ、通貨、パーセントなどのいくつかのスタイルが事前定義されています。

Aspose.Cells を使用すると、これらのスタイルのいずれか、または必要な属性で定義したその他のスタイルを変更できます。

{{% /alert %}}

##  **Microsoft Excelの使用**

Microsoft Excel 97-2003 でスタイルを更新するには:

1. で**フォーマット**メニューで、*スタイル**をクリックします。
1. から変更したいスタイルを選択します。**スタイル名**リスト。
1. [*変更**] をクリックします。
1. 「Cells の形式」ダイアログのタブを使用して、必要なスタイル オプションを選択します。
1. [*OK**] をクリックします。
1. *スタイルに含まれるもの** で、必要なスタイル機能を指定します。
1. クリック**OK**をクリックしてスタイルを保存し、選択した範囲に適用します。

##  **Aspose.Cellsを使用する**

次の例は、使用方法を示しています。[**スタイル.アップデート**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)方法。

###  **スタイルの作成と変更**

この例では、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトを取得し、それをセル範囲に適用し、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。変更は、スタイルが適用されたセルと範囲に自動的に適用されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

###  **既存のスタイルの変更**

この例では、パーセントというスタイルがすでに範囲に適用されている単純なテンプレート Excel ファイルを使用します。例：

1. スタイルを手に入れ、
1. スタイルオブジェクトを作成し、
1. スタイルの書式設定を変更します。

変更は、スタイルが適用された範囲に自動的に適用されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
