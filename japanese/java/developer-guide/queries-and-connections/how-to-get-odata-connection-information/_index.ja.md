---
title: OData接続情報を取得する方法
type: docs
weight: 60
url: /ja/java/how-to-get-odata-connection-information/
---

## **OData接続情報を取得**

開発者がExcelファイルからOData情報を取り出す必要がある場合があります。Aspose.Cellsは、Excelファイルに含まれるDataMashup情報を返す[**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)プロパティを提供します。この情報はDataMashupクラスで表されます。DataMashupクラスにはPowerQueryFormulasプロパティがあり、これはPowerQueryFormulaCollctionコレクションを返します。PowerQueryFormulaCollctionからPowerQueryFormulaとPowerQueryFormulaItemにアクセスできます。

次のコードスニペットは、これらのクラスを使用してOData情報を取得する方法を示しています。

以下のコードスニペットで使用されるソースファイルは参照用に添付されています。

[ソースファイル](ODataSample.xlsx)

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **コンソール出力**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
