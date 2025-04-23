---
title: Excelドキュメントを作成したアプリケーションのバージョン番号を取得する
type: docs
weight: 210
url: /ja/python-net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

多くの場合、Microsoft Excelドキュメントを作成したアプリケーションのバージョン番号を知る必要があります。Aspose.Cells for Python via .NETは、その目的のために[**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version)プロパティを提供します。

{{% /alert %}}

次のサンプルコードでは、[**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version)プロパティの使用方法を示しています。これは、Microsoft Excel 2003、2007、2010、2013で作成したExcelファイルをロードして、これらのExcelドキュメントを作成したアプリケーションのバージョン番号を出力します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-GetApplicationVersion-1.py" >}}
