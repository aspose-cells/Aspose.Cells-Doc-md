---
title: Metin Koşullu Biçimlendirme nasıl eklenir
description: Aspose.Cells for Python via .NET kullanarak Metin koşullu biçimlendirme nasıl uygulanır. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha fazla kontrol edebilirsiniz.
keywords: Aspose.Cells, Metin Koşullu Biçimlendirme, Python, Koşullu, Biçimlendirme
type: docs
weight: 70
url: /tr/python-net/how-to-add-text-conditional-formatting/
---

## **Olası Kullanım Senaryoları**
Elektronik tablolarında metne dayalı koşullu biçimlendirme kullanmak, belirli çıkış kriterlerini karşılayan hücreleri vurgulamak için faydalıdır. Bu, veri analizini geliştirebilir ve büyük bir veri kümesinde önemli bilgileri bulmayı kolaylaştırabilir. İşte metin koşullu biçimlendirme kullanmanın bazı nedenleri:

Özel Metinleri Vurgula: Belirli kelime, ifadeler veya karakterlere bağlı biçimlendirme uygulayabilirsiniz. Örneğin, "Acil" veya "Tamamlandı" içeren tüm hücreleri vurgulamak, projedeki görevleri kolayca ayırt etmenize yardımcı olabilir.
Desenleri veya Eğilimleri Tanımlayın: "Yüksek", "Orta", "Düşük" gibi kategoriler veya durumlar ile çalışıyorsanız, metne dayalı koşullu biçimlendirme bunları görsel olarak ayırt edebilir, böylece ilerlemeyi takip etmek veya görevleri önceliklendirmek daha kolay olur.
Hata veya Veri Girşi Uyarıları: Metin biçimlendirme tutarsız veya hatalı girişleri, yanlış yazılmış kelimeleri, eksik metinleri veya yanlış değerleri işaretleyebilir. Bu, çok sayıda metinsel giriş içeren veri kümelerinde özellikle faydalıdır.
Gelişmiş Okunabilirlik: Metne renk kodu uygulamak veya stilini değiştirmek ( kalın, italik vb.), önemli bilgilerin öne çıkmasını sağlar ve belgeyi genel olarak daha okunabilir hale getirir.
Dinamik Geri Bildirim: Metin belirli koşulları karşıladığında otomatik olarak biçimlendirmeyi ayarlayan kurallar kurabilirsiniz. Bu, veriler değiştikçe biçimlendirmeyi manuel olarak güncellemenize gerek kalmaz.

Özetle, metin koşullu biçimlendirme, ilgili bilgileri, hataları ve trendleri hızlıca fark etmenize yardımcı olur ve metinsel verilerin yönetim ve yorumlanmasında güçlü bir araçtır.

## **Excel Kullanarak Metin Koşullu Biçimlendirme Nasıl Eklenir**
Excel'de metne dayalı koşullu biçimlendirme eklemek için şu adımları izleyin:

Hücre Aralığını Seçin: Koşullu biçimlendirmeyi uygulamak istediğiniz hücreleri vurgulayın.
Koşullu Biçimlendirme Menüsünü Açın: Excel şeridindeki Anahtar sekmesine gidin. "Stiller" grubunda Koşullu Biçimlendirme'ye tıklayın.
Yeni Kural Seçin: Açılır menüden Yeni Kural'ı seçin.
"Sadece hücreleri biçimlendir" seçeneğini seçin: Yeni Biçimlendirme Kuralı iletişim kutusunda, "Bir Kural Türü Seçin" bölümünde "Sadece hücreleri biçimlendir"yi seçin.
Kural Kriterlerini Belirleyin: "Hücreleri biçimlendir" bölümünde, açılır menüden Belirli Metin'i seçin. Koşula göre içeren, başlar veya biter seçin. Biçimlendirmek istediğiniz metni girin (örneğin, "Acil" veya "Tamamlandı").
Biçimlendirmeyi Seçin: Biçim düğmesine tıklayın. Hücreleri Biçimlendir iletişim kutusunda, yazı tipi rengi, dolgu rengi veya diğer biçimlendirme seçeneklerini seçebilirsiniz.
Kuralı Uygula: İstediğiniz biçimi belirledikten sonra, Kuralı uygula'ya tıklayın. Yeni Biçimlendirme Kuralı iletişim kutusunda tekrar Tamam'a tıklayarak kapatın.
Sonuçları Görüntüle: Belirttiğiniz metni içeren hücreler artık biçimlendirilmiş olacak, bu da ilgili bilgileri kolayca görmenizi sağlar.


