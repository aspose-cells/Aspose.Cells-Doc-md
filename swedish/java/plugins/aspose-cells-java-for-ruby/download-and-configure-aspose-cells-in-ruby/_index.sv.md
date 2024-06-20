---
title: Ladda ner och konfigurera Aspose.Cells i Ruby
type: docs
weight: 10
url: /sv/java/download-and-configure-aspose-cells-in-ruby/
---

## **Hämta nödvändiga bibliotek**
Hämta nödvändiga bibliotek som anges nedan. Dessa krävs för att köra Aspose.Cells Java för Ruby-exempel.

- [Aspose.Cell för Java-komponent](https://downloads.aspose.com/cells/java/)
## **Hämta exempel från sociala kodningssajter**
Följande versioner av körande exempel finns tillgängliga att ladda ner på nedan angivna sociala kodningssajter:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installation**
Det är mycket enkelt och lätt att installera Aspose.cells Java för Ruby-pärla, följ dessa enkla steg:

1. Lägg till den här raden i din applikations Gemfile. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. Och sedan utföra 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**ELLER**

1. Kör följande kommando. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Användning**
Inkludera de nödvändiga filerna för att arbeta med helloworld-exemplet.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Låt oss förstå koden ovan.

1. Den första raden ser till att aspose celler är laddade och tillgängliga.
1. Inkludera filerna som krävs för att komma åt aspose cells.
1. Initialisera biblioteken. Aspose JAVA-klasserna laddas från den sökväg som anges i aspose.yml-filen.
