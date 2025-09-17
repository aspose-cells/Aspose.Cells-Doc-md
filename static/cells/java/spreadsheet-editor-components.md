##Spreadsheet Editor - Components
**Table of Contents**
- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [WorksheetView](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)
HTML5 Spreadsheet Editor is built from a few components that join together to make the complete system. Here we describe purpose and role of each.
### **Index.html**
It is a JSF page that describes the UI of editor and the main endpoint of our application. All interaction that is performed between web browser and server are performed through this endpoint.
Besides defining the UI, all backend services are attached here using JSF technologies. When user interact with the UI events and data is passed to-and-fro between services and user to complete our tasks e.g. exporting spreadsheets.
It has two main areas of interest.
**Ribbon**
The tabbed-toolbar area on top is called ribbon, technically. It contains buttons, dropdowns, radios menus, text-boxes and some hidden fields which are used to perform many operations on the spreadsheet. These buttons when clicked send commands to server and update the sheet accordingly.
**Sheet**
The sheet is the rows and columns. When cells are clicked, ribbon gets updated accordingly without sending requests to the server as all data that is needed by the ribbon is attached to each cell. Ribbon also keeps track on the selected cell, row and column when user navigate through the sheet.
Each cell has its own inline editor which becomes visible when a cell is in editing mode.
### **WorksheetView**
It is a view-scoped JSF backend bean responsible to manage the dynamic contents of UI described in index.html. It has event-handlers for Ajax requests which are triggered as the user interact with UI.
### **WorkbookService**
The WorkbookService is a view-scoped JSF backend bean. It works as a service component and gets the spreadsheet loaded and unloaded with the help of other services. It has the following endpoints:
**init**
The **init** is **PostConstruct** method that is executed right after the object creation is completed by the Java Application Server. It check for **url** parameter in request parameters map and loads the corresponding spreadsheet from given location, if possible.
**destroy**
It is responsible to cleanup all acquired resources when they are no more required.
### **LoaderService**
It creates instances of spreadsheet and keep them in memory as long as they are needed.
### **CellsService**
The **CellsService** manages cache of rows, columns, cells, formatting, and structure of worksheets.
