---
title: 许可
type: docs
weight: 50
url: /zh/cpp/licensing/
---

## **评估版本限制**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **使用文件或流对象应用许可**
许可证可以从文件或流对象加载。Aspose.Cells for C++将尝试在以下位置查找许可证：

1. 明确的路径。
1. 包含Aspose.Cells.dll的文件夹。
1. 包含调用Aspose.Cells.dll的程序集所在的文件夹。
1. 包含入口程序集（您的.exe）的文件夹。
1. 包含调用Aspose.Cells.dll的程序集中的嵌入式资源。

设置许可证最简单的方法是将许可文件放在与Aspose.Cells.dll文件相同的文件夹中，并指定文件名，不带路径，如下面的例子所示。
### **从文件加载许可证**
应用许可证最简单的方法是将许可文件放在与Aspose.Cells.dll文件相同的文件夹中，并仅指定文件名而不带路径。

{{% alert color="primary" %}} 

当调用SetLicense方法时，传递的许可证名称应该是许可证文件的名称。例如，如果将许可证文件名更改为"Aspose.Cells.lic.xml"，则将该文件名传递给Cel1->SetLicense(...)方法。

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **从流对象加载许可证**
以下示例显示如何从流中加载许可证。

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
