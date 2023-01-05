---
title: Recibir notificaciones al fusionar datos con marcadores inteligentes
type: docs
weight: 20
url: /es/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells Las API proporcionan la[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) clase a[trabajar con marcadores inteligentes](https://docs.aspose.com/cells/net/smart-markers/) donde se colocan el formato y las fórmulas en el[hojas de calculo de diseñador](/cells/es/net/what-is-a-designer-spreadsheet/) y luego procesado con[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) clase para completar los datos de acuerdo con los marcadores inteligentes especificados. A veces, puede ser necesario recibir notificaciones sobre la referencia de celda o el marcador inteligente en particular que se está procesando. Esto se puede lograr usando el[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) propiedad y[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interfaz expuesta con el lanzamiento de Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

 El siguiente fragmento de código demuestra el uso de[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interfaz para definir una nueva clase que maneja la devolución de llamada para[WorkbookDesigner.Proceso](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)método.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 El resto del proceso incluye cargar la hoja de cálculo del diseñador que contiene los marcadores inteligentes con[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)procesarlo configurando la fuente de datos. Para simplificar el ejemplo, hemos utilizado una hoja de cálculo de diseñador predefinida que contiene solo dos marcadores inteligentes, como se muestra en la siguiente instantánea, donde la fuente de datos se crea dinámicamente para fusionar los datos de acuerdo con los marcadores inteligentes especificados.

|![todo:imagen_alternativa_texto](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
