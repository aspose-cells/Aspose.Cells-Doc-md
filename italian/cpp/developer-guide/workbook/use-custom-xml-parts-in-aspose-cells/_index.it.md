---
title: Usa parti personalizzate XML in Aspose.Cells con C++
linktitle: Utilizza parti XML personalizzate
type: docs
weight: 390
url: /it/cpp/use-custom-xml-parts-in-aspose-cells/
description: Impara a usare le parti XML personalizzate nei file Excel programmaticamente usando Aspose.Cells con C++.
---

## Utilizzo di Parti XML Personalizzate in Aspose.Cells

Le parti XML personalizzate sono dati XML memorizzati da diverse applicazioni come SharePoint all'interno di un file Excel. Questi dati sono utilizzati da varie applicazioni che ne necessitano. Microsoft Excel non utilizza questi dati, quindi non esiste un'interfaccia grafica per aggiungerli. Puoi visualizzare questi dati cambiando l'estensione di **.xlsx** in **.zip** e aprendolo con **WinZip**. Puoi anche aprire il file ZIP con qualsiasi utility di compressione Windows di terze parti come WinRAR o WinZip. I dati sono presenti all'interno della cartella **customXml**.

Puoi aggiungere parti XML personalizzate usando Aspose.Cells tramite il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/).

Il seguente esempio di codice utilizza il metodo [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) per aggiungere l'**XML del catalogo libri**, il cui nome è **BookStore**. L'immagine seguente mostra il risultato di questo codice. Come puoi vedere, l'XML del catalogo libri è stato aggiunto all'interno del nodo BookStore, che è il nome di questa proprietà.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Codice C++ per usare parti XML personalizzate

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Articolo Correlato

- [Aggiunta di proprietà personalizzate visibili nel pannello delle informazioni del documento](/cells/it/cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="cpp" >}}
