﻿---
title: Создание динамических диаграмм
type: docs
weight: 200
url: /ru/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

Динамические (или интерактивные) диаграммы могут изменяться при изменении объема данных. Другими словами, динамические диаграммы могут автоматически отражать изменения при смене источника данных. Чтобы вызвать изменение в источнике данных, можно использовать параметр фильтрации таблиц Excel или использовать элемент управления, такой как ComboBox или раскрывающийся список.

В этой статье демонстрируется использование API Aspose.Cells for Java для создания динамических диаграмм с использованием обоих вышеупомянутых подходов.

{{% /alert %}}

## **Использование таблиц Excel**

{{% alert color="primary" %}}

 Таблицы Excel называются ListObjects в перспективе Aspose.Cells, поэтому для ясности мы будем использовать термин «ListObject» вместо «Table». Пожалуйста, прочитайте подробно о том, как[создать ListObjects](/cells/ru/java/creating-a-list-object/) с Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects предоставляет встроенную функциональность для сортировки и фильтрации данных при взаимодействии с пользователем. Как сортировка, так и фильтрация доступны через раскрывающиеся списки, которые автоматически добавляются в строку заголовка объекта ListObject. Благодаря этим функциям (сортировка и фильтрация) объект ListObject кажется идеальным кандидатом на роль источника данных для динамической диаграммы, поскольку при изменении сортировки или фильтрации представление данных на диаграмме будет изменено, чтобы отражать текущую диаграмму. состояние ListObject.

Чтобы сделать демонстрацию простой для понимания, мы создадим рабочую тетрадь с нуля и будем продвигаться вперед шаг за шагом, как описано ниже.

1. Создайте пустую рабочую книгу.
1. Получите доступ к Cells первого рабочего листа в рабочей книге.
1. Вставьте некоторые данные в ячейки.
1. Создайте ListObject на основе вставленных данных.
1. Создайте диаграмму на основе диапазона данных ListObject.
1. Сохранить результат на диск.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Использование динамических формул**

Если вы не хотите использовать ListObjects в качестве источника данных для динамической диаграммы, другим вариантом является использование функций Excel (или формул) для создания динамического диапазона данных и элемента управления (например, ComboBox) для запуска изменения в данных. В этом сценарии мы будем использовать функцию VLOOKUP для получения соответствующих значений на основе выбора ComboBox. При изменении выбора функция ВПР обновит значение ячейки. Если диапазон ячеек использует функцию ВПР, весь диапазон может быть обновлен при взаимодействии с пользователем, поэтому его можно использовать в качестве источника для динамической диаграммы.

Чтобы сделать демонстрацию простой для понимания, мы создадим рабочую тетрадь с нуля и будем продвигаться вперед шаг за шагом, как описано ниже.

1. Создайте пустую рабочую книгу.
1. Получите доступ к Cells первого рабочего листа в рабочей книге.
1. Вставьте некоторые данные в ячейки, создав именованный диапазон. Эти данные будут служить сериями для динамической диаграммы.
1. Создайте ComboBox на основе именованного диапазона, созданного на предыдущем шаге.
1. Вставьте дополнительные данные в ячейки, которые будут служить источником для функции ВПР.
1. Вставьте функцию ВПР (с соответствующими параметрами) в диапазон ячеек. Этот диапазон будет служить источником для динамического графика.
1. Создайте диаграмму на основе диапазона, созданного на предыдущем шаге.
1. Сохранить результат на диск.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}