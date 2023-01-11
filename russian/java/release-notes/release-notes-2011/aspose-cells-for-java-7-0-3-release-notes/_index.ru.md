﻿---
title: Aspose.Cells for Java 7.0.3 Примечания к выпуску
type: docs
weight: 10
url: /ru/java/aspose-cells-for-java-7-0-3-release-notes/
---
{{% alert color="primary" %}} 

 Эта страница содержит примечания к выпуску для[Aspose.Cells for Java 7.0.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.0.3/)

{{% /alert %}} 

 Мы рады сообщить Aspose.Cells for Java v7.0.3!

 Общие характеристики/улучшения

 Поддержка LightCellsDataProvider для сохранения файла XLS

 Внесены улучшения для функции Excel-to-PDF.

 31329 - Включите полезный метод: PivotField.getBaseIndex()

40015 - Сделать библиотеку совместимой с webservices-rt.jar

 40011 — Поддержка получения всех цветов, которые используются различными объектами в рабочей книге.

 Исключения

 40022 - Чтение файла шаблона XLS с установленным параметром: LoadDataOnly=true дает исключение

 40017 - Метод WorksheetCollection.getNamedRanges() дает исключение

 40033 - Получить исключение «Неверный пароль» при чтении файла шаблона XLSX

 Ошибки

 31303 - значение Cell с символами '"' и ',' было сохранено неправильно для файла CSV

 31376 - Сохранение PDF заняло слишком много времени и создало очень большой файл PDF

 40001 - символ валюты был потерян при форматировании значений ячейки

 40003 - Текстовая ориентация объединенных ячеек изменена в сгенерированном файле PDF

 40002 - Сохраненная сводная таблица вызывает ошибку MS Excel

 40010 — вставка строк приводит к нарушению работы объединенных ячеек

 40013 - Символы автофильтра дублировались и становились крупнее при пересохранении файла XLS

40014 - Линии сетки не отображались на сгенерированном изображении для листа.

 40016 - Сохраненный файл XLS заставляет MS Excel выдавать предупреждающие сообщения -1

 40020 - Сохраненный файл XLS заставляет MS Excel выдавать предупреждающие сообщения -2

 40021 - Сохраненный файл XLS заставляет MS Excel выдавать предупреждающие сообщения -3

 40023 - Cell потерять формат после удаления строк

 40024 - удалить гиперссылки при очистке содержимого диапазона ячеек

 40028 - Color.equals() не возвращает true, когда значения RGB совпадают

 40031 - SortNames() уничтожает именованные диапазоны

 40032 - При установке меток данных точки диаграммы теряются унаследованные настройки из меток данных серии.

 40084 - значения DateTime читаются как двойной формат

 40085 - Когда строка/столбец превышает ограничение файла XLS, сохраненный XLS вызывает ошибку «Excel обнаружил нечитаемое содержимое» при открытии в MS Excel