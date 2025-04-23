---
title: ブックのVBAプロジェクトが署名されているかどうかを確認
type: docs
weight: 70
url: /ja/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Microsoft Excelでは、**ツール > デジタル署名...**メニューコマンドを使用してVBAプロジェクトが署名されているかどうかを確認できます。同様に、Aspose.Cellsの[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned)プロパティを使用してプログラムで確認することも可能です。

{{% /alert %}}

## **C#でワークブックのVBAプロジェクトが署名されているかどうかを確認する**

以下のコードは、ワークブックをロードし、[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned)プロパティを使用してそのVBAプロジェクトが署名されているかどうかをチェックします。プロパティはプロジェクトが署名されている場合は**true**を返し、それ以外の場合は**false**を返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
