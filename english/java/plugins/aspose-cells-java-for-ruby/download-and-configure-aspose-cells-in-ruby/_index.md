---
title: Download and Configure Aspose.Cells in Ruby
type: docs
weight: 10
url: /java/download-and-configure-aspose-cells-in-ruby/
---

## **Download Required Libraries**
Download required libraries mentioned below. These are the required for executing Aspose.Cells Java for Ruby examples.

- [Aspose.Cell for Java Component](https://downloads.aspose.com/cells/java/)
## **Download Examples from Social Coding Sites**
Following releases of running examples are available to download on below mentioned social coding sites:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installing**
It is very simple and easy to install Aspose.cells Java for Ruby gem, please follow these simple steps:

1. Add this line to your application's Gemfile. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. And then execute 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**OR**

1. Run following command. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Using**
Include the required files for working with the helloworld example.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Let's understand the above code.

1. The first line makes sure that the aspose cells is loaded and available.
1. Include the files that are required to access the aspose cells.
1. Initialize the libraries. The aspose JAVA classes are loaded from the path provided in the aspose.yml file/
