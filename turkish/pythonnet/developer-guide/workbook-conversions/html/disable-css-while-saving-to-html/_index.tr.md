---
title: Kaydetme sırasında CSS yi devre dışı bırakırken HTML ile Python.NET kullan
linktitle: HTML ye Kaydederken CSS yi Devre Dışı Bırakın
type: docs
weight: 320
url: /tr/python-net/disable-css-while-saving-to-html/
description: Aspose.Cells for Python via .NET API kullanarak Excel dosyalarını HTML formatına kaydederken CSS stillerini nasıl devre dışı bırakacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı tek sayfa HTML'ye kaydettiğinizde, genellikle CSS öğeleri HTML dosyasına gömülür ve HEAD bölümünde bulunur. Bu dosyayı bir e-posta içeriği/gövdesi olarak eklediğinizde, CSS öğeleri çoğu e-posta istemcisi tarafından kaldırılır ve bu da yanlış görüntüleme ile sonuçlanır. Aspose.Cells for Python via .NET API, CSS'yi isteğe bağlı olarak devre dışı bırakmanızı sağlayan bir seçenek sunar; böylece stiller doğrudan HTML öğeleri içinde uygulanabilir. E-posta içeriği/gövdesi olarak HTML ayarlamak istiyorsanız, lütfen [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) özelliğini kullanın ve **True** olarak ayarlayın.

## ** Kaydetme sırasında CSS'yi Devre Dışı Bırakın**

 Aşağıdaki örnek kod, [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) özelliğinin kullanımını gösterir.

## **Örnek Kod**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Load sample workbook
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleDisableCss.xlsx"))

# Disable CSS
opts = HtmlSaveOptions()
opts.disable_css = True

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in html
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}
