---
title: Настройка уровня сжатия книги Excel
type: docs
weight: 180
url: /ru/python-net/adjust-workbook-compression-level/
---

## **Настройка уровня сжатия книги**

Разработчики могут настроить уровень сжатия рабочей книги при работе с большими файлами. Можно отдавать предпочтение меньшему размеру файла или меньшему времени обработки. Aspose.Cells для Python via .NET предоставляет перечисление [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype), которое можно использовать для установки уровня сжатия рабочей книги. Перечисление [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) содержит следующие элементы.

- Level1: Самое быстрое, но наименее эффективное сжатие.
- Level2: Немного медленнее, но лучше, чем уровень 1.
- Level3: Немного медленнее, но лучше, чем уровень 2.
- Level4: Немного медленнее, но лучше, чем уровень 3.
- Level5: Немного медленнее, чем уровень 4, но с лучшим сжатием.
- Level6: Хороший баланс скорости и эффективности сжатия.
- Уровень7: Довольно хорошее сжатие!
- Уровень8: Лучшее сжатие, чем на уровне 7!
- Уровень9: Самое "лучшее" сжатие, где лучший означает наибольшее уменьшение размера входного потока данных. Это также самое медленное сжатие.

В следующем фрагменте кода демонстрируется использование перечисления [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) и сравнение времени преобразования для уровней 1, 6 и 9. Также можно сравнить размеры созданных файлов.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
