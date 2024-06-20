---
title: タイムラインのレンダリング
type: docs
weight: 40
url: /ja/java/rendering-timeline/
description: Aspose.Cells For JavaでExcelファイルのタイムラインを管理する。
keywords: Office 2013、Office 2016、Office 2019、Office 365を使用せずにタイムラインをレンダリング
---

## **可能な使用シナリオ**
Aspose.Cellsは、Office 2013、Office 2016、Office 2019、Office 365を使用せずにタイムラインの形状をレンダリングすることをサポートしています。ワークシートを画像に変換したり、ワークブックをPDFやHTML形式で保存すると、タイムラインが適切にレンダリングされます。

## **タイムラインのレンダリング**
以下のサンプルコードは、既存のタイムラインを含む[サンプルExcelファイル](input.xlsx)をロードします。その後、タイムラインの名前に応じてシェイプオブジェクトを取得し、Shape.ToImage()メソッドを使用して画像にレンダリングします。以下の画像は、レンダリングされたタイムラインを示す[出力画像](out.png)です。タイムラインが適切にレンダリングされており、サンプルExcelファイルと同じように見えます。

![todo:image_alt_text](out.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-RenderingTimeline.java" >}}

