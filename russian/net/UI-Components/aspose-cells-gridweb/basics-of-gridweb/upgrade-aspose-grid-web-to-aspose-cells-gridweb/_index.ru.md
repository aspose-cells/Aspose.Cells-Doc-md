---
title: Обновите Aspose.Grid.Web до Aspose.Cells.GridWeb
type: docs
weight: 30
url: /ru/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: В этой статье рассматривается процесс обновления в GridWeb.
---

{{% alert color="primary" %}}

Для упрощения обновления мы поддерживаем документ, описывающий информацию, критическую для существующих пользователей, особенно тех, кто использовал более старый Aspose.Grid.Web и нуждается в обновлении до Aspose.Cells.GridWeb.

Эти заметки предназначены быть краткими, и вы должны быть способны найти более подробную информацию, изучая разделы [Руководства разработчика](/cells/ru/net/aspose-cells-gridweb/developer-guide/).

{{% /alert %}}

## **Обновление до Aspose.Cells.GridWeb**

Пользователи Aspose.Grid.Web могут столкнуться с проблемами при использовании нового Aspose.Cells.GridWeb при его обновлении. Следует отметить, что Aspose.Grid.Web был переименован и стал частью Aspose.Cells, поэтому мы не будем продолжать или вносить изменения в более старые версии элемента управления. 

Обновление до последнего компонента Aspose.Cells.GridWeb несложно.

{{% alert color="primary" %}}

Изменения в API связаны в основном с пространствами имен элемента управления и другими тегами или атрибутами, хотя классы с членами, структурами, перечислениями и т. д. остаются прежними.

{{% /alert %}}

Ниже приведен список пространств имен и других атрибутов/тегов, которые теперь изменены:

1. Пространство имен Aspose.Grid.Web было переименовано в Aspose.Cells.GridWeb.
1. Пространство имен Aspose.Grid.Web.Data было переименовано в Aspose.Cells.GridWeb.Data.
1. Пространство имен Aspose.Grid.Web.Design было переименовано в Aspose.Cells.GridWeb.Design.
1. Пространство имен Aspose.Grid.Formula было переименовано в Aspose.Cells.GridFormula, и с последними выпусками компонента это пространство имен было полностью удалено из публичного API.
1. Тег agw:GridWeb был изменен на acw:GridWeb в форме aspx.
1. Старый путь клиента Aspose.Grid.Web, agw_client, был изменен на acw_client для Aspose.Cells.GridWeb.
1. Настройка пути клиента в файле web.config, например: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

была изменена на 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
