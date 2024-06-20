---
title: Hücreden HTML5 dizesi al
type: docs
weight: 90
url: /tr/python-net/get-html5-string-from-cell/
description: Python via .NET API si aracılığıyla Aspose.Cells ile Hücreden HTML5 dizesi almayı öğrenin.
keywords: Python Excel Kütüphanesi, Python da Hücreden HTML5 dizesi al, Python da Hücreden HTML5 dizesi alarak Python kullanımı, Python da Hücreden HTML5 dizesini yönet.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET, bir boolean parametre alan [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) yöntemini kullanarak hücrenin HTML dizesini döndürür. Parametre olarak **false** geçirirseniz Normal HTML döndürür, ancak **true** geçirirseniz HTML5 dizesini döndürür.

## **Hücreden HTML5 dizesi al**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışsayısının A1 hücresine bazı metinler ekler. Ardından, A1 hücresinden Normal HTML ve HTML5 dizelerini [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) yöntemini kullanarak alır ve bunları konsola yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
