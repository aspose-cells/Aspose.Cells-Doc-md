---
title: Как использовать Aspose.Cells.GridWeb с ядром .NET
type: docs
weight: 40
url: /ru/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

В этом разделе объясняется, как использовать Aspose.Cells.GridWeb с приложениями .NET Core с помощью Visual Studio.NET 2019. Этот раздел полезен для разработчиков начального уровня, работающих с Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Используйте Aspose.Cells.GridWeb с ядром .NET.**
В этом разделе показано, как использовать Aspose.Cells.GridWeb, создав образец веб-сайта в Visual Studio 2019. Процесс разбит на этапы.
### **Шаг 1: Создание нового проекта**
1. Откройте Visual Studio 2019.
1.  От**Файл** меню, выберите**Новый** , тогда**Проект**.
 Открывается диалоговое окно создания нового проекта.
1.  Выбирать**ASP.NET Основное веб-приложение** из установленных шаблонов проектов Visual Studio и щелкните**Следующий**.

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  Укажите место, где находится место и имя проекта, и нажмите**Создавать**.

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  Выберите**Веб-приложение (модель-представление-контроллер)** шаблон и убедитесь, что**ASP .NET Ядро 2.1** выбран.

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  Нажмите**Создавать**.
### **Шаг 2: Проверка исходного вида**
Запуск только что созданного проекта показывает шаблон по умолчанию в браузере, как показано на изображении ниже.



![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Шаг 3: Добавление Aspose.Cells.GridWeb**
1. Добавьте в проект следующие пакеты Nuget.

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Добавить пакет Aspose.Cells.GridWeb

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Добавьте следующее в файл **_ViewImports.cshtml** в папке Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Файл будет выглядеть так после модификаций

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Поместите следующий код в метод Index HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Не забудьте обновить SessionStorePath и путь ImportExcelFile.

{{% /alert %}} 

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  Добавьте следующий код в**Индекс.cshtml** файл в папке View > Home.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

После изменения файл будет выглядеть так.

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Добавьте поддержку сеанса и GridSchedudService в файл Startup.cs.
 1. Добавьте следующий фрагмент кода в метод ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Добавьте следующий фрагмент кода в метод Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Поместите последнюю версию acw_client в каталог: **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1.  Добавлять**AcwController**в контроллерах, чтобы иметь дело с картой маршрутов acw, которая может предоставить все операции по умолчанию для общего действия редактирования.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Шаг 4. Протестируйте приложение**
Запуск приложения приведет к выводу, аналогичному показанному на изображении ниже.

![дело:изображение_альтернативный_текст](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
