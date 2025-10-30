---
title: Inserción de objetos OLE en la hoja de cálculo
type: docs
weight: 20
url: /es/cpp/inserting-ole-objects-into-the-worksheet/
---

## **Escenarios de uso posibles**
Aspose.Cells le permite insertar un objeto OLE dentro de la hoja de cálculo. Utilice el método [Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) para este propósito. Necesitará una matriz de bytes de imagen que se utilizará para insertar el objeto OLE dentro de la hoja de cálculo y bytes de datos del objeto OLE que serán su objeto real para insertar dentro de la hoja de cálculo. 
## **Inserción de objetos OLE en la hoja de cálculo**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Logotipo de Aspose</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
