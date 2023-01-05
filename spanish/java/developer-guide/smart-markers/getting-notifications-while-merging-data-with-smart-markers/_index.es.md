---
title: Recibir notificaciones al fusionar datos con marcadores inteligentes
type: docs
weight: 460
url: /es/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells Las API proporcionan la[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) clase a[trabajar con marcadores inteligentes](/cells/es/java/smart-markers/) donde se colocan el formato y las fórmulas en el[hojas de calculo de diseñador](/cells/es/java/what-is-a-designer-spreadsheet/) y luego procesado con[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) clase para completar los datos de acuerdo con los marcadores inteligentes especificados. A veces, puede ser necesario recibir notificaciones sobre la referencia de celda o el marcador inteligente en particular que se está procesando. Esto se puede lograr usando el[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) propiedad y[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)interfaz expuesta con el lanzamiento de Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Reciba notificaciones mientras fusiona datos con marcadores inteligentes**
 El siguiente fragmento de código demuestra el uso de[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)interfaz para definir una nueva clase que maneja la devolución de llamada para[WorkbookDesigner.proceso](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Para mantener el ejemplo simple y directo, el siguiente fragmento crea una hoja de cálculo de diseñador vacía, inserta un marcador inteligente y lo procesa con la fuente de datos creada dinámicamente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
