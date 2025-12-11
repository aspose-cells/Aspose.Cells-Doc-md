---
title: Download and Configure Aspose.Cells in Ruby
type: docs
weight: 10
url: /java/download-and-configure-aspose-cells-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Download Required Libraries**
Download required libraries mentioned below. These are required for executing Aspose.Cells Java for Ruby examples.

- [Aspose.Cells for Java Component](https://downloads.aspose.com/cells/java/)

## **Download Examples from Social Coding Sites**
The following runnable examples are available for download on the social coding sites mentioned below:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)

## **Installing**
It is very simple and easy to install Aspose.Cells Java for Ruby gem; please follow these simple steps:

1. Add this line to your application's Gemfile. 

{{< highlight ruby >}}
gem 'aspose-cellsjava'
{{< /highlight >}}

2. And then execute 

{{< highlight ruby >}}
$ bundle
{{< /highlight >}}

**OR**

1. Run the following command. 

{{< highlight ruby >}}
$ gem install aspose-cellsjava
{{< /highlight >}}

## **Using**
Include the required files for working with the HelloWorld example.

{{< highlight ruby >}}
require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include AsposeCellsJava
include AsposeCellsJava::HelloWorld

initialize_aspose_cells
{{< /highlight >}}

Let's understand the above code.

1. The first line makes sure that the Aspose.Cells library is loaded and available.  
2. Include the files required to access Aspose.Cells.  
3. Initialize the libraries. The Aspose Java classes are loaded from the path provided in the `aspose.yml` file.
