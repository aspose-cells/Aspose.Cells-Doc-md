---
title: Excel ドキュメントを作成したアプリケーションのバージョン番号を取得する
type: docs
weight: 150
url: /ja/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

多くの場合、Microsoft Excel ドキュメントを作成したアプリケーションのバージョン番号を知る必要があります。 Aspose.Cells は[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)この目的のためのプロパティ。

{{% /alert %}}

次のサンプル コードは、[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)財産。 Microsoft Excel 2003、2007、2010、および 2013 で作成された Excel ファイルを読み込み、これらの Excel ドキュメントを作成したアプリケーションのバージョン番号を出力します。

参考までに、サンプル コードが作成するコンソール出力を以下に示します。

{{< highlight "java" >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
