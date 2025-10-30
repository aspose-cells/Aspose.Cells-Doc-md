---
title: Python.NET kullanarak Gelişmiş Koşullu Biçimlendirme Uygula
linktitle: Gelişmiş Koşullu Biçimlendirme Uygulama
type: docs
weight: 70
url: /tr/python-net/apply-advanced-conditional-formatting/
description: Aspose.Cells for Python via .NET kullanarak veri çubukları, renk ölçekleri ve simge setleri gibi gelişmiş koşullu biçimlendirme özelliklerini nasıl uygulayacağınızı öğrenin.
keywords: Python Excel biçimlendirme, Koşullu biçimlendirme Python, Veri çubukları Python, Renk ölçekleri Python, Simge setleri Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 ve sonraki sürümler (2010/2013/2016) gelişmiş koşullu biçimlendirme özellikleri sağlar; hücre gölgeleme, kenarlıklar, renkli simgeler, oklar, rozetler ve yazı tipi biçimlendirmeyi içerir.

{{% /alert %}} 

## **Excel Dosyalarında Gelişmiş Koşullu Biçimlendirmeyi Uygula**
Aspose.Cells for Python via .NET tüm gelişmiş koşullu biçimlendirme özelliklerini destekler;

- Basit bir çubuk grafiğini hücrelere gömerek altta yatan sayıları grafiksel olarak vurgulamak için gölgeli veri çubukları ekleyebilir.
- Hücreleri otomatik olarak renk skalalarına göre gölgelendirir, bu, aralıktaki diğer hücrelerdeki değerlere bağlı olarak en düşük değeri kırmızıdan en yüksek değeri yeşile hareket ettirir.
- Renk skalaları gibi simge setlerini renk skalaları gibi kullanır, ancak hücreleri gölgelendirmek yerine oklar ve trafik ışıkları gibi küçük simgeler ekler.

Aspose.Cells, Microsoft Excel 2007 ve sonraki sürümlerin sağladığı koşullu biçimlendirmeleri XLSX formatında çalışma zamanında tamamen destekler. Bu örnek, farklı özelliklere sahip simge setleri, veri çubukları, renk skalaları, zaman periyotları, en üst/en alt ve diğer kurallara yönelik gelişmiş koşullu biçimlendirme türleri için bir egzersiz göstermektedir.

- [**Adding Color Scale Conditional Formattings**](/cells/tr/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/tr/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/tr/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/tr/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/tr/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/tr/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/tr/python-net/how-to-add-top10-conditional-formatting/)



### **Excel'in Renk Seçimi ile Renk Skalası Biçimlendirilmesi Hesapla**
Bu kod, Excel'in Renk Skalası koşullu biçimlendirme kuralları için seçtiği rengi belirlemeye nasıl kullanılır gösterir:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
