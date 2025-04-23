---
title: ワークブック内の未使用のスタイルを削除する
type: docs
weight: 470
url: /ja/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Excelファイル内の未使用のスタイルはスペースをとるだけでなく、PDFやHTMLなどの異なる形式に変換する際にパフォーマンスの問題を引き起こします。Aspose.Cellsは[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--)を提供しており、ワークブック内の未使用のスタイルをすべて削除できます。

{{% /alert %}} 
## **ワークブック内の未使用のスタイルを削除する**
以下のコードは[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--)の使用例を示しています。指定されたリンクからダウンロード可能な[テンプレートのExcelファイル](5473451.xlsx)をロードし、未使用のスタイル名**AsposeStyle**を含んでいます。このスタイルと他の未使用スタイルは、コード実行後に削除されます。詳細は次のスクリーンショットをご参照ください。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
