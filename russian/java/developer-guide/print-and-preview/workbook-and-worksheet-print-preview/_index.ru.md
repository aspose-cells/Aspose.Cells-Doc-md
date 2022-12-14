---
title: Предварительный просмотр рабочей книги и рабочего листа
type: docs
weight: 130
url: /ru/java/workbook-and-worksheet-print-preview/
---
## **Сценарий использования**

Могут быть случаи, когда файлы Excel с миллионами страниц необходимо преобразовать в PDF или изображения. Обработка таких файлов потребует много времени и ресурсов. В таких случаях функция предварительного просмотра рабочей книги и рабочего листа может оказаться полезной. Перед преобразованием таких файлов пользователь может проверить общее количество страниц, а затем решить, следует ли преобразовать файл или нет. В этой статье основное внимание уделяется использованию[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)а также[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)классы, чтобы узнать общее количество страниц.

## **Предварительный просмотр рабочей книги и рабочего листа**

Aspose.Cells предоставляет функцию предварительного просмотра перед печатью. Для этого API предоставляет[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)а также[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)классы. Чтобы создать предварительный просмотр всей книги, создайте экземпляр[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)класс, пройдя[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)а также[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)объекты конструктору.[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)класс предоставляет[**Эвалуатедпажекаунт**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)метод, который возвращает количество страниц в сгенерированном предварительном просмотре. Похожий на[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)класс,[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)Класс используется для создания предварительного просмотра печати для определенного рабочего листа. Чтобы создать предварительный просмотр рабочего листа, создайте экземпляр[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)класс, пройдя[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)а также[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)объекты конструктору.[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)класс также предоставляет[**Эвалуатедпажекаунт**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)метод, который возвращает количество страниц в сгенерированном предварительном просмотре.

Следующий фрагмент кода демонстрирует использование обоих[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)а также[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)занятия с помощью[образец эксель файла](Book1.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Ниже приведен вывод, полученный при выполнении вышеуказанного кода.

### **Консольный вывод**

Количество страниц рабочей книги: 1</br>
Количество страниц рабочего листа: 1
