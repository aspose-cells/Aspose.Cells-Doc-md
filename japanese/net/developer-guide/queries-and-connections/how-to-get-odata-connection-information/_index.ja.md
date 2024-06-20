---
title: OData接続情報を取得する方法
type: docs
weight: 60
url: /ja/net/how-to-get-odata-connection-information/
---

## **OData接続情報を取得**

開発者がExcelファイルからOData情報を抽出する必要がある場合があります。Aspose.Cellsは、Excelファイルに存在するDataMashup情報を返す [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) プロパティを提供します。この情報は [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) クラスによって表されます。[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) クラスは [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) プロパティを提供し、 [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) コレクションを返します。 [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) から、 [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) と [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem) にアクセスできます。

次のコードスニペットは、これらのクラスを使用してOData情報を取得する方法を示しています。

以下のコードスニペットで使用されるソースファイルは参照用に添付されています。

[ソースファイル](96928098.xlsx)

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **コンソール出力**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
