---
title: ブックのVBAプロジェクトが署名されているかどうかを確認
type: docs
weight: 70
url: /ja/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Microsoft Excelの**ツール > デジタル署名…**メニューコマンドを使用して、VBAプロジェクトに署名されているかどうかを確認できます。同様に、Aspose.Cells for Python via .NETの[**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed)プロパティを使ってプログラム的に確認することも可能です。

{{% /alert %}}

## **PythonでワークブックのVBAプロジェクトが署名されているか確認する**

以下のコードは、ワークブックをロードし、[**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed)プロパティを使用してそのVBAプロジェクトが署名されているかどうかをチェックします。プロパティはプロジェクトが署名されている場合は**true**を返し、それ以外の場合は**false**を返します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
