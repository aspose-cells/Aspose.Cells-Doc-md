---
title: Actualizar días conservando el historial de registros de revisión en un libro compartido
type: docs
weight: 90
url: /es/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Escenarios de uso posibles**

Cuando comparta un libro de trabajo, obtendrá una opción que dice ***Mantener historial de cambios durante N días*** como se muestra en la siguiente captura de pantalla. Puede actualizar el número de días para conservar el historial usando Aspose.Cells con la propiedad [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Actualizar Días de Conservación del Historial de Revisiones en Libro de Trabajo Compartido**

El siguiente código de ejemplo crea un libro de trabajo vacío, lo comparte y actualiza los días de conservación del historial de revisiones a 7 días, que normalmente es de 30 días. Consulte el [archivo de Excel de salida](60489784.xlsx) generado por el código para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
