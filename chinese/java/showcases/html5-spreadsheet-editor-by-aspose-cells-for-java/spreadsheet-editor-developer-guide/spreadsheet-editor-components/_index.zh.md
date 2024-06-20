---
title: 电子表格编辑器  组件
type: docs
weight: 50
url: /zh/java/spreadsheet-editor-components/
---

**目录**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [工作表视图](#SpreadsheetEditor-Components-WorksheetView)
- [工作簿服务](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5电子表格编辑器由几个组件构建而成，这些组件共同构成了完整的系统。在这里，我们描述了每个组件的目的和作用。
### **Index.html**
这是一个描述编辑器用户界面和我们应用程序的主要端点的JSF页面。在 Web 浏览器和服务器之间执行的所有互动都是通过这个端点执行的。

除了定义用户界面，所有的后端服务都使用 JSF 技术附加在这里。当用户与用户界面进行交互时，事件和数据在服务和用户之间来回传递，以完成我们的任务，例如导出电子表格。

它有两个主要的兴趣领域。

**功能区**

顶部的选项卡工具栏区域在技术上称为功能区。它包含按钮、下拉菜单、单选按钮菜单、文本框和一些隐藏字段，用于在电子表格上执行许多操作。单击这些按钮会向服务器发送命令，并相应地更新工作表。

**工作表**

表格是行和列。当单元格被点击时，功能区会相应地更新而无需向服务器发送请求，因为功能区所需的所有数据都附加到每个单元格上。当用户在表格中导航时，功能区还会跟踪所选的单元格、行和列。

每个单元格都有自己的内联编辑器，当单元格处于编辑模式时才可见。
### **工作表视图**
这是一个视图范围的 JSF 后端 Bean，负责管理在 index.html 中描述的用户界面的动态内容。它具有用于处理随用户与用户界面交互而触发的 Ajax 请求的事件处理程序。
### **工作簿服务**
WorkbookService 是一个视图范围的 JSF 后端 bean。它作为一个服务组件工作，并通过其他服务加载和卸载电子表格。它具有以下端点：

**init**

**init** 是一个 **PostConstruct** 方法，它在 Java 应用服务器执行对象创建完成后立即被执行。它检查请求参数映射中的 **url** 参数，并从给定位置加载相应的电子表格，如果可能的话。

**destroy**

当不再需要时，它负责清理所有获取的资源。
### **LoaderService**
它创建电子表格的实例，并在需要时将它们保存在内存中。
### **CellsService**
**CellsService** 管理行、列、单元格、格式化和工作表结构的缓存。
