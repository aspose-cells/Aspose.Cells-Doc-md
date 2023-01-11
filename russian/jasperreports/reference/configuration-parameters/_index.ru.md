﻿---
title: Параметры конфигурации
type: docs
weight: 10
url: /ru/jasperreports/configuration-parameters/
---
{{% alert color="primary" %}} 

 В следующей таблице перечислены параметры конфигурации.

{{% /alert %}} 

|**Имя параметра** |**Описание** |
|:- |:- |
| FORMAT_TYPE| Можно установить значение «EXCEL97TO2003» или «EXCEL2007» для создания файлов формата Microsoft Excel 79 0 2003 или Excel 2007.|
|ЯВЛЯЕТСЯ_ОДИН_СТРАНИЦА_ПЕР_ ЛИСТ| Логическое значение, указывающее, следует ли записывать каждую страницу отчета на другой рабочий лист XLS.|
|ЯВЛЯЕТСЯ_УДАЛИТЬ_ПУСТОЙ_ПРОСТРАНСТВО_ BETWEEN_ROWS| Логическое значение, указывающее, следует ли удалять пустые места, которые могут появляться между строками.|
|ЯВЛЯЕТСЯ_УДАЛИТЬ_ПУСТОЙ_ПРОСТРАНСТВО_ BETWEEN_COLUMNS|Логическое значение, указывающее, следует ли удалять пустые пространства, которые могут появляться между столбцами.|
|ЯВЛЯЕТСЯ_БЕЛЫЙ_ PAGE_BACKGROUND| Логическое значение, указывающее, должен ли фон страницы быть белым или цветом фона по умолчанию XLS. Цвет фона XLS может варьироваться в зависимости от свойств средства просмотра XLS или цветовой схемы операционной системы.|
|ЯВЛЯЕТСЯ_ОБНАРУЖЕНИЕ_ CELL_TYPE| Флаг, используемый для указания, должен ли экспортер учитывать тип выражений исходного текстового поля и соответствующим образом устанавливать типы и значения ячеек.|
| SHEET_NAMES|Массив строк, представляющих пользовательские имена листов. Это полезно при использовании с IS_ОДИН_СТРАНИЦА_ПЕР_ параметр ЛИСТ.|
|ЯВЛЯЕТСЯ_ШРИФТ_РАЗМЕР_ИСПРАВИТЬ_ ВКЛЮЧЕНО| Флаг для уменьшения размера шрифта, чтобы текст помещался в указанную высоту ячейки.|
|МАКСИМУМ_РЯДЫ_ PER_SHEET|Целочисленное значение, указывающее максимальное количество строк, которые могут отображаться на листе. Если установлено, создается новый лист для отображения оставшихся строк. Отрицательные значения или ноль означают, что ограничение не установлено.|
|ЯВЛЯЕТСЯ_ИГНОРИРОВАТЬ_ ГРАФИКА| Флаг для игнорирования графических элементов и экспорта только текстовых элементов.|
|ЯВЛЯЕТСЯ_КРАХ_ ROW_SPAN| Отметьте сворачивающийся диапазон строк и избегайте слияния ячеек между строками.|
|ЯВЛЯЕТСЯ_ИГНОРИРОВАТЬ_ CELL_BORDER| Флаг игнорирования границы ячейки.|
|ЯВЛЯЕТСЯ_ИСПОЛЬЗОВАТЬ_ EXCEL_CHART| Флаг для использования редактируемой диаграммы в формате Microsoft Excel, а не статических изображений. Значение по умолчанию верно.|
