---
title: Почему не использовать Open XML SDK
type: docs
weight: 20
url: /ru/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

Иногда мы слышим этот вопрос:

**Почему мы должны использовать продукты Aspose вместо бесплатного Open XML SDK?**

На этот вопрос легко ответить: **функции и возможности**.

{{% /alert %}} 
## **Что такое Open XML SDK?**
Согласно библиотеке MSDN, Open XML SDK определяется следующим образом: Open XML SDK 2.0 упрощает задачу манипулирования пакетами Open XML и основными элементами схемы Open XML внутри пакета. Open XML SDK 2.0 инкапсулирует многие общие задачи, которые разработчики выполняют с пакетами Open XML, чтобы вы могли выполнять сложные операции всего лишь несколькими строками кода. Документы Open XML по сути своей являются сжатыми XML-файлами, и Open XML SDK представляет собой набор классов, позволяющих вам работать с содержимым документов Open XML в строго типизированном виде. То есть вместо извлечения XML-файла из архива, загрузки этого XML в объектное дерево DOM и работы с XML-элементами и атрибутами непосредственно, Open XML SDK предоставляет классы для выполнения этих действий.
## **Что такое Aspose.Cells?**
Aspose.Cells - это библиотека классов, которая позволяет вашему приложению выполнять следующие задачи по обработке электронных таблиц: Качественные преобразования между всеми популярными форматами Excel, включая преобразование в PDF, HTML, TIFF и печать. Программирование с моделью объектов книги. Возможность создавать документы из фрагментов, из одного или нескольких документов, автоматически объединяя данные по стилевому форматированию, диаграммам и графике. Высокоуровневые функции, такие как импорт данных из различных источников данных, включая массив, ArrayList, DataTable / ResultSet. Надежный движок расчета формул, который поддерживает практически все стандартные и расширенные функции Microsoft Excel.


## **Сравнение Open XML SDK и Aspose.Cells**
Следующая таблица сравнивает функции Open XML SDK и Aspose.Cells. 

|**Функция или Категория функций**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Поддерживаемые форматы Excel и другие|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, разделенные табуляцией, ODS, обычный текст (TXT), PDF, XPS|
|Конвертируйте между форматами Excel|Нет|Да|
|<p>Программирование на высоком уровне с объектной моделью книги:</p><p>- Поиск и замена.</p><p>- Составление электронных таблиц.</p><p>- Копирование фрагментов и листов между книгами.</p>|Нет|Да|
|Детальное программирование с объектной моделью документа, доступ к отдельным элементам и свойствам форматирования всех элементов электронных таблиц.|Да|Да|
|Низкоуровневый прямой и полный доступ к базовым элементам и атрибутам XML, таким как идентификаторы отношений, идентификаторы списка документа OOXML.|Да|Нет|
|<p>Генерация отчетов, заполнение документов данными:</p><p>- Импорт/Экспорт данных в/из *DataTable /* ResultSet.</p><p>- Возможность интеллектуальных маркеров.</p><p>- Вставка/Удаление строк/столбцов/диапазонов.</p><p>- Пользовательские источники данных.</p>| Нет | Да |
|<p>Представление и печать:* Отображать страницы листов книги в растровые изображения (TIFF, многостраничный TIFF, PNG, JPEG, BMP).* Отображать страницы электронных таблиц в векторные изображения (EMF).* Преобразовывать диаграммы в изображения (TIFF, многостраничный TIFF, PNG, JPEG, BMP, EMF и т. д.)</p><p>- Указывать разрешение изображения, качество, сжатие и другие параметры.</p><p>- Печать электронных таблиц с использованием инфраструктуры печати .NET. Компонент содержит встроенный метод печати для отображения листов, как это показано в предварительном просмотре печати MS Excel.</p>| Нет | Да |
|Расчет/Перерасчет формул динамически| Нет | Да |
|Поддерживаемые платформы|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Заключение**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}
