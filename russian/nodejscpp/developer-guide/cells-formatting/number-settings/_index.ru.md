---  
title: Настройки чисел
linktitle: Настройки чисел  
description: Aspose.Cells — это библиотека Node.js для работы с файлами электронных таблиц, которая поддерживает различные настройки нумерации ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для управления настройками чисел в ячейках и корректировки форматов чисел в таблицах.  
keywords: Aspose.Cells, библиотека Node.js, электронные таблицы, настройки номеров ячеек, форматирование, управление, Форматы чисел и дат  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/cells-number-settings/  
---  

## **Как установить отображаемые форматы чисел и дат**  

Одной из сильных сторон Microsoft Excel является возможность задавать форматы отображения числовых значений и дат. Мы знаем, что числовые данные могут использоваться для представления различных значений, включая десятичные, валютные, процентные, дробные или бухгалтерские значения и т. д. Все эти числовые значения отображаются в различных форматах в зависимости от типа информации, которую они представляют. Аналогично, существует множество форматов отображения даты или времени.  
Aspose.Cells поддерживает эту функциональность и позволяет разработчикам устанавливать отображаемый формат для числа или даты.  

### **Как установить отображаемые форматы в Microsoft Excel**  

Чтобы установить отображаемые форматы в Microsoft Excel:  

1. Щелкните правой кнопкой мыши любую ячейку.  
2. Выберите **Формат ячеек**. Появится диалоговое окно, в котором можно установить форматы отображения для любого значения.  

Слева в диалоговом окне есть множество категорий значений, таких как **Общий**, **Число**, **Валюта**, **Бухгалтерия**, **Дата**, **Время**, **Процент** и др. Aspose.Cells поддерживает все эти форматы отображения.  

Aspose.Cells предоставляет модуль, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Excel. Модуль [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен модулем [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Модуль [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) представляет объект модуля [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells предоставляет методы [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) и [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) для модуля [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Эти методы используются для получения и установки форматирования ячейки. Модуль [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) предоставляет полезные свойства для работы с форматами отображения чисел и дат.  

### **Как использовать встроенные форматы чисел**  

Aspose.Cells предлагает некоторые встроенные форматы чисел для настройки отображения чисел и дат. Эти встроенные форматы могут применяться с помощью метода [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Все встроенные форматы имеют уникальные числовые значения. Разработчики могут присваивать любое желаемое числовое значение методу [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) для применения формата отображения. Этот подход быстрый. Ниже приведен список поддерживаемых встроенных форматов чисел Aspose.Cells.  

|**Значение**|**Тип**|**Строка формата**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|т:мм:сс|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **Как использовать пользовательские форматы чисел**  

Чтобы определить собственный формат строки для настройки формата отображения, используйте метод [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Этот подход менее быстр, чем использование предустановленных форматов, но более гибкий.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

Если вы используете метод [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) для установки числового формата, любой предыдущий формат, установленный с помощью метода [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-), будет переопределен. И наоборот.  

{{% /alert %}}  

## **Продвинутые темы**  
- [Проверьте Пользовательский числовой формат при установке Свойства Custom.](/cells/ru/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Список поддерживаемых форматов чисел](/cells/ru/nodejs-cpp/list-of-supported-number-formats/)  
- [Отображение пользовательского формата даты Шаблон g и ge mm dd](/cells/ru/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Укажите пользовательские разделители десятичных и групповых чисел для рабочей книги](/cells/ru/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Указание форматирования собственного шаблона DBNum](/cells/ru/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
