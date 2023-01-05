---
title: Обновите Aspose.Grid.Web до Aspose.Cells.GridWeb
type: docs
weight: 30
url: /ru/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

Чтобы упростить обновление, мы поддерживаем документ, описывающий информацию, важную для существующих пользователей, особенно для тех, кто использовал старую версию Aspose.Grid.Web и нуждается в обновлении до объединенной версии Aspose.Cells.GridWeb.

 Это должны быть краткие заметки, и вы сможете найти дополнительную информацию, просматривая разделы[Руководство для разработчиков](/cells/ru/net/developer-guide/).

{{% /alert %}}

## **Обновление до Aspose.Cells.GridWeb**

 Пользователи Aspose.Grid.Web могут столкнуться с проблемами при использовании нового Aspose.Cells.GridWeb при обновлении до него. Следует отметить, что Aspose.Grid.Web был переименован и стал частью Aspose.Cells, поэтому мы не будем продолжать или вносить изменения в старые версии элемента управления.

Обновить до последней версии компонента Aspose.Cells.GridWeb несложно.

{{% alert color="primary" %}}

В API есть несколько изменений, поскольку классы с элементами, структурами, перечислениями и т. д. остаются прежними. Большинство изменений было внесено в пространства имен элементов управления и другие теги или атрибуты.

{{% /alert %}}

Ниже приведен список пространств имен и других атрибутов/тегов, которые сейчас изменены:

1. Пространство имен Aspose.Grid.Web было переименовано в Aspose.Cells.GridWeb.
1. Пространство имен Aspose.Grid.Web.Data было переименовано в Aspose.Cells.GridWeb.Data.
1. Пространство имен Aspose.Grid.Web.Design было переименовано в Aspose.Cells.GridWeb.Design.
1. Пространство имен Aspose.Grid.Formula было переименовано в Aspose.Cells.GridFormula, а с недавними выпусками компонента указанное пространство имен было полностью удалено из общего доступа API.
1. Тег agw:GridWeb изменен на acw:GridWeb в формате aspx.
1. Старый путь клиента Aspose.Grid.Web, agw_клиент, изменился на acw_клиент для Aspose.Cells.GridWeb .
1.  Параметр пути клиента в файле web.config, например:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 изменился на

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
