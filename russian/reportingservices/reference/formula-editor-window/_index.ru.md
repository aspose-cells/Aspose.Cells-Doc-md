﻿---
title: Окно редактора формул
type: docs
weight: 20
url: /ru/reportingservices/formula-editor-window/
---
{{% alert color="primary" %}} 

Редактор формул позволяет создавать формулы для отчета.

{{% /alert %}} 

Чтобы изменить формулу в ячейке Excel Microsoft:

1. В Excel Microsoft выберите ячейку.
1.  Откройте диалоговое окно «Редактировать формулу», нажав**Изменить формулу** на панели инструментов.
   ([Добавление формул служб Reporting Services](/cells/ru/reportingservices/adding-reporting-services-formulas/) показывает пример, который редактирует формулу.)
 Диалог разделен на секции: область редактирования вверху и область формул внизу. Используйте область формул, чтобы заполнить область редактирования.
1.  Выберите категорию (пользователь, параметры, поля и т. д.) из**Поля отчета** список (левый список).
1.  Выберите тип из списка**Функции** список (посередине).
1.  Выберите вариант из**Операторы** список (правый список).
1.  Нажмите**Вставлять**чтобы добавить выражение к**Редактировать** площадь.
1.  Нажмите**Вставлять** когда выражение завершено.
 Формула вставляется в ячейку.

**Диалоговое окно «Редактировать формулу»** 

![дело:изображение_альтернативный_текст](formula-editor-window_1.png)

Диалоговое окно «Редактировать формулу» разделено на разделы, описанные ниже.
#### **Редактировать область**
 Это область, в которой вы создаете или редактируете формулу. Создайте формулу, дважды щелкнув любой из компонентов, перечисленных в**Поля отчета**, **Функции** или же**Операторы** списки. При выборе компонента также вставляется требуемый синтаксис. Вы также можете вручную ввести формулу.
#### **Формула площади**
Область формул содержит три раздела, в каждом из которых содержится информация, используемая для построения формулы.

- Поля отчета - в левом списке перечислены все поля базы данных, доступные для отчета. В нем также перечислены все уже созданные формулы или группы.
- Функции — средний список содержит функции, предварительно созданные процедуры, которые возвращают значения. Они выполняют такие вычисления, как AVERAGE, SUM, COUNT, SIN, UPPERCASE и так далее.
- Операторы — «глаголы действия», используемые в формулах. Операторы описывают операцию или действие, выполняемое между двумя или более значениями. Примеры операторов: сложить, вычесть, меньше и больше и т. д.
#### **Элементы управления**
Диалог имеет несколько элементов управления:

|**Название кнопки** |**Описание** |
|:- |:- |
| Отменить| Отменяет действие.|
| Вставить| Вставляет строку символов, состоящую из компонентов, перечисленных в области формулы, в область редактирования.|
| Вставлять| Принимает значение в области редактирования и вставляет его как формулу в ячейку.|
| Выход| Закрывает редактор формул.|
{{% alert color="primary" %}} 

Похожие темы:

- [Список формул](/cells/ru/reportingservices/formula-list/) - список полей и операторов.

{{% /alert %}}