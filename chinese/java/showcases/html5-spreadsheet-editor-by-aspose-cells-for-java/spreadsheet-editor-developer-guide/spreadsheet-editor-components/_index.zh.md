---
title: 电子表格编辑器-组件
type: docs
weight: 50
url: /zh/java/spreadsheet-editor-components/
---

**目录**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [WorksheetView](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5电子表格编辑器由几个组件组成，这些组件共同组成完整的系统。在这里，我们描述每个组件的目的和作用。
### **Index.html**
这是一个JSF页面，描述了编辑器的UI和我们应用程序的主端点。所有在Web浏览器和服务器之间进行的交互都是通过这个端点进行的。

除了定义UI，所有后端服务都使用JSF技术连接在这里。用户与UI交互时，事件和数据在服务和用户之间来回传递，以完成我们的任务，例如导出电子表格。

它有两个主要的关注点。

**功能区**

顶部的分页工具栏区域在技术上被称为功能区。它包含按钮、下拉菜单、单选菜单、文本框和一些隐藏字段，用于在电子表格上执行许多操作。单击这些按钮会发送命令到服务器并相应地更新工作表。

**工作表**

工作表是由行和列组成的。当单元格被点击时，功能区相应地更新，而无需向服务器发送请求，因为附加到每个单元格的所有功能区所需的数据都已连接。当用户在工作表中导航时，功能区还会跟踪所选单元格、行和列。

每个单元格都有自己的内联编辑器，当单元格处于编辑模式时可见。
### **WorksheetView**
这是一个视图范围的 JSF 后端 bean，负责管理 index.html 中描述的 UI 的动态内容。它具有与用户与 UI 交互时触发的 Ajax 请求的事件处理程序。
### **WorkbookService**
WorkbookService 是一个视图范围的 JSF 后端 bean。它作为服务组件工作，并借助其他服务加载和卸载电子表格。它具有以下端点：

init

init 是在 Java 应用服务器完成对象创建后立即执行的 PostConstruct 方法。它检查请求参数映射中的 url 参数，并从给定位置加载相应的电子表格（如果可能）。

destroy

该方法负责清除所有不再需要的资源。
### **LoaderService**
它创建电子表格的实例，并在需要时将它们保存在内存中。
### **CellsService**
CellsService 管理行、列、单元格的缓存，以及工作表的格式和结构。
