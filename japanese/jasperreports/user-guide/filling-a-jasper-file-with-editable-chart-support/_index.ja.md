---
title: .jasper ファイルに編集可能なチャート サポートを入力する
type: docs
weight: 10
url: /ja/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

Aspose.Cells for JasperReports では、XLS ファイルにエクスポートする前に、.jasper ファイルを .jrprint または JasperPrint オブジェクトに入力する必要があります。 .jrxml ファイルを変更する必要はまったくありません。塗りつぶし手順は、チャートの内部表現を JasperPrint オブジェクトに保存し、編集可能なチャートを生成するために使用されます。

{{% /alert %}} 

レポートの記入方法の詳細については、JasperReports のドキュメントを参照してください。

次に例を示します。

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
