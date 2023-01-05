---
title: Aspose.Cells for Java 17.10 Примечания к выпуску
type: docs
weight: 30
url: /ru/java/aspose-cells-for-java-17-10-release-notes/
---
{{% alert color="primary" %}} 

 Эта страница содержит примечания к выпуску для[Aspose.Cells for Java 17.10](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.10/).

{{% /alert %}} 

|**Ключ**|**Резюме**|**Категория**|
|:- |:- |:- |
|CELLSJAVA-42423|Отменить длительное вычисление метода Workbook.calculateFormula|Новая особенность|
|CELLSJAVA-42414|Получить поле SheetId рабочего листа MS Excel|Новая особенность|
|CELLSJAVA-42402|Хороший HTML нужен для прикрепленного HTML|Улучшение|
|CELLSJAVA-42372|Положение длинных дефисов не совпадает с Microsoft Excel|Улучшение|
|CELLSJAVA-42399|Точки стрелок не четкие в выходном Pdf|Ошибка|
|CELLSJAVA-42419|Текст усекается в выводе HTML|Ошибка|
|CELLSJAVA-42418|Цвет границы не совпадает с цветом MS Excel в выводе HTML|Ошибка|
|CELLSJAVA-42417|Цвет фона не совпадает с цветом Ms Excel в выводе HTML.|Ошибка|
|CELLSJAVA-42385|обратный вызов IFilePathProvider никогда не вызывается, а затем файл HTML имеет «нулевой» путь|Ошибка|
|CELLSJAVA-42412|Метки оси значений отсутствуют при преобразовании Excel в PDF|Ошибка|
|CELLSJAVA-42408|Проблема перекрытия текста после рендеринга рабочего листа в изображение|Ошибка|
|CELLSJAVA-42420|Отмена и проблема с нехваткой памяти из-за большого диапазона данных диаграммы|Ошибка|
|CELLSJAVA-42415|Выходная диаграмма не похожа на исходную диаграмму на выходе HTML.|Ошибка|
|CELLSJAVA-42410|Область диаграммы, метки, легенды и т. д. отображаются неправильно в выходных данных PDF и PNG.|Ошибка|
|CELLSJAVA-42409|Область диаграммы отображается неправильно в выходных данных PDF и PNG диаграммы MS Excel.|Ошибка|
|CELLSJAVA-41046|Последовательность легенд диаграммы изменилась при отображении электронной таблицы в формате PDF.|Ошибка|
|CELLSJAVA-40416|Цвета и стиль диаграммы теряются|Ошибка|
## **Public API и обратно несовместимые изменения**
Ниже приведен список любых изменений, внесенных в общедоступный номер API, таких как добавленные, переименованные, удаленные или устаревшие члены, а также любые несовместимые с предыдущими изменениями, внесенные в номер Aspose.Cells for Java. Если у вас есть сомнения по поводу каких-либо перечисленных изменений, сообщите об этом на форум поддержки Aspose.Cells.
### **Добавляет метод AbstractCalculationMonitor.Interrupt(string)**
Позволяет пользователям прерывать ход вычисления формулы.
### **Добавляет перечисление HtmlCrossType.MSExport**
Отображает строку, аналогичную экспорту MS Excel HTML.
### **Добавляет свойство Worksheet.TabId**
Получает внутренний идентификатор листа.
### **Добавляет перечисление OLEDBCommandType.None**
Тип команды не указан.
### **Добавляет enum ConnectionDataSourceType**
Представляет тип подключения к источнику данных.
### **Устарело свойство ExternalConnection.Credentials и ExternalConnection.ReConnectionMethod.**
Вместо этого используйте свойства ExternalConnection.CredentialsMethodType и ExternalConnection.ReconnectionMethodType.
### **Устарело свойство WebQueryConnection.EditPage.**
Вместо этого используйте свойство WebQueryConnection.EditWebPage.
### **Добавляет свойство Series.ValuesFormatCode**
Представляет код числового формата значений ряда.


### **Примеры использования**
Пожалуйста, проверьте список разделов справки, добавленных в Aspose.Cells вики-документы:

- [Установите код формата значений серии диаграммы](/cells/ru/java/set-the-values-format-code-of-chart-series/)
- [Используйте свойство Sheet.SheetId OpenXml, используя Aspose.Cells](/cells/ru/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Чтение и запись внешнего соединения файла XLSB](/cells/ru/java/read-and-write-external-connection-of-xlsb-or-xls-file/)
- [Прервать или отменить расчет формулы рабочей книги](/cells/ru/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Укажите, как пересекать строку в выводе HTML с помощью HtmlCrossType.](/cells/ru/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
