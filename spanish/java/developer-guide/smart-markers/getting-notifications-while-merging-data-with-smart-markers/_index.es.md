---
title: Obtener notificaciones al fusionar datos con Smart Markers
type: docs
weight: 460
url: /es/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Las API de Aspose.Cells proporcionan la clase [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) para [trabajar con marcadores inteligentes](/cells/es/java/smart-markers/), donde el formato y las fórmulas se colocan en las [hojas de cálculo del diseñador](/cells/es/java/what-is-a-designer-spreadsheet/) y luego se procesan con la clase [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) para completar los datos de acuerdo con los marcadores inteligentes especificados. A veces, puede ser necesario recibir notificaciones sobre la referencia de celda o el marcador inteligente particular que se está procesando. Esto se puede lograr usando la propiedad [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) y la interfaz [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) expuesta con la versión Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Obtener notificaciones al fusionar datos con marcadores inteligentes**
El siguiente fragmento de código demuestra el uso de la interfaz [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) para definir una nueva clase que maneje la llamada de retorno para el método [WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Con el fin de mantener el ejemplo simple y directo, el siguiente fragmento de código crea una hoja de cálculo de diseñador vacía, inserta un Marcador Inteligente y la procesa con la fuente de datos creada dinámicamente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
{{< app/cells/assistant language="java" >}}
