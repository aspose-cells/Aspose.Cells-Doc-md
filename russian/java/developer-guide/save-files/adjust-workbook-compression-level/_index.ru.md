---
title: Настройка уровня сжатия книги
type: docs
weight: 130
url: /ru/java/adjust-workbook-compression-level/
---
## **Настройка уровня сжатия книги**

Разработчики могут настроить уровень сжатия книги при работе с большими книгами. Разработчики могут отдавать предпочтение файлам меньшего размера, а не времени обработки, или наоборот. Aspose.Cells предоставляет**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**перечисление, которое можно использовать для установки уровня сжатия книги.**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** перечисление предоставляет следующие элементы.

- **[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: самое быстрое, но наименее эффективное сжатие.
- **[LEVEL_2](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: Немного медленнее, но лучше, чем уровень 1.
- **[LEVEL_3](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**Немного медленнее, но лучше, чем уровень 2.
- **[LEVEL_4](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: Немного медленнее, но лучше, чем уровень 3.
- **[LEVEL_5](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: Немного медленнее, чем уровень 4, но с лучшим сжатием.
- **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**: Хороший баланс скорости и эффективности сжатия.
- **[LEVEL_7](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: Довольно хорошее сжатие!
- **[LEVEL_8](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: Лучшее сжатие, чем Level7!
- **[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**«лучшее» сжатие, где «лучшее» означает максимальное уменьшение размера входного потока данных. Это также самое медленное сжатие.

Следующий фрагмент кода демонстрирует использование**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** перечисление и сравнивает время преобразования для**[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)** , и**[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**. Вы также можете сравнить размеры сгенерированных файлов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
