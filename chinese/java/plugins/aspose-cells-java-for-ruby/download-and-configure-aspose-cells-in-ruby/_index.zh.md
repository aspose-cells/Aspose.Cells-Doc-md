---
title: 下载并配置在Ruby中的Aspose.Cells
type: docs
weight: 10
url: /zh/java/download-and-configure-aspose-cells-in-ruby/
---

## **下载所需库**
下载下面提到的所需库。这些库是执行Aspose.Cells Java for Ruby示例所需的。

- [Aspose.Cell for Java组件](https://downloads.aspose.com/cells/java/)
## **从社交编码网站下载示例**
以下版本的正在运行的示例可在下面提到的社交编码网站上下载:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **安装**
安装Aspose.cells Java for Ruby gem非常简单易行，请按照以下简单步骤操作：

1. 在应用的Gemfile中添加这一行。 

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
包括用于使用helloworld示例的所需文件。

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

让我们理解上述代码。

1. 第一行确保加载并获取aspose cells。
1. 包括访问aspose cells所需的文件。
1. 初始化库。 aspose JAVA类是从aspose.yml文件提供的路径加载的。
