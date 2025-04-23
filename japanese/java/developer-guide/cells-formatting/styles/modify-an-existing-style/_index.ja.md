---
title: 既存のスタイルを修正する
type: docs
weight: 50
url: /ja/java/modify-an-existing-style/
description: Microsoft ExcelおよびAspose.Cells for Java APIを使用してExcelでスタイルを変更する方法を学びます。
keywords: Excelで既存のスタイルを変更する、Excelで既存のスタイルを変更するjava、Excelでスタイルを変更する、Excelでスタイルを変更するjava、Excelでスタイルを変更する、Excelでスタイルを変更するjava、Excelでスタイルを変更する、Excelでスタイルを変更するjava、Excelでスタイルを変更する、Excelでスタイルを変更するjava、Excelでスタイルを変更するjava、Excelで既存のスタイルを変更する、Excelで既存のスタイルを変更するjava、Excelでスタイルを変更する、Excelでスタイルを変更するjava、Excelでスタイルを変更する、JavaでExcelでスタイルを変更する、JavaでExcelでスタイルを変更する、JavaでExcelでスタイルを変更する、JavaでExcelでスタイルを変更する
---

{{% alert color="primary" %}}

セルに同じ書式オプションを適用するには、新しい書式スタイルオブジェクトを作成してください。書式スタイルオブジェクトは、フォント、フォントサイズ、インデント、番号、ボーダー、パターンなどの書式の組み合わせであり、名前を付けて保存されたセットです。適用すると、そのスタイルのすべての書式が適用されます。

既存のスタイルを使用して、ブックと共に保存し、同じ属性で情報を書式設定することもできます。

セルが明示的にフォーマットされていない場合、**通常**スタイル(ワークブックのデフォルトスタイル)が適用されます。Microsoft Excelでは、通常スタイルに加えてComma、Currency、Percentなどのスタイルがいくつか事前に定義されています。

Aspose.Cellsを使用すると、これらのスタイルのいずれか、または独自の属性で定義したスタイルを修正することができます。

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

## **Aspose.Cellsの使用**

Aspose.Cellsは既存のスタイルを更新するための [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) メソッドを提供します。

Aspose.Cellsを使用して動的に作成したスタイルまたは事前定義の名前付きスタイルを変更するには、[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) メソッドを呼び出して、セルや範囲に適用されたスタイルの変更を反映させます。

[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) メソッドは **OK** ボタンと同様の挙動を示します。既にセルの範囲にスタイルを適用しており、スタイルの属性を変更し、メソッドを呼び出すと、これらのセルの書式が自動的に更新されます。

### **スタイルの作成と変更**

この例では、スタイルオブジェクトを作成し、セルの範囲に適用し、スタイルオブジェクトを変更します。変更は自動的にセルと適用された範囲に適用されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **既存のスタイルの変更**

この例では、範囲にすでに適用されているPercentという名前のスタイルが含まれる単純なテンプレートExcelファイルを使用します。具体的な手順は以下の通りです:

1. スタイルを取得します。
1. スタイルオブジェクトを作成します。
1. スタイルフォーマットを変更します。

変更は自動的に適用された範囲に適用されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
{{< app/cells/assistant language="java" >}}
