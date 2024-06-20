---
title: ワークブック内の未使用のスタイルを削除する
type: docs
weight: 470
url: /ja/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Excelファイル内の未使用のスタイルは、ストレージを占有するだけでなく、PDF、HTMLなどの異なる形式での変換時にパフォーマンスの問題を引き起こします。Aspose.Cellsは、[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\))を提供して、ワークブック内の未使用のスタイルをすべて削除します。

{{% /alert %}} 
## **ワークブック内の未使用のスタイルを削除する**
以下のコードは、[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\))の使用方法を説明しています。コードは、提供されたリンクからダウンロードできる[テンプレートExcelファイル](5473451.xlsx)をロードします。このファイルには **AsposeStyle** という未使用のスタイルが含まれており、コードの実行後にこのスタイルと他の未使用のスタイルがすべて削除されます。詳しい説明については、以下のスクリーンショットを参照してください。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
