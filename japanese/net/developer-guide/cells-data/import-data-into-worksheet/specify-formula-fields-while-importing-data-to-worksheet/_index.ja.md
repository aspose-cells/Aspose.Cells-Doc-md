---
title: データをワークシートにインポートする際の数式フィールドの指定
type: docs
weight: 300
url: /ja/net/specify-formula-fields-while-importing-data-to-worksheet/
---
## **考えられる使用シナリオ**

を使用してワークシートにデータをインポートするときに、数式フィールドを指定できます。[**ImportTableOptions.IsFormulas**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/isformulas) .このプロパティはブール配列を取り、値は**真実**フィールドが数式フィールドであることを意味します。たとえば、3 番目のフィールドが数式フィールドの場合、配列の 3 番目の値は次のようになります。**真実**.

## **データをワークシートにインポートする際の数式フィールドの指定**

データをワークシートにインポートする際に数式フィールドを指定する方法を説明する次のサンプル コードを参照してください。をご覧ください[出力エクセルファイル](61767838.xlsx)コードによって生成されたものと、出力 Excel ファイルに対するコードの効果を示すスクリーンショット。

![todo:画像_代替_文章](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.cs" >}}
