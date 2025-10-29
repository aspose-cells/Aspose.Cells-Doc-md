---
title: Умное импортирование вложенных объектов в Excel с помощью умных маркеров
type: docs
weight: 30
url: /ru/net/how-to-import-nested-objects-with-smart-markers/
---

## **Почему использовать вложенные объекты для умных маркеров**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. Представление иерархических данных: реальные данные по своей природе вложены (например, Заказ содержит Покупателя, у которого есть Адрес). Вложенные объекты отражают эту структуру, избегая плоских/искусственных полей, таких как город_покупателя.
2. Избежание коллизий в именах: плоские структуры рискуют столкновениями (например, product_name против supplier_name). Вложенность помогает естественным образом организовать имена:
<<product.name>> vs. <<supplier.name>>.
3. Модульность и повторное использование: повторное использование под-объектов в разных контекстах. Объект Адрес можно встроить в маркеры Покупателя, Поставщика или Сотрудника. Изменения в Адресе распространяются повсеместно.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. Поддержка фреймворками/инструментами: современные движки (например, Handlebars, React, FoxPro) нативно разрешают вложенные пути. Совместимо с JSON/API, где вложенные данные стандартны.

## **Как импортировать анонимные типы или пользовательские объекты с помощью умных маркеров**
Aspose.Cells также поддерживает анонимные типы или пользовательские объекты в умных маркерах. Приведенный ниже пример показывает, как это работает. Для импорта данных из динамических объектов с использованием умных маркеров посетите следующую статью:

[Импорт из динамического объекта в качестве источника данных](/cells/ru/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **Как импортировать вложенные объекты с помощью умных маркеров**
Aspose.Cells поддерживает вложенные объекты в умных маркерах, вложенные объекты должны быть простыми. Мы используем простой файл шаблона. Смотрите дизайнерскую электронную таблицу, содержащую некоторые вложенные умные маркеры.

|**Первый лист файла SM_NestedObjects.xlsx, показывающий вложенные умные маркеры.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Приведенный ниже пример показывает, как это работает.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Как импортировать обычный список как вложенный объект с помощью умных маркеров**
Aspose.Cells теперь также поддерживает использование обобщенного списка в качестве вложенного объекта. Пожалуйста, проверьте скриншот выходного файла Excel, сгенерированного следующим кодом. Как видно на скриншоте, объект 'Преподаватель' содержит несколько вложенных объектов 'Студент'.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **Как импортировать вложенные объекты не построчно с помощью умных маркеров**
Текущий метод обработки по умолчанию - обрабатывать умные маркеры построчно. Но иногда умные маркеры одной и той же таблицы данных нужно обрабатывать вместе, независимо 
от того, находятся ли они в одной строке или нет. В этом случае необходимо указать именованный диапазон "_CellsSmartMarkers" и указать, что WorkbookDesigner.LineByLine равно false перед вызовом обработки.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
