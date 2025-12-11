---
title: Spreadsheet Editor - Components
type: docs
weight: 50
url: /java/spreadsheet-editor-components/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

**Table of Contents**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [WorksheetView](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5 Spreadsheet Editor is built from a few components that join together to make the complete system. Here we describe the purpose and role of each.

### **Index.html**
It is a JSF page that describes the UI of the editor and the main endpoint of our application. All interaction **between the** web browser and the server **is** performed through this endpoint.

Besides defining the UI, all backend services are attached here using JSF technologies. **When the** user **interacts** with the UI, events and data are passed to **and fro** between services and the user to complete **tasks**, e.g., exporting spreadsheets.

It has two main areas of interest.

**Ribbon**

The tabbed‑toolbar area on top is called **Ribbon**, technically. It contains buttons, dropdowns, **radio** menus, text boxes, and some hidden fields which are used to perform many operations on the spreadsheet. **These buttons, when clicked, send commands to the server and update the sheet accordingly.**

**Sheet**

The sheet is the rows and columns. When cells are clicked, **the Ribbon** gets updated accordingly without sending requests to the server, as all data that is needed by the Ribbon is attached to each cell. **The Ribbon also keeps track of the selected cell, row, and column when the user navigates through the sheet.**

Each cell has its own inline editor which becomes visible when a cell is in editing mode.

### **WorksheetView**
It is a view‑scoped JSF backend bean responsible **for managing** the dynamic contents of UI described in **index.html**. It has event handlers for Ajax requests which are triggered as the user **interacts** with UI.

### **WorkbookService**
The WorkbookService is a view‑scoped JSF backend bean. It works as a service component and **loads** and **unloads** the spreadsheet with the help of other services. It has the following endpoints:

**init**

The **init** is a **PostConstruct** method that is executed right after the object creation is completed by the Java Application Server. It **checks** for the **url** parameter in the request parameters map and loads the corresponding spreadsheet from the given location, if possible.

**destroy**

It is responsible to **clean up** all acquired resources when they are no more required.

### **LoaderService**
It creates instances of **spreadsheets** and **keeps** them in memory as long as they are needed.

### **CellsService**
The **CellsService** manages the cache of rows, columns, cells, formatting, and structure of worksheets.
{{< app/cells/assistant language="java" >}}
