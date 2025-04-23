---
title: ワークシートへのデータインポート時に式フィールドを指定
type: docs
weight: 220
url: /ja/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **可能な使用シナリオ**

データをワークシートにインポートする際に、[**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas)メソッドを使用して式フィールドを指定できます。このメソッドは、値**true**がフィールドが式フィールドであることを意味するBoolean配列を受け取ります。たとえば、3番目のフィールドが式フィールドの場合、配列の3番目の値は**true**になります。

## **ワークシートにデータをインポートする際に式フィールドを指定する**

次に、ワークシートにデータをインポートする際に式フィールドを指定する方法を説明したサンプルコードを参照してください。コードによって生成された[出力Excelファイル](61767850.xlsx)と、出力Excelファイルへのコードの影響を示すスクリーンショットを参照してください。

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
