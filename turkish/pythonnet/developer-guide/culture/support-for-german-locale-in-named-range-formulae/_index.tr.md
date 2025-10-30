---
title: Python.NET ile Tanımlı İsimli Aralık Formüllerinde Almanca Yerel Ayarlara Destek
linktitle: Adlandırılmış Aralık Formüllerinde Alman Locale Desteği
type: docs
weight: 60
url: /tr/python-net/support-for-german-locale-in-named-range-formulae/
description: Aspose.Cells for Python via .NET kullanarak Excel de isimli aralık formülleri için Almanca yerel ayarlarını nasıl yöneteceğinizi öğrenin.
---

İngilizce formüller, adlandırılmış bölgelerde yazılır. Bu Excel dosyası, sisteminizin Almanca yerel ayarda yapılandırıldığı bir ortamda açılabilir ve İngilizce formüller Almanca diline çevrilebilir. Bu örnek, Almanca dil ayarlarına sahip Excel yüklü ve sistem yerel ayarı Almanca olan ortamlar için uygundur.

Bu özelliğin test edilmesi için örnek dosya indirilebilir:  
[sampleNamedRangeTest.xlsm](73990165.xlsm)

```python
import os
from aspose.cells import Workbook

source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

name = "HasFormula"
value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

wb_source = Workbook(os.path.join(source_dir, "sampleNamedRangeTest.xlsm"))
ws_col = wb_source.worksheets

name_index = ws_col.names.add(name)
named_range = ws_col.names[name_index]
named_range.refers_to = value

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb_source.save(os.path.join(output_dir, "sampleOutputNamedRangeTest.xlsm"))
```
{{< app/cells/assistant language="python-net" >}}
