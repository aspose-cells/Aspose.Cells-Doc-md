---
title: Написать клиентский скрипт для GridWeb
type: docs
weight: 10
url: /ru/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: Эта статья рассказывает, как работать с клиентскими js API в GridWeb.
---

{{% alert color="primary" %}} 

Разработчики могут писать клиентские скрипты для элемента управления Aspose.Cells.GridWeb. Это означает, что можно вызывать клиентскую функцию JavaScript для выполнения определенной задачи, связанной с элементом управления GridWeb. Например, разработчики могут писать JavaScript-функции для отправки данных GridWeb на сервер или вывода сообщения предупреждения, когда происходит ошибка валидации и т. д.

Эта тема объясняет эту функцию с помощью примеров.

{{% /alert %}} 
## **Написание клиентских скриптов для Aspose.Cells.GridWeb**
### **Основная информация**
Aspose.Cells.GridWeb предоставляет два свойства, созданные специально для поддержки клиентских скриптов:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Создайте JavaScript-функции на странице ASPX и присвойте имена этих функций свойствам OnSubmitClientFunction и OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

Функция на JavaScript, которая будет присвоена свойству OnSubmitClientFunction, должна быть правильно определена, как показано ниже:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

где параметр [arg] представляет команду, сгенерированную управлением. Команда может быть "Сохранить", "Отправить", "Отменить" и т.д., а параметр [cancelEdit] - это логическое значение, которое указывает, отменен ввод пользователя или нет.

Любая JavaScript-функция, назначенная свойству OnSubmitClientFunction, вызывается каждый раз элементом управления GridWeb перед отправкой данных GridWeb на сервер. Аналогично, если функция назначена свойству OnValidationErrorClientFunction, то эта функция будет вызвана каждый раз, когда происходит ошибка проверки.

{{% /alert %}} 
### **Функции для клиентского сценарного программирования**
Aspose.Cells.GridWeb также предоставляет функции специально для клиентского сценарного программирования. Эти функции могут использоваться внутри JavaScript-функций для более тесного контроля над Aspose.Cells.GridWeb. Эти функции на стороне клиента включают следующее:

|**Функции**|**Описание**|
| :- | :- |
|updateData(bool cancelEdit)|Обновляет все клиентские данные Aspose.Cells.GridWeb перед отправкой их на сервер. Если параметр cancelEdit равен true, то GridWeb отклоняет весь ввод пользователя.|
|validateAll()|Используется для проверки наличия ошибок проверки ввода пользователей. Если возникает ошибка, функция возвращает false, в противном случае - true.|
|submit(string arg, bool cancelEdit)|Вызовите эту функцию для отправки данных на сервер. Эта функция выполняет оба задания: обновление данных и проверку ввода пользователя. Эта функция также может запустить событие команды на стороне сервера. Используйте параметр arg для передачи вашей команды. Например: команда SAVE используется для нажатия кнопки **Сохранить** на панели команд элемента управления GridWeb, а CCMD:MYCOMMAND команда запускает событие пользовательской команды.|
|setActiveCell(int row, int column)|Используется для активации определенной ячейки.|
|setCellValue(int row, int column, string value)|Используется для ввода значения в любую указанную ячейку по ее номерам строки и столбца.|
|getCellValue(int row, int column)|Возвращает значение любой указанной ячейки.|
|getActiveRow()|Используется с функцией getActiveColumn() для определения положения активной ячейки.|
|getActiveColumn()|Используется с функцией getActiveRow() для определения положения активной ячейки.|
|getSelectRange()|Возвращает последний выбранный диапазон.|
|setSelectRange()|Выбирает заданный диапазон.|
|clearSelections()|Сбрасывает все выделение, исключая текущую активную ячейку.|
|getCellsArray()|Используется с другими связанными функциями, такими как getCellName(), getCellValueByCell(), getCellRow() и getCellColumn(). Пожалуйста, прочитайте эту статью для получения более подробной информации о использовании этой функции: [Чтение значений ячеек GridWeb на стороне клиента](/cells/ru/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
Для создания тестового приложения, содержащего клиентские скрипты, работающие с Aspose.Cells.GridWeb, выполните следующие шаги:

1. Создайте JavaScript-функции, которые будут вызываться GridWeb.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. Назначьте имена функций свойствам OnSubmitClientFunction и OnValidationErrorClientFunction.

Результат примера кода показан ниже:

**Добавлена проверка в ячейку C1** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

Добавьте недопустимое значение и нажмите **Сохранить**. Произойдет ошибка проверки, и будет выполнена функция ValidationErrorFunction.

**ValidationErrorFunction вызвана при ошибке проверки** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

Пока вы не введете допустимое значение, данные не будут отправлены на сервер. Введите допустимое значение и нажмите **Сохранить**. Выполнится функция ConfirmFunction.

**ConfirmFunction вызвана перед отправкой данных GridWeb на сервер** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
