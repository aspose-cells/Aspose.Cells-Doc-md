---
title: OData 接続情報を取得する方法
type: docs
weight: 60
url: /ja/java/how-to-get-odata-connection-information/
---
## **OData 接続情報を取得する**

開発者が Excel ファイルから OData 情報を抽出する必要がある場合があります。 Aspose.Cells は[**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)Excel ファイルに存在する DataMashup 情報を返すプロパティ。この情報は、DataMashup クラスによって表されます。 DataMashup クラスは、PowerQueryFormulaColllction コレクションを返す PowerQueryFormulas プロパティを提供します。 PowerQueryFormulaColllction から、PowerQueryFormula と PowerQueryFormulaItem にアクセスできます。

次のコード スニペットは、これらのクラスを使用して OData 情報を取得する方法を示しています。

次のコード スニペットで使用されているソース ファイルは、参照用に添付されています。

[ソースファイル](ODataSample.xlsx)

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **コンソール出力**

接続名: 注文

名前: ソース

値: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

名前: Orders_table

値: ソース{[名前="注文",署名="テーブル"]}[データ]