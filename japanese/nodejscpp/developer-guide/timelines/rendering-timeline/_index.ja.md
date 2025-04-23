---
title: タイムラインのレンダリング
type: docs
weight: 40
url: /ja/nodejs-cpp/rendering-timeline/
description: Aspose.Cells for Node.js via C++でExcelファイルのタイムライン管理
keywords: Office 2013、Office 2016、Office 2019、Office 365を使用せずにタイムラインをレンダリング
---

## **可能な使用シナリオ**
Aspose.Cells for Node.js via C++は、Office 2013、Office 2016、Office 2019、および Office 365を使用せずにタイムラインシェイプのレンダリングをサポートしています。ワークシートを画像に変換したり、ブックをPDFやHTML形式で保存した場合でも、タイムラインは正しくレンダリングされているのが見えます。

## **タイムラインのレンダリング**
以下のサンプルコードは、既存のタイムラインを含む[サンプルExcelファイル](input.xlsx)をロードします。その後、タイムラインの名前に応じてシェイプオブジェクトを取得し、Shape.ToImage()メソッドを使用して画像にレンダリングします。以下の画像は、レンダリングされたタイムラインを示す[出力画像](out.png)です。タイムラインが適切にレンダリングされており、サンプルExcelファイルと同じように見えます。

![todo:image_alt_text](out.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-RenderingTimeline.js" >}}
