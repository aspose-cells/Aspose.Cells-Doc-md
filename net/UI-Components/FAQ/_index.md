---
title: FAQ
type: docs
weight: 400
url: /net/grid-faq/
---

## **Is there any limitation in the evaluation version of Aspose.Cells Grid Controls?**
No, there is no limitation of features in the evaluation version of Aspose.Cells Grid Controls. The evaluation version provides full features of the licensed version except that it adds an extra worksheet (containing **Evaluation Copyright Warning** ) to the output files.
## **There are so many Grid controls available in the market. Why should i buy Aspose.Cells Grid Controls?**
Well, Aspose.Cells Grid Controls are very well priced to be affordable for all kinds of users. In a very reasonable price, it provides you a suite of two controls to work on Windows & Web Applications. Moreover, it is not just a simple Grid, it is your **Spreadsheet Viewer, Editor & Creator** at the same time. You cannot only bind it with any kind of Data Source (like normal Grid controls) but also create & manage Excel files. It also provides a strong & rich **Formula Calculation Engine** to calculate not only built-in functions (supported by Aspose.Cells Grid Controls) but also custom formulas defined by you. There are much more features of Aspose.Cells Grid suite that can't be covered here, please refer to Edition Types page for more detailed features list.
## **I've recently purchased my license for Aspose.Cells Grid Controls. How can i use that license in my application with Aspose.Cells Grid Control?**
Please refer to the [Licensing](/cells/net/licensing/) page of Aspose.Cells Grid Controls. It provides complete details about how to use the license with Aspose.Cells Grid Controls in your applications.
## **Are Aspose.Cells Grid Controls supported on Visual Studio.NET 2005?**
Yes, Aspose.Cells Grid Controls are fully supported on Visual Studio.NET 2005 and later versions.
## **I am using Aspose.Cells.GridWeb control in my web site using Visual Studio.NET 2005. But, it's not functioning at all. What's the problem?**
Aspose.Cells.GridWeb supports both **File System** and **HTTP** modes of Visual Studio.NET 2005. If you are still confused, please take a look at a step by step guide for Working with Aspose.Cells.GridWeb using Visual Studio.NET 2005.
## **How can I deploy my Aspose.Cells.GridWeb based web project/ solution on the Server?**
If you need to deploy the web application having GridWeb control, you would copy the "acw_client" directory into your project folder least your web application (deployed over the server) could not find it. You can always specify the scripting path by adding the following lines of code into the configuration section (e.g in the web.config file in your VS.NET Project). The "acw_client" is a folder that contains files and Aspose.Cells.GridWeb uses this folder to manage its internal configuration, it has scripts files, image files and other files to specify GridWeb's behavior and set other operations. The config file is used to prevent the control from using the embedded client resources (images, scripts, etc.) which is useful in some cases / scenarios.

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

The path is always related to the project's directory. You should not use any directory which is outside of the project's directory. So it is necessary to copy the "acw_client" directory (@ your GridWeb installation folder) into the project's directory.

{{% /alert %}} 
## **Running Aspose.Cell.GridWeb in Internet Explorer 10 or 11**
Currently Aspose.Cells.GridWeb does not work very well on Internet Explorer 10 or 11, so you have to use the compatibility mode of IE8/9 to work with it on IE10/11 browser type. You should add the following line of **<meta>** tag in the header section in **.aspx** page:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

