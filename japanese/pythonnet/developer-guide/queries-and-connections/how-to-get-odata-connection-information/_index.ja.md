---
title: OData接続情報を取得する方法
type: docs
weight: 60
url: /ja/python-net/how-to-get-odata-connection-information/
---

## **OData接続情報を取得**

開発者が Excel ファイルから OData 情報を抽出する必要がある場合があります。Aspose.Cells for Python via .NET は、Excel ファイルに存在する DataMashup 情報を返す [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) プロパティを提供します。この情報は [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) クラスで表されます。[**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) クラスは [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) プロパティを提供し、[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) コレクションを返します。[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) から [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) と [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem) にアクセスできます。

次のコードスニペットは、これらのクラスを使用してOData情報を取得する方法を示しています。

以下のコードスニペットで使用されるソースファイルは参照用に添付されています。

[ソースファイル](96928098.xlsx)

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **コンソール出力**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

