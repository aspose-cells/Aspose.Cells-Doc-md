---
title: Условное форматирование
type: docs
weight: 120
url: /ru/java/conditional-formatting/
---

{{% alert color="primary" %}} 

Условное форматирование - это продвинутая функция Microsoft Excel, которая позволяет применять форматы к ячейке или диапазону ячеек и изменять этот формат в зависимости от значения ячейки или значения формулы. Например, вы можете сделать ячейку жирной только тогда, когда значение ячейки больше 500. Когда значение ячейки соответствует условию, к ячейке применяется указанный формат. Если значение ячейки не соответствует условию, используется формат по умолчанию. В Microsoft Excel выберите **Формат**, затем **Условное форматирование**, чтобы открыть диалоговое окно условного форматирования.

**Условное форматирование в Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells поддерживает применение условного форматирования к ячейкам во время выполнения. В этой статье объясняется, как это сделать.

{{% /alert %}} 
## **Применение условного форматирования**
Aspose.Cells поддерживает условное форматирование двумя способами:

- [Использование дизайнерской электронной таблицы](/cells/ru/java/conditional-formatting/)
- [Создание условного форматирования во время выполнения](/cells/ru/java/conditional-formatting/)
### **Использование дизайнерской таблицы**
Разработчики могут создать дизайнерскую электронную таблицу, которая содержит условное форматирование в Microsoft Excel, а затем открыть эту электронную таблицу с помощью Aspose.Cells. Aspose.Cells загружает и сохраняет дизайнерскую электронную таблицу, сохраняя любые настройки условного форматирования. Чтобы узнать больше о дизайнерских электронных таблицах, прочтите [Что такое дизайнерская электронная таблица](/cells/ru/java/what-is-a-designer-spreadsheet/).
## **Применение условного форматирования во время выполнения**
Aspose.Cells поддерживает применение условного форматирования во время выполнения.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **Установить шрифт**
**Настройка шрифтов в Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **Установить границу**
**Установка границ в Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **Установить узор**
**Установка шаблона ячейки в Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **Продвинутые темы**
- [Добавление набора условных значков с текстом ячейки](/cells/ru/java/add-conditional-icons-set-with-the-cell-text/)
- [Добавление условных форматирований 2-цветной шкалы и 3-цветной шкалы](/cells/ru/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Применение условного форматирования в рабочих листах](/cells/ru/java/apply-conditional-formatting-in-worksheets/)
- [Применение заливки для чередующихся строк и столбцов с условным форматированием](/cells/ru/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

