---
title: 应用许可证
type: docs
weight: 40
url: /zh/java/applying-a-license/
---

{{% alert color="primary" %}}

一旦您对Aspose.Cells的评估满意，在Aspose网站上购买许可证。熟悉提供的不同许可证类型。如果您有任何疑问，请随时联系Aspose销售团队。

每个Aspose许可证都享有一年的订阅权，可免费升级到此期间推出的任何新版本或修复版。技术支持是免费且无限的，向持有许可证的用户和评估用户提供支持。

许可证是一个包含产品名称、许可的开发者数量、订阅到期日期等详细信息的纯文本XML文件。该文件经过数字签名，因此不要修改文件：即使是在文件中添加额外换行符也会使其无效。

在执行任何文档操作之前，您需要设置许可证。确保在创建文档对象之前这样做。每个应用程序或进程只需设置一次许可证。

{{% /alert %}}

## **加载许可证文件**

在Aspose.Cells for Android via Java中，许可证可以[嵌入为资源](/cells/zh/java/applying-a-license/#applying-a-license-from-an-embedded-resource)，或从流中加载：

1. 将许可证文件放在**/mnt/sdcard/**的任何位置。
1. 创建一个引用文件的流。
1. 将包含许可证文件的流传递给SetLicense方法。

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **从嵌入资源应用许可证**

从Android包文件中按名称访问许可证资源:

1. 将许可证文件添加为应用程序的**res/raw**文件夹中的资源。
   许可证文件应在**res/raw**文件夹中可见。
1. 使用以下代码示例从资源中访问/加载许可证。

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
