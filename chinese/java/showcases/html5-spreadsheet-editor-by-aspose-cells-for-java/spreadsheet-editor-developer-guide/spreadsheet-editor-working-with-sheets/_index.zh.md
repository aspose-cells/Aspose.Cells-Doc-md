---
title: 表格编辑器 - 与工作表一起工作
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
- [在表格之间切换](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **添加和删除工作表？**
Microsoft Excel允许在单个文件中有多个工作表。HTML5电子表格编辑器允许用户添加和删除工作表。在“工作表”选项卡上，我们有一个工作表的下拉列表。所选的工作表是编辑器打开的工作表。

添加新工作表：

1. 切换到 **工作表** 选项卡。
1. 单击 **+**（加号）按钮。

将添加一个新的工作表，并编辑器将切换到它。

要删除当前选定的工作表：

1. 切换到 **工作表** 选项卡。
1. 单击 **-**（减号）按钮。

当前选定的工作表将被删除，并编辑器将切换到最后选定的工作表。

![todo:image_alt_text](4wgvmu8.png)

**它是如何工作的？**

当用户单击 **+**（加号）和 **-**（减号）按钮时，JSF后端Bean **WorksheetView** 使用 **WorksheetView.onAddNewSheet** 和 **WorksheetView.onRemoveActiveSheet** 方法来处理事件。
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
要重命名工作表：

1. 切换到 **工作表** 选项卡。
1. 点击文本框中的工作表名称以编辑它。
1. 更改工作表的名称。
1. 完成后，按ENTER键，或单击文本框外的任何地方。

工作表将被重命名。

![todo:image_alt_text](4wgvmu8.png)

**它是如何工作的？**

当文本框的值发生更改时，由JSF后端bean **WorksheetView** 使用方法 **WorksheetView.setActiveSheet** 处理事件。
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
### **在表格之间切换**
切换到另一个工作表：

1. 切换到 **工作表** 选项卡。
1. 从下拉菜单中选择一个工作表。

编辑器将切换到所选的工作表。

![todo:image_alt_text](4wgvmu8.png)

**它是如何工作的？**

当下拉选择器的值发生更改时，由JSF后端bean **WorksheetView** 使用方法 **WorksheetView.setActiveSheet** 处理事件。
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
