---
title: 既存のスタイルを変更する
type: docs
weight: 50
url: /ja/java/modify-an-existing-style/
description: Microsoft Excel と Aspose.Cells for Java API で Excel のスタイルを変更する方法を学びます。
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

同じ書式設定オプションをセルに適用するには、新しい書式設定スタイル オブジェクトを作成します。フォーマット スタイル オブジェクトは、フォント、フォント サイズ、インデント、数値、境界線、パターンなどのフォーマット特性の組み合わせであり、名前が付けられ、セットとして保存されます。適用すると、そのスタイルのすべての書式が適用されます。

また、既存のスタイルを使用してブックと共に保存し、それを使用して同じ属性で情報をフォーマットすることもできます。

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

Aspose.Cells は[**スタイル更新**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()既存のスタイルを更新するためのメソッド。

名前付きスタイルを変更するには、Aspose.Cells を使用して動的に作成されたか事前定義されたかにかかわらず、[**スタイル更新**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) メソッドを使用して、セルまたは範囲に適用されたスタイルの変更を反映します。

の[**スタイル更新**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) メソッドは次のように動作します**わかった**スタイル ダイアログのボタン: 既存のスタイルに変更を加えた後、呼び出して変更を実装します。セルの範囲に既にスタイルを適用している場合、スタイル属性を変更してメソッドを呼び出すと、それらのセルの書式設定が自動的に更新されます

### **スタイルの作成と変更**

この例では、スタイル オブジェクトを作成し、それをセル範囲に適用して、スタイル オブジェクトを変更します。変更は、スタイルが適用されたセルと範囲に自動的に適用されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **既存のスタイルの変更**

この例では、Percent というスタイルが既に範囲に適用されている簡単なテンプレート Excel ファイルを使用します。例：

1. スタイルを取得し、
1. スタイル オブジェクトを作成し、
1. スタイルの書式を変更します。

変更は、スタイルが適用された範囲に自動的に適用されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
