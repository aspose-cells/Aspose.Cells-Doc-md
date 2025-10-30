---
title: Aggiungi parti XML personalizzate e selezionale per ID con C++
linktitle: Aggiungi Parti XML personalizzate e selezionale per ID
type: docs
weight: 70
url: /it/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Impara come aggiungere e selezionare parti XML personalizzate nei file Excel utilizzando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Le parti XML personalizzate sono dati XML memorizzati all’interno dei documenti Microsoft Excel e sono utilizzate dalle applicazioni che interagiscono con essi. Attualmente non esiste un modo diretto per aggiungerle tramite l’interfaccia utente di Microsoft Excel. Tuttavia, puoi aggiungerle programmaticamente in vari modi, ad esempio utilizzando VSTO o Aspose.Cells. Usa il metodo [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/) per aggiungere una parte XML personalizzata tramite l’API Aspose.Cells. Puoi anche impostare il suo ID utilizzando la proprietà [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Allo stesso modo, se desideri selezionare una parte XML personalizzata per ID, puoi usare il metodo [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Aggiungi parti XML personalizzate e selezionale per ID**

Il seguente esempio di codice aggiunge prima quattro parti XML personalizzate utilizzando il metodo [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/). Successivamente, imposta i loro ID usando la proprietà [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Infine, trova o seleziona una delle parti XML personalizzate aggiunte usando il metodo [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Consulta anche l’output di console del codice di seguito come riferimento.

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
