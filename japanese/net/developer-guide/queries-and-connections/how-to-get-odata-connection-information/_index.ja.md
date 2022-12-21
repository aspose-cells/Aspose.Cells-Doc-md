---
title: OData 接続情報を取得する方法
type: docs
weight: 60
url: /ja/net/how-to-get-odata-connection-information/
---
## **OData 接続情報を取得する**

開発者が Excel ファイルから OData 情報を抽出する必要がある場合があります。 Aspose.Cells は[**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup)Excel ファイルに存在する DataMashup 情報を返すプロパティ。この情報は、[**データマッシュアップ**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)クラス。の[**データマッシュアップ**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)クラスが提供する[**PowerQuery式**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas)を返すプロパティ[**PowerQuery式コレクション**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)コレクション。から[**PowerQuery式コレクション**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)にアクセスできます[**PowerQuery式**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula)と[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

次のコード スニペットは、これらのクラスを使用して OData 情報を取得する方法を示しています。

次のコード スニペットで使用されているソース ファイルは、参照用に添付されています。

[ソースファイル](96928098.xlsx)

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **コンソール出力**

接続名: 注文

名前: ソース

値: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

名前: Orders_table

値: ソース{[名前="注文",署名="テーブル"]}[データ]