---
title: 編集可能なチャートサポートを持つ.jasperファイルを埋める
type: docs
weight: 10
url: /ja/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports は、.jasper ファイルを .jrprint または JasperPrint オブジェクトに変換して XLS ファイルにエクスポートする前に、.jrxml ファイルを変更する必要はありません。この埋め込み手順は、編集可能なチャートを生成するために使用されます。 

{{% /alert %}} 

レポートを埋める方法の詳細については、JasperReportsのドキュメントをお読みください。

次に例を示します。

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
