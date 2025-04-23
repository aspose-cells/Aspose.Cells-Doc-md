---
title: Python.NET ile HTML ye kaydederken CSS Özel Özelliklerini Etkinleştir
linktitle: HTML ye Kaydederken CSS Özel Özelliklerini Etkinleştir
type: docs
weight: 320
url: /tr/python-net/enable-css-custom-properties-while-saving-to-html/
description: Aspose.Cells for Python via .NET API kullanarak Excel dosyalarını HTML ye kaydederken CSS özel özelliklerini nasıl etkinleştireceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, bir temel64 resminin birden çok kez oluştuğu durumlarda, CSS özel özelliklerini kullanmak, görüntü verisinin yalnızca bir kez kaydedilmesini sağlar. Bu, ortaya çıkan HTML'nin performansını artırır. Lütfen [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) özniteliğini kullanın ve kaydederken **True** olarak ayarlayın.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## ** HTML'ye Kaydederken CSS Özel Özelliklerini Etkinleştir**

 Aşağıdaki örnek kod, [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) özniteliğinin kullanımını gösterir. Ekran görüntüsü, bu özelliğin **True** olarak ayarlanmadığında etkisini gösterir. Bu kodda kullanılan örnek Excel dosyasını ([örnek Excel dosyası](50528260.xlsx)) ve oluşturulan çıktı HTML'sini ([çıktı HTMLsi](50528261.zip)) referans olması için indirin.

## **Örnek Kod**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Load sample workbook
wb = Workbook(os.path.join(source_dir, "sampleEnableCssCustomProperties.xlsx"))

# Configure HTML save options
opts = HtmlSaveOptions()
opts.export_images_as_base64 = True
opts.enable_css_custom_properties = True

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputEnableCssCustomProperties.html"), opts)
```
