﻿---
title: Использование спарклайнов и настроек 3D-формата
type: docs
weight: 40
url: /ru/net/using-sparklines-and-settings-3d-format/
---
## **Использование спарклайнов**
Microsoft Excel 2010 может анализировать информацию самыми разными способами. Это позволяет пользователям отслеживать и выделять важные тенденции данных с помощью новых инструментов анализа и визуализации данных. Спарклайны — это мини-диаграммы, которые вы можете разместить внутри ячеек, чтобы вы могли просматривать данные и диаграмму в одной таблице. При правильном использовании спарклайнов анализ данных выполняется быстрее и точнее. Они также обеспечивают простое представление информации, избегая переполненных рабочих листов с большим количеством занятых диаграмм.

Aspose.Cells предоставляет API для управления спарклайнами в электронных таблицах.
### **Спарклайны в Microsoft Excel**
Чтобы вставить спарклайны в Microsoft Excel 2010:

1. Выберите ячейки, в которых вы хотите, чтобы отображались спарклайны. Чтобы их было легко просматривать, выберите ячейки рядом с данными.
1.  Нажмите**Вставлять** на ленте, а затем выберите**столбец** в**Спарклайны** группа.
1. Выберите или введите диапазон ячеек на листе, содержащих исходные данные. Графики появятся.

Спарклайны помогают увидеть тенденции, например, количество побед или поражений в лиге софтбола. Спарклайны могут даже подводить итоги всего сезона каждой команды в лиге.
### **Спарклайны с использованием Aspose.Cells**
 Разработчики могут создавать, удалять или читать спарклайны (в файле шаблона), используя API, предоставленный Aspose.Cells. Классы, управляющие спарклайнами, содержатся в[Aspose.Cells.Charts](https://reference.aspose.com/cells/net/aspose.cells.charts)пространство имен, поэтому вам необходимо импортировать это пространство имен перед использованием этих функций.

Добавляя пользовательскую графику для заданного диапазона данных, разработчики могут свободно добавлять различные типы крошечных диаграмм в выбранные области ячеек.

Пример ниже демонстрирует функцию Sparklines. В примере показано, как:

1. Откройте простой файл шаблона.
1. Чтение информации о спарклайнах для рабочего листа.
1. Добавьте новые спарклайны для заданного диапазона данных в область ячеек.
1. Сохраните файл Excel на диск.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-UsingSparklines-1.cs" >}}
## **Настройка формата 3D**
Вам могут понадобиться стили трехмерных диаграмм, чтобы вы могли получить результаты только для своего сценария. Aspose.Cells предоставляет соответствующий API для применения форматирования Microsoft Excel 2007 3D.

Полный пример приведен ниже, чтобы продемонстрировать, как создать диаграмму и применить Microsoft Excel 2007 3D-форматирование. После выполнения примера кода на рабочий лист будет добавлена столбчатая диаграмма (с 3D-эффектами).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-Applying3DFormat-1.cs" >}}