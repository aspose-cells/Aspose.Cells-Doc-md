---
title: Adlandırılmış Aralıkları Sil
type: docs
weight: 90
url: /tr/python-net/delete-named-ranges/
description: Aspose.Cells for Python aracılığıyla Excel veya OpenOffice dosyalarından tanımlanan isimleri veya adlandırılmış aralıkları nasıl kaldıracağınızı öğrenebilirsiniz.
keywords: Python Excel Kitaplığı, Python Yinelemeli Tanımlı Adları Kaldırma, Python Yinelemeli Tanımlı Adları Silme.
---

## **Giriş**
Eğer Excel dosyalarında çok fazla tanımlanmış isim veya adlandırılmış aralık varsa, tekrar atıfta bulunulmadığından bazılarını temizlememiz gerekebilir.

## **MS Excel'de Adlandırılmış Aralığı Kaldır**

Excel'den adlandırılmış bir aralığı kaldırmak için şu adımları izleyebilirsiniz:
1. Microsoft Excel'i açın ve adlandırılmış aralığı içeren çalışma kitabını açın.
2. Excel kurdelesindeki "Formüller" sekmesine gidin.
3. "Tanımlı İsimler" grubundaki "Ad Yöneticisi" düğmesini tıklayın. Bu, Ad Yöneticisi iletişim kutusunu açacaktır.
4. Ad Yöneticisi iletişim kutusunda, kaldırmak istediğiniz adlandırılmış aralığı seçin.
5. "Sil" düğmesine tıklayın. İstenildiğinde silme işlemini onaylayın.
6. Ad Yöneticisi iletişim kutusunu kapatmak için "Kapat" düğmesine tıklayın.
7. Değişiklikleri korumak için çalışma kitabını kaydedin.

## **Aspose.Cells for .Net kullanarak Adlandırılmış Aralığı Silme**
Aspose.Cells for .Net ile, listede yer alan adları [metin](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str) kullanarak kaldırabilirsiniz.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

Not: Tanımlı isim formüller tarafından başvuruluyorsa, kaldırılamaz. Sadece tanımlı ismin formülünü kaldırabiliriz.

## **Bazı Adlandırılmış Aralıkları Kaldırma**
Bir tanımlı ismi kaldırdığımızda, dosyadaki tüm formüller tarafından kullanılıp kullanılmadığını kontrol etmeliyiz.
Adlandırılmış aralıkları kaldırmak için performansı iyileştirmek için birlikte bazılarını kaldırabiliriz.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **Yinelenen Tanımlı İsimleri Kaldırma**
Bazı Excel dosyaları, bazı tanımlı isimlerin yinelenmesi nedeniyle bozulur. Bu yinelenen isimleri kaldırarak dosyayı onarabiliriz.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
