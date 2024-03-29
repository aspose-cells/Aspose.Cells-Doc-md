﻿---
title: Как Aspose.Cells использует шрифты TrueType
type: docs
weight: 10
url: /ru/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells требует шрифты TrueType при отображении электронных таблиц в такие форматы, как PDF, XPS и изображения.

Когда Aspose.Cells отображает электронную таблицу, ему требуется доступ к шрифтам TrueType, используемым в электронной таблице. Это обычная практика во время PDF, XPS и создания изображений, которая гарантирует, что преобразованный документ или изображение будут выглядеть одинаково для любого зрителя.

{{% /alert %}}

## **О шрифтах**

### **Наличие и замена шрифтов**

Электронная таблица может быть отформатирована с использованием различных шрифтов, таких как Arial, Times New Roman, Verdana и других. Когда Aspose.Cells отображает электронную таблицу, он пытается выбрать шрифты, используемые в электронной таблице. Однако бывают ситуации, когда точный шрифт может быть недоступен, поэтому вместо него Aspose.Cells необходимо заменить похожий шрифт.

Ниже показан процесс, который Aspose.Cells следует за сценой.

1. Aspose.Cells пытается найти шрифты в файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1. Если Aspose.Cells не может найти шрифты с точно такими же именами, он пытается использовать шрифт по умолчанию, указанный в свойстве DefaultStyle.Font рабочей книги.
1. Если Aspose.Cells не может найти шрифт, определенный в свойстве DefaultStyle.Font книги, он пытается выбрать наиболее подходящий шрифт из всех доступных шрифтов.
1. Наконец, если Aspose.Cells не может найти шрифты в файловой системе, он отображает электронную таблицу с использованием Arial.

### **Где Aspose.Cells ищет шрифты**

Aspose.Cells пытается автоматически найти шрифты TrueType в файловой системе. В большинстве случаев вы можете полагаться на поведение по умолчанию Aspose.Cell для поиска шрифтов TrueType, но иногда вам может потребоваться указать папки, содержащие шрифты TrueType, с помощью фабричного метода FontConfigs.setFontFolder.

### **Типичные проблемы, связанные со шрифтами, и их решения**

В этой таблице перечислены некоторые проблемы, с которыми вы можете столкнуться при рендеринге электронных таблиц в PDF с использованием Aspose.Cells, и их решения.

{{% alert color="primary" %}}

 При копировании любых шрифтов помните, что большинство шрифтов защищены авторским правом. Сначала найдите лицензию шрифта заранее и убедитесь, что ее можно свободно перенести на другую машину.

{{% /alert %}}

|**Проблема** |**Причина** |**Решение** |
|:- |:- |:- |
| Макет и шрифты в обработанном документе отличаются от оригинала.| Вы используете Aspose.Cells в Linux или Mac OS, где шрифты TureType отсутствуют по умолчанию, поэтому Aspose.Cells не может найти шрифты на вашем компьютере.|Скопируйте файлы шрифтов TrueType с компьютера Windows или установите пакет шрифтов TrueType. Используйте фабричный метод FontConfigs.setFontFolder, чтобы указать расположение файлов шрифтов.|

{{% alert color="primary" %}}

Ознакомьтесь с подробными статьями о

- [Как разместить шрифты TrueType в Linux](/cells/ru/java/how-to-install-truetype-fonts-on-linux/).
- [Как указать расположение шрифтов TrueType](/cells/ru/java/how-to-specify-truetype-fonts-location/).
- [Как получить предупреждения при подмене шрифта](/cells/ru/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
