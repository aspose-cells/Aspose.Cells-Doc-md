---
title: Редактор электронных таблиц  Работа с листами
type: docs
weight: 20
url: /ru/java/spreadsheet-editor-working-with-sheets/
---

**Содержание**

- [Добавить и удалить таблицы?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [Переименовать листы](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [Переключение между листами](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **Добавить и удалить таблицы?**
Microsoft Excel позволяет использовать несколько листов в одном файле. Редактор электронных таблиц HTML5 позволяет пользователю добавлять и удалять листы. На вкладке Листы у нас есть выпадающий список листов. Выбранный лист открывается редактором.

Чтобы добавить новый лист:

1. Перейдите на вкладку **Листы**.
1. Нажмите на кнопку **+** (плюс).

Будет добавлен новый лист, и редактор переключится на него.

Чтобы удалить выбранный лист:

1. Перейдите на вкладку **Листы**.
1. Нажмите на кнопку **-** (минус).

Выбранный лист будет удален, и редактор переключится на последний выбранный.

![todo:image_alt_text](4wgvmu8.png)

**Как это работает?**

Когда пользователь нажимает на кнопки **+** (плюс) и **-** (минус), бэкэнд-бин JSF **WorksheetView** обрабатывает события с использованием методов **WorksheetView.onAddNewSheet** и **WorksheetView.onRemoveActiveSheet**.
#### **WorksheetView.onAddNewSheet**
{{< highlight java >}}

     public void onAddNewSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().add();

                getAsposeWorksheets().setActiveSheetIndex(i);

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("New Worksheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}

#### **WorksheetView.onRemoveActiveSheet**
{{< highlight java >}}

     public void onRemoveActiveSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().getActiveSheetIndex();

                getAsposeWorksheets().removeAt(i);

                if (getAsposeWorksheets().getCount() == 0) {

                    int j = getAsposeWorksheets().add();

                    getAsposeWorksheets().setActiveSheetIndex(j);

                }

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("Could not remove sheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}
### **Переименовать листы**
Чтобы переименовать лист:

1. Перейдите на вкладку **Листы**.
1. Нажмите на имя листа в текстовом поле, чтобы отредактировать его.
1. Измените имя листа.
1. После завершения нажмите клавишу ВВОД или щелкните где-либо за пределами поля.

Лист будет переименован.

![todo:image_alt_text](4wgvmu8.png)

**Как это работает?**

Когда изменяется значение текстового поля, событие обрабатывается на сервере с помощью бэкенд-бина JSF **WorksheetView** с использованием метода **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
### **Переключение между листами**
Для переключения на другой лист:

1. Перейдите на вкладку **Листы**.
1. Выберите лист из выпадающего меню.

Редактор переключится на выбранный лист.

![todo:image_alt_text](4wgvmu8.png)

**Как это работает?**

Когда изменяется значение селектора выпадающего списка, событие обрабатывается на сервере с помощью бэкенд-бина JSF **WorksheetView** с использованием метода **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
