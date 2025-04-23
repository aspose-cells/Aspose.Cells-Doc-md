---  
title: Нахождение или Поиск Данных
type: docs  
weight: 50  
url: /ru/nodejs-cpp/find-or-search-data/  
description: Узнайте, как находить или искать ячейки в листе с указанными данными с помощью API Aspose.Cells for Node.js via C++.  
keywords: Найти данные Node.js через C++, искать данные Node.js через C++, найти ячейки, содержащие формулы, Node.js через C++, искать ячейки с формулами, Node.js через C++, найти данные или формулы с помощью FindOptions, Node.js через C++, искать данные или формулы с помощью FindOptions, Node.js через C++, искать или находить ячейки с указанным строковым значением или числом, Node.js через C++, находить или искать ячейки с указанными данными  
---  

{{% alert color="primary" %}}  
Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные.  
{{% /alert %}}  

## **Поиск ячеек, содержащих указанные данные**  

### **Использование Microsoft Excel**  

Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные. Если выбрать **Редактировать** в меню **Найти** Microsoft Excel, появится диалоговое окно, в котором можно указать значение поиска.  

Здесь мы ищем значение "Апельсины". Aspose.Cells также позволяет разработчикам находить ячейки в листе с указанными значениями.  

### **Использование Aspose.Cells for Node.js via C++**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--), которая отображает все ячейки листа. Коллекция [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) содержит несколько методов для поиска ячеек, содержащих пользовательские данные. Некоторые из этих методов подробно рассматриваются ниже.  

{{% alert color="primary" %}}  
Все методы поиска возвращают ссылки на ячейки, содержащие указанные искомые данные.  
{{% /alert %}}  

## **Поиск ячеек, содержащих формулу**  

Разработчики могут найти заданную формулу в листе, вызвав метод [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Обычно метод [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) принимает три параметра:  

- **Объект:** объект для поиска. Тип должен быть int, double, DateTime, string, bool.  
- **Предыдущая ячейка:** Предыдущая ячейка с тем же объектом. Этот параметр можно установить в null, если поиск начинать с начала.  
- **FindOptions:** Опции для поиска нужного объекта.  

Ниже приведены примеры использования данных листа для тренировки методов поиска:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **Поиск данных или формул с использованием FindOptions**  

Возможно найти указанные значения, используя метод [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) с различными [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). Обычно метод [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) принимает следующие параметры:  

- **Значение поиска**, данные или значение для поиска.  
- **Предыдущая ячейка**, последняя ячейка, содержавшая то же значение. Этот параметр может быть установлен в null при поиске с начала.  
- **Параметры поиска**, параметры поиска.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Поиск ячеек, содержащих указанное строковое значение или число**  

Можно найти указанные строковые значения, вызвав тот же метод [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) с различными [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

Укажите свойства [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) и [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-). Следующий пример показывает, как использовать эти свойства для поиска ячеек с различным количеством строк в **начале**, **посередине** или **в конце** строки ячейки.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Продвинутые темы**  
- [Нахождение ячеек с определенным стилем](/cells/ru/nodejs-cpp/find-cells-with-specific-style/)  
- [Определите, начинается ли значение ячейки с одинарной кавычки](/cells/ru/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Поиск данных с использованием исходных значений](/cells/ru/nodejs-cpp/search-data-using-original-values/)  

