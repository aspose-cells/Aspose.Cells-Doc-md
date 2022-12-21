---
title: Excel を ODS に変換する
type: docs
weight: 40
url: /ja/python-java/convert-excel-to-ods/
---
## **Excel を ODS に変換する**
ODS ファイルは、Apache OpenOffice Suite の一部である Calc プログラムによって作成されます。 ODS ファイルには、行と列で編成され、OASIS OpenDocument XML ベースの標準を使用してフォーマットされたデータが格納されます。

Aspose.Cells for Python via Java は、作業中の ODS ファイルをサポートします。次の例は、Excel を ODS ファイルに変換する方法を示しています。
### **直接変換**
Excel ファイルを ODS に変換する最も簡単な方法は、ワークブックを読み込んで、[SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS)の 2 番目のパラメータとして[Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)） 方法。

次のコード スニペットは、Excel を ODS に直接変換する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **ODS ドキュメントを ODF 1.1 または 1.2 仕様で保存します**
Aspose.Cells for Python via Java は、ODF 1.1 および ODF 1.2 仕様の ODS ファイルの保存をサポートします。このために、API が提供します。[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11)財産。このプロパティを**真実**ODF 1.1 仕様でファイルを保存します。のデフォルト値[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11)は**間違い**ということで、特別な設定をせずに保存したODSファイルはODF1.2仕様で保存されます。

次のコード スニペットは、ODF 1.1 および 1.2 仕様で ODS ファイルを保存する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
