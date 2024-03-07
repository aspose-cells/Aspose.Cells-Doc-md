---
title: Evaluation Version Limitations
type: docs
weight: 50
url: /net/evaluation-version-limitations/
description: Aspose.Cells for .NET provides different plans for purchase or offers a Free Trial and a 30-day Temporary License for evaluation using Licensing and Subscription policies in C#.
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---

## **How to Get Evaluation Version of Aspose.Cells**

You can download an evaluation version of **Aspose.Cells** for NET from [its download page](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. The evaluation version provides absolutely the same capabilities as the licensed version of the product. Furthermore, evaluation version simply becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

Once you are happy with your evaluation of **Aspose.Cells**, you can [purchase a license](https://purchase.aspose.com) at the Aspose website. Make yourself familiar with the different subscription types offered. If you have any questions, do not hesitate to contact the Aspose sales team.

Every Aspose license carries a one-year subscription for free upgrades to any new versions or fixes that come out during this time. Technical support is free and unlimited and provided both to licensed and evaluation users.

## **How to Test Aspose.Cells Without Evaluation Version Limitations**

If you want to test **Aspose.Cells** without evaluation version limitations, request a 30-day temporary license. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license) for more information.


## **Evaluation Version Limitations**

Evaluation version of **Aspose.Cells** product (without a license specified) provides full product functionality, but it is limited to open 100 files in one program and an extra worksheet with evaluation watermark.

The limitations are shown below:

### **1st Limitation: Number of Opened Files**

When running your program, you can only open 100 Excel files. If your application exceeds this number, an exception will be thrown.

### **2nd Limitation: Worksheet with Evaluation Watermark**
This worksheet will always show as the active worksheet. Only in licensed version, you can set the active worksheet to other worksheets.
<br>
<image src="1.png" width="70%" />
<br>

### **3rd Limitation: Plain Text with Evaluation information**
In the output Plain Text file by Aspose.Cells, an evaluation information would be added at the end of the document.
<br>
<image src="2.png" width="70%" />
<br>

### **4th Limitation: PDF and Image with Evaluation Watermark**
In the output PDF or image file by Aspose.Cells, an evaluation watermark would be pasted at the top of the document/image.You can’t hide the Evaluation Copyright Warning (the extra worksheet) in the GridWeb control too, it will always be added (at the end in the worksheet tabs) in the control.
<br>
<image src="3.png" width="70%" />
<br>

### **5th Limitation: Config file settings (Aspose.Cells.GridWeb)**
You can't re-specify the script path by adding the following lines of code into the configuration section (e.g in the web.config file). The acw_client is a folder that contains files and Aspose.Cells.GridWeb uses this folder to manage its internal configuration, it has script files, image files and other files to specify GridWeb's behavior and set other operations. The config file is used to prevent the control from using the embedded client resources (images, scripts, etc.) which is useful in some cases / scenarios. Moreover, this configuration settings in the web.config file will only take effect with the LICENSED version of the control.

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

These settings might be compulsory in some cases / scenarios if you are using Aspose.Cells.GridWeb control in File System Websites or MS Ajax extensions etc.

{{% /alert %}}