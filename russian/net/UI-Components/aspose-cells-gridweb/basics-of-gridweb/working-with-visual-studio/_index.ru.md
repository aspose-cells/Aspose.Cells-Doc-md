---
title: Работа с Visual Studio
type: docs
weight: 20
url: /ru/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: В этой статье рассматривается использование GridWeb в Visual Studio.
---

{{% alert color="primary" %}} 

Данный материал объясняет, как использовать Aspose.Cells.GridWeb в приложениях ASP.NET с использованием Visual Studio.NET 2005. Эта тема полезна для разработчиков начального уровня, работающих с Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Работа с Aspose.Cells.GridWeb с помощью Visual Studio 2013**
Данная тема показывает, как использовать Aspose.Cells.GridWeb, создав пример веб-сайта в Visual Studio 2013. Процесс разделен на этапы.
### **Шаг 1: Создание нового веб-сайта**
1. Откройте Visual Studio 2013.
1. В меню **Файл** выберите **Новое меню**, затем **Веб-сайт**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


Открывается диалоговое окно Нового веб-сайта. 

1. Выберите **ASP.NET веб-сайт форм** из установленных шаблонов Visual Studio.
1. Выберите режим HTTP для местоположения веб-сайта. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Укажите местоположение, где будут созданы и храниться файлы веб-сайта. 
   1. Нажмите **Обзор** в диалоговом окне Нового веб-сайта. 

![todo:image_alt_text](working-with-visual-studio_3.png)



Отображается диалоговое окно Выбор местоположения. 

1. Нажмите вкладку **Локальный IIS**.
   Отображаются все папки и веб-приложения, сохраненные в корневой папке IIS (например: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Теперь создайте новое веб-приложение в вашем локальном IIS, где будут храниться файлы веб-сайта.
   Диалоговое окно Выбор местоположения позволяет создавать и удалять веб-приложения или виртуальные каталоги в вашем локальном IIS. Чтобы создать веб-приложение, нажмите соответствующую кнопку, как показано на рисунке ниже. 

![todo:image_alt_text](working-with-visual-studio_5.png)



Создается новое веб-приложение с именем по умолчанию WebSite. 

1. Переименуйте веб-приложение. Мы переименовали его в GridWebOn2013.
1. Нажмите **Открыть**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Нажмите **OK**, чтобы Visual Studio создал веб-сайт. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Шаг 2: Проверка исходного и дизайн-видов веб-страницы**
Visual Studio 2013 уже создал веб-сайт по умолчанию. Он содержит веб-страницу default.aspx с некоторым фиктивным текстом и разметкой. 

**Исходный вид страницы default.aspx** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Все веб-страницы (включая ASP.NET) могут быть открыты в двух режимах. Один - это исходный вид, который позволяет разработчикам получить доступ и изменить исходный код. Второй режим - это дизайн-вид, который можно использовать для проектирования веб-страниц в режиме WYSIWYG. На рисунке выше показан исходный вид веб-страницы default.aspx. Чтобы просмотреть дизайн-вид, нажмите **Дизайн**. 

**Представление дизайна страницы default.aspx** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Удалите страницу Default.aspx, добавленную Visual Studio, и добавьте новую пустую страницу Default.aspx.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Шаг 3: Добавление Aspose.Cells.GridWeb на веб-страницу**
Вы можете просто добавить элемент управления Aspose.Cells.GridWeb (или GridWeb) на веб-страницу, перетащив его из панели инструментов. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Если вы не знаете, как добавить Aspose.Cells.GridWeb на панель инструментов, см. [Интеграция элементов управления Aspose.Cells Grid с Visual Studio.NET](/cells/ru/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

После того как элемент управления GridWeb добавлен на веб-страницу, он будет отображаться вот так: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Выберите полный тег. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Шаг 5: Изменение размеров элемента управления Aspose.Cells.GridWeb**
Вы можете изменить ширину и высоту элемента управления GridWeb после его перетаскивания на веб-сайт. 

В режиме дизайна вы можете изменить ширину и высоту GridWeb. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Шаг 6: Настройка свойств Aspose.Cells.GridWeb**
Настройте свойства Aspose.Cells.GridWeb в WYSIWYG, нажав кнопку **Свойства** справа в Visual Studio 2013 IDE. 
Отображается диалоговое окно свойств. 

![todo:image_alt_text](working-with-visual-studio_15.png)



Панель свойств позволяет настраивать внешний вид и некоторые другие свойства элемента управления GridWeb, чтобы управлять его поведением.
### **Шаг 7: Запуск вашего первого веб-сайта, содержащего элемент управления Aspose.Cells.GridWeb**
Постройте и запустите веб-сайт. 

1. Запустите веб-сайт напрямую из Visual Studio, нажав Ctrl+F5 или кликнув **Начать отладку**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Теперь вы можете начать работу с элементом управления GridWeb. 

**Элемент управления GridWeb в действии** 

![todo:image_alt_text](working-with-visual-studio_17.png)
