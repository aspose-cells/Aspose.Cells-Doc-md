﻿---
title: Настройка уровня сжатия книги
type: docs
weight: 180
url: /ru/net/adjust-workbook-compression-level/
---
## **Настройка уровня сжатия рабочей книги**

Разработчики могут настроить уровень сжатия книги при работе с большими книгами. Разработчики могут отдавать предпочтение файлам меньшего размера, а не времени обработки, или наоборот. Aspose.Cells предоставляет**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** перечисление, которое можно использовать для установки уровня сжатия книги.**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** перечисление предоставляет следующие элементы.

- Уровень 1: самое быстрое, но наименее эффективное сжатие.
- Уровень 2: немного медленнее, но лучше, чем уровень 1.
- Уровень 3: немного медленнее, но лучше, чем уровень 2.
- Уровень 4: немного медленнее, но лучше, чем уровень 3.
- Уровень 5: немного медленнее, чем уровень 4, но с лучшим сжатием.
- Уровень 6: Хороший баланс скорости и эффективности сжатия.
- Уровень 7: Довольно хорошее сжатие!
- Level8: Лучшее сжатие, чем Level7!
- Уровень 9: «лучшее» сжатие, где «лучшее» означает максимальное уменьшение размера входного потока данных. Это также самое медленное сжатие.

 Следующий фрагмент кода демонстрирует использование**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**перечисление и сравнивает время преобразования для Level1, Level6 и Level9. Вы также можете сравнить размеры сгенерированных файлов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
