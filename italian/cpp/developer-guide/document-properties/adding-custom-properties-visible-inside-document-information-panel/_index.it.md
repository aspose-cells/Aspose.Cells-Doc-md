---
title: Aggiunta di proprietà personalizzate visibili nel pannello delle informazioni sul documento con C++
linktitle: Aggiunta di proprietà personalizzate visibili all interno del pannello delle informazioni sul documento
type: docs
weight: 300
url: /it/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Impara come aggiungere proprietà personalizzate visibili nel pannello delle informazioni sul documento usando Aspose.Cells con C++.
---

## **Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento**

Aspose.Cells può essere utilizzato per aggiungere proprietà personalizzate all'interno dell'oggetto del foglio di lavoro visibili all'interno del pannello delle informazioni del documento. È possibile aprire il pannello delle informazioni del documento in Microsoft Excel utilizzando i comandi del menu File > Informazioni > Proprietà > Mostra pannello del documento.

Usa il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) per aggiungere una proprietà personalizzata che sarà visibile nel Pannello Informazioni Documento.

Il codice di esempio seguente aggiunge due proprietà personalizzate. La prima proprietà non ha alcun tipo e la seconda ha un tipo come DateTime. Una volta aperto il file Excel generato da questo codice, vedrai queste due proprietà all'interno del Pannello Informazioni Documento.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object with specified format
    Workbook workbook(FileFormatType::Xlsx);

    // Add simple property without any type
    workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");

    // Add date time property with type
    workbook.GetContentTypeProperties().Add(u"MK32", u"04-Mar-2015", u"DateTime");

    // Save the workbook
    workbook.Save(srcDir + u"AddingCustomPropertiesVisible_out.xlsx");

    std::cout << "Custom properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Articolo correlato**

{{% alert color="primary" %}}

- [Utilizza parti XML personalizzate in Aspose.Cells](/cells/it/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
