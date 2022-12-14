---
title: 在 Ruby 中下载并配置 Aspose.Cells
type: docs
weight: 10
url: /zh/java/download-and-configure-aspose-cells-in-ruby/
---
## **下载所需的库**
下载下面提到的所需库。这些是为 Ruby 示例执行 Aspose.Cells Java 所必需的。

- [Aspose.Cell for Java 组件](https://downloads.aspose.com/cells/java/)
## **从社交编码网站下载示例**
以下版本的运行示例可在下面提到的社交编码网站上下载：

**GitHub**

- [Aspose.Cells Java 红宝石](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **安装中**
安装 Aspose.cells Java for Ruby gem 非常简单易行，请按照以下简单步骤操作：

1. 将此行添加到应用程序的 Gemfile 中。

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. 然后执行

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**或者**

1. 运行以下命令。

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **使用**
包括使用 helloworld 示例所需的文件。

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

让我们理解上面的代码。

1. 第一行确保 aspose 单元格已加载且可用。
1. 包括访问 aspose 单元所需的文件。
1. 初始化库。 aspose JAVA 类是从 aspose.yml 文件中提供的路径加载的/
