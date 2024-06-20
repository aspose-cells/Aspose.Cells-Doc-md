---
title: ExcelをODSに変換
type: docs
weight: 40
url: /ja/python-java/convert-excel-to-ods/
---

## **ExcelをODSに変換**
ODSファイルは、Apache OpenOffice Suiteの一部であるCalcプログラムによって作成されます。 ODSファイルには、行と列で整理されたデータが格納され、OASIS OpenDocumentベースの標準形式でフォーマットされます。

Aspose.Cells for Python via Javaは、ODSファイルの作業をサポートしています。以下の例は、ExcelをODSファイルに変換する方法を示しています。
### **直接変換**
ExcelファイルをODSに変換するもっとも簡単な方法は、ワークブックをロードし、[Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\))メソッドの第2パラメータとして[SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS)を渡すことです。

次のコードスニペットは、Excelを直接ODSに変換する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **ODSドキュメントをODF 1.1または1.2の仕様に保存する**
Aspose.Cells for Python via Javaは、ODSファイルをODF 1.1およびODF 1.2の仕様に保存することをサポートしています。そのために、APIは[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11)プロパティを提供しています。このプロパティを**true**に設定すると、ODF 1.1の仕様でファイルが保存されます。デフォルト値は**false**ですので、特別な設定なしで保存されるODSファイルはODF 1.2の仕様で保存されます。

次のコードスニペットは、ODF 1.1および1.2の仕様でODSファイルを保存する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
