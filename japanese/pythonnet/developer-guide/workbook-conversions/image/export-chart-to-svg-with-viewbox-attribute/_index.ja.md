---
title: viewBox属性を使用してチャートをSVG形式にエクスポート
type: docs
weight: 280
url: /ja/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cells for Python via .NETを使用して、 viewBox 属性を使用してSVG形式にチャートをエクスポートします。
keywords: PythonでviewBox属性を持つSVGにチャートをエクスポート、PythonでviewBox属性を持つSVGにチャートをエクスポートするvia NET、PythonでviewBox属性を持つSVGにチャートを変換する。
---

{{% alert color="primary" %}}

デフォルトでは、チャートをSVG形式にエクスポートすると、そのXMLに**viewBox**属性は含まれません。ただし、Aspose.Cells for Python via .NETは、**true**に設定すると、**viewBox**属性を含めてチャートをSVG形式にエクスポートするプロパティを提供します。

{{% /alert %}}

## viewBox属性を含むSVG形式でチャートをエクスポート

次のコードサンプルは、viewBox属性を含むSVG形式でチャートをエクスポートします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

チャートのSVGをNotepadで開くと、次のような**viewBox**属性が見つかります。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
