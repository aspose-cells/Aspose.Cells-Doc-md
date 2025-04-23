---
title: ワークブックからOLEオブジェクトを抽出
type: docs
weight: 110
url: /ja/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

時には、WorkbookからOLEオブジェクトを抽出する必要があります。Aspose.Cells for Python via .NETは、そのOleオブジェクトの抽出と保存をサポートしています。

この記事は、少数のコード行でVisual Studio.Netでコンソールアプリケーションを作成し、ワークブックから異なるOLEオブジェクトを抽出する方法を示しています。

{{% /alert %}}

## **ワークブックからOLEオブジェクトを抽出**

### **テンプレートワークブックの作成**

1. Microsoft Excelでワークブックを作成しました。
1. 最初のワークシートにMicrosoft Wordドキュメント、Excelワークブック、PDFドキュメントをOLEオブジェクトとして追加しました。

|**OLEオブジェクトを含むテンプレートドキュメント（OleFile.xls）**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

次に、OLEオブジェクトを抽出し、それらをそれぞれのファイルタイプでハードディスクに保存します。

### **Aspose.Cells for Python Excelライブラリを使用したOLEオブジェクトの抽出**

以下のコードは実際にOLEオブジェクトを検出して抽出する実際の作業を行います。OLEオブジェクト（DOC、XLS、PDFファイル）はディスクに保存されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
