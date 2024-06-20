---
title: Как использовать Aspose.Cells.GridWeb с .NET Core
type: docs
weight: 40
url: /ru/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: Эта статья рассказывает, как использовать GridWeb в веб приложении .net core
---

{{% alert color="primary" %}} 

Эта тема объясняет, как использовать Aspose.Cells.GridWeb с приложениями .NET Core с помощью Visual Studio.NET 2019. Эта тема полезна для разработчиков начального уровня, работающих с Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Использовать Aspose.Cells.GridWeb с .NET Core**
Эта тема показывает, как использовать Aspose.Cells.GridWeb, создав пример веб-сайта в Visual Studio 2019. Процесс разделен на шаги.
### **Шаг 1: Создание нового проекта**
1. Откройте Visual Studio 2019.
1. Из меню **Файл** выберите **Новый**, затем **Проект**.
   Открывается диалоговое окно создания нового проекта.
1. Выберите **ASP.NET Core Web Application** из установленных шаблонов проектов Visual Studio и нажмите **Далее**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Укажите расположение и имя проекта, а затем нажмите **Создать**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. Выберите шаблон **Web Application (Model-View-Controller)** и убедитесь, что выбран **ASP .NET Core 2.1**. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. Нажмите **Создать**.
### **Шаг 2: Проверка начального вида**
Запуск вновь созданного проекта показывает шаблон по умолчанию в браузере, как показано на изображении ниже.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Шаг 3: Добавление Aspose.Cells.GridWeb**
1. Добавьте следующие пакеты Nuget в проект

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1.Добавьте пакет Aspose.Cells.GridWeb

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Добавьте следующее в файл **_ViewImports.cshtml** в папке Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

После модификаций файл будет выглядеть так

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Вставьте следующий код в метод Index HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Не забудьте обновить путь SessionStorePath и путь ImportExcelFile.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. Добавьте следующий код в файл **Index.cshtml** в каталоге View > Home.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

После изменения файл будет выглядеть так

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Добавьте поддержку сессий и GridScheduedService в файле Startup.cs
   1.Добавьте следующий отрывок кода в метод ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1.Добавьте следующий отрывок кода в метод Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Поместите последний acw_client в каталог: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. Добавьте **AcwController** в Контроллеры для обработки маршрута acw, который может предоставить все стандартные операции для общего действия редактирования.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Шаг 4: Проверьте приложение**
Запуск приложения даст выход, аналогичный показанному на изображении ниже.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
