---
title: Защитить и снять защиту листа
type: docs
weight: 50
url: /ru/java/protect-and-unprotect-worksheet/
---

## **Защита листов**

Когда лист защищен, пользовательские действия ограничены. Например, они не могут вводить данные, вставлять или удалять строки или столбцы и т. д. Основные параметры защиты в Microsoft Excel:

- Содержимое
- Объекты
- Сценарии

Защищенные листы не скрывают или защищают конфиденциальные данные, поэтому это отличается от шифрования файлов. Обычно защита листа подходит для презентационных целей. Она предотвращает конечного пользователя от изменения данных, содержимого и форматирования на листе.

### **Добавление или удаление защиты**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс Workbook содержит WorksheetCollection, которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Класс Worksheet предоставляет метод [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect-int-), который используется для применения защиты к листу. Метод Protect принимает следующие параметры:

- Тип защиты, тип защиты, применяемый к листу. Тип защиты применяется с помощью перечисления [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType).
- Новый пароль, новый пароль, используемый для защиты листа.
- Старый пароль, старый пароль, если лист уже защищен паролем. Если лист еще не защищен, просто передайте null.

Перечисление ProtectionType содержит следующие предопределенные типы защиты:

|**Типы защиты**|**Описание**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|Пользователь не может изменять что-либо на этом листе|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|Пользователь не может вводить данные на этом листе|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|Пользователь не может изменять рисуночные объекты|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|Пользователь не может изменять сохраненные сценарии|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|Пользователь не может изменять сохраненную структуру|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|Пользователь не может изменять сохраненные окна|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Нет защиты|

Приведенный ниже пример показывает, как защитить лист паролем.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

После использования приведенного выше кода для защиты листа, проверьте защиту на листе, открыв его. Как только вы откроете файл и попробуете добавить некоторые данные на лист, будет отображен следующий диалоговое окно:

**Диалоговое окно предупреждения, что пользователь не может изменять лист** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

Чтобы работать с листом, снимите защиту с листа, выбрав **Защита**, затем **Снять защиту листа** из меню **Инструменты**, как показано ниже.

**Выбор пункта меню Снять защиту листа** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

Открывается диалоговое окно, запрашивающее пароль.

**Ввод пароля для снятия защиты с листа** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Защита нескольких ячеек**

Могут быть определенные сценарии, когда вам нужно заблокировать только некоторые ячейки на листе. Если вы хотите заблокировать определенные ячейки на листе, вам нужно разблокировать все остальные ячейки на листе. Все ячейки на листе уже инициализированы для блокировки, вы можете проверить это, открыв любой файл Excel в MS Excel и щелкнув **Формат | Ячейки...** чтобы показать диалоговое окно **Формат ячеек**, а затем щелкните вкладку **Защита** и убедитесь, что флажок «Заблокирован» установлен по умолчанию.

Ниже приведены два подхода к выполнению задачи.

**Метод1:**

Следующие пункты описывают, как заблокировать несколько ячеек с помощью MS Excel. Этот метод применим к Microsoft Office Excel 97, 2000, 2002, 2003 и более новым версиям.

1. Выберите весь лист, нажав кнопку Выбрать все (серый прямоугольник непосредственно над номером строки для строки 1 и слева от буквы столбца A).
1. Нажмите Ячейки на меню Формат, выберите вкладку Защита, а затем снимите флажок с защиты.

   Это разблокирует все ячейки на листе.

{{% alert color="primary" %}}

Если команда 'Ячейки' недоступна, то части листа могут быть уже заблокированы. В меню 'Инструменты' указать для пункта 'Защита' и затем щелкнуть 'Снять защиту листа'.

{{% /alert %}}

1. Выберите только те ячейки, которые вы хотите заблокировать, и повторите шаг 2, но на этот раз установите флажок 'Заблокирован'.
1. В меню **Инструменты** выберите **Защита**, щелкните **Защита листа**, затем щелкните **OK**.

{{% alert color="primary" %}}

В диалоговом окне "Защита листа" у вас есть возможность указать пароль и выбрать элементы, которые вы хотите, чтобы пользователи могли менять.

{{% /alert %}}

**Метод2:**

В этом методе мы используем только Aspose.Cells API для выполнения этой задачи.

Приведенный ниже пример показывает, как защитить несколько ячеек на листе. Сначала разблокируются все ячейки на листе, а затем блокируются 3 ячейки (A1, B1, C1) в нем. Наконец, защищается лист. У объекта row / column есть метод Style API, который содержит метод set Locked. Вы можете использовать данный метод, чтобы заблокировать или разблокировать строку / столбец.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Защита строки на листе**

Aspose.Cells позволяет легко заблокировать любую строку на листе. Здесь мы можем использовать метод [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) класса [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) для применения стиля к конкретной строке на листе. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) и структуру [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), которая содержит все члены, связанные с примененным форматированием.

