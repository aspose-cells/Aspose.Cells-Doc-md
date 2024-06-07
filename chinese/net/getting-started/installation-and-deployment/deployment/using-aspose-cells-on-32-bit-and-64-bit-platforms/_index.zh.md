---
title: 在32位和64位平台上使用Aspose.Cells
type: docs
weight: 10
url: /zh/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells是一个纯.NET组件，可以通过使用XCOPY部署简化部署流程。要安装Aspose.Cells，您只需将组件程序集(Aspose.Cells.dll)复制到应用程序目录中：应用程序可以立即开始使用它。这是由于.NET组件的自描述性质造成的。这种部署方式对安装过程没有任何影响。

{{% /alert %}} 
## **部署**
Aspose.Cells支持32位和64位环境。当您使用Aspose.Cells MSI安装程序安装Aspose.Cells .NET组件时，不同的DLL将被添加到Aspose.Cells ${installation_Path}文件夹中的不同文件夹中。查看表中的描述，了解哪个文件夹包含您需要与特定版本的.NET Framework一起使用的程序集。

|**文件夹**|**描述**|
| :- | :- |
|net2.0|包含用于.NET Framework 2.0、3.0、3.5、4.0和Mono的程序集。这些是您通常应该在32位和64位环境中使用的程序集。|
|net2.0_AuthenticodeSigned|与上述相同，但程序集使用Authenticode进行数字签名。签名的程序集可能加载速度较慢。|
|net3.5_ClientProfile|包含用于.NET Framework 3.5或4.0客户端概要的程序集。|
|net3.5_ClientProfile_AuthenticodeSigned|与上述相同，但程序集使用Authenticode进行数字签名。签名的程序集可能加载速度较慢。|
|net3.5|包含用于.NET Framework 3.5或4.0的程序集。|
|net3.5_AuthenticodeSigned|与上述相同，但程序集使用Authenticode进行数字签名。签名的程序集可能加载速度较慢。|
|net4.0|包含用于.NET Framework 4.0和4.5的程序集。|
|netStandard|包含用于.Net Standard 2.0的程序集。|
|netcoreapp2.1|包含用于.Net Core 2.1的程序集。|
|Xamarin.iOS|包含用于Xamarin.iOS的程序集。|
|Xamarin.Android|包含用于Xamarin.Android的程序集。|
|net5.0|包含用于.net5.0的程序集。|
|net6.0|包含用于.net6.0的程序集。|
{{% alert color="primary" %}} 

在VS.NET（例如2005、2008、2010、2012等）项目中，当向Aspose.Cells添加引用时，添加引用对话框会分别引用net2.0或net3.5文件夹中的Aspose.Cells.dll文件。（欲了解详细信息，请阅读【从.NET项目引用Aspose.Cells指南】。）您可以根据环境更改对库的引用。请注意，如果项目的目标框架是.NET Framework 3.5/4客户端概要，请使用位于net_ClientProfile文件夹中的Aspose.Cells.dll组件文件。

{{% /alert %}}
