---
title: Представления рабочего листа
type: docs
weight: 10
url: /ru/java/worksheet-views/
---
## **Предварительный просмотр разрыва страницы**
Все рабочие листы можно просматривать в двух режимах:

- Нормальный вид.
- Предварительный просмотр разрыва страницы.

Обычный вид — это вид рабочего листа по умолчанию. Предварительный просмотр разрыва страницы — это режим редактирования, в котором рабочий лист отображается в том виде, в котором он будет напечатан. Предварительный просмотр разрыва страницы показывает, какие данные будут размещены на каждой странице, поэтому вы можете настроить область печати и разрывы страниц. Используя Aspose.Cells, разработчики могут включить режимы обычного просмотра или предварительного просмотра с разрывом страницы.
### **Управление режимами просмотра**
 Aspose.Cells предоставляет[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)который позволяет получить доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы включить обычный режим или режим предварительного просмотра с разрывом страницы, используйте кнопку[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)метод.
#### **Включение обычного просмотра**
Установите любой рабочий лист в обычный вид с помощью[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) метод[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс и прохождение**ЛОЖЬ** как параметр.
#### **Включение предварительного просмотра разрыва страницы**
Установите любой рабочий лист для предварительного просмотра разрыва страницы, используя[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)метод[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс и прохождение**истинный**как параметр.

 Ниже приведен полный пример, демонстрирующий использование[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)метод, чтобы включить режим предварительного просмотра разрыва страницы для первого рабочего листа файла Excel.

На снимке экрана ниже видно, что файл Book1.xls находится в обычном режиме.

**Book1.xls: рабочий лист до изменения** 

![дело:изображение_альтернативный_текст](worksheet-views_1.png)

 Book1.xls открывается с помощью[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class и режим переключается на предварительный просмотр разрыва страницы для первого рабочего листа. Измененный файл сохраняется как output.xls.

**Outut.xls: рабочий лист после модификации** 

![дело:изображение_альтернативный_текст](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Коэффициент масштабирования**
Microsoft Excel предоставляет функцию, которая позволяет пользователям устанавливать масштаб рабочего листа или коэффициент масштабирования. Эта функция помогает пользователям просматривать содержимое рабочего листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.

**Установка коэффициента масштабирования с помощью Microsoft Excel** 

![дело:изображение_альтернативный_текст](worksheet-views_3.png)

Aspose.Cells также позволяет разработчикам устанавливать коэффициент масштабирования рабочего листа.
### **Управление коэффициентом масштабирования**
Aspose.Cells предоставляет[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)который позволяет получить доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы установить коэффициент масштабирования рабочего листа, используйте кнопку[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)метод.

 Ниже приведен полный пример, демонстрирующий, как использовать[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)метод для установки коэффициента масштабирования первого рабочего листа в файле Excel.

На снимке экрана ниже вы можете увидеть файл Book1.xls в представлении по умолчанию.

**Book1.xls: рабочий лист до изменения** 

![дело:изображение_альтернативный_текст](worksheet-views_4.png)

 Файл Book1.xls открывается с[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class, а коэффициент масштабирования первого рабочего листа установлен равным 75. Измененный файл сохраняется как output.xls.

**Output.xls: рабочий лист после модификации** 

![дело:изображение_альтернативный_текст](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Замерзшие оконные стекла**
Закрепить области — это функция, предоставляемая Microsoft Excel. Замораживание панелей позволяет выбрать данные, которые будут оставаться видимыми при прокрутке рабочего листа.

**Использование стоп-панелей в Microsoft Excel** 

![дело:изображение_альтернативный_текст](worksheet-views_6.png)

Aspose.Cells также позволяет разработчикам применять области закрепления к рабочим листам во время выполнения.

Aspose.Cells предоставляет[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)который позволяет получить доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы настроить стоп-панели, вызовите[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[замерзшие оконные стекла](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) метод.[замерзшие оконные стекла](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) принимает следующие параметры:

- **Строка**, индекс строки ячейки, с которой начнется замораживание.
- **Столбец**, индекс столбца ячейки, с которой начнется замораживание.
- **Замороженные строки**, количество видимых строк в верхней панели.
- **Замороженные столбцы**, количество видимых столбцов на левой панели

 Ниже приведен полный пример, который показывает, как использовать[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[замерзшие оконные стекла](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) метод заморозки строк и столбцов (начиная с C4, представленных 4-й строкой и 3-м столбцом, где строки и столбцы начинаются с 0 индексов) первого рабочего листа файла Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


На скриншоте ниже вы можете увидеть файл Book1.xls без областей закрепления.

**Book1.xls: вид рабочего листа до внесения каких-либо изменений** 

![дело:изображение_альтернативный_текст](worksheet-views_7.png)

 Файл Book1.xls открывается с[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class, а затем несколько строк и столбцов замораживаются на первом листе. Измененный файл сохраняется как output.xls.

**Outlook.xls: вид листа после изменения** 

![дело:изображение_альтернативный_текст](worksheet-views_8.png)
## **Разделить панели**
Если вам нужно разделить экран, чтобы получить два разных представления на одном листе, разделите панели. Microsoft Excel предлагает очень удобную функцию, позволяющую просматривать несколько копий рабочего листа и иметь возможность независимо прокручивать каждую панель рабочего листа: разделение панелей.

Панели работают одновременно. Если вы вносите изменения в один, это изменение одновременно появляется и в другом. Aspose.Cells предоставляет пользователям функцию разделения панелей.
### **Применение и удаление разделенных панелей**
#### **Разделение панелей**
Aspose.Cells предоставляет[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Класс предоставляет широкий набор свойств и методов для управления файлами Excel. Чтобы реализовать разделенные представления, используйте[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[расколоть](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) метод. Чтобы удалить разделенные панели, используйте[удалитьСплит](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) метод.

В этом примере мы используем простой файл шаблона, который загружается, а затем к ячейке на первом рабочем листе применяется функция установки разделенных панелей. Обновленный файл сохраняется.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



После запуска приведенного выше кода сгенерированный файл имеет разделенное представление.

**Разделение панелей в выходном файле** 

![дело:изображение_альтернативный_текст](worksheet-views_9.png)
#### **Удаление панелей**
 Разработчики могут удалять разделенные панели с помощью[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[удалитьСплит](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Предварительные темы**
- [Скрытие отображения нулевых значений на рабочем листе](/cells/ru/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Установить цвет вкладки рабочего листа](/cells/ru/java/set-worksheet-tab-color/)
- [Показать и скрыть элементы](/cells/ru/java/show-and-hide-elements/)
- [Показывать формулы вместо значений на листе](/cells/ru/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Используйте параметры проверки ошибок](/cells/ru/java/use-error-checking-options/)
