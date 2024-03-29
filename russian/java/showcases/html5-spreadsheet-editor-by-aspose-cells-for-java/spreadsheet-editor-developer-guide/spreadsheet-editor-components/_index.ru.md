﻿---
title: Редактор электронных таблиц — Компоненты
type: docs
weight: 50
url: /ru/java/spreadsheet-editor-components/
---
**Оглавление**

- [Индекс.html](#SpreadsheetEditor-Components-Index.html)
- [Вид рабочего листа](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

Редактор электронных таблиц HTML5 состоит из нескольких компонентов, которые объединяются в единую систему. Здесь мы описываем цель и роль каждого из них.
### **Индекс.html**
Это страница JSF, которая описывает пользовательский интерфейс редактора и основную конечную точку нашего приложения. Все взаимодействие между веб-браузером и сервером осуществляется через эту конечную точку.

Помимо определения пользовательского интерфейса, сюда подключаются все серверные службы с использованием технологий JSF. Когда пользователь взаимодействует с пользовательским интерфейсом, события и данные передаются туда-сюда между службами и пользователем для выполнения наших задач, например экспорта электронных таблиц.

Он имеет две основные области интересов.

**Лента**

Область панели инструментов с вкладками наверху технически называется лентой. Он содержит кнопки, раскрывающиеся списки, радио-меню, текстовые поля и некоторые скрытые поля, которые используются для выполнения многих операций с электронной таблицей. Эти кнопки при нажатии отправляют команды на сервер и соответственно обновляют лист.

**Лист**

Лист — это строки и столбцы. При щелчке по ячейкам лента обновляется соответствующим образом без отправки запросов на сервер, поскольку все данные, необходимые ленте, прикрепляются к каждой ячейке. Лента также отслеживает выбранную ячейку, строку и столбец, когда пользователь перемещается по листу.

Каждая ячейка имеет собственный встроенный редактор, который становится видимым, когда ячейка находится в режиме редактирования.
### **Вид рабочего листа**
Это внутренний компонент JSF с областью видимости, отвечающий за управление динамическим содержимым пользовательского интерфейса, описанным в index.html. Он имеет обработчики событий для запросов Ajax, которые запускаются, когда пользователь взаимодействует с пользовательским интерфейсом.
### **WorkbookService**
WorkbookService — это серверный компонент JSF с областью представления. Он работает как сервисный компонент и загружает и выгружает электронную таблицу с помощью других сервисов. Он имеет следующие конечные точки:

**в этом**

**в этом** является**PostConstruct** метод, который выполняется сразу после завершения создания объекта сервером приложений Java. Он проверяет**URL** в карте параметров запроса и загружает соответствующую электронную таблицу из заданного места, если это возможно.

**разрушать**

Он несет ответственность за очистку всех приобретенных ресурсов, когда они больше не требуются.
### **LoaderService**
Он создает экземпляры электронных таблиц и хранит их в памяти до тех пор, пока они необходимы.
### **CellsService**
**CellsService** управляет кешем строк, столбцов, ячеек, форматированием и структурой листов.
