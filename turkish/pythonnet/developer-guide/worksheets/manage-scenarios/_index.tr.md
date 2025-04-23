---
title: Python ile Çalışma Sayfalarından Senaryolar Oluşturma, Manipüle Etme veya Kaldırma via .NET
linktitle: Senaryoları Yönetme
type: docs
weight: 190
url: /tr/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Aspose.Cells for Python via .NET API lerini kullanarak Excel çalışma sayfalarında programlı olarak senaryolar oluşturmayı, değiştirmeyi ve silmeyi öğrenin.
keywords: Python Excel senaryoları, çalışma sayfası senaryolarını yönet Python, senaryo ekle Python, çalışma sayfası senaryosunu kaldır Python, senaryoları değiştir Python
---

{{% alert color="primary" %}}

Bazen çalışma tablolarında senaryolar oluşturmanız, manipüle etmeniz veya silmeniz gerekebilir. Bir senaryo, değişken giriş hücreleri ve bir veya daha fazla formül ile bağlantılı adlandırılmış 'what if?' modelidir. Bir senaryo oluşturmadan önce, en az bir formüle bağlı hücreler içeren ve farklı değerler alabilen hücreler içerecek şekilde çalışma sayfasını tasarlayın. Bu örnek, Aspose.Cells for Python via .NET kullanarak çalışma sayfalarındaki senaryoların nasıl yönetileceğini gösterir.

{{% /alert %}}

Aspose.Cells, senaryolarla çalışma yapmak için birkaç sınıf sağlar:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

Senaryolara erişmek için [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) özelliğini kullanın. Aşağıdaki kod şu işlemleri gösterir:
1. Senaryolar içeren bir Excel dosyasını açın
2. Mevcut bir senaryoyu kaldırın
3. Yeni bir senaryo ekleyin

4. Değiştirilen çalışma kitabını kaydedin

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate the Workbook and load an Excel file
workbook = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
# Access first worksheet
worksheet = workbook.worksheets[0]

if len(worksheet.scenarios) > 0:
    # Remove the existing first scenario from the sheet
    worksheet.scenarios.remove_at(0)

    # Create a scenario
    i = worksheet.scenarios.add("MyScenario")
    # Get the scenario
    scenario = worksheet.scenarios[i]
    # Add comment to it
    scenario.comment = "Test sceanrio is created."
    # Get the input cells for the scenario
    sic = scenario.input_cells
    # Add the scenario on B4 (as changing cell) with default value
    sic.add(3, 1, "1100000")

    output_path = os.path.join(data_dir, "outBk_scenarios1.out.xlsx")

    # Save the Excel file
    workbook.save(output_path)
    print(f"\nProcess completed successfully.\nFile saved at {output_path}")
```