Приведенный ниже пример показывает, как защитить строку на листе. Сначала разблокируются все ячейки на листе, а затем блокируется первая строка в нем. Наконец, защищается лист. У объекта row / column есть метод Style API, который содержит метод setCellLocked. Вы можете заблокировать или разблокировать строку / столбец, используя структуру StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Защита столбца на листе**

Aspose.Cells позволяет легко заблокировать любой столбец на листе. Здесь мы можем использовать метод [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) класса [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) для применения стиля к конкретному столбцу на листе. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) и структуру [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), которая содержит все члены, связанные с примененным форматированием.

Приведенный ниже пример показывает, как защитить столбец на листе. Сначала разблокируются все ячейки на листе, а затем блокируется первый столбец в нем. Наконец, защищается лист. У объекта row / column есть метод Style API, который содержит метод set Locked. Вы можете заблокировать или разблокировать строку / столбец, используя структуру StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Снятие защиты с листа**

[Защита листов](/cells/ru/java/protect-and-unprotect-worksheet/#protect-worksheets) и [Расширенные настройки защиты с Excel XP](/cells/ru/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) обсудили различные подходы к защите листов. Что делать, если разработчику нужно удалить защиту с защищенного листа во время выполнения, чтобы внести некоторые изменения в файл? Это легко сделать с Aspose.Cells.

### **Использование Microsoft Excel**

Для снятия защиты с листа:

Выберите **Защита** из меню **Инструменты**, а затем **Снять защиту листа**.

**Выбор снятия защиты листа** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

Защита снимается, если только лист защищен паролем. В этом случае появляется диалоговое окно для ввода пароля.

**Ввод пароля для снятия защиты с листа** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Использование Aspose.Cells**

Лист можно снять с защиты, вызвав метод [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Метод [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) может использоваться двумя способами, описанными ниже.

### **Снятие защиты с просто защищенного листа**

Просто защищенный лист - это лист, который не защищен паролем. Такие листы можно снять с защиты, вызвав метод снятия защиты без передачи параметра.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Снятие защиты с листа, защищенного паролем**

Лист с защитой паролем - это лист, защищенный паролем. Такие листы можно разблокировать, вызвав перегруженную версию метода Unprotect, которая принимает пароль в качестве параметра.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Расширенные настройки защиты с момента появления Excel XP**

[Защита листов](/cells/ru/java/protect-and-unprotect-worksheet/#protect-worksheets) обсуждает защиту листа в Microsoft Excel 97 и 2000. Начиная с выпуска Excel 2002 или XP, Microsoft добавила множество расширенных настроек защиты. Эти настройки защиты ограничивают или разрешают пользователям:

- Удалить строки или столбцы.
- Изменить содержимое, объекты или сценарии.
- Форматировать ячейки, строки или столбцы.
- Вставить строки, столбцы или гиперссылки.
- Выбирать заблокированные или разблокированные ячейки.
- Использовать сводные таблицы и многое другое.

Aspose.Cells поддерживает все расширенные настройки защиты, предлагаемые Excel XP и последующими версиями.

### **Настройки расширенной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть доступные настройки защиты в Excel XP:

1. Из меню **Инструменты** выберите **Защита**, а затем **Защита листа**.
   Отображается диалоговое окно.

   **Диалог для отображения вариантов защиты в Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. Разрешите или ограничьте функции листов или примените пароль.

### **Настройки расширенной защиты с использованием Aspose.Cells**

Aspose.Cells поддерживает все расширенные настройки защиты.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс Workbook содержит коллекцию WorksheetCollection, которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Класс Worksheet предоставляет свойство Protection для применения этих расширенных настроек защиты. Свойство Protection фактически является объектом класса [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection), который инкапсулирует несколько логических свойств для отключения или включения ограничений.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство поддерживаемых Excel XP и более поздних версий настроек защиты.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Сохраните файл в формате EXCEL97TO2003 или XLSX, потому что эти продвинутые настройки защиты поддерживаются только MS Excel XP и более поздних версиях.

{{% /alert %}}

### **Проблема блокировки ячеек**

Если вы хотите ограничить пользователей от редактирования ячеек, необходимо заблокировать ячейки до применения любых настроек защиты. В противном случае ячейки можно редактировать, даже если рабочий лист защищен. В Microsoft Excel XP ячейки можно заблокировать через следующий диалоговое окно:

**Диалоговое окно блокировки ячеек в Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Также можно блокировать ячейки с использованием API Aspose.Cells. У каждой ячейки есть метод Style API, который далее содержит метод setLocked. Используйте его для блокировки или разблокировки ячеек.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
{{< app/cells/assistant language="java" >}}
