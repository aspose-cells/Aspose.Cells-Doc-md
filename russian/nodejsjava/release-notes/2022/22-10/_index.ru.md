﻿---
title: Aspose.Cells for Node.js via Java 22.10 Примечания к выпуску
type: docs
weight: 3
url: /ru/nodejs-java/aspose-cells-for-node-js-via-java-22-10-release-notes/
---
{{% alert color="primary" %}}

 Эта страница содержит примечания к выпуску для[Aspose.Cells for Node.js via Java 22.10](https://releases.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.10/).

{{% /alert %}}

|**Ключ**|**Резюме**|**Категория**|
|:- |:- |:- |
|CELLSJAVA-44890|поддержка файла импорта с открытым паролем для GridWeb|
|CELLSJAVA-44884| Номера списка неверны после преобразования XLSX в HTML или PDF|
|CELLSJAVA-44883| Рабочая книга, содержащая сводную таблицу, повреждается после обработки в ней сводной таблицы|
|CELLSJAVA-44879|Отформатированный результат для GridWeb отличался от Cell.DisplayStringValue.|
|CELLSJAVA-44327|Границы и меньшее количество линий, показанные в черно-белых сегментах круговой диаграммы на рендеринге изображения|
|CELLSJAVA-44853|Данные об угле оси x не совпадают с данными Excel в диаграмме для рендеринга изображения.|
|CELLSJAVA-44854|Данные на шаге по оси Y не совпадают с данными Excel в диаграмме для рендеринга изображения.|
|CELLSJAVA-44904|Проблемы при преобразовании диаграмм Excel в JPG|
|CELLSJAVA-44850|При импорте файла XLT текст не отображается полностью при использовании последних демонстраций с последней версией Aspose.Cells.GridWeb с последними файлами ресурсов.|
|CELLSJAVA-44857|При использовании версии Aspose.Cells.GridWeb for Java v22.8 с последними файлами ресурсов для открытия документа Excel эффект ячеек отличается от исходного документа.|
|CELLSJAVA-44903|SVG воспроизведение не работает должным образом|
|CELLSJAVA-44909| Когда несколько строк выделены жирным шрифтом, кажется, что они излишне перетекают в другие строки.|
|CELLSJAVA-44898|Чтение из GZIPInputStream иногда выдает фиктивную ошибку «Файл поврежден» в 22.7 и более поздних версиях.|
|CELLSJAVA-44881|Исключение «java.lang.ArrayIndexOutOfBoundsException: 15070» при загрузке файла XLS|

## **Public API и обратно несовместимые изменения**

Ниже приведен список любых изменений, внесенных в общедоступный номер API, таких как добавленные, переименованные, удаленные или устаревшие члены, а также любые несовместимые с предыдущими изменениями, внесенные в номер Aspose.Cells for Java. Если у вас есть сомнения по поводу каких-либо перечисленных изменений, сообщите об этом на форум поддержки Aspose.Cells.

### **Изменен лимит перемещения ячеек за пределы листа для вставки строк**

В старых версиях, если есть ячейки с настройками форматирования, но не имеющие значения и которые будут перемещены за пределы листа, операция вставки не допускается. С 22.10 операция вставки разрешена для такой ситуации, и теперь такое поведение такое же, как и в ms excel.

### **Добавляет класс DataModelConnection**

Указывает подключение к модели данных.

### **Добавляет методы Chart.ChangeTemplate(byte[])**

Измените тип диаграммы с помощью предустановленного файла шаблона.

### **Добавляет метод ChartCollection.Add(byte[] data, string dataRange, bool isVertical, int topRow, int leftColumn, int rightRow, int bottomColumn).**

Добавляет график с предустановленным файлом шаблона.