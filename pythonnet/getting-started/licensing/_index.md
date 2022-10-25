---
title: Licensing
type: docs
weight: 19
url: /python-net/licensing/
---

{{% alert color="primary" %}}

You can easily download an evaluation version of Aspose.Cells Python via .Net from its [download page](https://pypi.org/project/aspose-cells-python/) @ Pypi repos. The evaluation version provides absolutely the same capabilities as the licensed version of the component. Furthermore, evaluation version simply becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

{{% /alert %}}

## **Evaluation Version Limitations**

Evaluation version of Aspose.Cells Python via .Net product (without a license specified) provides full product functionality, but it is limited to open 100 files in one program and an extra worksheet with evaluation watermark.

The limitations are shown below:

- **Number of Opened Files** (Aspose.Cells Python via .Net)
  When running your program, you can only open 100 Excel files using Aspose.Cells Python via .Net library. If your application exceeds this number, an exception will be thrown.


Moreover, a worksheet with evaluation watermark will always show as the active worksheet in the generated excel file using Aspose.Cells library. Only in licensed version, you can set the active worksheet to other worksheets. In the output PDF or image file by Aspose.Cells, an evaluation watermark would be pasted at the top of the document/image.

{{% alert color="primary" %}}

If you want to test Aspose.Cells without evaluation version limitations, you can also request a [30 Day Temporary License](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Applying a License in Aspose.Cells Component**

The license is a plain text XML file that contains details such as the product name, number of developers it is licensed to, subscription expiry date and so on. The file is digitally signed, so don't modify the file. Even inadvertent addition of an extra line break into the file will invalidate it.You need to set a license before utilizing Aspose.Cells if you want to avoid its evaluation limitation. It is only required to set a license once per application (or process). The license can be loaded from a file, stream or an embedded resource.

Aspose.Cells tries to find the license in explicit path locations.

There are two common methods to apply a license, from file or stream.

### **Applying a License from Disk or Stream**

The easiest way to set a license, is to put the license file in the explicit path.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Window 
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("home/user/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

When you call the set_license method, the license name should be same as that of your license file name. For example, you may change the license file name to **Aspose.Cells.lic.xml**. Then in your code, you should use the modified license name (**Aspose.Cells.lic.xml**) for the set_license method.

{{% /alert %}}

It is also possible to load a license from a stream.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

license = License();

license.set_license(myStream);

{{< /highlight >}}
