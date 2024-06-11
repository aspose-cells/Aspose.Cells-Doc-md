---
title: 下载并配置Aspose.Cells在Ruby中
type: docs
weight: 10
url: /zh/java/download-and-configure-aspose-cells-in-ruby/
---

## **下载所需的库**
下载下面提到的所需库。这些是执行Aspose.Cells Java for Ruby示例所需的。

- [Aspose.Cell for Java组件](https://downloads.aspose.com/cells/java/)
## **从社交编码网站下载示例**
可在下面列出的社交编码网站上下载以下版本的运行示例:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **安装**
安装Aspose.cells Java for Ruby gem非常简单，请按照以下简单步骤操作:

1. 在您的应用程序的Gemfile中添加以下行。 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. 然后执行 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**或者**

1. 运行以下命令。 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **使用**
包括与helloworld示例一起使用的所需文件。

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

让我们了解上述代码。

1. 第一行确保加载和使用aspose cells。
1. 包括访问aspose cells所需的文件。
1. 初始化库。从aspose.yml文件中提供的路径加载aspose JAVA类。
