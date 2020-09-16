---
title: Upgrade Aspose.Grid.Web to Aspose.Cells.GridWeb
type: docs
weight: 30
url: /net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---

{{% alert color="primary" %}}

To make it easier to upgrade, we maintain a document describing information critical to existing users, especially ones who have used the older Aspose.Grid.Web and need to upgrade to the merged Aspose.Cells.GridWeb.

These are intended to be brief notes, and you should be able to find more information by looking at the sections of the [Developer Guide](/cells/net/developer-guide/).

{{% /alert %}}

## **Upgrading to Aspose.Cells.GridWeb**

Aspose.Grid.Web users might come across issues using the new Aspose.Cells.GridWeb when they upgrade to it. It is to be noted that Aspose.Grid.Web has been renamed and become a part of Aspose.Cells so we will not continue or make amendments to older versions of the control. 

It is not hard to upgrade to the latest Aspose.Cells.GridWeb component.

{{% alert color="primary" %}}

There are a few changes in the API as the classes with the members, structs, enumerations etc. remain the same. Most of the changes have been made to the control’s namespaces and other tags or attributes.

{{% /alert %}}

The following is the namespaces list and other attributes/tags that are changed now:

1. The Aspose.Grid.Web namespace has renamed to Aspose.Cells.GridWeb.
1. The Aspose.Grid.Web.Data namespace has renamed Aspose.Cells.GridWeb.Data.
1. The Aspose.Grid.Web.Design namespace has renamed Aspose.Cells.GridWeb.Design.
1. The Aspose.Grid.Formula namespace was renamed to Aspose.Cells.GridFormula, and with recent releases of the component, the said namespace was completely removed from the public API.
1. The tag agw:GridWeb has changed to acw:GridWeb in the aspx form.
1. The older Aspose.Grid.Web client path, agw_client, has changed to acw_client for Aspose.Cells.GridWeb .
1. The client path setting in the web.config file, for example: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

has changed to 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
