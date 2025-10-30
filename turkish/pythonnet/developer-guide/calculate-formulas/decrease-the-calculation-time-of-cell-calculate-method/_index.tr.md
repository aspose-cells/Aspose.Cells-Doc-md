---
title: Cell.Calculate Yönteminin Hesaplama Süresini Python.NET ile Azaltın
linktitle: Cell.Calculate Hesaplama Süresini Azaltın
type: docs
weight: 100
url: /tr/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Aspose.Cells for Python via .NET kullanarak Excel hücre hesaplama performansını nasıl optimize edeceğinizi öğrenin. Hesaplama süresini CalculationOptions ayarlarıyla azaltın.
keywords: python excel hesaplama, hücre hesaplamasını optimize et, Aspose.Cells Python, hesaplama performansı, tekrar eden hesaplama seçenekleri
---

## **Olası Kullanım Senaryoları**

Genellikle, kullanıcıların [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) yöntemini bir kez çağırmasını ve ardından bireysel hücrelerin hesaplanan değerlerini almasını öneririz. Tek hücre hesaplamalarıyla çalışırken, [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/) özelliğini kullanarak hesaplama süresini önemli ölçüde azaltabilirsiniz. Bu özelliği `False` olarak ayarlamak, bağlı hücreleri sonraki çağrılarda yeniden hesaplamayı önler.

## **Hücre Hesaplama Performansını Optimize Etme**

Aşağıdaki örnek, özyinelemeli özelliğin kullanımını gösterir. Performans farkını test etmek için sağlanan [örnek Excel dosyasını](5113710.xlsx) kullanın. Kod, `recursive=False` olarak ayarlamanın gereksiz bağlı hücre yeniden hesaplamalarını önleyerek hesaplama süresini nasıl azalttığını gösterir.

```python
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Test calculation time after setting recursive true
test_calc_time_recursive(True)

# Test calculation time after setting recursive false
test_calc_time_recursive(False)
```

```python
import os
import time
from aspose.cells import Workbook, CalculationOptions

def test_calc_time_recursive(rec):
    """
    Tests calculation time with recursive option and prints elapsed seconds
    """
    # The path to the documents directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")

    # Load sample workbook
    wb = Workbook(os.path.join(data_dir, "sample.xlsx"))

    # Access first worksheet
    ws = wb.worksheets[0]

    # Set calculation options
    opts = CalculationOptions()
    opts.recursive = rec

    # Start timing
    start_time = time.perf_counter()

    # Calculate cell A1 one million times
    for _ in range(1000000):
        ws.cells.get("A1").calculate(opts)

    # Calculate elapsed time
    elapsed_time = int(time.perf_counter() - start_time)

    # Print results
    print(f"Recursive {rec}: {elapsed_time} seconds")
```

## **Performans Karşılaştırma Sonuçları**

Optimize edilmiş kodun örnek dosya ile çalıştırıldığında gösterdiği tipik çıktı önemli ölçüde zaman azalması sağlar:

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
