---
title: Aspose.Cells for Java 7.2.2 Примечания к выпуску
type: docs
weight: 60
url: /ru/java/aspose-cells-for-java-7-2-2-release-notes/
---
{{% alert color="primary" %}} 

 Эта страница содержит примечания к выпуску для[Aspose.Cells for Java 7.2.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.2/)

{{% /alert %}} 

Мы
 рад сообщить Aspose.Cells for Java v7.2.2!

 Новые особенности

- Текстовый поиск RegEx для метода Cells.Find()

 Улучшения

- Сделать Aspose.Cells совместимым со старыми версиями банок Woodstox.
- Встроенные OLE-файлы OOXML в XLS выходят как упакованные файлы OLE вместо распакованных файлов
- Поддержка ExportObjectListener для сохранения файлов HTML.
- Копировать условное форматирование при копировании строк

 Исключения

- Picture.isPrintable() для Picture inPageSetup вызывает исключение NullPointerException
- Сохранение зашифрованной книги с помощью сводной таблицы вызывает исключение java.lang.NegativeArraySizeException

 Ошибки

- Cells.importCustomObjects() с указанным форматом DateTime не работает
- Неверный тип диаграммы точечной диаграммы
- Двойное значение теряет точность при чтении из файла шаблона CSV
- Серии диаграмм переворачивались вверх дном при преобразовании их в изображение
- Повторно сохраненный файл XLSX вызывает ошибку «Excel обнаружил нечитаемое содержимое…»
- Сохраненная сводная таблица вызывала «ProtectionView» при открытии в MS Excel
- Использование проверки списка с помощью Aspose.Cellscreates файла XLS, который не работает после изменения системного разделителя списков
