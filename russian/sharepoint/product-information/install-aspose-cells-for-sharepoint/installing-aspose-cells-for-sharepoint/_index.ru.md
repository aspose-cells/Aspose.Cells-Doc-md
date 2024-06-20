---
title: Установка Aspose.Cells for SharePoint
type: docs
weight: 10
url: /ru/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint доступен в виде архива Aspose.Cells.SharePoint.zip. 

{{% /alert %}} 
### **Содержание архива**
Архив Aspose.Cells.SharePoint.zip содержит:

- Aspose.Cells.SharePoint.wsp – Файл решения для SharePoint. Aspose.Cells for SharePoint упакован в виде решения для SharePoint для упрощения развертывания/отката и активации/деактивации функций во всей ферме серверов.
- Aspose_LicenseAgreement.rtf – Лицензионное соглашение конечного пользователя
- Aspose.Cells for SharePoint.pdf – Пользовательская документация
- Aspose.Cells for SharePoint Documentation.chm – Пользовательская документация с ссылкой на общедоступный API
- setup.exe – Программа установки
- setup.exe.config – Файл конфигурации установки

Программа установки проверяет следующие условия перед продолжением установки:

- Установлен WSS 3.0, MOSS 2007 или SharePoint 2010.
- У пользователя есть разрешение на установку решений SharePoint.
- База данных SharePoint в онлайн-режиме.
- Служба администрирования WSS запущена.
- Служба таймеров WSS запущена.

Службы администрирования WSS и таймеров необходимы, потому что некоторые действия установки зависят от задания таймера для распространения на все серверы фермы серверов. 
#### **Для установки Aspose.Cells for SharePoint**
1. Распакуйте файл Aspose.Cells.SharePoint.zip на локальный диск сервера MOSS 7.0 или WSS 3.0.
2. Запустите setup.exe и следуйте инструкциям на экране.

Программа установки выполняет следующие действия:

1. Проверка предварительных требований к установке. Установка не будет продолжена, если проверка не пройдена. 

   **Проверка системы** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




2. Отображение лицензионного соглашения конечного пользователя. Пользователь должен принять соглашение, чтобы продолжить. 

   **Лицензионное соглашение** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. Отображение диалога выбора целевого развертывания. Пользователь выбирает веб-приложения и коллекции сайтов, где функция должна быть активирована. См. рисунок ниже. 

   **Целевые развертывания** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. Развертывание функции в ферме серверов. 

   **Запущенная установка** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. Активация функции для выбранных коллекций сайтов и настройка их родительских веб-приложений.
1. Отображение списка веб-приложений и коллекций сайтов, где функция была развернута и активирована. 

   **Установка завершена** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
