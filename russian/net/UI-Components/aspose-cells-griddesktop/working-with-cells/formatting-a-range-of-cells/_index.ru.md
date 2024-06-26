---
title: Форматирование диапазона ячеек
type: docs
weight: 60
url: /ru/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop, формат, стиль, ячейки
description: Эта статья представляет, как применять стилевой формат к ячейкам в GridDesktop.
---

{{% alert color="primary" %}} 

Эта тема также относится к серии тем, связанных с применением настроек шрифта и других стилей форматирования ячеек. Наши последние темы рассказывали о работе с такими функциями. Например, вы можете обратиться к темам [Изменение шрифта и цвета ячейки](/cells/ru/net/changing-the-font-and-color-of-a-cell/) и [Применение стилей к ячейкам](/cells/ru/net/applying-styles-on-cells/) для изучения тех же функций. Что же нового в этой теме, если мы уже рассмотрели эти концепции? Ну, единственное отличие этой темы от предыдущих заключается в том, что мы будем применять настройки форматирования (связанные с шрифтами и другими стилями) к диапазону ячеек вместо одной ячейки. Надеемся, что вы все еще найдете эту тему полезной для себя.

{{% /alert %}} 
## **Установка шрифта и стиля диапазона ячеек**
Прежде чем говорить о настройках форматирования (о которых мы уже много раз говорили в предыдущих темах), мы должны знать, как создать диапазон ячеек. Мы можем создать диапазон ячеек, используя класс **CellRange**, чей конструктор принимает некоторые параметры для указания диапазона ячеек. Мы можем указать диапазон ячеек, используя **Имена** или **Индексы строки и столбца** начальной и конечной ячеек.

После того как мы создали объект **CellRange**, мы можем использовать перегруженные версии методов **SetStyle**, **SetFont** & **SetFontColor** класса Worksheet, которые могут принимать объект **CellRange**, чтобы применить настройки форматирования на указанный диапазон ячеек.

Давайте рассмотрим пример, чтобы понять эту базовую концепцию.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
