---
title: Use Your Own Icons Instead of the GridWeb Default Icons
type: docs
weight: 10
url: /net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb,icon,icons
description: This article describes how to use icons in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sometimes you might want to use your own icons (images) instead of Aspose.Cells.GridWeb control's default icons. This article explains how to do this.

{{% /alert %}} 

The control’s default icons are located in the URL path "/acw_client/". The file path can be: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" by default. You find files like `submit.gif`, `save.gif`, etc., in that folder. If you want to replace these images with your own, add a config section to the **web.config** file of your web application.

**XML**

{{< highlight csharp >}}
<appSettings>
  <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />
</appSettings>
{{< /highlight >}}

You may have noticed that this configuration only affects the control images path and doesn't affect the control’s client‑scripts path. For example, if you run your page with the GridWeb control and check the source file in the browser, you may find that the `acw_client_path` property of the grid’s DIV element still says: “/yourApp/webform1.aspx/”. In some cases, you may need to redefine the client‑script path. To force the control to use the redefined image path as the client‑script path, add another config setting in the **appSettings** section.

**XML**

{{< highlight csharp >}}
<add key="Aspose.Cells.GridWeb.force_script_path" value="true" />
{{< /highlight >}}

{{% alert color="primary" %}} 

This config will only take effect with the licensed control.

{{% /alert %}}
