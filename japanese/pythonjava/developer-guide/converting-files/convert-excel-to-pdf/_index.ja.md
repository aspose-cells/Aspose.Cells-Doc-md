---
title: Excel を PDF に変換
type: docs
weight: 50
url: /ja/python-java/convert-excel-to-pdf/
description: Excel を Python で PDF に変換する方法。
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Excel を PDF に変換**

PDF ドキュメントは、組織、政府部門、および個人の間でドキュメントを交換するための標準形式として広く使用されています。ソフトウェア開発者は、Microsoft Excel ファイルを PDF ドキュメントに簡単に変換する方法を考案するように求められることがよくあります。 Aspose.Cells for Python via Java API は、Excel ファイルを PDF ドキュメント (PDF/A を含む) に変換する機能を提供します。 Aspose.Cell's は、スプレッドシートを高い精度と忠実度で PDF に変換します。

### **直接変換**

Excel ファイルを PDF に直接保存するには、[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) メソッドとパス[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) 番目のパラメーターとして。

次のコード スニペットは、[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)そしてその[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)メソッドを使用して、Excel を PDF 形式に変換します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **高度な変換**

PDF への変換をより詳細に制御するために、API は[**PDF保存オプション**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)クラス。の[**PDF保存オプション**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)クラスを使用して、変換用のさまざまな属性を設定できます。のさまざまなプロパティの設定[**PDF保存オプション**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)クラスを使用すると、結果の PDF ファイルの印刷、フォント、セキュリティ、および圧縮設定を制御できます。最も注目すべきプロパティは、[**コンプライアンス**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)これにより、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できます。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) メソッドをスプレッドシートを PDF にレンダリングする直前に実行します。これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
