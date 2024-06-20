---
title: Работа с ячейками GridWeb
type: docs
weight: 50
url: /ru/java/working-with-cells-gridweb/
---

## **Доступ к ячейкам в таблице**
В этой теме рассматриваются ячейки, изучается самая основная функция GridWeb: доступ к ячейкам.

Каждая таблица содержит объект GridCells, коллекцию объектов GridCell. Объект GridCell представляет собой ячейку в Aspose.Cells.GridWeb. Возможно получить доступ к любой ячейке, используя GridWeb. Существует два предпочтительных метода:

- [Доступ к ячейке по имени](/cells/ru/java/working-with-cells-gridweb/).
- [Доступ к ячейке по индексам строки и столбца](/cells/ru/java/working-with-cells-gridweb/).

Ниже рассмотрены оба подхода.
### **Использование имени ячейки**
Все ячейки имеют уникальное имя. Например, A1, A2, B1, B2 и т. д. Aspose.Cells.GridWeb позволяет разработчикам получить доступ к любой желаемой ячейке, используя имя ячейки. Просто передайте имя ячейки (в качестве индекса) в коллекцию GridCells объекта GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Использование индексов строки и столбца**
Ячейку также можно распознать по ее расположению в терминах индексов строки и столбца. Просто передайте индексы строки и столбца ячейки в коллекцию GridCells объекта GridWorksheet. Этот подход более быстрый, чем предыдущий.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Доступ и изменение значения ячейки**
[Доступ к ячейкам в таблице](/cells/ru/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) обсуждает доступ к ячейкам. В этой теме расширяется эта дискуссия, чтобы показать, как получить доступ и изменить значения ячеек, используя API GridWeb.
### **Доступ и изменение значения ячейки**
#### **Строковые значения**
Прежде чем получать доступ и изменять значение ячейки, нужно знать, как получить доступ к ячейкам. Для получения подробной информации о различных подходах к доступу к ячейкам обратитесь к [Доступ к ячейкам в таблице](/cells/ru/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

У каждой ячейки есть свойство с именем getStringValue(). После того как ячейка получена, разработчики могут использовать метод getStringValue() для доступа к строковому значению ячеек.

{{% alert color="primary" %}} 

ВАЖНО: В ячейках могут храниться пять типов значений (логический, целый, двойной, дата-время и строка), но методы getValue()/setValue() можно использовать только для доступа к/изменения объектного значения.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Все типы значений**
Aspose.Cells.GridWeb также предоставляет специальный метод putValue для каждой ячейки. С помощью этого метода возможно вставить или изменить любой тип значения (логический, целый, двойной, дата-время и строка) в ячейке.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Также существует перегруженная версия метода putValue, которая может принимать любой тип значения в виде строки и автоматически преобразовать его в соответствующий тип данных. Для этого передайте логическое значение true в другой параметр метода putValue, как показано ниже в примере.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Добавление формул в ячейки**
Самая ценная функция, предлагаемая Aspose.Cells.GridWeb, - это поддержка формул или функций. У Aspose.Cells.GridWeb есть свой собственный Движок формул, который вычисляет формулы в рабочих книгах. Aspose.Cells.GridWeb поддерживает как встроенные, так и определяемые пользователем функции или формулы. В этой теме подробно рассматривается добавление формул в ячейки с использованием API Aspose.Cells.GridWeb.
### **Как добавить и вычислить формулу?**
Возможно добавлять, получать доступ к и изменять формулы в ячейках, используя свойство Formula ячейки. Aspose.Cells.GridWeb поддерживает определяемые пользователем формулы от простых до сложных. Однако с Aspose.Cells.GridWeb также поставляется большое количество встроенных функций или формул (аналогично Microsoft Excel). Чтобы увидеть полный список встроенных функций, обратитесь к этому [списку поддерживаемых функций.](/cells/ru/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Синтаксис формулы должен быть совместим с синтаксисом Microsoft Excel. Например, все формулы должны начинаться с знака равенства (=).

Чтобы программно добавить формулу, Aspose.Cells.GridWeb будет распознавать ее как формулу, даже если вы не используете знак **=**, но если конечные пользователи, работающие в GUI, должны его использовать.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Формула добавлена в ячейку B3, но не вычислена GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

На скриншоте выше вы можете видеть, что формула была добавлена в ячейку B3, но еще не была вычислена. Для вычисления всех формул вызовите метод calculateFormula коллекции GridWorksheetControl GridWeb после добавления формул в листы, как показано ниже.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Пользователи также могут вычислять формулы, нажимая кнопку **Отправить**.

**Нажатие кнопки «Отправить» GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**ВАЖНО**: Если пользователь нажимает кнопки **Сохранить** или **Отменить**, или вкладки листов, все формулы автоматически вычисляются GridWeb.

**Результат формулы после вычисления** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Ссылка на ячейки из других рабочих книг**
С помощью Aspose.Cells.GridWeb можно ссылаться на значения, хранящиеся в разных рабочих книгах в их формулах, создавая сложные формулы.

Синтаксис для ссылки на значение ячейки из другой рабочей книги: НазваниеЛиста!ИмяЯчейки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Создание проверки данных в ячейке сетки GridWeb**
Aspose.Cells.GridWeb позволяет добавлять **проверку данных** с помощью метода GridWorksheet.getValidations().add(). Используя этот метод, вы должны указать **диапазон ячеек**. Но если вы хотите создать проверку данных в одной ячейке сетки, то вы можете сделать это непосредственно с помощью метода GridCell.createValidation(). Аналогично, вы можете удалить проверку данных из ячейки GridCell с помощью метода GridCell.removeValidation().

В следующем образце кода создается **Проверка данных** в ячейке B3. Если вы введете значение, которое не находится между 20 и 40, ячейка B3 покажет **Ошибка проверки** в виде **Красного XXXX**, как показано на этом снимке экрана.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Создание пользовательских кнопок команд**
Aspose.Cells.GridWeb содержит специальные кнопки, такие как Отправить, Сохранить и Отменить. Все эти кнопки выполняют определенные задачи для Aspose.Cells.GridWeb. Также возможно добавлять пользовательские кнопки, выполняющие пользовательские задачи. В этой теме объясняется, как использовать эту функцию.

В приведенном ниже образце кода объясняется, как создать пользоватскую командную кнопку и как обрабатывать ее событие нажатия. Вы можете использовать любую иконку для своей пользоватской командной кнопки. В иллюстративных целях мы использовали эту иконку изображения.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

Как видно на следующем снимке экрана, когда пользователь нажимает на пользовательскую кнопку команды, она добавляет текст в ячейку A1, который говорит: "Моя Пользовательская Кнопка Команды Нажата."

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Обработка событий пользовательской командной кнопки**
В следующем примере кода объясняется, как выполнять обработку событий пользовательской кнопки команды.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Форматирование ячеек для GridWeb**
### **Возможные сценарии использования**
GridWeb теперь поддерживает ввод данных ячейки в формате процентов, например, 3%, и данные в ячейке автоматически форматируются как 3,00%. Однако вы должны установить стиль ячейки в формат процента, который соответствует GridTableItemStyle.NumberType 9 или 10. Число 9 отформатирует 3% как 3%, а число 10 отформатирует 3% как 3,00%.

{{% alert color="primary" %}} 

Если вы не установили стиль ячейки в формат процента, то введенные данные 3% будут отображаться как 0,03.

{{% /alert %}} 
### **Введите данные ячейки рабочего листа GridWeb в формате процентов**
В следующем образце кода устанавливается стиль ячейки A1 GridTableItemStyle.NumberType как 10, поэтому введенные данные 3% автоматически форматируются как 3,00%, как показано на скриншоте.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
