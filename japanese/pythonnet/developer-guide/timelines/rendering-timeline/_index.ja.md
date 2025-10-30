---
title: タイムラインのレンダリング
type: docs
weight: 40
url: /ja/python-net/rendering-timeline/
description: Aspose.Cells for Python via .NETでExcelファイルのタイムラインを管理する。
keywords: PythonでAspose.Cells for Python via .NETを使用してExcelなしでタイムラインをレンダリングする方法、Aspose.Cells for Pythonライブラリを使ってタイムラインを画像にレンダリングする。
---

## **可能な使用シナリオ**
Aspose.Cells for Python via .NETは、オフィス2013、オフィス2016、オフィス2019、およびオフィス365を使用せずにタイムラインの形状をレンダリングすることをサポートしています。ワークシートを画像に変換したり、ワークブックをPDFやHTML形式に保存すると、タイムラインが適切にレンダリングされます。

## **Aspose.Cells for Python Excel Libraryを使用したタイムラインのレンダリング方法**
次のサンプルコードは、既存のタイムラインを含む[sample Excel file](input.xlsx)を読み込みます。タイムラインの名前に応じてシェイプオブジェクトを取得し、Shape.to_image()メソッドを使用して画像にレンダリングします。次の画像は、レンダリングされたタイムラインを示す[output image](out.png)です。タイムラインが適切にレンダリングされ、サンプルExcelファイルと同じように見えることがわかります。

![todo:image_alt_text](out.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-RenderingTimeline.py" >}}

{{< app/cells/assistant language="python-net" >}}
