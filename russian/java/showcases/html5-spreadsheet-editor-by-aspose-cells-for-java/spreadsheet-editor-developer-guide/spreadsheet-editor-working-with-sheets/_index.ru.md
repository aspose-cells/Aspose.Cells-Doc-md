---
title: Редактор электронных таблиц — Работа с листами
type: docs
weight: 20
url: /ru/java/spreadsheet-editor-working-with-sheets/
---
**Оглавление**

- [Добавить и удалить листы?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [Переименовать листы](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [Переключение между листами](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **Добавить и удалить листы?**
Microsoft Excel позволяет использовать несколько листов в одном файле. Редактор электронных таблиц HTML5 позволяет пользователю добавлять и удалять листы. На вкладке Sheets у нас есть выпадающий список листов. Выбранный лист открывается редактором.

Чтобы добавить новый лист:

1.  Переключить на**Вкладка "Листы"**.
1. Нажмите кнопку **+** (плюс).

Будет добавлен новый лист, и редактор переключится на него.

Чтобы удалить текущий выбранный лист:

1.  Переключить на**Вкладка "Листы"**.
1. Нажмите кнопку **-** (минус).

Текущий выбранный лист будет удален, и редактор переключится на последний выбранный лист.

![дело:изображение_альтернативный_текст](4wgvmu8.png)

**Как это работает?**

 Когда пользователь нажимает на** +** (плюс) и**-** кнопка (минус) нажата, внутренний компонент JSF**Вид рабочего листа** обрабатывает события с помощью**WorksheetView.onAddNewSheet** и**Методы WorksheetView.onRemoveActiveSheet**.
#### **WorksheetView.onAddNewSheet**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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

1.  Переключить на**Вкладка "Листы"**.
1. Щелкните имя листа в текстовом поле, чтобы отредактировать его.
1. Измените имя листа.
1. Когда закончите, нажмите клавишу ENTER или щелкните в любом месте за пределами поля.

Лист будет переименован.

![дело:изображение_альтернативный_текст](4wgvmu8.png)

**Как это работает?**

 Когда значение текстового поля изменяется, событие обрабатывается на сервере внутренним компонентом JSF.**Вид рабочего листа** используя метод**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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
Чтобы переключиться на другой лист:

1.  Переключить на**Вкладка "Листы"**.
1. Выберите лист из раскрывающегося меню.

Редактор переключится на выбранный лист.

![дело:изображение_альтернативный_текст](4wgvmu8.png)

**Как это работает?**

 Когда значение раскрывающегося селектора изменяется, событие обрабатывается на сервере внутренним компонентом JSF.**Вид рабочего листа** используя метод**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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
