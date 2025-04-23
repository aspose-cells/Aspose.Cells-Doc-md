---
title: Aggiungi Parti XML personalizzate e selezionale per ID
type: docs
weight: 70
url: /it/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Possibili Scenari di Utilizzo**

Le parti XML personalizzate sono i dati XML memorizzati all’interno dei documenti Microsoft Excel e vengono usati dalle applicazioni che le gestiscono. Attualmente non esiste un modo diretto per aggiungerle tramite l’interfaccia utente di Microsoft Excel. Tuttavia, puoi aggiungerle programmativamente in vari modi, ad esempio usando VSTO, usando Aspose.Cells, ecc. Utilizza il metodo [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) se desideri aggiungere una parte XML personalizzata usando l'API Aspose.Cells per Python via .NET. Puoi anche impostare il suo ID usando la proprietà [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Se vuoi invece selezionare una parte XML personalizzata tramite ID, puoi usare il metodo [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str).

## **Aggiungi parti XML personalizzate e selezionale per ID**

Il seguente codice di esempio aggiunge prima quattro parti XML personalizzate utilizzando il metodo [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes). Imposta quindi i loro ID utilizzando la proprietà [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Infine, trova o seleziona una delle parti XML personalizzate aggiunte utilizzando il metodo [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str). Si prega di consultare anche l'output della console del codice fornito di seguito per avere un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Output della console**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

