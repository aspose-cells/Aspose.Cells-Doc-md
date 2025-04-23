---
title: Obtener notificaciones al fusionar datos con Smart Markers
type: docs
weight: 20
url: /es/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Las API de Aspose.Cells proporcionan la clase [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) para [trabajar con Smart Markers](https://docs.aspose.com/cells/net/smart-markers/) donde el formato y las fórmulas se colocan en las [plantillas de diseñador](/cells/es/net/what-is-a-designer-spreadsheet/) y luego se procesan con la clase [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) para completar los datos de acuerdo con los Smart Markers especificados. A veces, puede ser necesario recibir notificaciones sobre la referencia de celda o el Smart Marker particular que se está procesando. Esto se puede lograr utilizando la propiedad [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) y la interfaz [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) expuesta con la versión Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

El siguiente fragmento de código demuestra el uso de la interfaz [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) para definir una nueva clase que maneje la devolución de llamada para el método [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



El resto del proceso incluye cargar la plantilla de diseñador que contiene los Smart Markers con [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) y procesarla configurando la fuente de datos. Para mantener el ejemplo simple, hemos utilizado una plantilla de diseñador predefinida que contiene solo dos Smart Markers como se muestra en la captura de pantalla a continuación, donde la fuente de datos se crea dinámicamente para fusionar los datos de acuerdo con los Smart Markers especificados.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
