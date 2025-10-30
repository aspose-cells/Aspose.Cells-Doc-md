---
title: Aspose.Cells で印刷時にジョブまたはドキュメント名を指定する
type: docs
weight: 270
url: /ja/python-net/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

印刷時にJob名やドキュメント名を指定できます。Aspose.Cells for Python via .NETは、WorkbookRender.ToPrinter(printerName, jobName)とSheetRender.ToPrinter(printerName, jobName)のメソッドを提供し、印刷中にジョブ名を指定可能です。

{{% /alert %}}

## **Aspose.Cells for Python via .NETを使って印刷する際に、ジョブまたはドキュメント名を指定してください。**

サンプルコードは、元のExcelファイルをロードし、WorkbookRender.ToPrinter（printerName、jobName）およびSheetRender.ToPrinter（printerName、jobName）メソッドを使用してジョブまたは文書名を指定して印刷用に送信します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SpecifyJobNameWhilePrinting.py" >}}
{{< app/cells/assistant language="python-net" >}}
