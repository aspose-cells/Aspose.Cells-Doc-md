---
title: Actualizar días conservando el historial de registros de revisión en el libro de trabajo compartido
type: docs
weight: 90
url: /es/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---
## **Posibles escenarios de uso**

Cuando comparte un libro de trabajo, obtiene una opción que dice***Conservar el historial de cambios durante N días***como se muestra en la siguiente captura de pantalla. Puede actualizar la cantidad de días para conservar el historial usando Aspose.Cells con[**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory)propiedad.

![todo:imagen_alternativa_texto](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Actualizar días conservando el historial de registros de revisión en el libro de trabajo compartido**

El siguiente código de ejemplo crea un libro de trabajo vacío, luego lo comparte y actualiza los días de registros de revisión conservando el historial a 7 días, que normalmente son 30 días. Por favor vea el[archivo de salida de Excel](60489784.xlsx)generado por el código para una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
