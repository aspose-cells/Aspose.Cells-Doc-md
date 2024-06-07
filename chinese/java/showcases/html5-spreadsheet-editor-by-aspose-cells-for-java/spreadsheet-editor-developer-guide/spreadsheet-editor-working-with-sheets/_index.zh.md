---
title: 电子表格编辑器 - 与工作表一起工作
type: docs
weight: 20
url: /zh/java/spreadsheet-editor-working-with-sheets/
---

**目录**

- [添加和删除工作表？](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [重命名工作表](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [在工作表之间切换](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **添加和删除工作表？**
Microsoft Excel允许在单个文件中拥有多个工作表。HTML5 电子表格编辑器允许用户添加和删除工作表。在工作表选项卡中，我们有一个工作表的下拉列表。所选的工作表是编辑器打开的工作表。

添加新工作表：

1. 切换到**工作表选项卡**。
1. 单击**+**（加号）按钮。

将添加新的工作表，并且编辑器将切换到它。

删除当前选定的工作表：

1. 切换到**工作表选项卡**。
1. 单击**-**（减号）按钮。

当前选定的工作表将被删除，编辑器将切换到上次选定的工作表。

![todo:image_alt_text](4wgvmu8.png)

**它是如何工作的？**

当用户单击**+**（加号）和**-** （减号）按钮时，JSF后端bean **WorksheetView** 使用**WorksheetView.onAddNewSheet**和**WorksheetView.onRemoveActiveSheet** 方法处理事件。
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
### **重命名工作表**
重命名工作表：

1. 切换到**工作表选项卡**。
1. 单击文本框中的工作表名称以进行编辑。
1. 更改工作表名称。
1. 完成后，按ENTER键，或单击框框外部的任何位置。

工作表将被重命名。

![todo:image_alt_text](4wgvmu8.png)

**它是如何工作的？**

当文本框的值发生更改时，通过JSF后端bean **WorksheetView** 使用方法**WorksheetView.setActiveSheet** 在服务器上处理事件。
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
### **在工作表之间切换**
要切换到另一个工作表：

1. 切换到**工作表选项卡**。
1. 从下拉菜单中选择一个工作表。

编辑器将切换到所选的工作表。

![todo:image_alt_text](4wgvmu8.png)

**它是如何工作的？**

当下拉选择器的值更改时，由JSF后端bean **WorksheetView** 处理事件，使用方法 **WorksheetView.setActiveSheet**。
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
