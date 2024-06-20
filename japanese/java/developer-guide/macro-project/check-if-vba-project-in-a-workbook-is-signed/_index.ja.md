---
title: ブックのVBAプロジェクトが署名されているかどうかを確認
type: docs
weight: 40
url: /ja/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Microsoft Excelを使用して **ツール** > **デジタル署名...** メニューコマンドを使用してVBAプロジェクトが署名されているかどうかを確認できます。 同様に、Aspose.Cellsの [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) メソッドを使用して、プログラムで確認できます。

{{% /alert %}}

## **WorkbookのVBAプロジェクトが署名されているかを確認する**

以下のコードは、ワークブックをロードし、[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)プロパティを使用してそのVBAプロジェクトが署名されているかどうかをチェックします。プロパティはプロジェクトが署名されている場合は**true**を返し、それ以外の場合は**false**を返します。

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
