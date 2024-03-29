﻿---
title: Общедоступный API Изменения в Aspose.Cells 8.1.1
type: docs
weight: 60
url: /ru/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.1.0 до 8.1.1, которые могут представлять интерес для разработчиков модулей и приложений. Он включает в себя не только[новые и обновленные публичные методы](/cells/ru/java/public-api-changes-in-aspose-cells-8-1-1/) , но и описание любого[изменения в поведении](/cells/ru/java/public-api-changes-in-aspose-cells-8-1-1/) за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные свойства и функции**
### **Добавлено свойство HtmlSaveOptions.PresentationPreference.**
Класс HtmlSaveOptions предоставляет метод получения/установки для свойства PresentationPreference, которое можно использовать для визуализации результатов с лучшим макетом при экспорте электронных таблиц в HTML или MHTML. Значение по умолчанию — false. тогда как если установлено значение true, Aspose.Cells API экспортирует содержимое рабочего листа с лучшим представлением.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Используйте опцию PresentationPreference для лучшего макета](/cells/ru/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Добавлена поддержка сценариев рабочего листа.**
Сценарий — это модель «что, если», которая включает переменные входные ячейки, связанные между собой одной или несколькими формулами. Aspose.Cells предоставляет методы получения и установки для свойства Worksheet.Scenarios, а также следующие классы, чтобы помочь разработчикам создавать сценарии, управлять ими и удалять их.

1. Сценарий: представляет отдельный сценарий.
1. ScenarioCollection: представляет набор сценариев.
1. ScenarioInputCellCollection: представляет список входных ячеек для определенного сценария.
1. ScenarioInputCell: представляет входную ячейку из коллекции входных ячеек для определенного сценария.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Как создавать, манипулировать или удалять сценарии из рабочих листов](/cells/ru/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Изменение поведения для CellsException**
В предыдущих выпусках Aspose.Cells for Java API, когда в экземпляр Workbook загружалась возможно поврежденная электронная таблица, API, как правило, выдавал общее сообщение, не упоминая, в чем может быть проблема. Мы изменили это поведение для версии 8.1.1, так что API выдает исключение со значимым сообщением, указывающим, где (какая ячейка) и что (выражение формулы) вызывает исключение при чтении файла шаблона.
