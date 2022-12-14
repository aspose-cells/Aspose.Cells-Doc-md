---
title: 电子表格编辑器 - 使用表格
type: docs
weight: 20
url: /zh/java/spreadsheet-editor-working-with-sheets/
---
**目录**

- [添加和删除工作表？](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - 工作表视图.onAddNewSheet
 - 工作表视图.onRemoveActiveSheet
- [重命名工作表](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 WorksheetView.setActiveSheet
- [在工作表之间切换](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 WorksheetView.setActiveSheet
### **添加和删除工作表？**
Microsoft Excel 允许在一个文件中包含多个工作表。 HTML5 电子表格编辑器允许用户添加和删除表格。在“工作表”选项卡上，我们有一个工作表下拉列表。所选工作表是编辑器打开的工作表。

要添加新工作表：

1. 切换到**工作表标签**.
1. 单击 **+**（加号）按钮。

将添加一个新工作表，编辑器将切换到它。

要删除当前选定的工作表：

1. 切换到**工作表标签**.
1. 单击 **-**（减号）按钮。

当前选择的工作表将被删除，编辑器将切换到最后选择的工作表。

![待办事项：图片_替代_文本](4wgvmu8.png)

**这个怎么运作？**

当用户点击**+**（加号）和**-**单击（减号）按钮，JSF 后端 bean**工作表视图**使用处理事件**工作表视图.onAddNewSheet**和**WorksheetView.onRemoveActiveSheet** 方法。
#### **工作表视图.onAddNewSheet**
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

#### **工作表视图.onRemoveActiveSheet**
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
### **重命名工作表**
要重命名工作表：

1. 切换到**工作表标签**.
1. 单击文本框中的工作表名称以对其进行编辑。
1. 更改工作表的名称。
1. 完成后，按 ENTER 键，或单击框外的任意位置。

工作表将被重命名。

![待办事项：图片_替代_文本](4wgvmu8.png)

**这个怎么运作？**

当文本框值更改时，事件由 JSF 后端 bean 在服务器上处理**工作表视图**使用方法**工作表视图.setActiveSheet**.
#### **工作表视图.setActiveSheet**
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
### **在工作表之间切换**
要切换到另一个工作表：

1. 切换到**工作表标签**.
1. 从下拉菜单中选择工作表。

编辑器将切换到选定的工作表。

![待办事项：图片_替代_文本](4wgvmu8.png)

**这个怎么运作？**

当下拉选择器的值改变时，事件由 JSF 后端 bean 在服务器上处理**工作表视图**使用方法**工作表视图.setActiveSheet**.
#### **工作表视图.setActiveSheet**
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
