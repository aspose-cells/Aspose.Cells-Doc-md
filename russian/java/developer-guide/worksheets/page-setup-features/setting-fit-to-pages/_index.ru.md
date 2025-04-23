---
title: Как напечатать Excel так, чтобы страницы были шириной и высотой, подогнанными под страницу
type: docs
weight: 200
url: /ru/java/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Эта статья показывает код, объясняющий, как устанавливать FitToPagesWide и FitToPagesTall с помощью библиотеки Aspose.Cells.
keywords: Java Как установить FitToPagesWide и FitToPagesTall, как добавить FitToPagesWide и FitToPagesTall в Java, как установить FitToPagesWide и FitToPagesTall в Excel, как очистить установку FitToPagesWide и FitToPagesTall в Excel, как напечатать Excel так, чтобы страницы были шириной и высотой, как напечатать лист как одну страницу, как напечатать все столбцы листа на одной странице.
---

## **Введение**

Настройки FitToPagesWide и FitToPagesTall используются в приложениях для работы с таблицами (таких как Microsoft Excel), чтобы контролировать масштабирование при печати. Эти настройки помогают обеспечить, чтобы напечатанный результат поместился на указанное количество страниц, как по горизонтали, так и по вертикали. Вот разъяснение каждого из параметров:

1. FitToPagesWide: Эта настройка задает количество страниц по ширине, в которые должна поместиться распечатка. Например, установка значения в 1 означает, что содержимое масштабируется для размещения на одной странице по ширине, независимо от ширины таблицы.
1. FitToPagesTall: Эта настройка задает количество страниц по высоте, в которые должна поместиться распечатка. Например, установка значения в 1 означает, что содержимое масштабируется для размещения на одной странице по высоте, независимо от количества строк.

## **Зачем использовать FitToPagesWide и FitToPagesTall**
Вот некоторые причины установки FitToPagesWide и FitToPagesTall:
1. Контроль над размещением при печати: задавая количество страниц по ширине и высоте, вы можете убедиться, что ваш печатный документ легко читаем и хорошо отформатирован, без нежелательного переноса столбцов или строк между страницами.
1. Последовательность: если вы печатаете несколько листов или отчетов, использование этих настроек помогает сохранить одинаковый формат, что облегчает сравнение и анализ распечатанных документов.
1. Профессиональная презентация: правильное масштабирование и размещение содержимого на заданное число страниц создаст более профессиональный и аккуратный вид ваших данных.

## **Как распечатать файл по страницам по ширине и высоте в Excel**

Чтобы установить параметры FitToPagesWide и FitToPagesTall в Microsoft Excel, выполните следующие шаги:

1. Откройте рабочую книгу Excel и перейдите к листу, который хотите распечатать.
1. Перейдите на вкладку Макет страницы на ленте.
1. В группе Настройка страницы нажмите на маленькую стрелку в правом нижнем углу, чтобы открыть диалоговое окно Настройка страницы.
1. В диалоговом окне Настройка страницы перейдите на вкладку Страница.
1. В разделе Масштабирование выберите опцию "Подогнать" и укажите количество страниц по ширине и высоте, которые вы хотите: введите желаемое количество страниц по ширине в первый блок (Подогнать x страниц по ширине). Введите желаемое количество страниц по высоте во второй блок (Подогнать y страниц по высоте).
<br>
<img src="2.png" width=60% />

1. Нажмите OK, чтобы применить настройки.


## **Как распечатать Excel как страницы по ширине и высоте, используя Aspose.Cells**

Чтобы установить FitToPagesWide и FitToPagesTall в конкретном листе: сначала загрузите [пробный файл](input.xlsx), затем вызовете методы [**Worksheet.PageSetup.setFitToPagesTall(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesTall-int-) и [**Worksheet.PageSetup.setFitToPagesWide(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesWide-int-) для объекта [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/) нужного листа. Вот пример на Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.java" >}}

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как напечатать лист как одну страницу, используя Aspose.Cells**

Чтобы распечатать лист как одну страницу: сначала загрузите [пробный файл](sample.xlsx), затем вызовите метод [**PdfSaveOptions.setOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setOnePagePerSheet-boolean-) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/). Вот пример на Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-OnePagePerSheet.java" >}}

Результат вывода:
<br>
<img src="3.png" width=60% />


## **Как распечатать все столбцы листа на одной странице, используя Aspose.Cells**

Чтобы распечатать все столбцы листа на одной странице: сначала загрузите [пробный файл](sample.xlsx), затем вызовите метод [**PdfSaveOptions.setAllColumnsInOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setAllColumnsInOnePagePerSheet-boolean-) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/). Вот пример на Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.java" >}}

Результат вывода:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="java" >}}
