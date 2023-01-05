---
title: Insertar objetos OLE en la hoja de trabajo
type: docs
weight: 20
url: /es/cpp/inserting-ole-objects-into-the-worksheet/
---
## **Posibles escenarios de uso**
 Aspose.Cells le permite insertar un objeto OLE dentro de la hoja de trabajo. Por favor use[IWorksheet->GetIOleObjects()->Add()](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object_collection#af230dd65a00cefabcc4b9f165b5dc7ba)método para este propósito. Necesitará una matriz de bytes de imagen que se usará para insertar el objeto OLE dentro de la hoja de trabajo y los bytes de datos del objeto Ole que serán su objeto real. Para insertar el objeto Ole dentro de la hoja de trabajo.
## **Insertar objetos OLE en la hoja de trabajo**
 El siguiente código de ejemplo crea el objeto del libro de trabajo e inserta el objeto Ole dentro de la primera hoja de trabajo y lo guarda como[archivo de salida de Excel](66519074.xlsx) . Por favor vea el[Aspose Logotipo](66519075.png) utilizados como bytes de imagen y[archivo de entrada de Excel](66519081.xlsx) utilizado como datos de objetos Ole dentro del código como referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
