---
title: Представления листа
type: docs
weight: 10
url: /ru/java/worksheet-views/
---

## **Предпросмотр разрывов страниц**
Все листы могут быть просмотрены в двух режимах:

- Обычный вид.
- Предварительный просмотр разрыва страницы.

Обычный вид - это вид листа по умолчанию. Предварительный просмотр разрыва страницы - это вид редактирования, который отображает лист так, как он будет напечатан. Предварительный просмотр разрыва позволяет увидеть, какие данные будут на каждой странице, чтобы можно было настроить область печати и разрывы страниц. С помощью Aspose.Cells разработчики могут включить обычный вид или режим предварительного просмотра разрыва страницы.
### **Управление режимами просмотра**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), который позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Чтобы включить нормальный или режим предварительного просмотра, используйте метод [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).
#### **Включение нормального режима**
Установите любой лист в нормальный режим, используя метод [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet), передав **false** в качестве параметра.
#### **Включение предварительного просмотра разрывов страниц**
Установите любой лист в режим предварительного просмотра разрывов страниц с помощью метода [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet), передав **true** в качестве параметра.

Ниже приведен полный пример, демонстрирующий использование метода [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) для включения режима предварительного просмотра разрывов страниц для первого листа в файле Excel.

На скриншоте ниже вы можете увидеть, что файл Book1.xls находится в нормальном режиме.

**Book1.xls: Лист до изменения** 

![todo:image_alt_text](worksheet-views_1.png)

Файл Book1.xls открыт с использованием класса [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), и режим переключен на предварительный просмотр разрывов страниц для первого листа. Измененный файл сохранен как output.xls.

**Ouput.xls: лист после изменения** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Коэффициент масштабирования**
Microsoft Excel предоставляет возможность установить коэффициент масштабирования листа. Эта функция помогает пользователям просматривать содержимое листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.

**Установка коэффициента масштабирования с помощью Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells также позволяет разработчикам устанавливать коэффициент масштабирования листа.
### **Управление коэффициентом масштабирования**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), который позволяет получить доступ к каждому листу в файле Excel.

Лист представляется классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Чтобы установить масштаб листа, используйте метод [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Ниже приведен полный пример, демонстрирующий, как использовать метод [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom), чтобы установить масштаб первого листа в файле Excel.

На скриншоте ниже вы можете увидеть файл Book1.xls в режиме по умолчанию.

**Book1.xls: лист перед внесением изменений** 

![todo:image_alt_text](worksheet-views_4.png)

Файл Book1.xls открывается с помощью класса [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) и масштаб первого листа устанавливается на 75. Измененный файл сохраняется как output.xls.

**output.xls: лист после внесения изменений** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Закрепить области**
Закрепление области экрана - это функция, предоставляемая Microsoft Excel. Закрепление области экрана позволяет выбрать данные, которые останутся видимыми при прокрутке на листе.

**Использование закрепления области экрана в Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells также позволяет разработчикам применять закрепление области экрана к листам во время выполнения.

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), что позволяет получить доступ к каждому листу в файле Excel.

Лист представляется классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Чтобы настроить закрепление панелей, вызовите метод [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-). Метод [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) принимает следующие параметры:

- **Строка**, индекс строки, с которой начнется закрепление.
- **Столбец**, индекс столбца, с которого начнется закрепление.
- **Закрепленные строки**, количество видимых строк в верхней панели.
- **Закрепленные столбцы**, количество видимых столбцов в левой панели.

Ниже приведен полный пример, показывающий, как использовать метод [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet), чтобы закрепить строки и столбцы (начиная с C4, что соответствует 4-й строке и 3-му столбцу, где нумерация строк и столбцов начинается с 0) первого листа Excel файла.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


На скриншоте ниже вы можете увидеть файл Book1.xls без закрепления области экрана.

**Book1.xls: представление листа до внесения изменений** 

![todo:image_alt_text](worksheet-views_7.png)

Файл Book1.xls открывается с помощью класса [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), а затем на первом листе закрепляются несколько строк и столбцов. Измененный файл сохраняется как output.xls.

**Outlook.xls: представление листа после внесения изменений** 

![todo:image_alt_text](worksheet-views_8.png)
## **Разделение областей экрана**
Если вам нужно разделить экран для получения двух разных представлений на одном листе, используйте разделение областей экрана. Microsoft Excel предлагает очень удобную функцию, которая позволяет просматривать более одной копии вашего листа и прокручивать каждую область листа независимо: разделение областей экрана.

Разделы работают одновременно. Если вы внесете изменение в один, изменение одновременно появится в другом. Aspose.Cells предоставляет функцию разделения панелей для пользователей.
### **Применение и удаление разделенных панелей**
#### **Разделение панелей**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) предоставляет широкий спектр свойств и методов для работы с файлами Excel. Для реализации раздельных областей используйте метод [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split--) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Чтобы удалить разделение панелей, используйте метод [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--)

В примере мы используем простой шаблонный файл, который загружается, затем устанавливается функция разделенных панелей для ячейки на первом листе. Обновленный файл сохраняется.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



После выполнения вышеуказанного кода, у сгенерированного файла появляется разделенный вид.

**Разделенные панели в выходном файле** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Удаление панелей**
Разработчики могут удалять разделения панелей с помощью метода [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Продвинутые темы**
- [Скрытие отображения нулевых значений в таблице](/cells/ru/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Установить цвет вкладки листа](/cells/ru/java/set-worksheet-tab-color/)
- [Показ и скрытие элементов](/cells/ru/java/show-and-hide-elements/)
- [Показывать формулы вместо значений в таблице](/cells/ru/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Использовать параметры проверки ошибок](/cells/ru/java/use-error-checking-options/)
{{< app/cells/assistant language="java" >}}
