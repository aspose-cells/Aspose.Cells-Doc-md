---
title: Ladda ner och konfigurera Aspose.Cells i Ruby
type: docs
weight: 10
url: /sv/java/download-and-configure-aspose-cells-in-ruby/
---
## **Ladda ner obligatoriska bibliotek**
Ladda ner nödvändiga bibliotek som nämns nedan. Dessa är nödvändiga för att köra Aspose.Cells Java för Ruby-exempel.

- [Aspose.Cell for Java Komponent](https://downloads.aspose.com/cells/java/)
## **Ladda ner exempel från webbplatser för social kodning**
Följande versioner av löpande exempel finns att ladda ner på nedan nämnda webbplatser för social kodning:

**GitHub**

- [Aspose.Cells Java för Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installerar**
Det är väldigt enkelt och lätt att installera Aspose.cells Java för Ruby gem, följ dessa enkla steg:

1.  Lägg till den här raden i din applikations Gemfile.

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1.  Och sedan avrätta

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**ELLER**

1.  Kör följande kommando.

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Använder sig av**
Inkludera de nödvändiga filerna för att arbeta med helloworld-exemplet.

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Låt oss förstå koden ovan.

1. Den första raden ser till att aspose-cellerna är laddade och tillgängliga.
1. Inkludera filerna som krävs för att komma åt aspose-cellerna.
1. Initiera biblioteken. Aspose JAVA-klasserna laddas från sökvägen i filen aspose.yml/
