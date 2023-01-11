﻿---
title: Aspose.Cells for Java 7.3.4 Примечания к выпуску
type: docs
weight: 10
url: /ru/java/aspose-cells-for-java-7-3-4-release-notes/
---
{{% alert color="primary" %}} 

 Эта страница содержит примечания к выпуску для[Aspose.Cells for Java 7.3.4](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.4/)

{{% /alert %}} 

Мы
рад сообщить Aspose.Cells for Java v7.3.4!

 Новые особенности

- Поддержка формата TIFF в функции Sheet-to-Image

 Улучшения

- Правый нижний колонтитул не находится над центральным нижним колонтитулом, как в MS Excel.

 Исключения

- Исключение нехватки памяти при преобразовании Excel в PDF
- Установка «+100» в качестве условной формулы вызвала исключение
- Исключение: «StackOverflowError» при вычислении формул
- «IllegalArgumentException» возникает при вызове Workbook.copy()

 Ошибки

- Арабский текст стал ненужными символами в сохраненном файле CSV с кодировкой UTF-8.
- Ошибка «Возможно, потеряны данные» для повторно сохраненного файла XLS пользователем Aspose.Cells
- «Excel обнаружил нечитаемое содержимое…..»ошибка для Aspose.Cells сгенерированного отчета
- Cell.getFormula() не различал диапазоны с разными именами с одинаковым именем, но с разной областью действия
- Автоматический заголовок для проблемы с круговой диаграммой
- Cell.getR1C1Formula() не различал разные именованные диапазоны с одинаковым именем, но с разной областью действия