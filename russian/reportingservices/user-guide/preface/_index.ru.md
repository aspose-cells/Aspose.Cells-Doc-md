﻿---
title: Предисловие
type: docs
weight: 20
url: /ru/reportingservices/preface/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services в основном содержит два компонента: Aspose.Cells.Report.Designer и Aspose.Cells.Renderer for Reporting Services. Первый используется для разработки отчетов непосредственно в Microsoft Excel, а второй отвечает за визуализацию RDL-отчета в Microsoft Excel.

{{% /alert %}} 
### **Создание отчета с помощью дизайнера отчетов**
Основные этапы разработки отчета с помощью Aspose.Cells.Report.Designer:

1. **Создание источников данных и запросов**.
 Microsoft Query интегрирован с Aspose.Cells.Report.Designer и используется как графический инструмент для создания источников данных и запросов. Пользователи также могут использовать существующий файл RDL, в котором источники данных и запросы доступны для операций.
1. **Параметры карты**.
 Если операторы SQL запроса включают параметры, пользователи должны создать параметры отчета и сопоставить параметры SQL с параметрами отчета. Вы можете назначить допустимые значения для параметра отчета в Aspose.Cells.Report.Designer.
1. **Дизайн Microsoft Содержимое, стили и форматы шаблона отчета Excel**.
Шаблон отчета Aspose.Cells может содержать любое количество следующих типов элементов отчета:
 1. Таблица
 1. Сводная таблица
 1. Диаграмма
 1. Текстовое поле
 1. Матрица
 Обычно запрос (то есть набор данных) используется в качестве источника данных для элемента отчета. Вы также можете использовать параметры, формулы и глобальные переменные служб Reporting Services в качестве источника данных для некоторых типов элементов отчета. Стили и форматы элементов отчета задаются простым заданием стилей и форматов ячеек, составляющих элементы отчета.
1. **Опубликовать отчет**.
 После вышеуказанных шагов отчет готов к публикации. Пользователи могут указать, в какой папке будет опубликован отчет. При необходимости вы можете назначить общий источник данных на сервере отчетов в качестве источника данных для отчета.
1. **Предварительный отчет**.
При выборе отчета для предварительного просмотра на сервере отчетов вам будет предложено указать формат файла для его экспорта (например, Microsoft Excel 97-2003 двоичный формат XLS, формат SpreadsheetML или Microsoft Excel 2007 XLSX), а также любые созданные входные параметры отчета. во время оформления отчета. После этого отчет заполняется данными, предоставленными Reporting Services.