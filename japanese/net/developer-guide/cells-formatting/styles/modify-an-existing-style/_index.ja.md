---
title: 既存のスタイルを変更する
type: docs
weight: 90
url: /ja/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

同じ書式設定オプションをセルに適用するには、新しい書式設定スタイル オブジェクトを作成します。フォーマット スタイル オブジェクトは、フォント、フォント サイズ、インデント、数値、境界線、パターンなどのフォーマット特性の組み合わせであり、名前が付けられ、セットとして保存されます。適用すると、そのスタイルのすべての書式が適用されます。

また、既存のスタイルを使用してブックと共に保存し、同じ属性で情報をフォーマットするために使用することもできます。

セルが明示的にフォーマットされていない場合、**普通**スタイル (ワークブックの既定のスタイル) が適用されます。 Microsoft Excel では、通常のスタイルに加えて、コンマ、通貨、パーセントなどのいくつかのスタイルが事前定義されています。

Aspose.Cells では、これらのスタイルのいずれか、または目的の属性で定義したその他のスタイルを変更できます。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel 97-2003 でスタイルを更新するには:

1. 上で**フォーマット**メニュー、クリック**スタイル**.
1. から変更するスタイルを選択します。**スタイル名**リスト。
1. クリック**変更**.
1. Format Cells ダイアログのタブを使用して、必要なスタイル オプションを選択します。
1. クリック**わかった**.
1. 下**スタイルが含まれています**で、必要なスタイル機能を指定します。
1. クリック**わかった**をクリックしてスタイルを保存し、選択した範囲に適用します。

## **Aspose.Cells を使用**

次の例は、使用方法を示しています[**スタイルの更新**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)方法。

### **スタイルの作成と変更**

この例では、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトをセル範囲に適用し、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。変更は、スタイルが適用されたセルと範囲に自動的に適用されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **既存のスタイルの変更**

この例では、Percent というスタイルが既に範囲に適用されている簡単なテンプレート Excel ファイルを使用します。例：

1. スタイルを取得し、
1. スタイル オブジェクトを作成し、
1. スタイルの書式を変更します。

変更は、スタイルが適用された範囲に自動的に適用されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
