---
title: FAQ
type: docs
weight: 400
url: /net/grid-faq/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Are there any limitations in the evaluation version of Aspose.Cells Grid Controls?**
No, there is no limitation of features in the evaluation version of those controls.

The evaluation version provides full features of the licensed version except that it adds an extra worksheet (containing **Evaluation Copyright Warning**) to the output files.

## **There are so many Grid controls available in the market. Why should I buy Aspose.Cells Grid Controls?**
Well, Aspose.Cells Grid Controls are well priced and affordable for all kinds of users. At a very reasonable price, it provides a suite of two controls for Windows and Web applications.

Moreover, it is not just a simple grid; it is your **Spreadsheet Viewer, Editor & Creator** at the same time.

You can not only bind it to any kind of data source (like normal grid controls) but also create & manage Excel files. It also provides a strong and rich **Formula Calculation Engine** to calculate not only built‑in functions (supported by Aspose.Cells Grid Controls) but also custom formulas defined by you. There are many more features of the Aspose.Cells Grid suite that can't be covered here; please refer to the **Edition Types** page for a more detailed feature list.

## **I've recently purchased my license for Aspose.Cells Grid Controls. How can I use that license in my application with Aspose.Cells Grid Control?**
Please refer to the [Licensing](/cells/net/licensing/) page of Aspose.Cells Grid Controls.

It provides complete details about how to use the license with Aspose.Cells Grid Controls in your applications.

## **How can I deploy my Aspose.Cells.GridWeb‑based web project/solution on the server?**
If you need to deploy the web application containing the GridWeb control, you should copy the "acw_client" directory into your project folder; otherwise your web application (deployed on the server) could not find it.

You can specify the scripting path by adding the following lines of code into the configuration section (e.g., in the web.config file in your VS.NET project). The "acw_client" folder contains files; Aspose.Cells.GridWeb uses this folder to manage its internal configuration. It has script files, image files, and other files to specify GridWeb's behavior and set other operations. The config file is used to prevent the control from using the embedded client resources (images, scripts, etc.), which is useful in some cases/scenarios.

**XML**

{{< highlight csharp >}}
<appSettings>
  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>
  <add key="aspose.cells.gridweb.force_script_path" value="true"/>
  <add key="aspose.cells.gridweb.forcepath" value="true"/>
</appSettings>
{{< /highlight >}}

{{% alert color="primary" %}}
The path is always related to the project's directory. You should not use any directory that is outside the project's directory. Therefore, it is necessary to copy the "acw_client" directory (from your GridWeb installation folder) into the project's directory.
{{% /alert %}}

## **Running Aspose.Cells.GridWeb in Internet Explorer**
Currently Aspose.Cells.GridWeb does not support Internet Explorer any more; it is an outdated browser.  
We support Chrome, Edge, Firefox, Safari, and Opera.