## **Aspose.Cells for Python via .NET kullanarak Metin Koşullu Biçimlendirme nasıl eklenir**

Aspose.Cells for Python via .NET, XLSX formatında hücrelerde Microsoft Excel 2007 ve sonrası sürümler tarafından sağlanan koşullu biçimlendirmeyi tam destekler. Bu örnek, gelişmiş koşullu biçimlendirme türleri için bir egzersiz gösterir; Bunlar arasında BeginsWith, ContainsBlank, ContainsText vb. bulunmaktadır.

### **Değer Belirtilen Metinle Başladığında Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_begin_with()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_begin_with.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_begin_with(self):
        conds = self.get_format_condition("E15:G16", Color.light_goldenrod_yellow)
        idx = conds.add_condition(FormatConditionType.BEGINS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E15").put_value("abc")
        self._sheet.cells.get("G16").put_value("babx")


    def get_format_condition(self, cell_area_name, color):
        index = self._sheet.conditional_formattings.add()
        format_conditions = self._sheet.conditional_formattings[index]
        area = self.get_cell_area_by_name(cell_area_name)
        format_conditions.add_area(area)
        self.fill_cell(cell_area_name, color)
        return format_conditions

    def fill_cell(self, cell_area_name, color):
        area = self.get_cell_area_by_name(cell_area_name)
        k = 0
        for i in range(area.start_column, area.end_column + 1):
            for j in range(area.start_row, area.end_row + 1):
                c = self._sheet.cells.get(j, i)
                if color != Color.empty:
                    s = c.get_style()
                    s.foreground_color = color
                    s.pattern = BackgroundType.SOLID
                    c.set_style(s)
                value = j + i + k
                c.put_value(value)
                k += 1

    @staticmethod
    def get_cell_area_by_name(s):
        area = CellArea()
        str_cell_range = s.replace("$", "").split(':')
        start_row, start_col = CellsHelper.cell_name_to_index(str_cell_range[0])
        area.start_row = start_row
        area.start_column = start_col
        if len(str_cell_range) == 1:
            area.end_row = start_row
            area.end_column = start_col
        else:
            end_row, end_col = CellsHelper.cell_name_to_index(str_cell_range[1])
            area.end_row = end_row
            area.end_column = end_col
        return area

```
### **Değer Boşsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_contains_blank()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_blank.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_contains_blank(self):
        conds = self.get_format_condition("E9:G10", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E9").put_value("  ")
        self._sheet.cells.get("G10").put_value("  ")

```

### **Hata İçeriyorsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_contains_error()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_error.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_contains_error(self):
        conds = self.get_format_condition("E17:G18", Color.light_sky_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E17").put_value("  ")
        self._sheet.cells.get("G18").put_value("  ")

```

### **Belirtilen Metni İçeriyorsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_contains_text()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_text.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_contains_text(self):
        conds = self.get_format_condition("E5:G6", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "1"

```

### **Tekrarlayan Değerleri İçeriyorsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_duplicate()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_duplicate.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_duplicate(self):
        conds = self.get_format_condition("E23:G24", Color.light_slate_gray)
        idx = conds.add_condition(FormatConditionType.DUPLICATE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E23").put_value("bb")
        self._sheet.cells.get("G24").put_value("bb")

```

### **Belirtilen Metinle Biten Değeri İçeriyorsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_end_with()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_end_with.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_end_with(self):
        conds = self.get_format_condition("E13:G14", Color.light_gray)
        idx = conds.add_condition(FormatConditionType.ENDS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E13").put_value("nnnab")
        self._sheet.cells.get("G14").put_value("mmmabc")

```

### **Değer Boş Değilse Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_not_contains_blank()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_blank.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_blank(self):
        conds = self.get_format_condition("E11:G12", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E11").put_value("abc")
        self._sheet.cells.get("G12").put_value("  ")

```

### **Hata İçermiyorsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_not_contains_error()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_error.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_error(self):
        conds = self.get_format_condition("E19:G20", Color.light_sea_green)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E19").put_value("  ")
        self._sheet.cells.get("G20").put_value("  ")

```

### **Belirtilen Metni İçermiyorsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_not_contains_text()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_text.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_text(self):
        conds = self.get_format_condition("E7:G8", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "3"
```

### **Benzersiz Değerleri İçeriyorsa Hücreyi Biçimlendir**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_unique()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_unique.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_unique(self):
        conds = self.get_format_condition("E21:G22", Color.light_salmon)
        idx = conds.add_condition(FormatConditionType.UNIQUE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E21").put_value("aa")
        self._sheet.cells.get("G22").put_value("aa")

```

{{< app/cells/assistant language="python-net" >}}
